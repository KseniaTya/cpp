import sys
#sys.path.append("C:/Users/ezik1/AppData/Local/Programs/Python/Python311/Scripts/antlr4.exe")
sys.path.append("C:/Users/ezik1/AppData/Local/Programs/Python/Python311/Lib/site-packages/llvmlite")
from antlr4 import *
import llvmlite.ir as ir

from parser.grCpp2Visitor import grCpp2Visitor
from parser.grCpp2Lexer import grCpp2Lexer
from parser.grCpp2Parser import grCpp2Parser

from code_generator.types import grCpp2Types
from code_generator.symbol_table import SymbolTable, RedefinitionError
from code_generator.util import *
from code_generator.errors import *


# класс-наследник, внутри которого переопределяются некоторые методы класса Visitor;
# Visitor был автоматически создан с помощью ANTLR4 для файла .g4
class grCpp2Generator(grCpp2Visitor):
    BASE_TYPE = 0
    ARRAY_TYPE = 1
    FUNCTION_TYPE = 2

    def __init__(self, error_listener=grCpp2ErrorListener()):
        self.module = ir.Module()
        self.builder = ir.IRBuilder()
        self.symbol_table = SymbolTable()

        self.continue_block = None
        self.break_block = None
        self.switch_context = None

        self.current_base_type = None
        self.is_global = True

        self.error_listener = error_listener
        self.global_context = ir.global_context
        self.struct_reflection = {}
        self.is_defining_struct = ''

    def visitExternalDeclaration(self, ctx:grCpp2Parser.DeclarationContext):
        if not match_text(ctx.children[0], ","):
            try:
                self.visit(ctx.children[0])
            except SemanticError as e:
                self.error_listener.register_semantic_error(e)

    def visitFunctionDefinition(self, ctx:grCpp2Parser.FunctiondefinitionContext):
        self.is_global = False

        # посещение правила declarationSpecifiers
        # получаем тип возвращаемого значения ф-ции
        ret_type = self.visit(ctx.declspecifierseq())
        self.current_base_type = ret_type

        # посещение правила declarator
        # получаем имя ф-ции, тип ф-ции и список аргументов
        _, func_name, function_type, arg_names = self.visit(ctx.declarator())

        # проверка наличия ф-ции в таблице символов
        if func_name in self.symbol_table:
            llvm_function = self.symbol_table[func_name]

            # проверка соответствия типов между объявлением и определением ф-ции
            if llvm_function.function_type != function_type:
                raise SemanticError(msg=f"Function {func_name}'s definition different from its declaration", ctx=ctx)
        else:
            # создание новой LLVM ф-ции, если её нет в таблице символов
            llvm_function = ir.Function(self.module, function_type, name=func_name)
            self.symbol_table[func_name] = llvm_function

        # создание объекта IRBuilder для генерации инструкций внутри ф-ции и вход в новую область видимости
        self.builder = ir.IRBuilder(llvm_function.append_basic_block(name="entry"))
        self.symbol_table.enter_scope()

        # добавление аргументов ф-ции в таблицу символов
        try:
            for arg_name, llvm_arg in zip(arg_names, llvm_function.args):
                self.symbol_table[arg_name] = llvm_arg
        except RedefinitionError as e:
            raise SemanticError(msg=f"Redefinition local variable {arg_name}", ctx=ctx)

        self.continue_block = None
        self.break_block = None

        # посещение правила functionbody
        # обработка тела ф-ции
        self.visit(ctx.functionbody())

        # если ф-ция возвращает void
        if function_type.return_type == grCpp2Types.void:
            # добавление инструкции возврата void
            self.builder.ret_void()

        # выход из текущей области видимости
        self.symbol_table.exit_scope()
        self.is_global = True

    def visitPrimaryExpression(self, ctx:grCpp2Parser.PrimaryexpressionContext):
        if len(ctx.children) == 3:
            # посещение правила expression
            return self.visit(ctx.expression())
        else:
            # извлекаем текст текущего контекста
            text = ctx.getText()

            # если текущий контекст - идентификатор
            if ctx.Identifier():
                # проверка наличия значения переменной в таблице символов
                if text in self.symbol_table:
                    var = self.symbol_table[text]

                    # если тип var - аргумент или ф-ция
                    if type(var) in [ir.Argument, ir.Function]:
                        var_val = var
                    else:
                        # если nbg var - массив или структура
                        if isinstance(var.type.pointee, ir.ArrayType) or isinstance(var.type.pointee, ir.IdentifiedStructType):
                            # создание константы нуля
                            zero = ir.Constant(grCpp2Types.int, 0)
                            # var_val присваиваем р-т ф-ции gep (получение указателя на эл-т внутри э-та) с указанием начального индекса
                            var_val = self.builder.gep(var, [zero, zero])
                        else:
                            # var_val присваивается значение, загруженное из var с помощью load
                            var_val = self.builder.load(var)
                    return var_val, var

                else:
                    raise SemanticError(msg=f"Undefined identifier {text}", ctx=ctx)

            # если текущий контекст - строковый литерал
            elif ctx.StringLiteral():
                str_len = len(parse_escape(text[1:-1]))
                # возвращаем специальный объект, представляющий строку в виде массива символов
                return grCpp2Types.get_const_from_str(ir.ArrayType(grCpp2Types.char, str_len+1), const_value=text, ctx=ctx), None

            # проверяем тип данный на соответствие double, char или int
            # формируем соответствующий объект const_value
            else:
                if '.' in text:
                    const_value = grCpp2Types.get_const_from_str(grCpp2Types.double, text, ctx=ctx)

                elif text.startswith("'"):
                    const_value = grCpp2Types.get_const_from_str(grCpp2Types.char, text, ctx=ctx)

                else:
                    const_value = grCpp2Types.get_const_from_str(grCpp2Types.int, text, ctx=ctx)

                return const_value, None

    def visitPostfixExpression(self, ctx:grCpp2Parser.PostfixexpressionContext):
        if match_rule(ctx.children[0], grCpp2Parser.RULE_primaryexpression):
            # посещение правила primaryExpression
            return self.visit(ctx.primaryexpression())

        elif match_rule(ctx.children[0], grCpp2Parser.RULE_postfixexpression):
            # посещение правила postfixExpression
            lhs, lhs_ptr = self.visit(ctx.postfixexpression())
            op = ctx.children[1].getText()

            # если оператор - квадратная скобка
            if op == '[':
                # посещение правила expression
                # получение индекса массива
                array_index, _ = self.visit(ctx.expression())
                # приведение типа индекса к int
                array_index = grCpp2Types.cast_type(self.builder, target_type=grCpp2Types.int, value=array_index, ctx=ctx)
                zero = ir.Constant(grCpp2Types.int, 0)

                if type(lhs_ptr) is ir.Argument:
                    # создание массива array_indices, содержащего индекс array_index
                    array_indices = [array_index]
                else:
                    # создание массива array_indices, содержащего нулевой индекс и индекс array_index
                    array_indices = [zero, array_index]

                # генерация инструкции GEP (Get Element Pointer)
                # для проекции указателя на структуру lhs_ptr на указанные индексы
                # + сохранение р-та в ptr
                ptr = self.builder.gep(lhs_ptr, array_indices)
                return self.builder.load(ptr), ptr

            # если оператор - круглая скобка
            elif op == '(':
                if len(ctx.children) == 4:
                    # посещение правила argumentExpressionList
                    # получение аргументов
                    # !!!
                    args = self.visit(ctx.expressionlist())
                else:
                    # пустой список
                    args = []

                # приводим все аргументы к типу, ожидаемому на вызове (callee_arg.type)
                converted_args = [grCpp2Types.cast_type(self.builder, value=arg, target_type=callee_arg.type, ctx=ctx)
                                  for arg, callee_arg in zip(args, lhs.args)]

                if len(converted_args) < len(args):
                    converted_args += args[len(lhs.args):]

                return self.builder.call(lhs, converted_args), None

            # если оператор - унарный оператор ++ или --
            elif op in ["++", "--"]:
                one = lhs.type(1)

                if op == '++':
                    res = self.builder.add(lhs, one)
                else:
                    res = self.builder.sub(lhs, one)

                self.builder.store(res, lhs_ptr)
                return lhs, lhs_ptr

            # если оператор - точка
            elif op == '.':
                # получение текста узла Identifier
                elem_name = ctx.Identifier().getText()
                # получение имени типа данных, на который указывает указатель типа lhs_ptr
                target_name = lhs_ptr.type.pointee.name

                # получение индекса эл-та elem_name из структуры с именем target_name из словаря self.struct_reflection
                # сохранение его в array_index
                array_index = self.struct_reflection[target_name][elem_name]['index']
                array_index = ir.Constant(grCpp2Types.int, array_index)
                zero = ir.Constant(grCpp2Types.int, 0)

                array_indices = [zero, array_index]
                ptr = self.builder.gep(lhs_ptr, array_indices)

                # возврат значения, на которое указывает указатель ptr
                return self.builder.load(ptr), ptr

            else:
                # если оператор это ->
                # получение текста узла Identifier
                elem_name = ctx.Identifier().getText()
                # получение имени типа данных, на который указывает указатель типа lhs
                target_name = lhs.type.pointee.name

                if type(lhs.type.pointee) != ir.IdentifiedStructType:
                    raise SemanticError(msg="Illegal operation on -> operator!", ctx=ctx)

                array_index = self.struct_reflection[target_name][elem_name]['index']
                array_index = ir.Constant(grCpp2Types.int, array_index)
                zero = ir.Constant(grCpp2Types.int, 0)

                array_indices = [zero, array_index]
                ptr = self.builder.gep(lhs, array_indices)

                # возврат значения, на которое указывает указатель ptr
                return self.builder.load(ptr), ptr

        raise NotImplementedError("visitPostfixExpression isn't completely implemented yet..")
