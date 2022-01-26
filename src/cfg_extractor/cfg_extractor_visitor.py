from antlr.gen.JavaParser import JavaParser
from antlr.gen.JavaParserVisitor import JavaParserVisitor
from src.cfg_extractor.lang_structures import (embed_in_function_structure, embed_in_do_while_structure,
                                               embed_in_for_structure, embed_in_switch_structure,
                                               embed_in_if_structure, embed_in_if_else_structure,
                                               embed_in_while_structure, embed_in_try_catch_structure)
from src.graph.utils import (build_single_node_graph, concat_graphs)


class CFGExtractorVisitor(JavaParserVisitor):
    """
    The class includes a method for each non-terminal (i.e., selection, iteration, jump and try-catch statements)
    Each method builds a part of a CFG rooted at its corresponding non-terminal.
    The extracted sub-graph is saved using the `networkx` library.
    visit() is the first method of the class which is invoked initially by the main.
    """

    def __init__(self):
        """
        `functions` is a dictionary to keep each function signature and its CFG reference.
        Each CFG is kept as a `networkx.DiGraph`.
        """
        self.functions = {}

    def visitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        gin = self.visit(ctx.methodBody())
        self.functions[ctx] = embed_in_function_structure(gin)

    def visitBlock(self, ctx: JavaParser.BlockContext):
        return self.visit(ctx.blockStatements())

    def visitBlockStatements(self, ctx: JavaParser.BlockStatementsContext):
        gins = []
        for block in ctx.blockStatement():
            if block is None:
                break
            gins.append(self.visit(block))
        g = gins[0]
        if len(gins) != 1:
            for i in range(1, len(gins)):
                g = concat_graphs(g, gins[i])
        return g

    def visitIfThenStatement(self, ctx: JavaParser.IfThenStatementContext):
        condition = ctx.expression()
        if_body = ctx.statement()
        gin = self.visit(if_body)
        return embed_in_if_structure(gin, condition)

    def visitIfThenElseStatement(self, ctx: JavaParser.IfThenElseStatementContext):
        condition = ctx.expression()
        if_body = ctx.statementNoShortIf()
        else_body = ctx.statement()
        gin_if = self.visit(if_body)
        gin_else = self.visit(else_body)
        return embed_in_if_else_structure(gin_if, gin_else, condition)

    def visitSwitchStatement(self, ctx: JavaParser.SwitchStatementContext):
        condition = ctx.expression()
        gin_by_case = self.visit(ctx.switchBlock())
        return embed_in_switch_structure(gin_by_case, condition)

    def visitSwitchBlock(self, ctx: JavaParser.SwitchBlockContext):
        return [self.visit(switch_group) for switch_group in ctx.switchBlockStatementGroup()]

    def visitSwitchBlockStatementGroup(self, ctx: JavaParser.SwitchBlockStatementGroupContext):
        case = ctx.switchLabels()
        block_graph = self.visit(ctx.blockStatements())
        return case, block_graph

    def visitBasicForStatement(self, ctx: JavaParser.BasicForStatementContext):
        init = ctx.forInit()
        condition = ctx.expression()
        successor = ctx.forUpdate()
        for_body = ctx.statement()
        gin = self.visit(for_body)
        return embed_in_for_structure(gin, init, condition, successor)

    def visitWhileStatement(self, ctx: JavaParser.WhileStatementContext):
        condition = ctx.expression()
        gin = self.visit(ctx.statement())
        return embed_in_while_structure(gin, condition)

    def visitDoStatement(self, ctx: JavaParser.DoStatementContext):
        condition = ctx.expression()
        gin = self.visit(ctx.statement())
        return embed_in_do_while_structure(gin, condition)

    def visitTryStatement1(self, ctx: JavaParser.TryStatement1Context):
        try_body = self.visit(ctx.block())
        catches = self.visit(ctx.catches())
        return embed_in_try_catch_structure(try_body, catches)

    def visitCatches(self, ctx: JavaParser.CatchesContext):
        return [self.visit(catches) for catches in ctx.catchClause()]

    def visitCatchClause(self, ctx: JavaParser.CatchClauseContext):
        catch_body = self.visit(ctx.block())
        exception = self.visit(ctx.catchFormalParameter())
        return exception, catch_body

    def visitCatchFormalParameter(self, ctx: JavaParser.CatchFormalParameterContext):
        return build_single_node_graph(ctx)

    def visitExpressionStatement(self, ctx: JavaParser.ExpressionStatementContext):
        return build_single_node_graph(ctx)

    def visitLocalVariableDeclarationStatement(self, ctx: JavaParser.LocalVariableDeclarationStatementContext):
        return build_single_node_graph(ctx)

    def visitSwitchLabel1(self, ctx: JavaParser.SwitchLabel1Context):
        return self.visit(ctx.constantExpression())

    def visitSwitchLabel3(self, ctx: JavaParser.SwitchLabel3Context):
        return build_single_node_graph(ctx)

    def visitConstantExpression(self, ctx: JavaParser.ConstantExpressionContext):
        return build_single_node_graph(ctx)

    def visitBreakStatement(self, ctx: JavaParser.BreakStatementContext):
        return build_single_node_graph(ctx)

    def visitLocalVariableDeclaration(self, ctx: JavaParser.LocalVariableDeclarationContext):
        return build_single_node_graph(ctx)

    def visitPostIncrementExpression(self, ctx: JavaParser.PostIncrementExpressionContext):
        return build_single_node_graph(ctx)

    def visitContinueStatement(self, ctx: JavaParser.ContinueStatementContext):
        return build_single_node_graph(ctx)

    def visitThrowStatement(self, ctx: JavaParser.ThrowStatementContext):
        return build_single_node_graph(ctx)

    def visitReturnStatement(self, ctx: JavaParser.ReturnStatementContext):
        return build_single_node_graph(ctx)
