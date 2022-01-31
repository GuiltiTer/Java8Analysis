from functools import reduce
from antlr.gen.JavaParser import JavaParser
from antlr.gen.JavaParserVisitor import JavaParserVisitor
from src.cfg_extractor.lang_structures import (embed_in_function_structure, embed_in_do_while_structure,
                                               embed_in_for_structure, embed_in_switch_structure,
                                               embed_in_if_structure, embed_in_if_else_structure,
                                               embed_in_while_structure, embed_in_try_catch_structure)
from src.graph.utils import (build_single_node_graph, concat_graphs)
from src.data_structures.graph.networkx_builder import NxDiGraphBuilder as DiGraphBuilder
from src.cfg_extractor.language_structure.digraph_embedder import DiGraphEmbedder


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
        self.functions[ctx] = DiGraphEmbedder.embed_in_function(gin).build()

    def visitBlock(self, ctx: JavaParser.BlockContext):
        return self.visit(ctx.blockStatements())

    def visitBlockStatements(self, ctx: JavaParser.BlockStatementsContext):
        gins = (self.visit(block) for block in ctx.blockStatement())
        return reduce(DiGraphEmbedder.merge, gins)

    def visitIfThenStatement(self, ctx: JavaParser.IfThenStatementContext):
        condition = ctx.expression()
        then_part = ctx.statement()
        then_part_graph = self.visit(then_part)
        return DiGraphEmbedder.embed_in_if(condition, then_part_graph)

    def visitIfThenElseStatement(self, ctx: JavaParser.IfThenElseStatementContext):
        condition = ctx.expression()
        then_part = ctx.statementNoShortIf()
        else_part = ctx.statement()
        then_part_graph = self.visit(then_part)
        else_part_graph = self.visit(else_part)
        return DiGraphEmbedder.embed_in_if_else(condition, then_part_graph, else_part_graph)

    # def visitSwitchStatement(self, ctx: JavaParser.SwitchStatementContext):
    #     condition = ctx.expression()
    #     gin_by_case = self.visit(ctx.switchBlock())
    #     return embed_in_switch_structure(gin_by_case, condition)

    # def visitSwitchBlock(self, ctx: JavaParser.SwitchBlockContext):
    #     return [self.visit(switch_group) for switch_group in ctx.switchBlockStatementGroup()]

    # def visitSwitchBlockStatementGroup(self, ctx: JavaParser.SwitchBlockStatementGroupContext):
    #     case = ctx.switchLabels()
    #     block_graph = self.visit(ctx.blockStatements())
    #     return case, block_graph

    def visitBasicForStatement(self, ctx: JavaParser.BasicForStatementContext):
        initializer = ctx.forInit()
        condition = ctx.expression()
        successor = ctx.forUpdate()
        body_graph = self.visit(ctx.statement())
        return DiGraphEmbedder.embed_in_for(condition, initializer, body_graph, successor)

    def visitWhileStatement(self, ctx: JavaParser.WhileStatementContext):
        condition = ctx.expression()
        body_graph = self.visit(ctx.statement())
        return DiGraphEmbedder.embed_in_while(condition, body_graph)

    def visitDoStatement(self, ctx: JavaParser.DoStatementContext):
        condition = ctx.expression()
        do_body = ctx.statement()
        do_body_graph = self.visit(do_body)
        return DiGraphEmbedder.embed_in_do_while(condition, do_body_graph)

    # def visitTryStatement1(self, ctx: JavaParser.TryStatement1Context):
    #     try_body = self.visit(ctx.block())
    #     catches = self.visit(ctx.catches())
    #     return embed_in_try_catch_structure(try_body, catches)
    #
    # def visitCatches(self, ctx: JavaParser.CatchesContext):
    #     return [self.visit(catches) for catches in ctx.catchClause()]
    #
    # def visitCatchClause(self, ctx: JavaParser.CatchClauseContext):
    #     catch_body = self.visit(ctx.block())
    #     exception = self.visit(ctx.catchFormalParameter())
    #     return exception, catch_body

    def visitExpressionStatement(self, ctx: JavaParser.ExpressionStatementContext):
        return DiGraphBuilder().add_node(value=[ctx])

    def visitLocalVariableDeclarationStatement(self, ctx: JavaParser.LocalVariableDeclarationStatementContext):
        return DiGraphBuilder().add_node(value=[ctx])

    def visitBreakStatement(self, ctx: JavaParser.BreakStatementContext):
        return DiGraphBuilder().add_node(value=[ctx])

    def visitLocalVariableDeclaration(self, ctx: JavaParser.LocalVariableDeclarationContext):
        return DiGraphBuilder().add_node(value=[ctx])

    def visitContinueStatement(self, ctx: JavaParser.ContinueStatementContext):
        return DiGraphBuilder().add_node(value=[ctx])

    def visitThrowStatement(self, ctx: JavaParser.ThrowStatementContext):
        return DiGraphBuilder().add_node(value=[ctx])

    def visitReturnStatement(self, ctx: JavaParser.ReturnStatementContext):
        return DiGraphBuilder().add_node(value=[ctx])
