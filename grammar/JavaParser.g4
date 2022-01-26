/*
 * [The "BSD license"]
 *  Copyright (c) 2014 Terence Parr
 *  Copyright (c) 2014 Sam Harwell
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 *  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 *  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 *  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 *  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 *  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/**
 * A Java 8 grammar for ANTLR 4 derived from the Java Language Specification
 * chapter 19.
 *
 * NOTE: This grammar results in a generated parser that is much slower
 *       than the Java 7 grammar in the grammars-v4/java directory. This
 *     one is, however, extremely close to the spec.
 *
 * You can test with
 *
 *  $ antlr4 Java8.g4
 *  $ javac *.java
 *  $ grun Java8 compilationUnit *.java
 *
 * Or,
~/antlr/code/grammars-v4/java8 $ java Test .
/Users/parrt/antlr/code/grammars-v4/java8/./Java8BaseListener.java
/Users/parrt/antlr/code/grammars-v4/java8/./Java8Lexer.java
/Users/parrt/antlr/code/grammars-v4/java8/./Java8Listener.java
/Users/parrt/antlr/code/grammars-v4/java8/./Java8Parser.java
/Users/parrt/antlr/code/grammars-v4/java8/./Test.java
Total lexer+parser time 30844ms.
 */
parser grammar JavaParser;

options {
    tokenVocab=JavaLexer;
}
/*
 * Productions from Â§3 (Lexical Structure)
 */

literal
	:	IntegerLiteral #literal1
	|	FloatingPointLiteral #literal2
	|	BooleanLiteral #literal3
	|	CharacterLiteral #literal4
	|	StringLiteral #literal5
	|	NullLiteral #literal6
	;

/*
 * Productions from Â§4 (Types, Values, and Variables)
 */
compilationUnit

	:	packageDeclaration? importDeclaration* typeDeclaration* EOF
	;

primitiveType
	:	annotation* numericType #primitiveType1
	|	annotation* 'boolean' #primitiveType2
	;

numericType
	:	integralType #numericType1
	|	floatingPointType #numericType2
	;

integralType
	:	'byte' #integralType1
	|	'short' #integralType2
	|	'int' #integralType3
	|	'long' #integralType4
	|	'char' #integralType5
	;

floatingPointType
	:	'float' #floatingPointType1
	|	'double' #floatingPointType2
	;

referenceType
	:	classOrInterfaceType #referenceType1
	|	typeVariable #referenceType2
	|	arrayType #referenceType3
	;

classOrInterfaceType
	:	(	classType_lfno_classOrInterfaceType
		|	interfaceType_lfno_classOrInterfaceType
		)
		(	classType_lf_classOrInterfaceType
		|	interfaceType_lf_classOrInterfaceType
		)*
	;

classType
	:	annotation* Identifier typeArguments? #classType1
	|	classOrInterfaceType '.' annotation* Identifier typeArguments? #classType2
	;

classType_lf_classOrInterfaceType
	:	'.' annotation* Identifier typeArguments?
	;

classType_lfno_classOrInterfaceType
	:	annotation* Identifier typeArguments?
	;

interfaceType
	:	classType
	;

interfaceType_lf_classOrInterfaceType
	:	classType_lf_classOrInterfaceType
	;

interfaceType_lfno_classOrInterfaceType
	:	classType_lfno_classOrInterfaceType
	;

typeVariable
	:	annotation* Identifier
	;

arrayType
	:	primitiveType dims #arrayType1
	|	classOrInterfaceType dims #arrayType2
	|	typeVariable dims #arrayType3
	;

dims
	:	annotation* '[' ']' (annotation* '[' ']')*
	;

typeParameter
	:	typeParameterModifier* Identifier typeBound?
	;

typeParameterModifier
	:	annotation
	;

typeBound
	:	'extends' typeVariable #typeBound1
	|	'extends' classOrInterfaceType additionalBound* #typeBound2
	;

additionalBound
	:	'&' interfaceType
	;

typeArguments
	:	'<' typeArgumentList '>'
	;

typeArgumentList
	:	typeArgument (',' typeArgument)*
	;

typeArgument
	:	referenceType #typeArgument1
	|	wildcard #typeArgument2
	;

wildcard
	:	annotation* '?' wildcardBounds?
	;

wildcardBounds
	:	'extends' referenceType #wildcardBounds1
	|	'super' referenceType #wildcardBounds2
	;

/*
 * Productions from Â§6 (Names)
 */

packageName
	:	Identifier #packageName1
	|	packageName '.' Identifier #packageName2
	;

typeName
	:	Identifier #typeName1
	|	packageOrTypeName '.' Identifier #typeName2
	;

packageOrTypeName
	:	Identifier #packageOrTypeName1
	|	packageOrTypeName '.' Identifier #packageOrTypeName2
	;

