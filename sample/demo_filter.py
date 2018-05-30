#!/usr/bin/env python

from panflute import *

def headerpagebreak(elem, doc):
    if isinstance(elem, Header):
        if elem.level == 1:
            return [RawBlock('\pagebreak', format='latex'), elem]

def rm_header2_or_greater(elem, doc):
    if isinstance(elem, Header):
        if elem.level >= 2:
            return Para(Emph(Strong(*elem.content)))


if __name__ == "__main__":
    run_filter(headerpagebreak)
    # run_filters(actions=[headerpagebreak, rm_header2_or_greater])
