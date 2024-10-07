# Generated from D:/cpp/parser/grCpp2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grCpp2Parser import grCpp2Parser
else:
    from grCpp2Parser import grCpp2Parser

# This class defines a complete generic visitor for a parse tree produced by grCpp2Parser.

class grCpp2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by grCpp2Parser#translationunit.
    def visitTranslationunit(self, ctx:grCpp2Parser.TranslationunitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#primaryexpression.
    def visitPrimaryexpression(self, ctx:grCpp2Parser.PrimaryexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#idexpression.
    def visitIdexpression(self, ctx:grCpp2Parser.IdexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#unqualifiedid.
    def visitUnqualifiedid(self, ctx:grCpp2Parser.UnqualifiedidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#qualifiedid.
    def visitQualifiedid(self, ctx:grCpp2Parser.QualifiedidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#nestednamespecifier.
    def visitNestednamespecifier(self, ctx:grCpp2Parser.NestednamespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#lambdaexpression.
    def visitLambdaexpression(self, ctx:grCpp2Parser.LambdaexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#lambdaintroducer.
    def visitLambdaintroducer(self, ctx:grCpp2Parser.LambdaintroducerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#lambdacapture.
    def visitLambdacapture(self, ctx:grCpp2Parser.LambdacaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#capturedefault.
    def visitCapturedefault(self, ctx:grCpp2Parser.CapturedefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#capturelist.
    def visitCapturelist(self, ctx:grCpp2Parser.CapturelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#capture.
    def visitCapture(self, ctx:grCpp2Parser.CaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#simplecapture.
    def visitSimplecapture(self, ctx:grCpp2Parser.SimplecaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#initcapture.
    def visitInitcapture(self, ctx:grCpp2Parser.InitcaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#lambdadeclarator.
    def visitLambdadeclarator(self, ctx:grCpp2Parser.LambdadeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#postfixexpression.
    def visitPostfixexpression(self, ctx:grCpp2Parser.PostfixexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typeidofexpr.
    def visitTypeidofexpr(self, ctx:grCpp2Parser.TypeidofexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typeidofthetypeid.
    def visitTypeidofthetypeid(self, ctx:grCpp2Parser.TypeidofthetypeidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#expressionlist.
    def visitExpressionlist(self, ctx:grCpp2Parser.ExpressionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#pseudodestructorname.
    def visitPseudodestructorname(self, ctx:grCpp2Parser.PseudodestructornameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#unaryexpression.
    def visitUnaryexpression(self, ctx:grCpp2Parser.UnaryexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#unaryoperator.
    def visitUnaryoperator(self, ctx:grCpp2Parser.UnaryoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#newexpression.
    def visitNewexpression(self, ctx:grCpp2Parser.NewexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#newplacement.
    def visitNewplacement(self, ctx:grCpp2Parser.NewplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#newtypeid.
    def visitNewtypeid(self, ctx:grCpp2Parser.NewtypeidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#newdeclarator.
    def visitNewdeclarator(self, ctx:grCpp2Parser.NewdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#noptrnewdeclarator.
    def visitNoptrnewdeclarator(self, ctx:grCpp2Parser.NoptrnewdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#newinitializer.
    def visitNewinitializer(self, ctx:grCpp2Parser.NewinitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#deleteexpression.
    def visitDeleteexpression(self, ctx:grCpp2Parser.DeleteexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#noexceptexpression.
    def visitNoexceptexpression(self, ctx:grCpp2Parser.NoexceptexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#castexpression.
    def visitCastexpression(self, ctx:grCpp2Parser.CastexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#pmexpression.
    def visitPmexpression(self, ctx:grCpp2Parser.PmexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#multiplicativeexpression.
    def visitMultiplicativeexpression(self, ctx:grCpp2Parser.MultiplicativeexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#additiveexpression.
    def visitAdditiveexpression(self, ctx:grCpp2Parser.AdditiveexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#shiftexpression.
    def visitShiftexpression(self, ctx:grCpp2Parser.ShiftexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#shiftoperator.
    def visitShiftoperator(self, ctx:grCpp2Parser.ShiftoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#relationalexpression.
    def visitRelationalexpression(self, ctx:grCpp2Parser.RelationalexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#equalityexpression.
    def visitEqualityexpression(self, ctx:grCpp2Parser.EqualityexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#andexpression.
    def visitAndexpression(self, ctx:grCpp2Parser.AndexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#exclusiveorexpression.
    def visitExclusiveorexpression(self, ctx:grCpp2Parser.ExclusiveorexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#inclusiveorexpression.
    def visitInclusiveorexpression(self, ctx:grCpp2Parser.InclusiveorexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#logicalandexpression.
    def visitLogicalandexpression(self, ctx:grCpp2Parser.LogicalandexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#logicalorexpression.
    def visitLogicalorexpression(self, ctx:grCpp2Parser.LogicalorexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#conditionalexpression.
    def visitConditionalexpression(self, ctx:grCpp2Parser.ConditionalexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#assignmentexpression.
    def visitAssignmentexpression(self, ctx:grCpp2Parser.AssignmentexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#assignmentoperator.
    def visitAssignmentoperator(self, ctx:grCpp2Parser.AssignmentoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#expression.
    def visitExpression(self, ctx:grCpp2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#constantexpression.
    def visitConstantexpression(self, ctx:grCpp2Parser.ConstantexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#statement.
    def visitStatement(self, ctx:grCpp2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#labeledstatement.
    def visitLabeledstatement(self, ctx:grCpp2Parser.LabeledstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#expressionstatement.
    def visitExpressionstatement(self, ctx:grCpp2Parser.ExpressionstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#compoundstatement.
    def visitCompoundstatement(self, ctx:grCpp2Parser.CompoundstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#statementseq.
    def visitStatementseq(self, ctx:grCpp2Parser.StatementseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#selectionstatement.
    def visitSelectionstatement(self, ctx:grCpp2Parser.SelectionstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#condition.
    def visitCondition(self, ctx:grCpp2Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#iterationstatement.
    def visitIterationstatement(self, ctx:grCpp2Parser.IterationstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#forinitstatement.
    def visitForinitstatement(self, ctx:grCpp2Parser.ForinitstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#forrangedeclaration.
    def visitForrangedeclaration(self, ctx:grCpp2Parser.ForrangedeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#forrangeinitializer.
    def visitForrangeinitializer(self, ctx:grCpp2Parser.ForrangeinitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#jumpstatement.
    def visitJumpstatement(self, ctx:grCpp2Parser.JumpstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declarationstatement.
    def visitDeclarationstatement(self, ctx:grCpp2Parser.DeclarationstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declarationseq.
    def visitDeclarationseq(self, ctx:grCpp2Parser.DeclarationseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declaration.
    def visitDeclaration(self, ctx:grCpp2Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#blockdeclaration.
    def visitBlockdeclaration(self, ctx:grCpp2Parser.BlockdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#aliasdeclaration.
    def visitAliasdeclaration(self, ctx:grCpp2Parser.AliasdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#simpledeclaration.
    def visitSimpledeclaration(self, ctx:grCpp2Parser.SimpledeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#static_assertdeclaration.
    def visitStatic_assertdeclaration(self, ctx:grCpp2Parser.Static_assertdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#emptydeclaration.
    def visitEmptydeclaration(self, ctx:grCpp2Parser.EmptydeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributedeclaration.
    def visitAttributedeclaration(self, ctx:grCpp2Parser.AttributedeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declspecifier.
    def visitDeclspecifier(self, ctx:grCpp2Parser.DeclspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declspecifierseq.
    def visitDeclspecifierseq(self, ctx:grCpp2Parser.DeclspecifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#storageclassspecifier.
    def visitStorageclassspecifier(self, ctx:grCpp2Parser.StorageclassspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#functionspecifier.
    def visitFunctionspecifier(self, ctx:grCpp2Parser.FunctionspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typedefname.
    def visitTypedefname(self, ctx:grCpp2Parser.TypedefnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typespecifier.
    def visitTypespecifier(self, ctx:grCpp2Parser.TypespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#trailingtypespecifier.
    def visitTrailingtypespecifier(self, ctx:grCpp2Parser.TrailingtypespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typespecifierseq.
    def visitTypespecifierseq(self, ctx:grCpp2Parser.TypespecifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#trailingtypespecifierseq.
    def visitTrailingtypespecifierseq(self, ctx:grCpp2Parser.TrailingtypespecifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#simpletypespecifier.
    def visitSimpletypespecifier(self, ctx:grCpp2Parser.SimpletypespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#thetypename.
    def visitThetypename(self, ctx:grCpp2Parser.ThetypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#decltypespecifier.
    def visitDecltypespecifier(self, ctx:grCpp2Parser.DecltypespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#elaboratedtypespecifier.
    def visitElaboratedtypespecifier(self, ctx:grCpp2Parser.ElaboratedtypespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumname.
    def visitEnumname(self, ctx:grCpp2Parser.EnumnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumspecifier.
    def visitEnumspecifier(self, ctx:grCpp2Parser.EnumspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumhead.
    def visitEnumhead(self, ctx:grCpp2Parser.EnumheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#opaqueenumdeclaration.
    def visitOpaqueenumdeclaration(self, ctx:grCpp2Parser.OpaqueenumdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumkey.
    def visitEnumkey(self, ctx:grCpp2Parser.EnumkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumbase.
    def visitEnumbase(self, ctx:grCpp2Parser.EnumbaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumeratorlist.
    def visitEnumeratorlist(self, ctx:grCpp2Parser.EnumeratorlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumeratordefinition.
    def visitEnumeratordefinition(self, ctx:grCpp2Parser.EnumeratordefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#enumerator.
    def visitEnumerator(self, ctx:grCpp2Parser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#namespacename.
    def visitNamespacename(self, ctx:grCpp2Parser.NamespacenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#originalnamespacename.
    def visitOriginalnamespacename(self, ctx:grCpp2Parser.OriginalnamespacenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#namespacedefinition.
    def visitNamespacedefinition(self, ctx:grCpp2Parser.NamespacedefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#namednamespacedefinition.
    def visitNamednamespacedefinition(self, ctx:grCpp2Parser.NamednamespacedefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#originalnamespacedefinition.
    def visitOriginalnamespacedefinition(self, ctx:grCpp2Parser.OriginalnamespacedefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#extensionnamespacedefinition.
    def visitExtensionnamespacedefinition(self, ctx:grCpp2Parser.ExtensionnamespacedefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#unnamednamespacedefinition.
    def visitUnnamednamespacedefinition(self, ctx:grCpp2Parser.UnnamednamespacedefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#namespacebody.
    def visitNamespacebody(self, ctx:grCpp2Parser.NamespacebodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#namespacealias.
    def visitNamespacealias(self, ctx:grCpp2Parser.NamespacealiasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#namespacealiasdefinition.
    def visitNamespacealiasdefinition(self, ctx:grCpp2Parser.NamespacealiasdefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#qualifiednamespacespecifier.
    def visitQualifiednamespacespecifier(self, ctx:grCpp2Parser.QualifiednamespacespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#usingdeclaration.
    def visitUsingdeclaration(self, ctx:grCpp2Parser.UsingdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#usingdirective.
    def visitUsingdirective(self, ctx:grCpp2Parser.UsingdirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#asmdefinition.
    def visitAsmdefinition(self, ctx:grCpp2Parser.AsmdefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#linkagespecification.
    def visitLinkagespecification(self, ctx:grCpp2Parser.LinkagespecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributespecifierseq.
    def visitAttributespecifierseq(self, ctx:grCpp2Parser.AttributespecifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributespecifier.
    def visitAttributespecifier(self, ctx:grCpp2Parser.AttributespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#alignmentspecifier.
    def visitAlignmentspecifier(self, ctx:grCpp2Parser.AlignmentspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributelist.
    def visitAttributelist(self, ctx:grCpp2Parser.AttributelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attribute.
    def visitAttribute(self, ctx:grCpp2Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributetoken.
    def visitAttributetoken(self, ctx:grCpp2Parser.AttributetokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributescopedtoken.
    def visitAttributescopedtoken(self, ctx:grCpp2Parser.AttributescopedtokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributenamespace.
    def visitAttributenamespace(self, ctx:grCpp2Parser.AttributenamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#attributeargumentclause.
    def visitAttributeargumentclause(self, ctx:grCpp2Parser.AttributeargumentclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#balancedtokenseq.
    def visitBalancedtokenseq(self, ctx:grCpp2Parser.BalancedtokenseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#balancedtoken.
    def visitBalancedtoken(self, ctx:grCpp2Parser.BalancedtokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#initdeclaratorlist.
    def visitInitdeclaratorlist(self, ctx:grCpp2Parser.InitdeclaratorlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#initdeclarator.
    def visitInitdeclarator(self, ctx:grCpp2Parser.InitdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declarator.
    def visitDeclarator(self, ctx:grCpp2Parser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#ptrdeclarator.
    def visitPtrdeclarator(self, ctx:grCpp2Parser.PtrdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#noptrdeclarator.
    def visitNoptrdeclarator(self, ctx:grCpp2Parser.NoptrdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#parametersandqualifiers.
    def visitParametersandqualifiers(self, ctx:grCpp2Parser.ParametersandqualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#trailingreturntype.
    def visitTrailingreturntype(self, ctx:grCpp2Parser.TrailingreturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#ptroperator.
    def visitPtroperator(self, ctx:grCpp2Parser.PtroperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#cvqualifierseq.
    def visitCvqualifierseq(self, ctx:grCpp2Parser.CvqualifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#cvqualifier.
    def visitCvqualifier(self, ctx:grCpp2Parser.CvqualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#refqualifier.
    def visitRefqualifier(self, ctx:grCpp2Parser.RefqualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#declaratorid.
    def visitDeclaratorid(self, ctx:grCpp2Parser.DeclaratoridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#thetypeid.
    def visitThetypeid(self, ctx:grCpp2Parser.ThetypeidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#abstractdeclarator.
    def visitAbstractdeclarator(self, ctx:grCpp2Parser.AbstractdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#ptrabstractdeclarator.
    def visitPtrabstractdeclarator(self, ctx:grCpp2Parser.PtrabstractdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#noptrabstractdeclarator.
    def visitNoptrabstractdeclarator(self, ctx:grCpp2Parser.NoptrabstractdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#abstractpackdeclarator.
    def visitAbstractpackdeclarator(self, ctx:grCpp2Parser.AbstractpackdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#noptrabstractpackdeclarator.
    def visitNoptrabstractpackdeclarator(self, ctx:grCpp2Parser.NoptrabstractpackdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#parameterdeclarationclause.
    def visitParameterdeclarationclause(self, ctx:grCpp2Parser.ParameterdeclarationclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#parameterdeclarationlist.
    def visitParameterdeclarationlist(self, ctx:grCpp2Parser.ParameterdeclarationlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#parameterdeclaration.
    def visitParameterdeclaration(self, ctx:grCpp2Parser.ParameterdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#functiondefinition.
    def visitFunctiondefinition(self, ctx:grCpp2Parser.FunctiondefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#functionbody.
    def visitFunctionbody(self, ctx:grCpp2Parser.FunctionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#initializer.
    def visitInitializer(self, ctx:grCpp2Parser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#braceorequalinitializer.
    def visitBraceorequalinitializer(self, ctx:grCpp2Parser.BraceorequalinitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#initializerclause.
    def visitInitializerclause(self, ctx:grCpp2Parser.InitializerclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#initializerlist.
    def visitInitializerlist(self, ctx:grCpp2Parser.InitializerlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#bracedinitlist.
    def visitBracedinitlist(self, ctx:grCpp2Parser.BracedinitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classname.
    def visitClassname(self, ctx:grCpp2Parser.ClassnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classspecifier.
    def visitClassspecifier(self, ctx:grCpp2Parser.ClassspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classhead.
    def visitClasshead(self, ctx:grCpp2Parser.ClassheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classheadname.
    def visitClassheadname(self, ctx:grCpp2Parser.ClassheadnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classvirtspecifier.
    def visitClassvirtspecifier(self, ctx:grCpp2Parser.ClassvirtspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classkey.
    def visitClasskey(self, ctx:grCpp2Parser.ClasskeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#memberspecification.
    def visitMemberspecification(self, ctx:grCpp2Parser.MemberspecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#memberdeclaration.
    def visitMemberdeclaration(self, ctx:grCpp2Parser.MemberdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#memberdeclaratorlist.
    def visitMemberdeclaratorlist(self, ctx:grCpp2Parser.MemberdeclaratorlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#memberdeclarator.
    def visitMemberdeclarator(self, ctx:grCpp2Parser.MemberdeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#virtspecifierseq.
    def visitVirtspecifierseq(self, ctx:grCpp2Parser.VirtspecifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#virtspecifier.
    def visitVirtspecifier(self, ctx:grCpp2Parser.VirtspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#purespecifier.
    def visitPurespecifier(self, ctx:grCpp2Parser.PurespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#baseclause.
    def visitBaseclause(self, ctx:grCpp2Parser.BaseclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#basespecifierlist.
    def visitBasespecifierlist(self, ctx:grCpp2Parser.BasespecifierlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#basespecifier.
    def visitBasespecifier(self, ctx:grCpp2Parser.BasespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#classordecltype.
    def visitClassordecltype(self, ctx:grCpp2Parser.ClassordecltypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#basetypespecifier.
    def visitBasetypespecifier(self, ctx:grCpp2Parser.BasetypespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#accessspecifier.
    def visitAccessspecifier(self, ctx:grCpp2Parser.AccessspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#conversionfunctionid.
    def visitConversionfunctionid(self, ctx:grCpp2Parser.ConversionfunctionidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#conversiontypeid.
    def visitConversiontypeid(self, ctx:grCpp2Parser.ConversiontypeidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#conversiondeclarator.
    def visitConversiondeclarator(self, ctx:grCpp2Parser.ConversiondeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#ctorinitializer.
    def visitCtorinitializer(self, ctx:grCpp2Parser.CtorinitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#meminitializerlist.
    def visitMeminitializerlist(self, ctx:grCpp2Parser.MeminitializerlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#meminitializer.
    def visitMeminitializer(self, ctx:grCpp2Parser.MeminitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#meminitializerid.
    def visitMeminitializerid(self, ctx:grCpp2Parser.MeminitializeridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#operatorfunctionid.
    def visitOperatorfunctionid(self, ctx:grCpp2Parser.OperatorfunctionidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#literaloperatorid.
    def visitLiteraloperatorid(self, ctx:grCpp2Parser.LiteraloperatoridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templatedeclaration.
    def visitTemplatedeclaration(self, ctx:grCpp2Parser.TemplatedeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templateparameterlist.
    def visitTemplateparameterlist(self, ctx:grCpp2Parser.TemplateparameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templateparameter.
    def visitTemplateparameter(self, ctx:grCpp2Parser.TemplateparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typeparameter.
    def visitTypeparameter(self, ctx:grCpp2Parser.TypeparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#simpletemplateid.
    def visitSimpletemplateid(self, ctx:grCpp2Parser.SimpletemplateidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templateid.
    def visitTemplateid(self, ctx:grCpp2Parser.TemplateidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templatename.
    def visitTemplatename(self, ctx:grCpp2Parser.TemplatenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templateargumentlist.
    def visitTemplateargumentlist(self, ctx:grCpp2Parser.TemplateargumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#templateargument.
    def visitTemplateargument(self, ctx:grCpp2Parser.TemplateargumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typenamespecifier.
    def visitTypenamespecifier(self, ctx:grCpp2Parser.TypenamespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#explicitinstantiation.
    def visitExplicitinstantiation(self, ctx:grCpp2Parser.ExplicitinstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#explicitspecialization.
    def visitExplicitspecialization(self, ctx:grCpp2Parser.ExplicitspecializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#tryblock.
    def visitTryblock(self, ctx:grCpp2Parser.TryblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#functiontryblock.
    def visitFunctiontryblock(self, ctx:grCpp2Parser.FunctiontryblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#handlerseq.
    def visitHandlerseq(self, ctx:grCpp2Parser.HandlerseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#handler.
    def visitHandler(self, ctx:grCpp2Parser.HandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#exceptiondeclaration.
    def visitExceptiondeclaration(self, ctx:grCpp2Parser.ExceptiondeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#throwexpression.
    def visitThrowexpression(self, ctx:grCpp2Parser.ThrowexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#exceptionspecification.
    def visitExceptionspecification(self, ctx:grCpp2Parser.ExceptionspecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#dynamicexceptionspecification.
    def visitDynamicexceptionspecification(self, ctx:grCpp2Parser.DynamicexceptionspecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#typeidlist.
    def visitTypeidlist(self, ctx:grCpp2Parser.TypeidlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#noexceptspecification.
    def visitNoexceptspecification(self, ctx:grCpp2Parser.NoexceptspecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#theoperator.
    def visitTheoperator(self, ctx:grCpp2Parser.TheoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#literal.
    def visitLiteral(self, ctx:grCpp2Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#booleanliteral.
    def visitBooleanliteral(self, ctx:grCpp2Parser.BooleanliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#pointerliteral.
    def visitPointerliteral(self, ctx:grCpp2Parser.PointerliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grCpp2Parser#userdefinedliteral.
    def visitUserdefinedliteral(self, ctx:grCpp2Parser.UserdefinedliteralContext):
        return self.visitChildren(ctx)



del grCpp2Parser