expressionName
	:	Identifier #expressionName1
	|	ambiguousName '.' Identifier #expressionName2
	;

methodName
	:	Identifier
	;

ambiguousName
	:	Identifier #ambiguousName1
	|	ambiguousName '.' Identifier #ambiguousName2
	;

/*
 * Productions from Â§7 (Packages)
 */


packageDeclaration
	:	packageModifier* 'package' packageName ';'
	;

packageModifier
	:	annotation
	;

importDeclaration
	:	singleTypeImportDeclaration #importDeclaration1
	|	typeImportOnDemandDeclaration #importDeclaration2
	|	singleStaticImportDeclaration #importDeclaration3
	|	staticImportOnDemandDeclaration #importDeclaration4
	;

singleTypeImportDeclaration
	:	'import' typeName ';'
	;

typeImportOnDemandDeclaration
	:	'import' packageOrTypeName '.' '*' ';'
	;

singleStaticImportDeclaration
	:	'import' 'static' typeName '.' Identifier ';'
	;

staticImportOnDemandDeclaration
	:	'import' 'static' typeName '.' '*' ';'
	;

typeDeclaration
	:	classDeclaration #typeDeclaration1
	|	interfaceDeclaration #typeDeclaration2
	|	';' #typeDeclaration3
	;

/*
 * Productions from Â§8 (Classes)
 */

classDeclaration
	:	normalClassDeclaration #classDeclaration1
	|	enumDeclaration #classDeclaration2
	;

normalClassDeclaration
	:	classModifier* 'class' Identifier typeParameters? superclass? superinterfaces? classBody
	;

classModifier
	:	annotation #classModifier1
	|	'public' #classModifier2
	|	'protected' #classModifier3
	|	'private' #classModifier4
	|	'abstract' #classModifier5
	|	'static' #classModifier6
	|	'final' #classModifier7
	|	'strictfp' #classModifier8
	;

typeParameters
	:	'<' typeParameterList '>'
	;

typeParameterList
	:	typeParameter (',' typeParameter)*
	;

superclass
	:	'extends' classType
	;

superinterfaces
	:	'implements' interfaceTypeList
	;

interfaceTypeList
	:	interfaceType (',' interfaceType)*
	;

classBody
	:	'{' classBodyDeclaration* '}'
	;

classBodyDeclaration
	:	classMemberDeclaration #classBodyDeclaration1
	|	instanceInitializer #classBodyDeclaration2
	|	staticInitializer #classBodyDeclaration3
	|	constructorDeclaration #classBodyDeclaration4
	;

classMemberDeclaration
	:	fieldDeclaration #classMemberDeclaration1
	|	methodDeclaration #classMemberDeclaration2
	|	classDeclaration #classMemberDeclaration3
	|	interfaceDeclaration #classMemberDeclaration4
	|	';' #classMemberDeclaration5
	;

fieldDeclaration
	:	fieldModifier* unannType variableDeclaratorList ';'
	;

fieldModifier
	:	annotation #fieldModifier1
	|	'public' #fieldModifier2
	|	'protected' #fieldModifier3
	|	'private' #fieldModifier4
	|	'static' #fieldModifier5
	|	'final' #fieldModifier6
	|	'transient' #fieldModifier7
	|	'volatile' #fieldModifier8
	;

variableDeclaratorList
	:	variableDeclarator (',' variableDeclarator)*
	;

variableDeclarator
	:	variableDeclaratorId ('=' variableInitializer)?
	;

variableDeclaratorId
	:	Identifier dims?
	;

variableInitializer
	:	expression #variableInitializer1
	|	arrayInitializer #variableInitializer2
	;

unannType
	:	unannPrimitiveType #unannType1
	|	unannReferenceType #unannType2
	;

unannPrimitiveType
	:	numericType #unannPrimitiveType1
	|	'boolean' #unannPrimitiveType2
	;

unannReferenceType
	:	unannClassOrInterfaceType #unannReferenceType1
	|	unannTypeVariable #unannReferenceType2
	|	unannArrayType #unannReferenceType3
	;

unannClassOrInterfaceType
	:	(	unannClassType_lfno_unannClassOrInterfaceType
		|	unannInterfaceType_lfno_unannClassOrInterfaceType
		)
		(	unannClassType_lf_unannClassOrInterfaceType
		|	unannInterfaceType_lf_unannClassOrInterfaceType
		)*
	;

unannClassType
	:	Identifier typeArguments? #unannClassType1
	|	unannClassOrInterfaceType '.' annotation* Identifier typeArguments? #unannClassType2
	;

unannClassType_lf_unannClassOrInterfaceType
	:	'.' annotation* Identifier typeArguments?
	;

unannClassType_lfno_unannClassOrInterfaceType
	:	Identifier typeArguments?
	;