"""
    def visitArgumentExpressionList(self, ctx:grCpp2Parser.ArgumentExpressionListContext):
        if len(ctx.children) == 1:
            arg_list = []
        else:
            # посещение правила argumentExpressionList
            arg_list = self.visit(ctx.argumentExpressionList())
        # посещение правила assignmentExpression
        arg, _ = self.visit(ctx.assignmentExpression())
        arg_list.append(arg)

        return arg_list
"""
    def visitUnaryExpression(self, ctx:grCpp2Parser.UnaryexpressionContext):
        if match_rule(ctx.children[0], grCpp2Parser.RULE_postfixexpression):
            # посещение правила postfixExpression
            return self.visit(ctx.postfixexpression())

        elif match_texts(ctx.children[0], ['++', '--']):
            # посещение правила unaryExpression
            rhs, rhs_ptr = self.visit(ctx.unaryexpression())
            one = grCpp2Types.int(1)

            if match_text(ctx.children[0], '++'):
                res = self.builder.add(rhs, one)
            else:
                res = self.builder.sub(rhs, one)

            self.builder.store(res, rhs_ptr)
            return res, rhs_ptr

        elif match_rule(ctx.children[0], grCpp2Parser.RULE_unaryoperator):
            # посещение правила unaryOperator
            op = self.visit(ctx.unaryoperator())
            # посещение правила castExpression
            rhs, rhs_ptr = self.visit(ctx.castexpression())

            if op == '&':
                return rhs_ptr, None

            elif op == '*':
                return self.builder.load(rhs), rhs

            elif op == '+':
                return rhs, None

            elif op == '-':
                zero = ir.Constant(rhs.type, 0)
                res = self.builder.sub(zero, rhs)
                return res, None

            elif op == '!':
                origin = grCpp2Types.cast_type(self.builder, grCpp2Types.int, rhs, ctx)
                zero = grCpp2Types.int(0)
                res = self.builder.icmp_signed("==", zero, origin)
                res = self.builder.zext(res, grCpp2Types.int)
                return res, None

            elif op == '~':
                if grCpp2Types.is_int(rhs.type):
                    res = self.builder.not_(rhs)
                    return res, None
                else:
                    raise SemanticError(msg="Wrong type argument to bit-complement!", ctx=ctx)
            else:
                raise SemanticError(msg="Shouldn't reach here!", ctx=ctx)
        else:
            raise NotImplementedError("visitUnaryExpression isn't completely implemented yet..")

    def visitUnaryOperator(self, ctx:grCpp2Parser.UnaryoperatorContext):
        return ctx.getText()

    def visitCastExpression(self, ctx:grCpp2Parser.CastexpressionContext):
        return self.visit(ctx.unaryexpression())

    def visitMultiplicativeExpression(self, ctx:grCpp2Parser.MultiplicativeexpressionContext):
        # посещение правила castExpression
        rhs, rhs_ptr = self.visit(ctx.pmexpression())

        if match_rule(ctx.children[0], grCpp2Parser.RULE_castexpression):
            return rhs, rhs_ptr
        else:
            # посещение правила multiplicativeExpression
            lhs, lhs_ptr = self.visit(ctx.multiplicativeexpression())
            converted_target = lhs.type

            converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=converted_target, ctx=ctx)
            op = ctx.children[1].getText()

            if grCpp2Types.is_int(converted_target):
                if op == '*':
                    return self.builder.mul(lhs, converted_rhs), None

                elif op == '/':
                    return self.builder.sdiv(lhs, converted_rhs), None

                else:
                    return self.builder.srem(lhs, converted_rhs), None

            elif grCpp2Types.is_float(converted_target):
                if op == '*':
                    return self.builder.fmul(lhs, converted_rhs), None

                elif op == '/':
                    return self.builder.fdiv(lhs, converted_rhs), None

                else:
                    raise SemanticError(msg="Float doesn't support % operation", ctx=ctx)
            else:
                raise SemanticError(msg=f"Illegal operation: {str(lhs)} {op} {str(rhs)}", ctx=ctx)

    def visitAdditiveExpression(self, ctx:grCpp2Parser.AdditiveexpressionContext):
        # посещение правила multiplicativeExpression
        rhs, rhs_ptr = self.visit(ctx.multiplicativeexpression())
        if len(ctx.children) == 1:
            return rhs, rhs_ptr
        else:
            # посещение правила additiveExpression
            lhs, _ = self.visit(ctx.additiveexpression())
            op = ctx.children[1].getText()
            convert_target = lhs.type
            converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=convert_target, ctx=ctx)

            if grCpp2Types.is_int(convert_target):
                if op == '+':
                    return self.builder.add(lhs, converted_rhs), None
                else:
                    return self.builder.sub(lhs, converted_rhs), None

            elif grCpp2Types.is_float(convert_target):
                if op == '+':
                    return self.builder.fadd(lhs, converted_rhs), None
                else:
                    return self.builder.fsub(lhs, converted_rhs), None

            else:
                raise SemanticError(msg=f"Illegal operation: {str(lhs)} {op} {str(rhs)}", ctx=ctx)

    def visitShiftExpression(self, ctx:grCpp2Parser.ShiftexpressionContext):
        # посещение правила additiveExpression
        rhs, rhs_ptr = self.visit(ctx.additiveexpression())

        if len(ctx.children) == 1:
            return rhs, rhs_ptr
        else:
            # посещение правила shiftExpression
            lhs, _ = self.visit(ctx.shiftexpression())

            if ctx.children[1].getText() == '<<':
                return self.builder.shl(lhs, rhs), None
            else:
                return self.builder.ashr(lhs, rhs), None

    def visitRelationalExpression(self, ctx:grCpp2Parser.RelationalexpressionContext):
        return self.visit_relation_and_equality_expression(ctx)

    def visitEqualityExpression(self, ctx:grCpp2Parser.EqualityexpressionContext):
        return self.visit_relation_and_equality_expression(ctx)

    def visitAndExpression(self, ctx:grCpp2Parser.AndexpressionContext):
        # посещение правила equalityExpression
        rhs, rhs_ptr = self.visit(ctx.equalityexpression())

        if len(ctx.children) == 1:
            return rhs, rhs_ptr
        else:
            # посещение правила andExpression
            lhs, _ = self.visit(ctx.andexpression())
            return self.builder.and_(lhs, rhs), None

    def visitExclusiveOrExpression(self, ctx:grCpp2Parser.ExclusiveorexpressionContext):
        # посещение правила andExpression
        rhs, rhs_ptr = self.visit(ctx.andexpression())

        if len(ctx.children) == 1:
            return rhs, rhs_ptr
        else:
            # посещение правила exclusiveOrExpression
            lhs, _ = self.visit(ctx.exclusiveorexpression())
            return self.builder.xor(lhs, rhs), None

    def visitInclusiveOrExpression(self, ctx:grCpp2Parser.InclusiveorexpressionContext):
        # посещение правила exclusiveOrExpression
        rhs, rhs_ptr = self.visit(ctx.exclusiveorexpression())

        if len(ctx.children) == 1:
            return rhs, rhs_ptr
        else:
            # посещение правила inclusiveOrExpression
            lhs, _ = self.visit(ctx.inclusiveorexpression())
            return self.builder.or_(lhs, rhs), None

    def visitLogicalAndExpression(self, ctx:grCpp2Parser.LogicalandexpressionContext):
        if len(ctx.children) == 1:
            # посещение правила inclusiveOrExpression
            rhs, rhs_ptr = self.visit(ctx.inclusiveorexpression())
            return rhs, rhs_ptr

        else:
            # посещение правила logicalAndExpression
            lhs, _ = self.visit(ctx.logicalandexpression())
            converted_lhs = grCpp2Types.cast_type(self.builder, value=lhs, target_type=grCpp2Types.bool, ctx=ctx)
            result = self.builder.alloca(grCpp2Types.bool)

            with self.builder.if_else(converted_lhs) as (then, otherwise):
                with then:
                    # посещение правила inclusiveOrExpression
                    rhs, rhs_ptr = self.visit(ctx.inclusiveorexpression())
                    converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=grCpp2Types.bool, ctx=ctx)
                    self.builder.store(converted_rhs, result)
                with otherwise:
                    self.builder.store(grCpp2Types.bool(0), result)
            return self.builder.load(result), None

    def visitLogicalOrExpression(self, ctx:grCpp2Parser.LogicalorexpressionContext):
        if len(ctx.children) == 1:
            # посещение правила logicalAndExpression
            rhs, rhs_ptr = self.visit(ctx.logicalandexpression())
            return rhs, rhs_ptr
        else:
            # посещение правила logicalOrExpression
            lhs, _ = self.visit(ctx.logicalorexpression())
            converted_lhs = grCpp2Types.cast_type(self.builder, value=lhs, target_type=grCpp2Types.bool, ctx=ctx)
            result = self.builder.alloca(grCpp2Types.bool)

            with self.builder.if_else(converted_lhs) as (then, otherwise):
                with then:
                    self.builder.store(grCpp2Types.bool(1), result)
                with otherwise:
                    # посещение правила logicalAndExpression
                    rhs, rhs_ptr = self.visit(ctx.logicalandexpression())
                    converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=grCpp2Types.bool, ctx=ctx)
                    self.builder.store(converted_rhs, result)

            return self.builder.load(result), None

    def visitConditionalExpression(self, ctx:grCpp2Parser.ConditionalexpressionContext):
        if ctx.expression() is None:
            # посещение правила logicalOrExpression
            return self.visit(ctx.logicalorexpression())

        # посещение правила logicalOrExpression
        cond_val, _ = self.visit(ctx.logicalorexpression())
        converted_cond_val = grCpp2Types.cast_type(self.builder, target_type=grCpp2Types.bool, value=cond_val, ctx=ctx)

        # посещение правила expression
        true_val, _ = self.visit(ctx.expression())
        # посещение правила conditionalExpression
        false_val, _ = self.visit(ctx.assignmentexpression())

        ret_pointer = self.builder.alloca(true_val.type)

        with self.builder.if_else(converted_cond_val) as (then, otherwise):
            with then:
                self.builder.store(true_val, ret_pointer)
            with otherwise:
                self.builder.store(false_val, ret_pointer)

        ret_val = self.builder.load(ret_pointer)
        return ret_val, None

    def visitAssignmentExpression(self, ctx:grCpp2Parser.AssignmentexpressionContext):
        if match_rule(ctx.children[0], grCpp2Parser.RULE_conditionalexpression):
            # посещение правила conditionalExpression
            lhs, lhs_ptr = self.visit(ctx.conditionalexpression())
            return lhs, lhs_ptr

        elif match_rule(ctx.children[0], grCpp2Parser.RULE_unaryexpression):
            # посещение правила unaryExpression
            lhs, lhs_ptr = self.visit(ctx.unaryExpression())
            # посещение правила assignmentOperator
            op = self.visit(ctx.assignmentoperator())
            # посещение правила assignmentExpression
            rhs, _ = self.visit(ctx.assignmentExpression())

            if op == '=':
                converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=lhs_ptr.type.pointee, ctx=ctx)
                self.builder.store(converted_rhs, lhs_ptr)
                return converted_rhs, None
            else:
                target_type = lhs_ptr.type.pointee
                converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=target_type, ctx=ctx)

                if op == '+=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.add(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        new_value = self.builder.fadd(lhs, converted_rhs)

                elif op == '-=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.sub(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        new_value = self.builder.fsub(lhs, converted_rhs)

                elif op == '*=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.mul(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        new_value = self.builder.fmul(lhs, converted_rhs)

                elif op == '/=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.sdiv(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        new_value = self.builder.fdiv(lhs, converted_rhs)

                elif op == '%=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.srem(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        raise SemanticError(msg="Float doesn't support % operation..", ctx=ctx)

                elif op == '<<=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.shl(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        raise SemanticError(msg="Float doesn't support << operation", ctx=ctx)

                elif op == '>>=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.ashr(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        raise SemanticError(msg="Float doesn't support >> operation", ctx=ctx)

                elif op == '|=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.or_(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        raise SemanticError(msg="Float doesn't support | operation", ctx=ctx)

                elif op == '&=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.and_(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        raise SemanticError(msg="Float doesn't support & operation", ctx=ctx)

                elif op == '^=':
                    if grCpp2Types.is_int(target_type):
                        new_value = self.builder.xor(lhs, converted_rhs)
                    elif grCpp2Types.is_float(target_type):
                        raise SemanticError(msg="Float doesn't support ^ operation", ctx=ctx)

                self.builder.store(new_value, lhs_ptr)
                return new_value, None

    def visitAssignmentOperator(self, ctx:grCpp2Parser.AssignmentoperatorContext):
        return ctx.getText()

    def visitDeclaration(self, ctx:grCpp2Parser.DeclarationContext):
        # посещение правила declarationSpecifiers
        var_type = self.visit(ctx.declarationSpecifiers())
        self.current_base_type = var_type

        if len(ctx.children) == 3:
            # посещение правила initDeclaratorList
            init_declarator_list = self.visit(ctx.initDeclaratorList())

            if init_declarator_list is not None:
                old_type, name, old_llvm_type, args = init_declarator_list

                if old_type == self.FUNCTION_TYPE:
                    func_name, function_type = name, old_llvm_type
                    llvm_function = ir.Function(self.module, function_type, name=func_name)

                    if func_name not in self.symbol_table:
                        self.symbol_table[func_name] = llvm_function

    def visitDeclarationSpecifiers(self, ctx:grCpp2Parser.DeclarationSpecifiersContext):
        return self.visit(ctx.children[-1])

    def visitInitDeclaratorList(self, ctx:grCpp2Parser.InitdeclaratorlistContext):
        if len(ctx.children) == 3:
            # посещение правила initDeclaratorList
            self.visit(ctx.initdeclaratorlist())

        # посещение правила initDeclarator
        declarator = self.visit(ctx.initdeclarator())

        return declarator

    def visitInitDeclarator(self, ctx:grCpp2Parser.InitdeclaratorContext):
        # посещение правила declarator
        old_type, name, old_llvm_type, args = self.visit(ctx.declarator())

        if old_type == self.FUNCTION_TYPE:
            return old_type, name, old_llvm_type, args
        else:
            var_name, var_type = name, old_llvm_type

            if len(ctx.children) == 3:
                # посещение правила initializer
                init_val = self.visit(ctx.initializer())

                if isinstance(init_val, list):
                    converted_val = ir.Constant(var_type, init_val)

                else:
                    if isinstance(var_type, ir.PointerType) and isinstance(init_val.type, ir.ArrayType) and var_type.pointee == init_val.type.element:
                        var_type = init_val.type

                    converted_val = grCpp2Types.cast_type(self.builder, value=init_val, target_type=var_type, ctx=ctx)
            try:
                if self.is_global:
                    self.symbol_table[var_name] = ir.GlobalVariable(self.module, var_type, name=var_name)
                    self.symbol_table[var_name].linkage = "internal"

                    if len(ctx.children) == 3:
                        self.symbol_table[var_name].initializer = converted_val

                else:
                    self.symbol_table[var_name] = self.builder.alloca(var_type)

                    if len(ctx.children) == 3:
                        self.builder.store(converted_val, self.symbol_table[var_name])

            except RedefinitionError as e:
                raise SemanticError(msg=f"Redefinition variable {var_name}", ctx=ctx)

    def visitTypeSpecifier(self, ctx:grCpp2Parser.TypespecifierContext):
        if match_rule(ctx.children[0], grCpp2Parser.RULE_typespecifier):
            # typeSpecifier pointer
            # посещение правила typeSpecifier
            base_type = self.visit(ctx.typeSpecifier())

            if base_type == grCpp2Types.void:
                base_type = grCpp2Types.int
            return ir.PointerType(base_type)

        elif match_texts(ctx, grCpp2Types.str2type.keys()):
            return grCpp2Types.str2type[ctx.getText()]

        elif match_text(ctx, "unsigned"):
            return None

        elif match_rule(ctx.children[0], grCpp2Parser.RULE_typedefname):
            # посещение правила typedefName
            return self.visit(ctx.typedefName())

        elif match_rule(ctx.children[0], grCpp2Parser.RULE_structOrUnionSpecifier):
            # посещение правила structOrUnionSpecifier
            return self.visit(ctx.structOrUnionSpecifier())

        else:
            raise NotImplementedError("visitTypeSpecifier isn't completely implemented yet..")

    def visitStructOrUnionSpecifier(self, ctx:grCpp2Parser.StructOrUnionSpecifierContext):
        if len(ctx.children) >= 4:
            # посещение правила structOrUnion
            s_or_u = self.visit(ctx.structOrUnion())

            if s_or_u == 'struct':
                if(len(ctx.children) == 5):
                    if ctx.Identifier().getText() in self.struct_reflection.keys():
                        raise SemanticError(msg=f"Struct {ctx.Identifier().getText()} Redefinition", ctx=ctx)
                    else:
                        struct_name = ctx.Identifier().getText()
                        self.is_defining_struct = struct_name

                        # посещение правила structDeclarationList
                        tmp_list = self.visit(ctx.structDeclarationList())
                        self.struct_reflection[struct_name] = {}
                        index = 0
                        ele_list = []

                        for ele in tmp_list:
                            self.struct_reflection[struct_name][ele['name']] = {
                                'type': ele['type'],
                                'index': index
                            }
                            ele_list.append(ele['type'])
                            index = index + 1

                        new_struct = self.global_context.get_identified_type(name=struct_name)
                        new_struct.set_body(*ele_list)     # переменная ele_list будет распакована и её эл-ты будут переданы как отдельные аргументы методу set_body
                        self.is_defining_struct = ''
                        return new_struct
                else:
                    raise NotImplementedError("Anonymous struct isn't supported yet..")
            else:
                raise NotImplementedError("Union isn't supported yet..")
        else:
            # посещение правила structOrUnion
            s_or_u = self.visit(ctx.structOrUnion())

            if s_or_u == 'struct':
                struct_name = ctx.Identifier().getText()

                if (ctx.Identifier().getText() in self.struct_reflection.keys()) or self.is_defining_struct == struct_name:
                    new_struct = self.global_context.get_identified_type(name=struct_name)
                    return new_struct
                else:
                    raise SemanticError(msg=f"Struct {ctx.Identifier().getText()} Undefined", ctx=ctx)
            else:
                raise NotImplementedError("Union isn't supported yet..")

    def visitStructOrUnion(self, ctx:grCpp2Parser.StructOrUnionContext):
        return ctx.getText()

    def visitStructDeclarationList(self, ctx:grCpp2Parser.StructDeclarationListContext):
        if len(ctx.children) == 2:
            sub_list = self.visit(ctx.structDeclarationList())
            sub_dict = self.visit(ctx.structDeclaration())

            sub_list.append(sub_dict)
            return sub_list
        else:
            sub_dict = self.visit(ctx.structDeclaration())
            return [sub_dict]

    def visitStructDeclaration(self, ctx:grCpp2Parser.StructDeclarationContext):
        if ctx.staticAssertDeclaration() or ctx.structDeclaratorList():
            raise NotImplementedError("Complex struct declaration isn't supported yet..")
        return self.visit(ctx.specifierQualifierList())

    def visitSpecifierQualifierList(self, ctx:grCpp2Parser.SpecifierQualifierListContext):
        if ctx.typeQualifier():
            raise NotImplementedError("typeQualifier isn't supported yet..")

        if len(ctx.children) == 1:
            return self.visit(ctx.children[0])
        else:
            sub_dict = {'type': self.visit(ctx.children[0]),
                        'name': self.visit(ctx.children[1])}
            return sub_dict

    def visitDeclarator(self, ctx:grCpp2Parser.DeclaratorContext):
        # посещение правила directDeclarator
        old_type, name, old_llvm_type, args = self.visit(ctx.directDeclarator())

        if old_type == self.ARRAY_TYPE:
            for size in reversed(args):
                old_llvm_type = ir.ArrayType(element=old_llvm_type, count=size)
            return old_type, name, old_llvm_type, []
        else:
            return old_type, name, old_llvm_type, args

    def visitDirectDeclarator(self, ctx:grCpp2Parser.DirectDeclaratorContext):
        if len(ctx.children) == 1:
            return self.BASE_TYPE, ctx.getText(), self.current_base_type, []

        elif match_rule(ctx.children[0], grCpp2Parser.RULE_directDeclarator):
            # посещение правила directDeclarator
            old_type, name, old_llvm_type, size_list = self.visit(ctx.directDeclarator())

            if ctx.children[1].getText() == '[':
                if match_text(ctx.children[2], ']'):
                    new_llvm_type = ir.PointerType(old_llvm_type)
                    return old_type, name, new_llvm_type, size_list
                else:
                    try:
                        array_size = int(ctx.children[2].getText())
                    except:
                        raise SemanticError(msg=f"Doesn't support array dimension {ctx.children[2].getText()}", ctx=ctx)

                    if array_size <= 0:
                        raise SemanticError(msg="Array dimension must be positive!", ctx=ctx)

                    size_list.append(array_size)
                    return self.ARRAY_TYPE, name, old_llvm_type, size_list

            elif ctx.children[1].getText() == '(':
                if match_rule(ctx.children[2], grCpp2Parser.RULE_parameterTypeList):
                    # посещение правила parameterTypeList
                    (arg_names, arg_types), var_arg = self.visit(ctx.parameterTypeList())
                    new_llvm_type = ir.FunctionType(old_llvm_type, arg_types, var_arg=var_arg)
                    return self.FUNCTION_TYPE, name, new_llvm_type, arg_names

                elif match_rule(ctx.children[2], grCpp2Parser.RULE_identifierList):
                    raise NotImplementedError("directDeclarator '(' identifierList ')' isn't supported yet..")
                else:
                    arg_names = []
                    arg_types = []
                    new_llvm_type = ir.FunctionType(old_llvm_type, arg_types)
                    return self.FUNCTION_TYPE, name, new_llvm_type, arg_names
        else:
            raise NotImplementedError("visitDirectDeclarator isn't completely implemented yet..")

    def visitParameterTypeList(self, ctx:grCpp2Parser.ParameterTypeListContext):
        if len(ctx.children) == 3:
            return self.visit(ctx.parameterList()), True
        else:
            return self.visit(ctx.parameterList()), False

    def visitParameterList(self, ctx:grCpp2Parser.ParameterListContext):
        if len(ctx.children) == 1:
            arg_names = []
            arg_types = []
        else:
            # посещение правила parameterList
            arg_names, arg_types = self.visit(ctx.parameterList())

        # посещение правила parameterDeclaration
        arg_name, arg_type = self.visit(ctx.parameterDeclaration())

        arg_names.append(arg_name)
        arg_types.append(arg_type)

        return arg_names, arg_types

    def visitParameterDeclaration(self, ctx:grCpp2Parser.ParameterdeclarationContext):
        # посещение правила declarationSpecifiers
        self.current_base_type = self.visit(ctx.declarationSpecifiers())
        # посещение правила declarator
        _, arg_name, arg_type, _ = self.visit(ctx.declarator())
        return arg_name, arg_type

    def visitTypedefName(self, ctx:grCpp2Parser.TypedefnameContext):
        return ctx.getText()

    def visitInitializer(self, ctx:grCpp2Parser.InitializerContext):
        if len(ctx.children) == 1:
            # посещение правила assignmentExpression
            value, _ = self.visit(ctx.assignmentExpression())
            return value
        else:
            # посещение правила initializerList
            return self.visit(ctx.initializerList())

    def visitInitializerList(self, ctx:grCpp2Parser.InitializerlistContext):
        if len(ctx.children) == 1:
            init_list = []
        else:
            # посещение правила initializerList
            init_list = self.visit(ctx.initializerlist())
        # посещение правила initializer
        init_list.append(self.visit(ctx.initializer()))

        return init_list

    def visitLabeledStatement(self, ctx:grCpp2Parser.LabeledstatementContext):
        if ctx.children[0].getText() == 'Identifier':
            raise NotImplementedError("Identifier label isn't supported yet..")

        if len(ctx.children) == 4:
            block_name, label = self.switch_context[2] + str(len(self.switch_context[0])),  ctx.constantexpression()
        else:
            block_name, label = self.switch_context[2] + 'default', 'default'

        content_block = self.builder.append_basic_block(name=block_name)
        self.builder.position_at_end(content_block)

        if self.switch_context[1] is not None:
            cur_block = self.builder.block
            self.builder.position_at_end(self.switch_context[1])

            try:
                self.builder.branch(cur_block)
            except AssertionError:
                pass

            self.builder.position_at_end(cur_block)

        self.switch_context[1] = self.builder.block
        self.symbol_table.enter_scope()
        self.visit(ctx.statement())
        self.symbol_table.exit_scope()
        self.switch_context[0].append((label, content_block))

    def visitBlockItem(self, ctx:grCpp2Parser.BlockItemContext):
        try:
            self.visit(ctx.children[0])
        except SemanticError as e:
            self.error_listener.register_semantic_error(e)

    def visitSelectionStatement(self, ctx:grCpp2Parser.SelectionstatementContext):
        if ctx.children[0].getText() == 'if':
            # посещение правила expression
            cond_val, _ = self.visit(ctx.expression())
            converted_cond_val = grCpp2Types.cast_type(self.builder, target_type=grCpp2Types.bool, value=cond_val, ctx=ctx)

            statements = ctx.statement()
            self.symbol_table.enter_scope()

            if len(statements) == 2:
                with self.builder.if_else(converted_cond_val) as (then, otherwise):
                    with then:
                        self.visit(statements[0])
                    with otherwise:
                        self.visit(statements[1])
            else:
                with self.builder.if_then(converted_cond_val):
                    self.visit(statements[0])

            self.symbol_table.exit_scope()

        else:
            name_prefix = self.builder.block.name
            start_block = self.builder.block
            end_block = self.builder.append_basic_block(name=name_prefix+'.end_switch')
            old_context = self.switch_context
            old_break = self.break_block
            self.break_block = end_block

            # посещение правила expression
            cond_val, _ = self.visit(ctx.expression())
            self.switch_context = [[], None, name_prefix + '.case.']
            self.visit(ctx.statement(0))

            try:
                self.builder.branch(end_block)
            except AssertionError:
                pass
            label_blocks = []

            for i in range(len(self.switch_context[0])):
                label_blocks.append(self.builder.append_basic_block(name=name_prefix+'.label.' + str(i)))

            self.builder.position_at_end(start_block)
            self.builder.branch(label_blocks[0])

            for i, (label, _block) in enumerate(self.switch_context[0]):
                self.builder.position_at_end(label_blocks[i])

                if isinstance(label, str):
                    self.builder.branch(_block)
                else:
                    constant, _ = self.visit(label)
                    condition = self.builder.icmp_signed(cmpop='==', lhs=cond_val, rhs=constant)

                    if i == len(self.switch_context[0]) - 1:
                        false_block = end_block
                    else:
                        false_block = label_blocks[i + 1]
                    self.builder.cbranch(condition, _block, false_block)

            self.builder.position_at_start(end_block)
            self.switch_context = old_context
            self.break_block = old_break

    def visitIterationStatement(self, ctx:grCpp2Parser.IterationstatementContext):
        self.symbol_table.enter_scope()
        name_prefix = self.builder.block.name

        do_block = self.builder.append_basic_block(name=name_prefix+"loop_do")
        cond_block = self.builder.append_basic_block(name=name_prefix+".loop_cond")
        loop_block = self.builder.append_basic_block(name=name_prefix+".loop_body")
        end_block = self.builder.append_basic_block(name=name_prefix+".loop_end")
        update_block = self.builder.append_basic_block(name=name_prefix+".loop_update")

        last_continue, last_break = self.continue_block, self.break_block
        self.continue_block, self.break_block = update_block, end_block

        iteration_type = ctx.children[0].getText()

        cond_expression = None
        update_expression = None

        if iteration_type == "while":
            cond_expression = ctx.expression()

        elif iteration_type == "for":
            cond_expression, update_expression = self.visit(ctx.forCondition())

        elif iteration_type == "do":
            cond_expression = ctx.expression()

        else:
            raise SemanticError(msg="Cannot recognize loop form!", ctx=ctx)

        self.builder.branch(do_block)
        self.builder.position_at_start(do_block)

        if iteration_type == "do":
            self.visit(ctx.statement())

        self.builder.branch(cond_block)
        self.builder.position_at_start(cond_block)

        if cond_expression:
            cond_val, _ = self.visit(cond_expression)
            converted_cond_val = grCpp2Types.cast_type(self.builder, target_type=grCpp2Types.bool, value=cond_val, ctx=ctx)
            self.builder.cbranch(converted_cond_val, loop_block, end_block)
        else:
            self.builder.branch(loop_block)

        self.builder.position_at_start(loop_block)
        self.visit(ctx.statement())
        self.builder.branch(update_block)

        self.builder.position_at_start(update_block)

        if update_expression:
            self.visit(update_expression)

        self.builder.branch(cond_block)

        self.builder.position_at_start(end_block)
        self.continue_block = last_continue
        self.break_block = last_break
        self.symbol_table.exit_scope()

    def visitForCondition(self, ctx:grCpp2Parser.ForConditionContext):
        idx = 0

        if match_rule(ctx.children[idx], grCpp2Parser.RULE_forDeclaration):
            idx += 2
            # посещение правила forDeclaration
            self.visit(ctx.forDeclaration())

        elif match_rule(ctx.children[idx], grCpp2Parser.RULE_expression):
            idx += 2
            # посещение правила expression
            self.visit(ctx.expression())
        else:
            idx += 1

        cond_expression = None
        update_expression = None

        if match_rule(ctx.children[idx], grCpp2Parser.RULE_forExpression):
            cond_expression = ctx.children[idx]
            idx += 2
        else:
            idx += 1

        if idx == len(ctx.children) - 1:
            update_expression = ctx.children[idx]

        return cond_expression, update_expression

    def visitForDeclaration(self, ctx:grCpp2Parser.ForDeclarationContext):
        # посещение правила declarationSpecifiers
        var_type = self.visit(ctx.declarationSpecifiers())
        self.current_base_type = var_type

        if len(ctx.children) == 2:
            # посещение правила initDeclaratorList
            self.visit(ctx.initDeclaratorList())

    def visitJumpStatement(self, ctx:grCpp2Parser.JumpstatementContext):
        jump_str = ctx.children[0].getText()

        if jump_str == "return":
            if len(ctx.children) == 3:
                # посещение правила expression
                ret_val, _ = self.visit(ctx.expression())
                converted_val = grCpp2Types.cast_type(self.builder, target_type=self.builder.function.type.pointee.return_type, value=ret_val, ctx=ctx)
                self.builder.ret(converted_val)
            else:
                self.builder.ret_void()

        elif jump_str == 'continue':
            if self.continue_block is None:
                raise SemanticError(msg="Continue can not be used here!", ctx=ctx)
            self.builder.branch(self.continue_block)

        elif jump_str == 'break':
            if self.break_block is None:
                raise SemanticError(msg="Break can not be used here!", ctx=ctx)
            self.builder.branch(self.break_block)
        else:
            raise NotImplementedError("goto isn't supported yet..")

    def visit_relation_and_equality_expression(self, ctx):
        rhs, rhs_ptr = self.visit(ctx.children[-1])

        if len(ctx.children) == 1:
            return rhs, rhs_ptr
        else:
            lhs, _ = self.visit(ctx.children[0])
            op = ctx.children[1].getText()
            converted_target = lhs.type

            if type(lhs.type) == ir.PointerType and type(rhs.type) == ir.IntType:
                converted_target = grCpp2Types.int
                converted_rhs = rhs
                lhs = grCpp2Types.cast_type(self.builder, value=lhs, target_type=grCpp2Types.int, ctx=ctx)
            else:
                converted_rhs = grCpp2Types.cast_type(self.builder, value=rhs, target_type=converted_target, ctx=ctx)

            if grCpp2Types.is_int(converted_target):
                return self.builder.icmp_signed(cmpop=op, lhs=lhs, rhs=converted_rhs), None

            elif grCpp2Types.is_float(converted_target):
                return self.builder.fcmp_ordered(cmpop=op, lhs=lhs, rhs=converted_rhs), None

            else:
                raise SemanticError(msg=f"Unknown relation expression: {str(lhs)} {str(op)} {str(rhs)}", ctx=ctx)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(repr(self.module))   # записываем в файл строковое представление объекта self.module


# генерация LLVM IR для соответствующего TinyC-файла
def generate_ir(input_filename, output_filename):
    lexer = grCpp2Lexer(FileStream(input_filename))
    stream = CommonTokenStream(lexer)
    parser = grCpp2Parser(stream)

    error_listener = grCpp2ErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.compilationUnit()

    generator = grCpp2Generator(error_listener)
    generator.visit(tree)
    generator.save(output_filename)

    if len(error_listener.errors) == 0:
        return True
    else:
        error_listener.print_errors()
        return False