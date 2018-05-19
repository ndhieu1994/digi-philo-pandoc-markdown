#!/usr/bin/env python

"""
Pandoc filter to convert divs with latex="true" to LaTeX
environments in LaTeX output. The first class
will be regarded as the name of the latex environment
e.g.
<div latex="true" class="note abc">...</div>
will becomes
\begin{note}...\end{note}
"""


from panflute import run_filter, RawBlock, Div

def latexblock(x):
    return RawBlock(x, format='latex')

def latex_env_div(elem, doc):
    if isinstance(elem, Div) and elem.attributes.get("latex") == "true":
        tex_environment = elem.classes[0]
        content = elem.content.list
        if elem.identifier == "":
            label = ""
        else:
            label = "\\label{" + elem.identifier + "}"
        return \
            [latexblock("\\begin{" + tex_environment + "}" + label)] \
            + content \
            + [latexblock("\\end{" + tex_environment + "}")]


def main(doc=None):
    return run_filter(action=latex_env_div, doc=doc)

if __name__ == '__main__':
    main()