unannInterfaceType
	:	unannClassType
	;

unannInterfaceType_lf_unannClassOrInterfaceType
	:	unannClassType_lf_unannClassOrInterfaceType
	;

unannInterfaceType_lfno_unannClassOrInterfaceType
	:	unannClassType_lfno_unannClassOrInterfaceType
	;

unannTypeVariable
	:	Identifier
	;

unannArrayType
	:	unannPrimitiveType dims #unannArrayType1
	|	unannClassOrInterfaceType dims #unannArrayType2
	|	unannTypeVariable dims #unannArrayType3
	;

methodDeclaration
	:	methodModifier* methodHeader methodBody
	;

methodModifier
	:	annotation #methodModifier1
	|	'public' #methodModifier2
	|	'protected' #methodModifier3
	|	'private' #methodModifier4
	|	'abstract' #methodModifier5
	|	'static' #methodModifier6
	|	'final' #methodModifier7
	|	'synchronized' #methodModifier8
	|	'native' #methodModifier9
	|	'strictfp' #methodModifier10
	;

methodHeader
	:	result methodDeclarator throws_? #methodHeader1
	|	typeParameters annotation* result methodDeclarator throws_? #methodHeader2
	;

result
	:	unannType #result1
	|	'void' #result2
	;

methodDeclarator
	:	Identifier '(' formalParameterList? ')' dims?
	;

formalParameterList
	:	receiverParameter #formalParameterList1
	|	formalParameters ',' lastFormalParameter #formalParameterList2
	|	lastFormalParameter #formalParameterList3
	;

formalParameters
	:	formalParameter (',' formalParameter)* #formalParameters1
	|	receiverParameter (',' formalParameter)* #formalParameters2
	;

formalParameter
	:	variableModifier* unannType variableDeclaratorId
	;

variableModifier
	:	annotation #variableModifier1
	|	'final' #variableModifier2
	;

lastFormalParameter
	:	variableModifier* unannType annotation* '...' variableDeclaratorId #lastFormalParameter1
	|	formalParameter #lastFormalParameter2
	;

receiverParameter
	:	annotation* unannType (Identifier '.')? 'this'
	;

throws_
	:	'throws' exceptionTypeList
	;

exceptionTypeList
	:	exceptionType (',' exceptionType)*
	;

exceptionType
	:	classType #exceptionType1
	|	typeVariable #exceptionType2
	;

methodBody
	:	block #methodBody1
	|	';' #methodBody2
	;

instanceInitializer
	:	block
	;

staticInitializer
	:	'static' block
	;

constructorDeclaration
	:	constructorModifier* constructorDeclarator throws_? constructorBody
	;

constructorModifier
	:	annotation #constructorModifier1
	|	'public' #constructorModifier2
	|	'protected' #constructorModifier3
	|	'private' #constructorModifier4
	;

constructorDeclarator
	:	typeParameters? simpleTypeName '(' formalParameterList? ')'
	;

simpleTypeName
	:	Identifier
	;

constructorBody
	:	'{' explicitConstructorInvocation? blockStatements? '}'
	;

explicitConstructorInvocation
	:	typeArguments? 'this' '(' argumentList? ')' ';' #explicitConstructorInvocation1
	|	typeArguments? 'super' '(' argumentList? ')' ';' #explicitConstructorInvocation2
	|	expressionName '.' typeArguments? 'super' '(' argumentList? ')' ';' #explicitConstructorInvocation3
	|	primary '.' typeArguments? 'super' '(' argumentList? ')' ';' #explicitConstructorInvocation4
	;

enumDeclaration
	:	classModifier* 'enum' Identifier superinterfaces? enumBody
	;

enumBody
	:	'{' enumConstantList? ','? enumBodyDeclarations? '}'
	;

enumConstantList
	:	enumConstant (',' enumConstant)*
	;

enumConstant
	:	enumConstantModifier* Identifier ('(' argumentList? ')')? classBody?
	;

enumConstantModifier
	:	annotation
	;

enumBodyDeclarations
	:	';' classBodyDeclaration*
	;

/*
 * Productions from Â§9 (Interfaces)
 */

interfaceDeclaration
	:	normalInterfaceDeclaration #interfaceDeclaration1
	|	annotationTypeDeclaration #interfaceDeclaration2
	;

normalInterfaceDeclaration
	:	interfaceModifier* 'interface' Identifier typeParameters? extendsInterfaces? interfaceBody
	;

interfaceModifier
	:	annotation #interfaceModifier1
	|	'public' #interfaceModifier2
	|	'protected' #interfaceModifier3
	|	'private' #interfaceModifier4
	|	'abstract' #interfaceModifier5
	|	'static' #interfaceModifier6
	|	'strictfp' #interfaceModifier7
	;

