files = metadata.yaml summary.md

FILTERS =\
    --filter pandoc-citeproc

.PHONY: all clean

all: summary.pdf
clean:
	rm test.tex summary.pdf

tex: test.tex

test.tex: $(files)
	pandoc $(FILTERS) -t latex $^ -o $@

summary.pdf: $(files)
	pandoc $(FILTERS) $^ -o $@
