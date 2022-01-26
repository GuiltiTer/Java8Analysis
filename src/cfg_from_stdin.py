from antlr4 import CommonTokenStream, StdinStream, FileStream

from antlr.gen.JavaLexer import JavaLexer
from antlr.gen.JavaParser import JavaParser
from src.cfg_extractor.cfg_extractor_visitor import CFGExtractorVisitor
from src.graph.visual import draw_CFG


def prompt():
    # is_read_file = input("Read from file/stream (f/s)? ").startswith(("f", "F"))
    # is_verbose = input("Verbose graph draw (y/n)? ").startswith(("y", "Y"))
    is_read_file = True
    is_verbose = True
    file_path = None
    if is_read_file:
        default_path = "../test_source/if.java"
        # file_path = input("Enter file path: ")
        file_path = ""
        file_path = file_path if file_path else default_path

    return is_read_file, is_verbose, file_path


def extract(stream):
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    parse_tree = parser.compilationUnit()
    cfg_extractor = CFGExtractorVisitor()
    cfg_extractor.visit(parse_tree)
    funcs = cfg_extractor.functions
    return funcs, token_stream


def main():
    is_read_file, is_verbose, file_path = prompt()
    stream = (FileStream(file_path, encoding="utf8") if is_read_file else StdinStream())
    funcs, token_stream = extract(stream)
    for i, g in enumerate(funcs.values()):
        draw_CFG(g, f"../test_output/temp{i}", token_stream, verbose=is_verbose)


if __name__ == '__main__':
    main()