extendsInterfaces
	:	'extends' interfaceTypeList
	;

interfaceBody
	:	'{' interfaceMemberDeclaration* '}'
	;

interfaceMemberDeclaration
	:	constantDeclaration #interfaceMemberDeclaration1
	|	interfaceMethodDeclaration #interfaceMemberDeclaration2
	|	classDeclaration #interfaceMemberDeclaration3
	|	interfaceDeclaration #interfaceMemberDeclaration4
	|	';' #interfaceMemberDeclaration5
	;

constantDeclaration
	:	constantModifier* unannType variableDeclaratorList ';'
	;

constantModifier
	:	annotation #constantModifier1
	|	'public' #constantModifier2
	|	'static' #constantModifier3
	|	'final' #constantModifier4
	;

interfaceMethodDeclaration
	:	interfaceMethodModifier* methodHeader methodBody
	;

interfaceMethodModifier
	:	annotation #interfaceMethodModifier1
	|	'public' #interfaceMethodModifier2
	|	'abstract' #interfaceMethodModifier3
	|	'default' #interfaceMethodModifier4
	|	'static' #interfaceMethodModifier5
	|	'strictfp' #interfaceMethodModifier6
	;

annotationTypeDeclaration
	:	interfaceModifier* '@' 'interface' Identifier annotationTypeBody
	;

annotationTypeBody
	:	'{' annotationTypeMemberDeclaration* '}'
	;

annotationTypeMemberDeclaration
	:	annotationTypeElementDeclaration #annotationTypeMemberDeclaration1
	|	constantDeclaration #annotationTypeMemberDeclaration2
	|	classDeclaration #annotationTypeMemberDeclaration3
	|	interfaceDeclaration #annotationTypeMemberDeclaration4
	|	';' #annotationTypeMemberDeclaration5
	;

annotationTypeElementDeclaration
	:	annotationTypeElementModifier* unannType Identifier '(' ')' dims? defaultValue? ';'
	;

annotationTypeElementModifier
	:	annotation #annotationTypeElementModifier1
	|	'public' #annotationTypeElementModifier2
	|	'abstract' #annotationTypeElementModifier3
	;

defaultValue
	:	'default' elementValue
	;

annotation
	:	normalAnnotation #annotation1
	|	markerAnnotation #annotation2
	|	singleElementAnnotation #annotation3
	;

normalAnnotation
	:	'@' typeName '(' elementValuePairList? ')'
	;

elementValuePairList
	:	elementValuePair (',' elementValuePair)*
	;

elementValuePair
	:	Identifier '=' elementValue
	;

elementValue
	:	conditionalExpression #elementValue1
	|	elementValueArrayInitializer #elementValue2
	|	annotation #elementValue3
	;

elementValueArrayInitializer
	:	'{' elementValueList? ','? '}'
	;

elementValueList
	:	elementValue (',' elementValue)*
	;

markerAnnotation
	:	'@' typeName
	;

singleElementAnnotation
	:	'@' typeName '(' elementValue ')'
	;

/*
 * Productions from Â§10 (Arrays)
 */

arrayInitializer
	:	'{' variableInitializerList? ','? '}'
	;

variableInitializerList
	:	variableInitializer (',' variableInitializer)*
	;

/*
 * Productions from Â§14 (Blocks and Statements)
 */

block
	:	'{' blockStatements? '}'
	;

blockStatements
	:	blockStatement+
	;

blockStatement
	:	localVariableDeclarationStatement #blockStatement1
	|	classDeclaration #blockStatement2
	|	statement #blockStatement3
	;

localVariableDeclarationStatement
	:	localVariableDeclaration ';'
	;

localVariableDeclaration
	:	variableModifier* unannType variableDeclaratorList
	;

statement
	:	statementWithoutTrailingSubstatement #statement1
	|	labeledStatement #statement2
	|	ifThenStatement #statement3
	|	ifThenElseStatement #statement4
	|	whileStatement #statement5
	|	forStatement #statement6
	;

statementNoShortIf
	:	statementWithoutTrailingSubstatement #statementNoShortIf1
	|	labeledStatementNoShortIf #statementNoShortIf2
	|	ifThenElseStatementNoShortIf #statementNoShortIf3
	|	whileStatementNoShortIf #statementNoShortIf4
	|	forStatementNoShortIf #statementNoShortIf5
	;

statementWithoutTrailingSubstatement
	:	block #statementWithoutTrailingSubstatement1
	|	emptyStatement_ #statementWithoutTrailingSubstatement2
	|	expressionStatement #statementWithoutTrailingSubstatement3
	|	assertStatement #statementWithoutTrailingSubstatement4
	|	switchStatement #statementWithoutTrailingSubstatement5
	|	doStatement #statementWithoutTrailingSubstatement6
	|	breakStatement #statementWithoutTrailingSubstatement7
	|	continueStatement #statementWithoutTrailingSubstatement8
	|	returnStatement #statementWithoutTrailingSubstatement9
	|	synchronizedStatement #statementWithoutTrailingSubstatement10
	|	throwStatement #statementWithoutTrailingSubstatement11
	|	tryStatement #statementWithoutTrailingSubstatement12
	;

