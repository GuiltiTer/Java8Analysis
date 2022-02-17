import html

import graphviz as gv

from src.antlr.rule_utils import extract_exact_text
from src.data_structures.graph.graph_interface import IGraph

FONT_SIZE = "22"
PEN_WIDTH = "2"


def draw_CFG(graph: IGraph, filename, token_stream=None, format="png", verbose=True):
    gr = gv.Digraph(comment=filename, format=format, node_attr={"shape": "none"})
    gr.node("start", style="filled", fillcolor="#aaffaa", shape="oval", fontsize=FONT_SIZE)

    for node, data in graph.node_items:
        block_contents = (stringify_block(data, token_stream) if verbose else stringify_block_lineno_only(data))
        gr.node(str(node), label=build_node_template(node, block_contents))
    gr.node(str(graph.last), label="end", style="filled", fillcolor="#ffaaaa", shape="oval", fontsize=FONT_SIZE)

    for (f, t), data in graph.edge_items:
        gr.edge(f"{str(f)}", f"{str(t)}", label=data, fontsize=FONT_SIZE, penwidth=PEN_WIDTH)
    gr.edge("start", str(graph.head), penwidth=PEN_WIDTH)

    gr.render(f"{filename}.gv", view=True)


def build_node_template(node_label, contents):
    b_len = len(contents.splitlines())
    line_height = 40
    s = f"""<<FONT POINT-SIZE="{FONT_SIZE}">  
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <tr>
                <td width="30" height="30" fixedsize="true">{node_label + 1}</td>
                <td width="9" height="9" fixedsize="true" style="invis"></td>
                <td width="9" height="9" fixedsize="true" style="invis"></td>
            </tr>
            <tr>
                <td width="30" height="{b_len * line_height}" fixedsize="true" sides="tlb"></td>
                <td width="50" height="{b_len * line_height}" fixedsize="false" sides="bt" PORT="here">{contents}</td>
                <td width="30" height="{b_len * line_height}" fixedsize="true" sides="brt"></td>
            </tr>
        </TABLE>
    </FONT>>"""
    return strip_lines(s)


def strip_lines(x: str): return "\n".join(line.strip() for line in x.splitlines())


def node_content_to_html(node_contents):
    delimiter = '<br align="left"/>\n'
    content_list_string = delimiter.join([html.escape(f"{l}: {content}") for l, content in node_contents])
    return content_list_string + delimiter


def stringify_block(data, token_stream):
    cs = [(rule.start.line, extract_exact_text(token_stream, rule)) for rule in data]
    b = node_content_to_html(cs)
    return b


def stringify_block_lineno_only(data):
    left, right = data[0].start.line, data[-1].stop.line
    if left == right:
        return f"{left}"

    return f"{left}..{right}"
