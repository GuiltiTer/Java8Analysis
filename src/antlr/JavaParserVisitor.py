# Generated from C:/Users/mohammad/PycharmProjects/ControlFlowGraph/grammar\JavaParser.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .JavaParser import JavaParser
else:
    from JavaParser import JavaParser


# This class defines a complete generic visitor for a parse tree produced by JavaParser.

class JavaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaParser#literal1.
    def visitLiteral1(self, ctx: JavaParser.Literal1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#literal2.
    def visitLiteral2(self, ctx: JavaParser.Literal2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#literal3.
    def visitLiteral3(self, ctx: JavaParser.Literal3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#literal4.
    def visitLiteral4(self, ctx: JavaParser.Literal4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#literal5.
    def visitLiteral5(self, ctx: JavaParser.Literal5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#literal6.
    def visitLiteral6(self, ctx: JavaParser.Literal6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primitiveType1.
    def visitPrimitiveType1(self, ctx: JavaParser.PrimitiveType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primitiveType2.
    def visitPrimitiveType2(self, ctx: JavaParser.PrimitiveType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#numericType1.
    def visitNumericType1(self, ctx: JavaParser.NumericType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#numericType2.
    def visitNumericType2(self, ctx: JavaParser.NumericType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#integralType1.
    def visitIntegralType1(self, ctx: JavaParser.IntegralType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#integralType2.
    def visitIntegralType2(self, ctx: JavaParser.IntegralType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#integralType3.
    def visitIntegralType3(self, ctx: JavaParser.IntegralType3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#integralType4.
    def visitIntegralType4(self, ctx: JavaParser.IntegralType4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#integralType5.
    def visitIntegralType5(self, ctx: JavaParser.IntegralType5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#floatingPointType1.
    def visitFloatingPointType1(self, ctx: JavaParser.FloatingPointType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#floatingPointType2.
    def visitFloatingPointType2(self, ctx: JavaParser.FloatingPointType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#referenceType1.
    def visitReferenceType1(self, ctx: JavaParser.ReferenceType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#referenceType2.
    def visitReferenceType2(self, ctx: JavaParser.ReferenceType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#referenceType3.
    def visitReferenceType3(self, ctx: JavaParser.ReferenceType3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx: JavaParser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classType1.
    def visitClassType1(self, ctx: JavaParser.ClassType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classType2.
    def visitClassType2(self, ctx: JavaParser.ClassType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classType_lf_classOrInterfaceType.
    def visitClassType_lf_classOrInterfaceType(self, ctx: JavaParser.ClassType_lf_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classType_lfno_classOrInterfaceType.
    def visitClassType_lfno_classOrInterfaceType(self, ctx: JavaParser.ClassType_lfno_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceType.
    def visitInterfaceType(self, ctx: JavaParser.InterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceType_lf_classOrInterfaceType.
    def visitInterfaceType_lf_classOrInterfaceType(self, ctx: JavaParser.InterfaceType_lf_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceType_lfno_classOrInterfaceType.
    def visitInterfaceType_lfno_classOrInterfaceType(self,
                                                     ctx: JavaParser.InterfaceType_lfno_classOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeVariable.
    def visitTypeVariable(self, ctx: JavaParser.TypeVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayType1.
    def visitArrayType1(self, ctx: JavaParser.ArrayType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayType2.
    def visitArrayType2(self, ctx: JavaParser.ArrayType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayType3.
    def visitArrayType3(self, ctx: JavaParser.ArrayType3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#dims.
    def visitDims(self, ctx: JavaParser.DimsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeParameter.
    def visitTypeParameter(self, ctx: JavaParser.TypeParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeParameterModifier.
    def visitTypeParameterModifier(self, ctx: JavaParser.TypeParameterModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeBound1.
    def visitTypeBound1(self, ctx: JavaParser.TypeBound1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeBound2.
    def visitTypeBound2(self, ctx: JavaParser.TypeBound2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#additionalBound.
    def visitAdditionalBound(self, ctx: JavaParser.AdditionalBoundContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeArguments.
    def visitTypeArguments(self, ctx: JavaParser.TypeArgumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeArgumentList.
    def visitTypeArgumentList(self, ctx: JavaParser.TypeArgumentListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeArgument1.
    def visitTypeArgument1(self, ctx: JavaParser.TypeArgument1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeArgument2.
    def visitTypeArgument2(self, ctx: JavaParser.TypeArgument2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#wildcard.
    def visitWildcard(self, ctx: JavaParser.WildcardContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#wildcardBounds1.
    def visitWildcardBounds1(self, ctx: JavaParser.WildcardBounds1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#wildcardBounds2.
    def visitWildcardBounds2(self, ctx: JavaParser.WildcardBounds2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#packageName2.
    def visitPackageName2(self, ctx: JavaParser.PackageName2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#packageName1.
    def visitPackageName1(self, ctx: JavaParser.PackageName1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeName1.
    def visitTypeName1(self, ctx: JavaParser.TypeName1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeName2.
    def visitTypeName2(self, ctx: JavaParser.TypeName2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#packageOrTypeName1.
    def visitPackageOrTypeName1(self, ctx: JavaParser.PackageOrTypeName1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#packageOrTypeName2.
    def visitPackageOrTypeName2(self, ctx: JavaParser.PackageOrTypeName2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#expressionName1.
    def visitExpressionName1(self, ctx: JavaParser.ExpressionName1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#expressionName2.
    def visitExpressionName2(self, ctx: JavaParser.ExpressionName2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodName.
    def visitMethodName(self, ctx: JavaParser.MethodNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#ambiguousName1.
    def visitAmbiguousName1(self, ctx: JavaParser.AmbiguousName1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#ambiguousName2.
    def visitAmbiguousName2(self, ctx: JavaParser.AmbiguousName2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#compilationUnit.
    def visitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx: JavaParser.PackageDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#packageModifier.
    def visitPackageModifier(self, ctx: JavaParser.PackageModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#importDeclaration1.
    def visitImportDeclaration1(self, ctx: JavaParser.ImportDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#importDeclaration2.
    def visitImportDeclaration2(self, ctx: JavaParser.ImportDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#importDeclaration3.
    def visitImportDeclaration3(self, ctx: JavaParser.ImportDeclaration3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#importDeclaration4.
    def visitImportDeclaration4(self, ctx: JavaParser.ImportDeclaration4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#singleTypeImportDeclaration.
    def visitSingleTypeImportDeclaration(self, ctx: JavaParser.SingleTypeImportDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeImportOnDemandDeclaration.
    def visitTypeImportOnDemandDeclaration(self, ctx: JavaParser.TypeImportOnDemandDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#singleStaticImportDeclaration.
    def visitSingleStaticImportDeclaration(self, ctx: JavaParser.SingleStaticImportDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#staticImportOnDemandDeclaration.
    def visitStaticImportOnDemandDeclaration(self, ctx: JavaParser.StaticImportOnDemandDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeDeclaration1.
    def visitTypeDeclaration1(self, ctx: JavaParser.TypeDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeDeclaration2.
    def visitTypeDeclaration2(self, ctx: JavaParser.TypeDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeDeclaration3.
    def visitTypeDeclaration3(self, ctx: JavaParser.TypeDeclaration3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classDeclaration1.
    def visitClassDeclaration1(self, ctx: JavaParser.ClassDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classDeclaration2.
    def visitClassDeclaration2(self, ctx: JavaParser.ClassDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx: JavaParser.NormalClassDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier1.
    def visitClassModifier1(self, ctx: JavaParser.ClassModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier2.
    def visitClassModifier2(self, ctx: JavaParser.ClassModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier3.
    def visitClassModifier3(self, ctx: JavaParser.ClassModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier4.
    def visitClassModifier4(self, ctx: JavaParser.ClassModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier5.
    def visitClassModifier5(self, ctx: JavaParser.ClassModifier5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier6.
    def visitClassModifier6(self, ctx: JavaParser.ClassModifier6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier7.
    def visitClassModifier7(self, ctx: JavaParser.ClassModifier7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classModifier8.
    def visitClassModifier8(self, ctx: JavaParser.ClassModifier8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeParameters.
    def visitTypeParameters(self, ctx: JavaParser.TypeParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeParameterList.
    def visitTypeParameterList(self, ctx: JavaParser.TypeParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#superclass.
    def visitSuperclass(self, ctx: JavaParser.SuperclassContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#superinterfaces.
    def visitSuperinterfaces(self, ctx: JavaParser.SuperinterfacesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceTypeList.
    def visitInterfaceTypeList(self, ctx: JavaParser.InterfaceTypeListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classBody.
    def visitClassBody(self, ctx: JavaParser.ClassBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classBodyDeclaration1.
    def visitClassBodyDeclaration1(self, ctx: JavaParser.ClassBodyDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classBodyDeclaration2.
    def visitClassBodyDeclaration2(self, ctx: JavaParser.ClassBodyDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classBodyDeclaration3.
    def visitClassBodyDeclaration3(self, ctx: JavaParser.ClassBodyDeclaration3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classBodyDeclaration4.
    def visitClassBodyDeclaration4(self, ctx: JavaParser.ClassBodyDeclaration4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classMemberDeclaration1.
    def visitClassMemberDeclaration1(self, ctx: JavaParser.ClassMemberDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classMemberDeclaration2.
    def visitClassMemberDeclaration2(self, ctx: JavaParser.ClassMemberDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classMemberDeclaration3.
    def visitClassMemberDeclaration3(self, ctx: JavaParser.ClassMemberDeclaration3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classMemberDeclaration4.
    def visitClassMemberDeclaration4(self, ctx: JavaParser.ClassMemberDeclaration4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classMemberDeclaration5.
    def visitClassMemberDeclaration5(self, ctx: JavaParser.ClassMemberDeclaration5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx: JavaParser.FieldDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier1.
    def visitFieldModifier1(self, ctx: JavaParser.FieldModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier2.
    def visitFieldModifier2(self, ctx: JavaParser.FieldModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier3.
    def visitFieldModifier3(self, ctx: JavaParser.FieldModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier4.
    def visitFieldModifier4(self, ctx: JavaParser.FieldModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier5.
    def visitFieldModifier5(self, ctx: JavaParser.FieldModifier5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier6.
    def visitFieldModifier6(self, ctx: JavaParser.FieldModifier6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier7.
    def visitFieldModifier7(self, ctx: JavaParser.FieldModifier7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldModifier8.
    def visitFieldModifier8(self, ctx: JavaParser.FieldModifier8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableDeclaratorList.
    def visitVariableDeclaratorList(self, ctx: JavaParser.VariableDeclaratorListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx: JavaParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx: JavaParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableInitializer1.
    def visitVariableInitializer1(self, ctx: JavaParser.VariableInitializer1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableInitializer2.
    def visitVariableInitializer2(self, ctx: JavaParser.VariableInitializer2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannType1.
    def visitUnannType1(self, ctx: JavaParser.UnannType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannType2.
    def visitUnannType2(self, ctx: JavaParser.UnannType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannPrimitiveType1.
    def visitUnannPrimitiveType1(self, ctx: JavaParser.UnannPrimitiveType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannPrimitiveType2.
    def visitUnannPrimitiveType2(self, ctx: JavaParser.UnannPrimitiveType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannReferenceType1.
    def visitUnannReferenceType1(self, ctx: JavaParser.UnannReferenceType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannReferenceType2.
    def visitUnannReferenceType2(self, ctx: JavaParser.UnannReferenceType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannReferenceType3.
    def visitUnannReferenceType3(self, ctx: JavaParser.UnannReferenceType3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannClassOrInterfaceType.
    def visitUnannClassOrInterfaceType(self, ctx: JavaParser.UnannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannClassType1.
    def visitUnannClassType1(self, ctx: JavaParser.UnannClassType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannClassType2.
    def visitUnannClassType2(self, ctx: JavaParser.UnannClassType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannClassType_lf_unannClassOrInterfaceType.
    def visitUnannClassType_lf_unannClassOrInterfaceType(self,
                                                         ctx: JavaParser.UnannClassType_lf_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannClassType_lfno_unannClassOrInterfaceType.
    def visitUnannClassType_lfno_unannClassOrInterfaceType(self,
                                                           ctx: JavaParser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannInterfaceType.
    def visitUnannInterfaceType(self, ctx: JavaParser.UnannInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannInterfaceType_lf_unannClassOrInterfaceType.
    def visitUnannInterfaceType_lf_unannClassOrInterfaceType(self,
                                                             ctx: JavaParser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannInterfaceType_lfno_unannClassOrInterfaceType.
    def visitUnannInterfaceType_lfno_unannClassOrInterfaceType(self,
                                                               ctx: JavaParser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannTypeVariable.
    def visitUnannTypeVariable(self, ctx: JavaParser.UnannTypeVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannArrayType1.
    def visitUnannArrayType1(self, ctx: JavaParser.UnannArrayType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannArrayType2.
    def visitUnannArrayType2(self, ctx: JavaParser.UnannArrayType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unannArrayType3.
    def visitUnannArrayType3(self, ctx: JavaParser.UnannArrayType3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier1.
    def visitMethodModifier1(self, ctx: JavaParser.MethodModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier2.
    def visitMethodModifier2(self, ctx: JavaParser.MethodModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier3.
    def visitMethodModifier3(self, ctx: JavaParser.MethodModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier4.
    def visitMethodModifier4(self, ctx: JavaParser.MethodModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier5.
    def visitMethodModifier5(self, ctx: JavaParser.MethodModifier5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier6.
    def visitMethodModifier6(self, ctx: JavaParser.MethodModifier6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier7.
    def visitMethodModifier7(self, ctx: JavaParser.MethodModifier7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier8.
    def visitMethodModifier8(self, ctx: JavaParser.MethodModifier8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier9.
    def visitMethodModifier9(self, ctx: JavaParser.MethodModifier9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodModifier10.
    def visitMethodModifier10(self, ctx: JavaParser.MethodModifier10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodHeader1.
    def visitMethodHeader1(self, ctx: JavaParser.MethodHeader1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodHeader2.
    def visitMethodHeader2(self, ctx: JavaParser.MethodHeader2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#result1.
    def visitResult1(self, ctx: JavaParser.Result1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#result2.
    def visitResult2(self, ctx: JavaParser.Result2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodDeclarator.
    def visitMethodDeclarator(self, ctx: JavaParser.MethodDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#formalParameterList1.
    def visitFormalParameterList1(self, ctx: JavaParser.FormalParameterList1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#formalParameterList2.
    def visitFormalParameterList2(self, ctx: JavaParser.FormalParameterList2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#formalParameterList3.
    def visitFormalParameterList3(self, ctx: JavaParser.FormalParameterList3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#formalParameters1.
    def visitFormalParameters1(self, ctx: JavaParser.FormalParameters1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#formalParameters2.
    def visitFormalParameters2(self, ctx: JavaParser.FormalParameters2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#formalParameter.
    def visitFormalParameter(self, ctx: JavaParser.FormalParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableModifier1.
    def visitVariableModifier1(self, ctx: JavaParser.VariableModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableModifier2.
    def visitVariableModifier2(self, ctx: JavaParser.VariableModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lastFormalParameter1.
    def visitLastFormalParameter1(self, ctx: JavaParser.LastFormalParameter1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lastFormalParameter2.
    def visitLastFormalParameter2(self, ctx: JavaParser.LastFormalParameter2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#receiverParameter.
    def visitReceiverParameter(self, ctx: JavaParser.ReceiverParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#throws_.
    def visitThrows_(self, ctx: JavaParser.Throws_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#exceptionTypeList.
    def visitExceptionTypeList(self, ctx: JavaParser.ExceptionTypeListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#exceptionType1.
    def visitExceptionType1(self, ctx: JavaParser.ExceptionType1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#exceptionType2.
    def visitExceptionType2(self, ctx: JavaParser.ExceptionType2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodBody1.
    def visitMethodBody1(self, ctx: JavaParser.MethodBody1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodBody2.
    def visitMethodBody2(self, ctx: JavaParser.MethodBody2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#instanceInitializer.
    def visitInstanceInitializer(self, ctx: JavaParser.InstanceInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#staticInitializer.
    def visitStaticInitializer(self, ctx: JavaParser.StaticInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx: JavaParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorModifier1.
    def visitConstructorModifier1(self, ctx: JavaParser.ConstructorModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorModifier2.
    def visitConstructorModifier2(self, ctx: JavaParser.ConstructorModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorModifier3.
    def visitConstructorModifier3(self, ctx: JavaParser.ConstructorModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorModifier4.
    def visitConstructorModifier4(self, ctx: JavaParser.ConstructorModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorDeclarator.
    def visitConstructorDeclarator(self, ctx: JavaParser.ConstructorDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#simpleTypeName.
    def visitSimpleTypeName(self, ctx: JavaParser.SimpleTypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constructorBody.
    def visitConstructorBody(self, ctx: JavaParser.ConstructorBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#explicitConstructorInvocation1.
    def visitExplicitConstructorInvocation1(self, ctx: JavaParser.ExplicitConstructorInvocation1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#explicitConstructorInvocation2.
    def visitExplicitConstructorInvocation2(self, ctx: JavaParser.ExplicitConstructorInvocation2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#explicitConstructorInvocation3.
    def visitExplicitConstructorInvocation3(self, ctx: JavaParser.ExplicitConstructorInvocation3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#explicitConstructorInvocation4.
    def visitExplicitConstructorInvocation4(self, ctx: JavaParser.ExplicitConstructorInvocation4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx: JavaParser.EnumDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumBody.
    def visitEnumBody(self, ctx: JavaParser.EnumBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumConstantList.
    def visitEnumConstantList(self, ctx: JavaParser.EnumConstantListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumConstant.
    def visitEnumConstant(self, ctx: JavaParser.EnumConstantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumConstantModifier.
    def visitEnumConstantModifier(self, ctx: JavaParser.EnumConstantModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx: JavaParser.EnumBodyDeclarationsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceDeclaration1.
    def visitInterfaceDeclaration1(self, ctx: JavaParser.InterfaceDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceDeclaration2.
    def visitInterfaceDeclaration2(self, ctx: JavaParser.InterfaceDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#normalInterfaceDeclaration.
    def visitNormalInterfaceDeclaration(self, ctx: JavaParser.NormalInterfaceDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier1.
    def visitInterfaceModifier1(self, ctx: JavaParser.InterfaceModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier2.
    def visitInterfaceModifier2(self, ctx: JavaParser.InterfaceModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier3.
    def visitInterfaceModifier3(self, ctx: JavaParser.InterfaceModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier4.
    def visitInterfaceModifier4(self, ctx: JavaParser.InterfaceModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier5.
    def visitInterfaceModifier5(self, ctx: JavaParser.InterfaceModifier5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier6.
    def visitInterfaceModifier6(self, ctx: JavaParser.InterfaceModifier6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceModifier7.
    def visitInterfaceModifier7(self, ctx: JavaParser.InterfaceModifier7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#extendsInterfaces.
    def visitExtendsInterfaces(self, ctx: JavaParser.ExtendsInterfacesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceBody.
    def visitInterfaceBody(self, ctx: JavaParser.InterfaceBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMemberDeclaration1.
    def visitInterfaceMemberDeclaration1(self, ctx: JavaParser.InterfaceMemberDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMemberDeclaration2.
    def visitInterfaceMemberDeclaration2(self, ctx: JavaParser.InterfaceMemberDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMemberDeclaration3.
    def visitInterfaceMemberDeclaration3(self, ctx: JavaParser.InterfaceMemberDeclaration3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMemberDeclaration4.
    def visitInterfaceMemberDeclaration4(self, ctx: JavaParser.InterfaceMemberDeclaration4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMemberDeclaration5.
    def visitInterfaceMemberDeclaration5(self, ctx: JavaParser.InterfaceMemberDeclaration5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx: JavaParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constantModifier1.
    def visitConstantModifier1(self, ctx: JavaParser.ConstantModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constantModifier2.
    def visitConstantModifier2(self, ctx: JavaParser.ConstantModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constantModifier3.
    def visitConstantModifier3(self, ctx: JavaParser.ConstantModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constantModifier4.
    def visitConstantModifier4(self, ctx: JavaParser.ConstantModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodDeclaration.
    def visitInterfaceMethodDeclaration(self, ctx: JavaParser.InterfaceMethodDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodModifier1.
    def visitInterfaceMethodModifier1(self, ctx: JavaParser.InterfaceMethodModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodModifier2.
    def visitInterfaceMethodModifier2(self, ctx: JavaParser.InterfaceMethodModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodModifier3.
    def visitInterfaceMethodModifier3(self, ctx: JavaParser.InterfaceMethodModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodModifier4.
    def visitInterfaceMethodModifier4(self, ctx: JavaParser.InterfaceMethodModifier4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodModifier5.
    def visitInterfaceMethodModifier5(self, ctx: JavaParser.InterfaceMethodModifier5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#interfaceMethodModifier6.
    def visitInterfaceMethodModifier6(self, ctx: JavaParser.InterfaceMethodModifier6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx: JavaParser.AnnotationTypeDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeBody.
    def visitAnnotationTypeBody(self, ctx: JavaParser.AnnotationTypeBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeMemberDeclaration1.
    def visitAnnotationTypeMemberDeclaration1(self, ctx: JavaParser.AnnotationTypeMemberDeclaration1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeMemberDeclaration2.
    def visitAnnotationTypeMemberDeclaration2(self, ctx: JavaParser.AnnotationTypeMemberDeclaration2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeMemberDeclaration3.
    def visitAnnotationTypeMemberDeclaration3(self, ctx: JavaParser.AnnotationTypeMemberDeclaration3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeMemberDeclaration4.
    def visitAnnotationTypeMemberDeclaration4(self, ctx: JavaParser.AnnotationTypeMemberDeclaration4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeMemberDeclaration5.
    def visitAnnotationTypeMemberDeclaration5(self, ctx: JavaParser.AnnotationTypeMemberDeclaration5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeElementDeclaration.
    def visitAnnotationTypeElementDeclaration(self, ctx: JavaParser.AnnotationTypeElementDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeElementModifier1.
    def visitAnnotationTypeElementModifier1(self, ctx: JavaParser.AnnotationTypeElementModifier1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeElementModifier2.
    def visitAnnotationTypeElementModifier2(self, ctx: JavaParser.AnnotationTypeElementModifier2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotationTypeElementModifier3.
    def visitAnnotationTypeElementModifier3(self, ctx: JavaParser.AnnotationTypeElementModifier3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#defaultValue.
    def visitDefaultValue(self, ctx: JavaParser.DefaultValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotation1.
    def visitAnnotation1(self, ctx: JavaParser.Annotation1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotation2.
    def visitAnnotation2(self, ctx: JavaParser.Annotation2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#annotation3.
    def visitAnnotation3(self, ctx: JavaParser.Annotation3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#normalAnnotation.
    def visitNormalAnnotation(self, ctx: JavaParser.NormalAnnotationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValuePairList.
    def visitElementValuePairList(self, ctx: JavaParser.ElementValuePairListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValuePair.
    def visitElementValuePair(self, ctx: JavaParser.ElementValuePairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValue1.
    def visitElementValue1(self, ctx: JavaParser.ElementValue1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValue2.
    def visitElementValue2(self, ctx: JavaParser.ElementValue2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValue3.
    def visitElementValue3(self, ctx: JavaParser.ElementValue3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx: JavaParser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#elementValueList.
    def visitElementValueList(self, ctx: JavaParser.ElementValueListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#markerAnnotation.
    def visitMarkerAnnotation(self, ctx: JavaParser.MarkerAnnotationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#singleElementAnnotation.
    def visitSingleElementAnnotation(self, ctx: JavaParser.SingleElementAnnotationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayInitializer.
    def visitArrayInitializer(self, ctx: JavaParser.ArrayInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#variableInitializerList.
    def visitVariableInitializerList(self, ctx: JavaParser.VariableInitializerListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#block.
    def visitBlock(self, ctx: JavaParser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#blockStatements.
    def visitBlockStatements(self, ctx: JavaParser.BlockStatementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#blockStatement1.
    def visitBlockStatement1(self, ctx: JavaParser.BlockStatement1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#blockStatement2.
    def visitBlockStatement2(self, ctx: JavaParser.BlockStatement2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#blockStatement3.
    def visitBlockStatement3(self, ctx: JavaParser.BlockStatement3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx: JavaParser.LocalVariableDeclarationStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx: JavaParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statement1.
    def visitStatement1(self, ctx: JavaParser.Statement1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statement2.
    def visitStatement2(self, ctx: JavaParser.Statement2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statement3.
    def visitStatement3(self, ctx: JavaParser.Statement3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statement4.
    def visitStatement4(self, ctx: JavaParser.Statement4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statement5.
    def visitStatement5(self, ctx: JavaParser.Statement5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statement6.
    def visitStatement6(self, ctx: JavaParser.Statement6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementNoShortIf1.
    def visitStatementNoShortIf1(self, ctx: JavaParser.StatementNoShortIf1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementNoShortIf2.
    def visitStatementNoShortIf2(self, ctx: JavaParser.StatementNoShortIf2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementNoShortIf3.
    def visitStatementNoShortIf3(self, ctx: JavaParser.StatementNoShortIf3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementNoShortIf4.
    def visitStatementNoShortIf4(self, ctx: JavaParser.StatementNoShortIf4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementNoShortIf5.
    def visitStatementNoShortIf5(self, ctx: JavaParser.StatementNoShortIf5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement1.
    def visitStatementWithoutTrailingSubstatement1(self, ctx: JavaParser.StatementWithoutTrailingSubstatement1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement2.
    def visitStatementWithoutTrailingSubstatement2(self, ctx: JavaParser.StatementWithoutTrailingSubstatement2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement3.
    def visitStatementWithoutTrailingSubstatement3(self, ctx: JavaParser.StatementWithoutTrailingSubstatement3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement4.
    def visitStatementWithoutTrailingSubstatement4(self, ctx: JavaParser.StatementWithoutTrailingSubstatement4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement5.
    def visitStatementWithoutTrailingSubstatement5(self, ctx: JavaParser.StatementWithoutTrailingSubstatement5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement6.
    def visitStatementWithoutTrailingSubstatement6(self, ctx: JavaParser.StatementWithoutTrailingSubstatement6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement7.
    def visitStatementWithoutTrailingSubstatement7(self, ctx: JavaParser.StatementWithoutTrailingSubstatement7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement8.
    def visitStatementWithoutTrailingSubstatement8(self, ctx: JavaParser.StatementWithoutTrailingSubstatement8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement9.
    def visitStatementWithoutTrailingSubstatement9(self, ctx: JavaParser.StatementWithoutTrailingSubstatement9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement10.
    def visitStatementWithoutTrailingSubstatement10(self,
                                                    ctx: JavaParser.StatementWithoutTrailingSubstatement10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement11.
    def visitStatementWithoutTrailingSubstatement11(self,
                                                    ctx: JavaParser.StatementWithoutTrailingSubstatement11Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementWithoutTrailingSubstatement12.
    def visitStatementWithoutTrailingSubstatement12(self,
                                                    ctx: JavaParser.StatementWithoutTrailingSubstatement12Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#emptyStatement_.
    def visitEmptyStatement_(self, ctx: JavaParser.EmptyStatement_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#labeledStatement.
    def visitLabeledStatement(self, ctx: JavaParser.LabeledStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#labeledStatementNoShortIf.
    def visitLabeledStatementNoShortIf(self, ctx: JavaParser.LabeledStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#expressionStatement.
    def visitExpressionStatement(self, ctx: JavaParser.ExpressionStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression1.
    def visitStatementExpression1(self, ctx: JavaParser.StatementExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression2.
    def visitStatementExpression2(self, ctx: JavaParser.StatementExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression3.
    def visitStatementExpression3(self, ctx: JavaParser.StatementExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression4.
    def visitStatementExpression4(self, ctx: JavaParser.StatementExpression4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression5.
    def visitStatementExpression5(self, ctx: JavaParser.StatementExpression5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression6.
    def visitStatementExpression6(self, ctx: JavaParser.StatementExpression6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpression7.
    def visitStatementExpression7(self, ctx: JavaParser.StatementExpression7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#ifThenStatement.
    def visitIfThenStatement(self, ctx: JavaParser.IfThenStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#ifThenElseStatement.
    def visitIfThenElseStatement(self, ctx: JavaParser.IfThenElseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#ifThenElseStatementNoShortIf.
    def visitIfThenElseStatementNoShortIf(self, ctx: JavaParser.IfThenElseStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assertStatement1.
    def visitAssertStatement1(self, ctx: JavaParser.AssertStatement1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assertStatement2.
    def visitAssertStatement2(self, ctx: JavaParser.AssertStatement2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchStatement.
    def visitSwitchStatement(self, ctx: JavaParser.SwitchStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchBlock.
    def visitSwitchBlock(self, ctx: JavaParser.SwitchBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx: JavaParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchLabels.
    def visitSwitchLabels(self, ctx: JavaParser.SwitchLabelsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchLabel1.
    def visitSwitchLabel1(self, ctx: JavaParser.SwitchLabel1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchLabel2.
    def visitSwitchLabel2(self, ctx: JavaParser.SwitchLabel2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#switchLabel3.
    def visitSwitchLabel3(self, ctx: JavaParser.SwitchLabel3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enumConstantName.
    def visitEnumConstantName(self, ctx: JavaParser.EnumConstantNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#whileStatement.
    def visitWhileStatement(self, ctx: JavaParser.WhileStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#whileStatementNoShortIf.
    def visitWhileStatementNoShortIf(self, ctx: JavaParser.WhileStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#doStatement.
    def visitDoStatement(self, ctx: JavaParser.DoStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forStatement1.
    def visitForStatement1(self, ctx: JavaParser.ForStatement1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forStatement2.
    def visitForStatement2(self, ctx: JavaParser.ForStatement2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forStatementNoShortIf1.
    def visitForStatementNoShortIf1(self, ctx: JavaParser.ForStatementNoShortIf1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forStatementNoShortIf2.
    def visitForStatementNoShortIf2(self, ctx: JavaParser.ForStatementNoShortIf2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#basicForStatement.
    def visitBasicForStatement(self, ctx: JavaParser.BasicForStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#basicForStatementNoShortIf.
    def visitBasicForStatementNoShortIf(self, ctx: JavaParser.BasicForStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forInit1.
    def visitForInit1(self, ctx: JavaParser.ForInit1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forInit2.
    def visitForInit2(self, ctx: JavaParser.ForInit2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#forUpdate.
    def visitForUpdate(self, ctx: JavaParser.ForUpdateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#statementExpressionList.
    def visitStatementExpressionList(self, ctx: JavaParser.StatementExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enhancedForStatement.
    def visitEnhancedForStatement(self, ctx: JavaParser.EnhancedForStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#enhancedForStatementNoShortIf.
    def visitEnhancedForStatementNoShortIf(self, ctx: JavaParser.EnhancedForStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#breakStatement.
    def visitBreakStatement(self, ctx: JavaParser.BreakStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#continueStatement.
    def visitContinueStatement(self, ctx: JavaParser.ContinueStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#returnStatement.
    def visitReturnStatement(self, ctx: JavaParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#throwStatement.
    def visitThrowStatement(self, ctx: JavaParser.ThrowStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#synchronizedStatement.
    def visitSynchronizedStatement(self, ctx: JavaParser.SynchronizedStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#tryStatement1.
    def visitTryStatement1(self, ctx: JavaParser.TryStatement1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#tryStatement2.
    def visitTryStatement2(self, ctx: JavaParser.TryStatement2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#tryStatement3.
    def visitTryStatement3(self, ctx: JavaParser.TryStatement3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#catches.
    def visitCatches(self, ctx: JavaParser.CatchesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#catchClause.
    def visitCatchClause(self, ctx: JavaParser.CatchClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#catchFormalParameter.
    def visitCatchFormalParameter(self, ctx: JavaParser.CatchFormalParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#catchType.
    def visitCatchType(self, ctx: JavaParser.CatchTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#finally_.
    def visitFinally_(self, ctx: JavaParser.Finally_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#tryWithResourcesStatement.
    def visitTryWithResourcesStatement(self, ctx: JavaParser.TryWithResourcesStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#resourceSpecification.
    def visitResourceSpecification(self, ctx: JavaParser.ResourceSpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#resourceList.
    def visitResourceList(self, ctx: JavaParser.ResourceListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#resource.
    def visitResource(self, ctx: JavaParser.ResourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primary.
    def visitPrimary(self, ctx: JavaParser.PrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray1.
    def visitPrimaryNoNewArray1(self, ctx: JavaParser.PrimaryNoNewArray1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray2.
    def visitPrimaryNoNewArray2(self, ctx: JavaParser.PrimaryNoNewArray2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray3.
    def visitPrimaryNoNewArray3(self, ctx: JavaParser.PrimaryNoNewArray3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray4.
    def visitPrimaryNoNewArray4(self, ctx: JavaParser.PrimaryNoNewArray4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray5.
    def visitPrimaryNoNewArray5(self, ctx: JavaParser.PrimaryNoNewArray5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray6.
    def visitPrimaryNoNewArray6(self, ctx: JavaParser.PrimaryNoNewArray6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray7.
    def visitPrimaryNoNewArray7(self, ctx: JavaParser.PrimaryNoNewArray7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray8.
    def visitPrimaryNoNewArray8(self, ctx: JavaParser.PrimaryNoNewArray8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray9.
    def visitPrimaryNoNewArray9(self, ctx: JavaParser.PrimaryNoNewArray9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray10.
    def visitPrimaryNoNewArray10(self, ctx: JavaParser.PrimaryNoNewArray10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray11.
    def visitPrimaryNoNewArray11(self, ctx: JavaParser.PrimaryNoNewArray11Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_arrayAccess.
    def visitPrimaryNoNewArray_lf_arrayAccess(self, ctx: JavaParser.PrimaryNoNewArray_lf_arrayAccessContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess1.
    def visitPrimaryNoNewArray_lfno_arrayAccess1(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess2.
    def visitPrimaryNoNewArray_lfno_arrayAccess2(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess3.
    def visitPrimaryNoNewArray_lfno_arrayAccess3(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess4.
    def visitPrimaryNoNewArray_lfno_arrayAccess4(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess5.
    def visitPrimaryNoNewArray_lfno_arrayAccess5(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess6.
    def visitPrimaryNoNewArray_lfno_arrayAccess6(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess7.
    def visitPrimaryNoNewArray_lfno_arrayAccess7(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess8.
    def visitPrimaryNoNewArray_lfno_arrayAccess8(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess9.
    def visitPrimaryNoNewArray_lfno_arrayAccess9(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_arrayAccess10.
    def visitPrimaryNoNewArray_lfno_arrayAccess10(self, ctx: JavaParser.PrimaryNoNewArray_lfno_arrayAccess10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary1.
    def visitPrimaryNoNewArray_lf_primary1(self, ctx: JavaParser.PrimaryNoNewArray_lf_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary2.
    def visitPrimaryNoNewArray_lf_primary2(self, ctx: JavaParser.PrimaryNoNewArray_lf_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary3.
    def visitPrimaryNoNewArray_lf_primary3(self, ctx: JavaParser.PrimaryNoNewArray_lf_primary3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary4.
    def visitPrimaryNoNewArray_lf_primary4(self, ctx: JavaParser.PrimaryNoNewArray_lf_primary4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary5.
    def visitPrimaryNoNewArray_lf_primary5(self, ctx: JavaParser.PrimaryNoNewArray_lf_primary5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary.
    def visitPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self,
                                                                    ctx: JavaParser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary1.
    def visitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary1(self,
                                                                       ctx: JavaParser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary2.
    def visitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary2(self,
                                                                       ctx: JavaParser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary3.
    def visitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary3(self,
                                                                       ctx: JavaParser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary4.
    def visitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary4(self,
                                                                       ctx: JavaParser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary1.
    def visitPrimaryNoNewArray_lfno_primary1(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary2.
    def visitPrimaryNoNewArray_lfno_primary2(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary3.
    def visitPrimaryNoNewArray_lfno_primary3(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary4.
    def visitPrimaryNoNewArray_lfno_primary4(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary5.
    def visitPrimaryNoNewArray_lfno_primary5(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary6.
    def visitPrimaryNoNewArray_lfno_primary6(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary7.
    def visitPrimaryNoNewArray_lfno_primary7(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary8.
    def visitPrimaryNoNewArray_lfno_primary8(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary9.
    def visitPrimaryNoNewArray_lfno_primary9(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary10.
    def visitPrimaryNoNewArray_lfno_primary10(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary11.
    def visitPrimaryNoNewArray_lfno_primary11(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary11Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary12.
    def visitPrimaryNoNewArray_lfno_primary12(self, ctx: JavaParser.PrimaryNoNewArray_lfno_primary12Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary.
    def visitPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self,
                                                                        ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary1.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary1(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary2.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary2(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary3.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary3(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary4.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary4(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary5.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary5(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary6.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary6(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary7.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary7(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary8.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary8(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary9.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary9(self,
                                                                           ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary10.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary10(self,
                                                                            ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary11.
    def visitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary11(self,
                                                                            ctx: JavaParser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary11Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classInstanceCreationExpression1.
    def visitClassInstanceCreationExpression1(self, ctx: JavaParser.ClassInstanceCreationExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classInstanceCreationExpression2.
    def visitClassInstanceCreationExpression2(self, ctx: JavaParser.ClassInstanceCreationExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classInstanceCreationExpression3.
    def visitClassInstanceCreationExpression3(self, ctx: JavaParser.ClassInstanceCreationExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classInstanceCreationExpression_lf_primary.
    def visitClassInstanceCreationExpression_lf_primary(self,
                                                        ctx: JavaParser.ClassInstanceCreationExpression_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classInstanceCreationExpression_lfno_primary1.
    def visitClassInstanceCreationExpression_lfno_primary1(self,
                                                           ctx: JavaParser.ClassInstanceCreationExpression_lfno_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#classInstanceCreationExpression_lfno_primary2.
    def visitClassInstanceCreationExpression_lfno_primary2(self,
                                                           ctx: JavaParser.ClassInstanceCreationExpression_lfno_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeArgumentsOrDiamond1.
    def visitTypeArgumentsOrDiamond1(self, ctx: JavaParser.TypeArgumentsOrDiamond1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#typeArgumentsOrDiamond2.
    def visitTypeArgumentsOrDiamond2(self, ctx: JavaParser.TypeArgumentsOrDiamond2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldAccess1.
    def visitFieldAccess1(self, ctx: JavaParser.FieldAccess1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldAccess2.
    def visitFieldAccess2(self, ctx: JavaParser.FieldAccess2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldAccess3.
    def visitFieldAccess3(self, ctx: JavaParser.FieldAccess3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldAccess_lf_primary.
    def visitFieldAccess_lf_primary(self, ctx: JavaParser.FieldAccess_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldAccess_lfno_primary1.
    def visitFieldAccess_lfno_primary1(self, ctx: JavaParser.FieldAccess_lfno_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#fieldAccess_lfno_primary2.
    def visitFieldAccess_lfno_primary2(self, ctx: JavaParser.FieldAccess_lfno_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayAccess.
    def visitArrayAccess(self, ctx: JavaParser.ArrayAccessContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayAccess_lf_primary.
    def visitArrayAccess_lf_primary(self, ctx: JavaParser.ArrayAccess_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayAccess_lfno_primary.
    def visitArrayAccess_lfno_primary(self, ctx: JavaParser.ArrayAccess_lfno_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation1.
    def visitMethodInvocation1(self, ctx: JavaParser.MethodInvocation1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation2.
    def visitMethodInvocation2(self, ctx: JavaParser.MethodInvocation2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation3.
    def visitMethodInvocation3(self, ctx: JavaParser.MethodInvocation3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation4.
    def visitMethodInvocation4(self, ctx: JavaParser.MethodInvocation4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation5.
    def visitMethodInvocation5(self, ctx: JavaParser.MethodInvocation5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation6.
    def visitMethodInvocation6(self, ctx: JavaParser.MethodInvocation6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation_lf_primary.
    def visitMethodInvocation_lf_primary(self, ctx: JavaParser.MethodInvocation_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation_lfno_primary1.
    def visitMethodInvocation_lfno_primary1(self, ctx: JavaParser.MethodInvocation_lfno_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation_lfno_primary2.
    def visitMethodInvocation_lfno_primary2(self, ctx: JavaParser.MethodInvocation_lfno_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation_lfno_primary3.
    def visitMethodInvocation_lfno_primary3(self, ctx: JavaParser.MethodInvocation_lfno_primary3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation_lfno_primary4.
    def visitMethodInvocation_lfno_primary4(self, ctx: JavaParser.MethodInvocation_lfno_primary4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodInvocation_lfno_primary5.
    def visitMethodInvocation_lfno_primary5(self, ctx: JavaParser.MethodInvocation_lfno_primary5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#argumentList.
    def visitArgumentList(self, ctx: JavaParser.ArgumentListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference1.
    def visitMethodReference1(self, ctx: JavaParser.MethodReference1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference2.
    def visitMethodReference2(self, ctx: JavaParser.MethodReference2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference3.
    def visitMethodReference3(self, ctx: JavaParser.MethodReference3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference4.
    def visitMethodReference4(self, ctx: JavaParser.MethodReference4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference5.
    def visitMethodReference5(self, ctx: JavaParser.MethodReference5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference6.
    def visitMethodReference6(self, ctx: JavaParser.MethodReference6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference7.
    def visitMethodReference7(self, ctx: JavaParser.MethodReference7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lf_primary.
    def visitMethodReference_lf_primary(self, ctx: JavaParser.MethodReference_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lfno_primary1.
    def visitMethodReference_lfno_primary1(self, ctx: JavaParser.MethodReference_lfno_primary1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lfno_primary2.
    def visitMethodReference_lfno_primary2(self, ctx: JavaParser.MethodReference_lfno_primary2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lfno_primary3.
    def visitMethodReference_lfno_primary3(self, ctx: JavaParser.MethodReference_lfno_primary3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lfno_primary4.
    def visitMethodReference_lfno_primary4(self, ctx: JavaParser.MethodReference_lfno_primary4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lfno_primary5.
    def visitMethodReference_lfno_primary5(self, ctx: JavaParser.MethodReference_lfno_primary5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#methodReference_lfno_primary6.
    def visitMethodReference_lfno_primary6(self, ctx: JavaParser.MethodReference_lfno_primary6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayCreationExpression1.
    def visitArrayCreationExpression1(self, ctx: JavaParser.ArrayCreationExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayCreationExpression2.
    def visitArrayCreationExpression2(self, ctx: JavaParser.ArrayCreationExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayCreationExpression3.
    def visitArrayCreationExpression3(self, ctx: JavaParser.ArrayCreationExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#arrayCreationExpression4.
    def visitArrayCreationExpression4(self, ctx: JavaParser.ArrayCreationExpression4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#dimExprs.
    def visitDimExprs(self, ctx: JavaParser.DimExprsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#dimExpr.
    def visitDimExpr(self, ctx: JavaParser.DimExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#constantExpression.
    def visitConstantExpression(self, ctx: JavaParser.ConstantExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#expression1.
    def visitExpression1(self, ctx: JavaParser.Expression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#expression2.
    def visitExpression2(self, ctx: JavaParser.Expression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lambdaExpression.
    def visitLambdaExpression(self, ctx: JavaParser.LambdaExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lambdaParameters1.
    def visitLambdaParameters1(self, ctx: JavaParser.LambdaParameters1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lambdaParameters2.
    def visitLambdaParameters2(self, ctx: JavaParser.LambdaParameters2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lambdaParameters3.
    def visitLambdaParameters3(self, ctx: JavaParser.LambdaParameters3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#inferredFormalParameterList.
    def visitInferredFormalParameterList(self, ctx: JavaParser.InferredFormalParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lambdaBody1.
    def visitLambdaBody1(self, ctx: JavaParser.LambdaBody1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#lambdaBody2.
    def visitLambdaBody2(self, ctx: JavaParser.LambdaBody2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentExpression1.
    def visitAssignmentExpression1(self, ctx: JavaParser.AssignmentExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentExpression2.
    def visitAssignmentExpression2(self, ctx: JavaParser.AssignmentExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignment.
    def visitAssignment(self, ctx: JavaParser.AssignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#leftHandSide1.
    def visitLeftHandSide1(self, ctx: JavaParser.LeftHandSide1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#leftHandSide2.
    def visitLeftHandSide2(self, ctx: JavaParser.LeftHandSide2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#leftHandSide3.
    def visitLeftHandSide3(self, ctx: JavaParser.LeftHandSide3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator1.
    def visitAssignmentOperator1(self, ctx: JavaParser.AssignmentOperator1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator2.
    def visitAssignmentOperator2(self, ctx: JavaParser.AssignmentOperator2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator3.
    def visitAssignmentOperator3(self, ctx: JavaParser.AssignmentOperator3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator4.
    def visitAssignmentOperator4(self, ctx: JavaParser.AssignmentOperator4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator5.
    def visitAssignmentOperator5(self, ctx: JavaParser.AssignmentOperator5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator6.
    def visitAssignmentOperator6(self, ctx: JavaParser.AssignmentOperator6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator7.
    def visitAssignmentOperator7(self, ctx: JavaParser.AssignmentOperator7Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator8.
    def visitAssignmentOperator8(self, ctx: JavaParser.AssignmentOperator8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator9.
    def visitAssignmentOperator9(self, ctx: JavaParser.AssignmentOperator9Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator10.
    def visitAssignmentOperator10(self, ctx: JavaParser.AssignmentOperator10Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator11.
    def visitAssignmentOperator11(self, ctx: JavaParser.AssignmentOperator11Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#assignmentOperator12.
    def visitAssignmentOperator12(self, ctx: JavaParser.AssignmentOperator12Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#conditionalExpression1.
    def visitConditionalExpression1(self, ctx: JavaParser.ConditionalExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#conditionalExpression2.
    def visitConditionalExpression2(self, ctx: JavaParser.ConditionalExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#conditionalOrExpression1.
    def visitConditionalOrExpression1(self, ctx: JavaParser.ConditionalOrExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#conditionalOrExpression2.
    def visitConditionalOrExpression2(self, ctx: JavaParser.ConditionalOrExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#conditionalAndExpression2.
    def visitConditionalAndExpression2(self, ctx: JavaParser.ConditionalAndExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#conditionalAndExpression1.
    def visitConditionalAndExpression1(self, ctx: JavaParser.ConditionalAndExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#inclusiveOrExpression2.
    def visitInclusiveOrExpression2(self, ctx: JavaParser.InclusiveOrExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#inclusiveOrExpression1.
    def visitInclusiveOrExpression1(self, ctx: JavaParser.InclusiveOrExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#exclusiveOrExpression1.
    def visitExclusiveOrExpression1(self, ctx: JavaParser.ExclusiveOrExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#exclusiveOrExpression2.
    def visitExclusiveOrExpression2(self, ctx: JavaParser.ExclusiveOrExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#andExpression2.
    def visitAndExpression2(self, ctx: JavaParser.AndExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#andExpression1.
    def visitAndExpression1(self, ctx: JavaParser.AndExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#equalityExpression3.
    def visitEqualityExpression3(self, ctx: JavaParser.EqualityExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#equalityExpression2.
    def visitEqualityExpression2(self, ctx: JavaParser.EqualityExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#equalityExpression1.
    def visitEqualityExpression1(self, ctx: JavaParser.EqualityExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#relationalExpression1.
    def visitRelationalExpression1(self, ctx: JavaParser.RelationalExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#relationalExpression2.
    def visitRelationalExpression2(self, ctx: JavaParser.RelationalExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#relationalExpression5.
    def visitRelationalExpression5(self, ctx: JavaParser.RelationalExpression5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#relationalExpression6.
    def visitRelationalExpression6(self, ctx: JavaParser.RelationalExpression6Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#relationalExpression3.
    def visitRelationalExpression3(self, ctx: JavaParser.RelationalExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#relationalExpression4.
    def visitRelationalExpression4(self, ctx: JavaParser.RelationalExpression4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#shiftExpression1.
    def visitShiftExpression1(self, ctx: JavaParser.ShiftExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#shiftExpression3.
    def visitShiftExpression3(self, ctx: JavaParser.ShiftExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#shiftExpression2.
    def visitShiftExpression2(self, ctx: JavaParser.ShiftExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#shiftExpression4.
    def visitShiftExpression4(self, ctx: JavaParser.ShiftExpression4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#additiveExpression1.
    def visitAdditiveExpression1(self, ctx: JavaParser.AdditiveExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#additiveExpression3.
    def visitAdditiveExpression3(self, ctx: JavaParser.AdditiveExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#additiveExpression2.
    def visitAdditiveExpression2(self, ctx: JavaParser.AdditiveExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#multiplicativeExpression1.
    def visitMultiplicativeExpression1(self, ctx: JavaParser.MultiplicativeExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#multiplicativeExpression4.
    def visitMultiplicativeExpression4(self, ctx: JavaParser.MultiplicativeExpression4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#multiplicativeExpression3.
    def visitMultiplicativeExpression3(self, ctx: JavaParser.MultiplicativeExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#multiplicativeExpression2.
    def visitMultiplicativeExpression2(self, ctx: JavaParser.MultiplicativeExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpression1.
    def visitUnaryExpression1(self, ctx: JavaParser.UnaryExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpression2.
    def visitUnaryExpression2(self, ctx: JavaParser.UnaryExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpression3.
    def visitUnaryExpression3(self, ctx: JavaParser.UnaryExpression3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpression4.
    def visitUnaryExpression4(self, ctx: JavaParser.UnaryExpression4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpression5.
    def visitUnaryExpression5(self, ctx: JavaParser.UnaryExpression5Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#preIncrementExpression.
    def visitPreIncrementExpression(self, ctx: JavaParser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#preDecrementExpression.
    def visitPreDecrementExpression(self, ctx: JavaParser.PreDecrementExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpressionNotPlusMinus1.
    def visitUnaryExpressionNotPlusMinus1(self, ctx: JavaParser.UnaryExpressionNotPlusMinus1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpressionNotPlusMinus2.
    def visitUnaryExpressionNotPlusMinus2(self, ctx: JavaParser.UnaryExpressionNotPlusMinus2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpressionNotPlusMinus3.
    def visitUnaryExpressionNotPlusMinus3(self, ctx: JavaParser.UnaryExpressionNotPlusMinus3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#unaryExpressionNotPlusMinus4.
    def visitUnaryExpressionNotPlusMinus4(self, ctx: JavaParser.UnaryExpressionNotPlusMinus4Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#postfixExpression.
    def visitPostfixExpression(self, ctx: JavaParser.PostfixExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#postIncrementExpression.
    def visitPostIncrementExpression(self, ctx: JavaParser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#postIncrementExpression_lf_postfixExpression.
    def visitPostIncrementExpression_lf_postfixExpression(self,
                                                          ctx: JavaParser.PostIncrementExpression_lf_postfixExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#postDecrementExpression.
    def visitPostDecrementExpression(self, ctx: JavaParser.PostDecrementExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#postDecrementExpression_lf_postfixExpression.
    def visitPostDecrementExpression_lf_postfixExpression(self,
                                                          ctx: JavaParser.PostDecrementExpression_lf_postfixExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#castExpression1.
    def visitCastExpression1(self, ctx: JavaParser.CastExpression1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#castExpression2.
    def visitCastExpression2(self, ctx: JavaParser.CastExpression2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JavaParser#castExpression3.
    def visitCastExpression3(self, ctx: JavaParser.CastExpression3Context):
        return self.visitChildren(ctx)


del JavaParser