emptyStatement_
	:	';'
	;

labeledStatement
	:	Identifier ':' statement
	;

labeledStatementNoShortIf
	:	Identifier ':' statementNoShortIf
	;

expressionStatement
	:	statementExpression ';'
	;

statementExpression
	:	assignment #statementExpression1
	|	preIncrementExpression #statementExpression2
	|	preDecrementExpression #statementExpression3
	|	postIncrementExpression #statementExpression4
	|	postDecrementExpression #statementExpression5
	|	methodInvocation #statementExpression6
	|	classInstanceCreationExpression #statementExpression7
	;

ifThenStatement
	:	'if' '(' expression ')' statement
	;

ifThenElseStatement
	:	'if' '(' expression ')' statementNoShortIf 'else' statement
	;

ifThenElseStatementNoShortIf
	:	'if' '(' expression ')' statementNoShortIf 'else' statementNoShortIf
	;

assertStatement
	:	'assert' expression ';' #assertStatement1
	|	'assert' expression ':' expression ';' #assertStatement2
	;

switchStatement
	:	'switch' '(' expression ')' switchBlock
	;

switchBlock
	:	'{' switchBlockStatementGroup* switchLabel* '}'
	;

switchBlockStatementGroup
	:	switchLabels blockStatements
	;

switchLabels
	:	switchLabel switchLabel*
	;

switchLabel
	:	'case' constantExpression ':' #switchLabel1
	|	'case' enumConstantName ':' #switchLabel2
	|	'default' ':' #switchLabel3
	;

enumConstantName
	:	Identifier
	;

whileStatement
	:	'while' '(' expression ')' statement
	;

whileStatementNoShortIf
	:	'while' '(' expression ')' statementNoShortIf
	;

doStatement
	:	'do' statement 'while' '(' expression ')' ';'
	;

forStatement
	:	basicForStatement #forStatement1
	|	enhancedForStatement #forStatement2
	;

forStatementNoShortIf
	:	basicForStatementNoShortIf #forStatementNoShortIf1
	|	enhancedForStatementNoShortIf #forStatementNoShortIf2
	;

basicForStatement
	:	'for' '(' forInit? ';' expression? ';' forUpdate? ')' statement
	;

basicForStatementNoShortIf
	:	'for' '(' forInit? ';' expression? ';' forUpdate? ')' statementNoShortIf
	;

forInit
	:	statementExpressionList #forInit1
	|	localVariableDeclaration #forInit2
	;

forUpdate
	:	statementExpressionList
	;

statementExpressionList
	:	statementExpression (',' statementExpression)*
	;

enhancedForStatement
	:	'for' '(' variableModifier* unannType variableDeclaratorId ':' expression ')' statement
	;

enhancedForStatementNoShortIf
	:	'for' '(' variableModifier* unannType variableDeclaratorId ':' expression ')' statementNoShortIf
	;

breakStatement
	:	'break' Identifier? ';'
	;

continueStatement
	:	'continue' Identifier? ';'
	;

returnStatement
	:	'return' expression? ';'
	;

throwStatement
	:	'throw' expression ';'
	;

synchronizedStatement
	:	'synchronized' '(' expression ')' block
	;

tryStatement
	:	'try' block catches #tryStatement1
	|	'try' block catches? finally_ #tryStatement2
	|	tryWithResourcesStatement #tryStatement3
	;

catches
	:	catchClause catchClause*
	;

catchClause
	:	'catch' '(' catchFormalParameter ')' block
	;

catchFormalParameter
	:	variableModifier* catchType variableDeclaratorId
	;

catchType
	:	unannClassType ('|' classType)*
	;

finally_
	:	'finally' block
	;

tryWithResourcesStatement
	:	'try' resourceSpecification block catches? finally_?
	;

resourceSpecification
	:	'(' resourceList ';'? ')'
	;

resourceList
	:	resource (';' resource)*
	;

resource
	:	variableModifier* unannType variableDeclaratorId '=' expression
	;

/*
 * Productions from Â§15 (Expressions)
 */

primary
	:	(	primaryNoNewArray_lfno_primary
		|	arrayCreationExpression
		)
		(	primaryNoNewArray_lf_primary
		)*
	;

