from antlr4 import CommonTokenStream, StdinStream, FileStream
from src.antlr.gen.JavaLexer import JavaLexer
from src.antlr.gen.JavaParser import JavaParser
from src.cfg.cfg_extractor_visitor import CFGExtractorVisitor


class CFGExtractor:
    def __init__(self):
        self.__extractor = CFGExtractorVisitor()

    def from_file(self, file_path):
        stream = FileStream(file_path, encoding="utf-8")
        return self.__extract(stream)

    def from_stdin(self):
        stream = StdinStream()
        return self.__extract(stream)

    def __extract(self, stream):
        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)
        parser = JavaParser(token_stream)
        parse_tree = parser.compilationUnit()
        funcs = self.__extractor.extract(parse_tree)
        return funcs, token_stream
