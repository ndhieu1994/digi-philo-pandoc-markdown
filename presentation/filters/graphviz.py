#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "graphviz" into
graphviz-generated images.

Needs pygraphviz
"""

import pygraphviz, os, sys, hashlib
from panflute import *

imagedir = "graphviz-images"

def sha1(x):
    return hashlib.sha1(x.encode(sys.getfilesystemencoding())).hexdigest()

def graphviz(elem, doc):
    if isinstance(elem, CodeBlock):
        if "graphviz" in elem.classes:

            if "caption" in elem.attributes.keys():
                caption = elem.attributes.get("caption")
                title = "fig:"
            else:
                caption = ""
                title = ""
            alt = Str(caption)

            code = elem.text
            G = pygraphviz.AGraph(string=code)
            G.layout()
            filename = sha1(code)
            filetype = {'html': 'png', 'latex': 'pdf'}.get(doc.format, 'png')
            imageurl = imagedir + '/' + filename + '.' + filetype
            if not os.path.isfile(imageurl):
                try:
                    os.mkdir(imagedir)
                    sys.stderr.write('Created directory ' + imagedir + '\n')
                except OSError:
                    pass
                G.draw(imageurl)
                sys.stderr.write('Created image ' + imageurl + '\n')
            return Para(Image( \
                alt, \
                url=imageurl, \
                title=title, \
                identifier=elem.identifier, \
                attributes=elem.attributes))

    return

def main():
    return run_filter(graphviz)

if __name__ == "__main__":
    main()