primaryNoNewArray
	:	literal #primaryNoNewArray1
	|	typeName ('[' ']')* '.' 'class' #primaryNoNewArray2
	|	'void' '.' 'class' #primaryNoNewArray3
	|	'this' #primaryNoNewArray4
	|	typeName '.' 'this' #primaryNoNewArray5
	|	'(' expression ')' #primaryNoNewArray6
	|	classInstanceCreationExpression #primaryNoNewArray7
	|	fieldAccess #primaryNoNewArray8
	|	arrayAccess #primaryNoNewArray9
	|	methodInvocation #primaryNoNewArray10
	|	methodReference #primaryNoNewArray11
	;

primaryNoNewArray_lf_arrayAccess
	:
	;

primaryNoNewArray_lfno_arrayAccess
	:	literal #primaryNoNewArray_lfno_arrayAccess1
	|	typeName ('[' ']')* '.' 'class' #primaryNoNewArray_lfno_arrayAccess2
	|	'void' '.' 'class' #primaryNoNewArray_lfno_arrayAccess3
	|	'this' #primaryNoNewArray_lfno_arrayAccess4
	|	typeName '.' 'this' #primaryNoNewArray_lfno_arrayAccess5
	|	'(' expression ')' #primaryNoNewArray_lfno_arrayAccess6
	|	classInstanceCreationExpression #primaryNoNewArray_lfno_arrayAccess7
	|	fieldAccess #primaryNoNewArray_lfno_arrayAccess8
	|	methodInvocation #primaryNoNewArray_lfno_arrayAccess9
	|	methodReference #primaryNoNewArray_lfno_arrayAccess10
	;

primaryNoNewArray_lf_primary
	:	classInstanceCreationExpression_lf_primary #primaryNoNewArray_lf_primary1
	|	fieldAccess_lf_primary #primaryNoNewArray_lf_primary2
	|	arrayAccess_lf_primary #primaryNoNewArray_lf_primary3
	|	methodInvocation_lf_primary #primaryNoNewArray_lf_primary4
	|	methodReference_lf_primary #primaryNoNewArray_lf_primary5
	;

primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary
	:
	;

primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary
	:	classInstanceCreationExpression_lf_primary #primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary1
	|	fieldAccess_lf_primary #primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary2
	|	methodInvocation_lf_primary #primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary3
	|	methodReference_lf_primary #primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary4
	;

primaryNoNewArray_lfno_primary
	:	literal #primaryNoNewArray_lfno_primary1
	|	typeName ('[' ']')* '.' 'class' #primaryNoNewArray_lfno_primary2
	|	unannPrimitiveType ('[' ']')* '.' 'class' #primaryNoNewArray_lfno_primary3
	|	'void' '.' 'class' #primaryNoNewArray_lfno_primary4
	|	'this' #primaryNoNewArray_lfno_primary5
	|	typeName '.' 'this' #primaryNoNewArray_lfno_primary6
	|	'(' expression ')' #primaryNoNewArray_lfno_primary7
	|	classInstanceCreationExpression_lfno_primary #primaryNoNewArray_lfno_primary8
	|	fieldAccess_lfno_primary #primaryNoNewArray_lfno_primary9
	|	arrayAccess_lfno_primary #primaryNoNewArray_lfno_primary10
	|	methodInvocation_lfno_primary #primaryNoNewArray_lfno_primary11
	|	methodReference_lfno_primary #primaryNoNewArray_lfno_primary12
	;

primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary
	:
	;

primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary
	:	literal #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary1
	|	typeName ('[' ']')* '.' 'class' #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary2
	|	unannPrimitiveType ('[' ']')* '.' 'class' #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary3
	|	'void' '.' 'class' #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary4
	|	'this' #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary5
	|	typeName '.' 'this' #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary6
	|	'(' expression ')' #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary7
	|	classInstanceCreationExpression_lfno_primary #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary8
	|	fieldAccess_lfno_primary #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary9
	|	methodInvocation_lfno_primary #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary10
	|	methodReference_lfno_primary #primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary11
	;

classInstanceCreationExpression
	:	'new' typeArguments? annotation* Identifier ('.' annotation* Identifier)* typeArgumentsOrDiamond? '(' argumentList? ')' classBody? #classInstanceCreationExpression1
	|	expressionName '.' 'new' typeArguments? annotation* Identifier typeArgumentsOrDiamond? '(' argumentList? ')' classBody? #classInstanceCreationExpression2
	|	primary '.' 'new' typeArguments? annotation* Identifier typeArgumentsOrDiamond? '(' argumentList? ')' classBody? #classInstanceCreationExpression3
	;

classInstanceCreationExpression_lf_primary
	:	'.' 'new' typeArguments? annotation* Identifier typeArgumentsOrDiamond? '(' argumentList? ')' classBody?
	;

