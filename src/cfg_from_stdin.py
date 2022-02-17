from src.cfg.visual import draw_CFG
from src.cfg.cfg_extractor import CFGExtractor


def prompt():
    is_read_file = input("Read from file/stream (f/s)? ").startswith(("f", "F"))
    is_verbose = input("Verbose graph draw (y/n)? ").startswith(("y", "Y"))
    file_path = None
    if is_read_file:
        default_path = "../test_source/test.java"
        file_path = input("Enter file path: ")
        file_path = file_path if file_path else default_path

    return is_read_file, is_verbose, file_path


def main():
    is_read_file, is_verbose, file_path = prompt()

    extractor = CFGExtractor()

    if is_read_file:
        funcs, token_stream = extractor.from_file(file_path)
    else:
        funcs, token_stream = extractor.from_stdin()

    for i, g in enumerate(funcs.values()):
        draw_CFG(g, f"../test_output/temp{i}", token_stream, verbose=is_verbose)


if __name__ == '__main__':
    main()
