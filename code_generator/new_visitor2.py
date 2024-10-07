from antlr4 import *
import llvmlite.ir as ir

from parser.grCpp2Visitor import grCpp2Visitor
from parser.grCpp2Lexer import grCpp2Lexer
from parser.grCpp2Parser import grCpp2Parser

from code_generator.types import grCpp2Types
from code_generator.symbol_table import SymbolTable, RedefinitionError
from code_generator.util import *
from code_generator.errors import *

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

    def visitTranslationunit(self, ctx:grCpp2Parser.TranslationunitContext):
    def visitPrimaryexpression(self, ctx:grCpp2Parser.PrimaryexpressionContext):

    def visitIdexpression(self, ctx:grCpp2Parser.IdexpressionContext):
    def visitUnqualifiedid(self, ctx:grCpp2Parser.UnqualifiedidContext):
    def visitQualifiedid(self, ctx:grCpp2Parser.QualifiedidContext):
    def visitNestednamespecifier(self, ctx:grCpp2Parser.NestednamespecifierContext):
    def visitLambdaexpression(self, ctx:grCpp2Parser.LambdaexpressionContext):
    def visitLambdaintroducer(self, ctx:grCpp2Parser.LambdaintroducerContext):
    def visitLambdacapture(self, ctx:grCpp2Parser.LambdacaptureContext):
    def visitCapturedefault(self, ctx:grCpp2Parser.CapturedefaultContext):
    def visitCapturelist(self, ctx:grCpp2Parser.CapturelistContext):
    def visitCapture(self, ctx:grCpp2Parser.CaptureContext):
    def visitSimplecapture(self, ctx:grCpp2Parser.SimplecaptureContext):
    def visitInitcapture(self, ctx:grCpp2Parser.InitcaptureContext):
    def visitLambdadeclarator(self, ctx:grCpp2Parser.LambdadeclaratorContext):
    def visitPostfixexpression(self, ctx:grCpp2Parser.PostfixexpressionContext):
    def visitTypeidofexpr(self, ctx:grCpp2Parser.TypeidofexprContext):
    def visitTypeidofthetypeid(self, ctx:grCpp2Parser.TypeidofthetypeidContext):
    def visitExpressionlist(self, ctx:grCpp2Parser.ExpressionlistContext):
    def visitPseudodestructorname(self, ctx:grCpp2Parser.PseudodestructornameContext):
    def visitUnaryexpression(self, ctx:grCpp2Parser.UnaryexpressionContext):
    def visitUnaryoperator(self, ctx:grCpp2Parser.UnaryoperatorContext):
        return ctx.getText()
    def visitNewexpression(self, ctx:grCpp2Parser.NewexpressionContext):
    def visitNewplacement(self, ctx:grCpp2Parser.NewplacementContext):
    def visitNewtypeid(self, ctx:grCpp2Parser.NewtypeidContext):
    def visitNewdeclarator(self, ctx:grCpp2Parser.NewdeclaratorContext):
    def visitNoptrnewdeclarator(self, ctx:grCpp2Parser.NoptrnewdeclaratorContext):
    def visitNewinitializer(self, ctx:grCpp2Parser.NewinitializerContext):
    def visitDeleteexpression(self, ctx:grCpp2Parser.DeleteexpressionContext):
    def visitNoexceptexpression(self, ctx:grCpp2Parser.NoexceptexpressionContext):
    def visitCastexpression(self, ctx:grCpp2Parser.CastexpressionContext):
        return self.visit(ctx.unaryexpression())
    def visitPmexpression(self, ctx:grCpp2Parser.PmexpressionContext):
    def visitMultiplicativeexpression(self, ctx:grCpp2Parser.MultiplicativeexpressionContext):
    def visitAdditiveexpression(self, ctx:grCpp2Parser.AdditiveexpressionContext):
    def visitShiftexpression(self, ctx:grCpp2Parser.ShiftexpressionContext):
    def visitShiftoperator(self, ctx:grCpp2Parser.ShiftoperatorContext):
    def visitRelationalexpression(self, ctx:grCpp2Parser.RelationalexpressionContext):
    def visitEqualityexpression(self, ctx:grCpp2Parser.EqualityexpressionContext):
    def visitAndexpression(self, ctx:grCpp2Parser.AndexpressionContext):
    def visitExclusiveorexpression(self, ctx:grCpp2Parser.ExclusiveorexpressionContext):
    def visitInclusiveorexpression(self, ctx:grCpp2Parser.InclusiveorexpressionContext):
    def visitLogicalandexpression(self, ctx:grCpp2Parser.LogicalandexpressionContext):
    def visitLogicalorexpression(self, ctx:grCpp2Parser.LogicalorexpressionContext):
    def visitConditionalexpression(self, ctx:grCpp2Parser.ConditionalexpressionContext):
    def visitAssignmentexpression(self, ctx:grCpp2Parser.AssignmentexpressionContext):
    def visitAssignmentoperator(self, ctx:grCpp2Parser.AssignmentoperatorContext):
    def visitExpression(self, ctx:grCpp2Parser.ExpressionContext):
    def visitConstantexpression(self, ctx:grCpp2Parser.ConstantexpressionContext):
    def visitStatement(self, ctx:grCpp2Parser.StatementContext):
    def visitLabeledstatement(self, ctx:grCpp2Parser.LabeledstatementContext):
    def visitExpressionstatement(self, ctx:grCpp2Parser.ExpressionstatementContext):
    def visitCompoundstatement(self, ctx:grCpp2Parser.CompoundstatementContext):
    def visitStatementseq(self, ctx:grCpp2Parser.StatementseqContext):
    def visitSelectionstatement(self, ctx:grCpp2Parser.SelectionstatementContext):
    def visitCondition(self, ctx:grCpp2Parser.ConditionContext):
    def visitIterationstatement(self, ctx:grCpp2Parser.IterationstatementContext):
    def visitForinitstatement(self, ctx:grCpp2Parser.ForinitstatementContext):
    def visitForrangedeclaration(self, ctx:grCpp2Parser.ForrangedeclarationContext):
    def visitForrangeinitializer(self, ctx:grCpp2Parser.ForrangeinitializerContext):
    def visitJumpstatement(self, ctx:grCpp2Parser.JumpstatementContext):
    def visitDeclarationstatement(self, ctx:grCpp2Parser.DeclarationstatementContext):
    def visitDeclarationseq(self, ctx:grCpp2Parser.DeclarationseqContext):
    def visitDeclaration(self, ctx:grCpp2Parser.DeclarationContext):
    def visitBlockdeclaration(self, ctx:grCpp2Parser.BlockdeclarationContext):
    def visitAliasdeclaration(self, ctx:grCpp2Parser.AliasdeclarationContext):
    def visitSimpledeclaration(self, ctx:grCpp2Parser.SimpledeclarationContext):
    def visitStatic_assertdeclaration(self, ctx:grCpp2Parser.Static_assertdeclarationContext):
    def visitEmptydeclaration(self, ctx:grCpp2Parser.EmptydeclarationContext):
    def visitAttributedeclaration(self, ctx:grCpp2Parser.AttributedeclarationContext):
    def visitDeclspecifier(self, ctx:grCpp2Parser.DeclspecifierContext):
    def visitDeclspecifierseq(self, ctx:grCpp2Parser.DeclspecifierseqContext):
    def visitStorageclassspecifier(self, ctx:grCpp2Parser.StorageclassspecifierContext):
    def visitFunctionspecifier(self, ctx:grCpp2Parser.FunctionspecifierContext):
    def visitTypedefname(self, ctx:grCpp2Parser.TypedefnameContext):
    def visitTypespecifier(self, ctx:grCpp2Parser.TypespecifierContext):
    def visitTrailingtypespecifier(self, ctx:grCpp2Parser.TrailingtypespecifierContext):
    def visitTypespecifierseq(self, ctx:grCpp2Parser.TypespecifierseqContext):
    def visitTrailingtypespecifierseq(self, ctx:grCpp2Parser.TrailingtypespecifierseqContext):
    def visitSimpletypespecifier(self, ctx:grCpp2Parser.SimpletypespecifierContext):
    def visitThetypename(self, ctx:grCpp2Parser.ThetypenameContext):
    def visitDecltypespecifier(self, ctx:grCpp2Parser.DecltypespecifierContext):
    def visitElaboratedtypespecifier(self, ctx:grCpp2Parser.ElaboratedtypespecifierContext):
    def visitEnumname(self, ctx:grCpp2Parser.EnumnameContext):
    def visitEnumspecifier(self, ctx:grCpp2Parser.EnumspecifierContext):

    def visitEnumhead(self, ctx:grCpp2Parser.EnumheadContext):

    def visitOpaqueenumdeclaration(self, ctx:grCpp2Parser.OpaqueenumdeclarationContext):

    def visitEnumkey(self, ctx:grCpp2Parser.EnumkeyContext):

    def visitEnumbase(self, ctx:grCpp2Parser.EnumbaseContext):

    def visitEnumeratorlist(self, ctx:grCpp2Parser.EnumeratorlistContext):

    def visitEnumeratordefinition(self, ctx:grCpp2Parser.EnumeratordefinitionContext):

    def visitEnumerator(self, ctx:grCpp2Parser.EnumeratorContext):

    def visitNamespacename(self, ctx:grCpp2Parser.NamespacenameContext):

    def visitOriginalnamespacename(self, ctx:grCpp2Parser.OriginalnamespacenameContext):

    def visitNamespacedefinition(self, ctx:grCpp2Parser.NamespacedefinitionContext):

    def visitNamednamespacedefinition(self, ctx:grCpp2Parser.NamednamespacedefinitionContext):

    def visitOriginalnamespacedefinition(self, ctx:grCpp2Parser.OriginalnamespacedefinitionContext):

    def visitExtensionnamespacedefinition(self, ctx:grCpp2Parser.ExtensionnamespacedefinitionContext):

    def visitUnnamednamespacedefinition(self, ctx:grCpp2Parser.UnnamednamespacedefinitionContext):

    def visitNamespacebody(self, ctx:grCpp2Parser.NamespacebodyContext):

    def visitNamespacealias(self, ctx:grCpp2Parser.NamespacealiasContext):

    def visitNamespacealiasdefinition(self, ctx:grCpp2Parser.NamespacealiasdefinitionContext):

    def visitQualifiednamespacespecifier(self, ctx:grCpp2Parser.QualifiednamespacespecifierContext):

    def visitUsingdeclaration(self, ctx:grCpp2Parser.UsingdeclarationContext):

    def visitUsingdirective(self, ctx:grCpp2Parser.UsingdirectiveContext):

    def visitAsmdefinition(self, ctx:grCpp2Parser.AsmdefinitionContext):

    def visitLinkagespecification(self, ctx:grCpp2Parser.LinkagespecificationContext):

    def visitAttributespecifierseq(self, ctx:grCpp2Parser.AttributespecifierseqContext):

    def visitAttributespecifier(self, ctx:grCpp2Parser.AttributespecifierContext):

    def visitAlignmentspecifier(self, ctx:grCpp2Parser.AlignmentspecifierContext):

    def visitAttributelist(self, ctx:grCpp2Parser.AttributelistContext):

    def visitAttribute(self, ctx:grCpp2Parser.AttributeContext):

    def visitAttributetoken(self, ctx:grCpp2Parser.AttributetokenContext):

    def visitAttributescopedtoken(self, ctx:grCpp2Parser.AttributescopedtokenContext):

    def visitAttributenamespace(self, ctx:grCpp2Parser.AttributenamespaceContext):

    def visitAttributeargumentclause(self, ctx:grCpp2Parser.AttributeargumentclauseContext):

    def visitBalancedtokenseq(self, ctx:grCpp2Parser.BalancedtokenseqContext):

    def visitBalancedtoken(self, ctx:grCpp2Parser.BalancedtokenContext):

    def visitInitdeclaratorlist(self, ctx:grCpp2Parser.InitdeclaratorlistContext):

    def visitInitdeclarator(self, ctx:grCpp2Parser.InitdeclaratorContext):

    def visitDeclarator(self, ctx:grCpp2Parser.DeclaratorContext):

    def visitPtrdeclarator(self, ctx:grCpp2Parser.PtrdeclaratorContext):

    def visitNoptrdeclarator(self, ctx:grCpp2Parser.NoptrdeclaratorContext):

    def visitParametersandqualifiers(self, ctx:grCpp2Parser.ParametersandqualifiersContext):

    def visitTrailingreturntype(self, ctx:grCpp2Parser.TrailingreturntypeContext):

    def visitPtroperator(self, ctx:grCpp2Parser.PtroperatorContext):

    def visitCvqualifierseq(self, ctx:grCpp2Parser.CvqualifierseqContext):

    def visitCvqualifier(self, ctx:grCpp2Parser.CvqualifierContext):

    def visitRefqualifier(self, ctx:grCpp2Parser.RefqualifierContext):

    def visitDeclaratorid(self, ctx:grCpp2Parser.DeclaratoridContext):

    def visitThetypeid(self, ctx:grCpp2Parser.ThetypeidContext):

    def visitPtrabstractdeclarator(self, ctx:grCpp2Parser.PtrabstractdeclaratorContext):

    def visitAbstractpackdeclarator(self, ctx:grCpp2Parser.AbstractpackdeclaratorContext):
    def visitNoptrabstractpackdeclarator(self, ctx:grCpp2Parser.NoptrabstractpackdeclaratorContext):
    def visitParameterdeclarationclause(self, ctx:grCpp2Parser.ParameterdeclarationclauseContext):
    def visitParameterdeclarationlist(self, ctx:grCpp2Parser.ParameterdeclarationlistContext):
    def visitParameterdeclaration(self, ctx:grCpp2Parser.ParameterdeclarationContext):
    def visitFunctiondefinition(self, ctx:grCpp2Parser.FunctiondefinitionContext):
    def visitFunctionbody(self, ctx:grCpp2Parser.FunctionbodyContext):
    def visitInitializer(self, ctx:grCpp2Parser.InitializerContext):
    def visitBraceorequalinitializer(self, ctx:grCpp2Parser.BraceorequalinitializerContext):
    def visitInitializerclause(self, ctx:grCpp2Parser.InitializerclauseContext):
    def visitInitializerlist(self, ctx:grCpp2Parser.InitializerlistContext):
    def visitBracedinitlist(self, ctx:grCpp2Parser.BracedinitlistContext):
    def visitClassname(self, ctx:grCpp2Parser.ClassnameContext):
    def visitClassspecifier(self, ctx:grCpp2Parser.ClassspecifierContext):
    def visitClasshead(self, ctx:grCpp2Parser.ClassheadContext):
    def visitClassheadname(self, ctx:grCpp2Parser.ClassheadnameContext):
    def visitClassvirtspecifier(self, ctx:grCpp2Parser.ClassvirtspecifierContext):
    def visitClasskey(self, ctx:grCpp2Parser.ClasskeyContext):
    def visitMemberspecification(self, ctx:grCpp2Parser.MemberspecificationContext):
    def visitMemberdeclaration(self, ctx:grCpp2Parser.MemberdeclarationContext):
    def visitMemberdeclaratorlist(self, ctx:grCpp2Parser.MemberdeclaratorlistContext):
    def visitMemberdeclarator(self, ctx:grCpp2Parser.MemberdeclaratorContext):
    def visitVirtspecifierseq(self, ctx:grCpp2Parser.VirtspecifierseqContext):
    def visitVirtspecifier(self, ctx:grCpp2Parser.VirtspecifierContext):
    def visitPurespecifier(self, ctx:grCpp2Parser.PurespecifierContext):
    def visitBaseclause(self, ctx:grCpp2Parser.BaseclauseContext):
    def visitBasespecifierlist(self, ctx:grCpp2Parser.BasespecifierlistContext):
    def visitBasespecifier(self, ctx:grCpp2Parser.BasespecifierContext):
    def visitClassordecltype(self, ctx:grCpp2Parser.ClassordecltypeContext):
    def visitBasetypespecifier(self, ctx:grCpp2Parser.BasetypespecifierContext):
    def visitAccessspecifier(self, ctx:grCpp2Parser.AccessspecifierContext):
    def visitConversionfunctionid(self, ctx:grCpp2Parser.ConversionfunctionidContext):
    def visitConversiontypeid(self, ctx:grCpp2Parser.ConversiontypeidContext):
    def visitConversiondeclarator(self, ctx:grCpp2Parser.ConversiondeclaratorContext):
    def visitCtorinitializer(self, ctx:grCpp2Parser.CtorinitializerContext):
    def visitMeminitializerlist(self, ctx:grCpp2Parser.MeminitializerlistContext):
    def visitMeminitializer(self, ctx:grCpp2Parser.MeminitializerContext):
    def visitMeminitializerid(self, ctx:grCpp2Parser.MeminitializeridContext):
    def visitOperatorfunctionid(self, ctx:grCpp2Parser.OperatorfunctionidContext):
    def visitLiteraloperatorid(self, ctx:grCpp2Parser.LiteraloperatoridContext):
    def visitTemplatedeclaration(self, ctx:grCpp2Parser.TemplatedeclarationContext):
    def visitTemplateparameterlist(self, ctx:grCpp2Parser.TemplateparameterlistContext):
    def visitTemplateparameter(self, ctx:grCpp2Parser.TemplateparameterContext):
    def visitTypeparameter(self, ctx:grCpp2Parser.TypeparameterContext):
    def visitSimpletemplateid(self, ctx:grCpp2Parser.SimpletemplateidContext):
    def visitTemplateid(self, ctx:grCpp2Parser.TemplateidContext):
    def visitTemplatename(self, ctx:grCpp2Parser.TemplatenameContext):
    def visitTemplateargumentlist(self, ctx:grCpp2Parser.TemplateargumentlistContext):
    def visitTemplateargument(self, ctx:grCpp2Parser.TemplateargumentContext):
    def visitTypenamespecifier(self, ctx:grCpp2Parser.TypenamespecifierContext):
    def visitExplicitinstantiation(self, ctx:grCpp2Parser.ExplicitinstantiationContext):
    def visitExplicitspecialization(self, ctx:grCpp2Parser.ExplicitspecializationContext):
    def visitTryblock(self, ctx:grCpp2Parser.TryblockContext):
    def visitFunctiontryblock(self, ctx:grCpp2Parser.FunctiontryblockContext):
    def visitHandlerseq(self, ctx:grCpp2Parser.HandlerseqContext):
    def visitHandler(self, ctx:grCpp2Parser.HandlerContext):
    def visitExceptiondeclaration(self, ctx:grCpp2Parser.ExceptiondeclarationContext):
    def visitThrowexpression(self, ctx:grCpp2Parser.ThrowexpressionContext):
    def visitExceptionspecification(self, ctx:grCpp2Parser.ExceptionspecificationContext):
    def visitDynamicexceptionspecification(self, ctx:grCpp2Parser.DynamicexceptionspecificationContext):
    def visitTypeidlist(self, ctx:grCpp2Parser.TypeidlistContext):
    def visitNoexceptspecification(self, ctx:grCpp2Parser.NoexceptspecificationContext):
    def visitTheoperator(self, ctx:grCpp2Parser.TheoperatorContext):
    def visitLiteral(self, ctx:grCpp2Parser.LiteralContext):
    def visitBooleanliteral(self, ctx:grCpp2Parser.BooleanliteralContext):
    def visitPointerliteral(self, ctx:grCpp2Parser.PointerliteralContext):
    def visitUserdefinedliteral(self, ctx:grCpp2Parser.UserdefinedliteralContext):