classInstanceCreationExpression_lfno_primary
	:	'new' typeArguments? annotation* Identifier ('.' annotation* Identifier)* typeArgumentsOrDiamond? '(' argumentList? ')' classBody? #classInstanceCreationExpression_lfno_primary1
	|	expressionName '.' 'new' typeArguments? annotation* Identifier typeArgumentsOrDiamond? '(' argumentList? ')' classBody? #classInstanceCreationExpression_lfno_primary2
	;

typeArgumentsOrDiamond
	:	typeArguments #typeArgumentsOrDiamond1
	|	'<' '>' #typeArgumentsOrDiamond2
	;

fieldAccess
	:	primary '.' Identifier #fieldAccess1
	|	'super' '.' Identifier #fieldAccess2
	|	typeName '.' 'super' '.' Identifier #fieldAccess3
	;

fieldAccess_lf_primary
	:	'.' Identifier
	;

fieldAccess_lfno_primary
	:	'super' '.' Identifier #fieldAccess_lfno_primary1
	|	typeName '.' 'super' '.' Identifier #fieldAccess_lfno_primary2
	;

arrayAccess
	:	(	expressionName '[' expression ']'
		|	primaryNoNewArray_lfno_arrayAccess '[' expression ']'
		)
		(	primaryNoNewArray_lf_arrayAccess '[' expression ']'
		)*
	;

arrayAccess_lf_primary
	:	(	primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary '[' expression ']'
		)
		(	primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary '[' expression ']'
		)*
	;

arrayAccess_lfno_primary
	:	(	expressionName '[' expression ']'
		|	primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary '[' expression ']'
		)
		(	primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary '[' expression ']'
		)*
	;

methodInvocation
	:	methodName '(' argumentList? ')' #methodInvocation1
	|	typeName '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation2
	|	expressionName '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation3
	|	primary '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation4
	|	'super' '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation5
	|	typeName '.' 'super' '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation6
	;

methodInvocation_lf_primary
	:	'.' typeArguments? Identifier '(' argumentList? ')'
	;

methodInvocation_lfno_primary
	:	methodName '(' argumentList? ')' #methodInvocation_lfno_primary1
	|	typeName '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation_lfno_primary2
	|	expressionName '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation_lfno_primary3
	|	'super' '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation_lfno_primary4
	|	typeName '.' 'super' '.' typeArguments? Identifier '(' argumentList? ')' #methodInvocation_lfno_primary5
	;

argumentList
	:	expression (',' expression)*
	;

methodReference
	:	expressionName '::' typeArguments? Identifier #methodReference1
	|	referenceType '::' typeArguments? Identifier #methodReference2
	|	primary '::' typeArguments? Identifier #methodReference3
	|	'super' '::' typeArguments? Identifier #methodReference4
	|	typeName '.' 'super' '::' typeArguments? Identifier #methodReference5
	|	classType '::' typeArguments? 'new' #methodReference6
	|	arrayType '::' 'new' #methodReference7
	;

methodReference_lf_primary
	:	'::' typeArguments? Identifier
	;

methodReference_lfno_primary
	:	expressionName '::' typeArguments? Identifier #methodReference_lfno_primary1
	|	referenceType '::' typeArguments? Identifier #methodReference_lfno_primary2
	|	'super' '::' typeArguments? Identifier #methodReference_lfno_primary3
	|	typeName '.' 'super' '::' typeArguments? Identifier #methodReference_lfno_primary4
	|	classType '::' typeArguments? 'new' #methodReference_lfno_primary5
	|	arrayType '::' 'new' #methodReference_lfno_primary6
	;

arrayCreationExpression
	:	'new' primitiveType dimExprs dims? #arrayCreationExpression1
	|	'new' classOrInterfaceType dimExprs dims? #arrayCreationExpression2
	|	'new' primitiveType dims arrayInitializer #arrayCreationExpression3
	|	'new' classOrInterfaceType dims arrayInitializer #arrayCreationExpression4
	;

dimExprs
	:	dimExpr dimExpr*
	;

dimExpr
	:	annotation* '[' expression ']'
	;

constantExpression
	:	expression
	;

expression
	:	lambdaExpression #expression1
	|	assignmentExpression #expression2
	;

lambdaExpression
	:	lambdaParameters '->' lambdaBody
	;

lambdaParameters
	:	Identifier #lambdaParameters1
	|	'(' formalParameterList? ')' #lambdaParameters2
	|	'(' inferredFormalParameterList ')' #lambdaParameters3
	;

inferredFormalParameterList
	:	Identifier (',' Identifier)*
	;

lambdaBody
	:	expression #lambdaBody1
	|	block #lambdaBody2
	;

assignmentExpression
	:	conditionalExpression #assignmentExpression1
	|	assignment #assignmentExpression2
	;

