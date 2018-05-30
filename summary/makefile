files = metadata.yaml summary.md

FILTERS =\
    --filter pandoc-citeproc

.PHONY: all clean

all: summary.pdf
clean:
	rm summary.pdf

summary.pdf: $(files)
	pandoc $(FILTERS) $^ -o $@