assignment
	:	leftHandSide assignmentOperator expression
	;

leftHandSide
	:	expressionName #leftHandSide1
	|	fieldAccess #leftHandSide2
	|	arrayAccess #leftHandSide3
	;

assignmentOperator
	:	'=' #assignmentOperator1
	|	'*=' #assignmentOperator2
	|	'/=' #assignmentOperator3
	|	'%=' #assignmentOperator4
	|	'+=' #assignmentOperator5
	|	'-=' #assignmentOperator6
	|	'<<=' #assignmentOperator7
	|	'>>=' #assignmentOperator8
	|	'>>>=' #assignmentOperator9
	|	'&=' #assignmentOperator10
	|	'^=' #assignmentOperator11
	|	'|=' #assignmentOperator12
	;

conditionalExpression
	:	conditionalOrExpression #conditionalExpression1
	|	conditionalOrExpression '?' expression ':' conditionalExpression #conditionalExpression2
	;

conditionalOrExpression
	:	conditionalAndExpression #conditionalOrExpression1
	|	conditionalOrExpression '||' conditionalAndExpression #conditionalOrExpression2
	;

conditionalAndExpression
	:	inclusiveOrExpression #conditionalAndExpression1
	|	conditionalAndExpression '&&' inclusiveOrExpression #conditionalAndExpression2
	;

inclusiveOrExpression
	:	exclusiveOrExpression #inclusiveOrExpression1
	|	inclusiveOrExpression '|' exclusiveOrExpression #inclusiveOrExpression2
	;

exclusiveOrExpression
	:	andExpression #exclusiveOrExpression1
	|	exclusiveOrExpression '^' andExpression #exclusiveOrExpression2
	;

andExpression
	:	equalityExpression #andExpression1
	|	andExpression '&' equalityExpression #andExpression2
	;

equalityExpression
	:	relationalExpression #equalityExpression1
	|	equalityExpression '==' relationalExpression #equalityExpression2
	|	equalityExpression '!=' relationalExpression #equalityExpression3
	;

relationalExpression
	:	shiftExpression #relationalExpression1
	|	relationalExpression '<' shiftExpression #relationalExpression2
	|	relationalExpression '>' shiftExpression #relationalExpression3
	|	relationalExpression '<=' shiftExpression #relationalExpression4
	|	relationalExpression '>=' shiftExpression #relationalExpression5
	|	relationalExpression 'instanceof' referenceType #relationalExpression6
	;

shiftExpression
	:	additiveExpression #shiftExpression1
	|	shiftExpression '<' '<' additiveExpression #shiftExpression2
	|	shiftExpression '>' '>' additiveExpression #shiftExpression3
	|	shiftExpression '>' '>' '>' additiveExpression #shiftExpression4
	;

additiveExpression
	:	multiplicativeExpression #additiveExpression1
	|	additiveExpression '+' multiplicativeExpression #additiveExpression2
	|	additiveExpression '-' multiplicativeExpression #additiveExpression3
	;

multiplicativeExpression
	:	unaryExpression #multiplicativeExpression1
	|	multiplicativeExpression '*' unaryExpression #multiplicativeExpression2
	|	multiplicativeExpression '/' unaryExpression #multiplicativeExpression3
	|	multiplicativeExpression '%' unaryExpression #multiplicativeExpression4
	;

unaryExpression
	:	preIncrementExpression #unaryExpression1
	|	preDecrementExpression #unaryExpression2
	|	'+' unaryExpression #unaryExpression3
	|	'-' unaryExpression #unaryExpression4
	|	unaryExpressionNotPlusMinus #unaryExpression5
	;

preIncrementExpression
	:	'++' unaryExpression
	;

preDecrementExpression
	:	'--' unaryExpression
	;

unaryExpressionNotPlusMinus
	:	postfixExpression #unaryExpressionNotPlusMinus1
	|	'~' unaryExpression #unaryExpressionNotPlusMinus2
	|	'!' unaryExpression #unaryExpressionNotPlusMinus3
	|	castExpression #unaryExpressionNotPlusMinus4
	;

postfixExpression
	:	(	primary
		|	expressionName
		)
		(	postIncrementExpression_lf_postfixExpression
		|	postDecrementExpression_lf_postfixExpression
		)*
	;

postIncrementExpression
	:	postfixExpression '++'
	;

postIncrementExpression_lf_postfixExpression
	:	'++'
	;

postDecrementExpression
	:	postfixExpression '--'
	;

postDecrementExpression_lf_postfixExpression
	:	'--'
	;

castExpression
	:	'(' primitiveType ')' unaryExpression #castExpression1
	|	'(' referenceType additionalBound* ')' unaryExpressionNotPlusMinus #castExpression2
	|	'(' referenceType additionalBound* ')' lambdaExpression #castExpression3
	;
