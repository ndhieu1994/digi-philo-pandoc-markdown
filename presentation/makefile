# Makefile
# converts multiple markdown files
# to standalone pdf files


INPUT_DIR = sections
METADATA = metadata.yaml
FILTERS = filters
OUTPUT_DIR = out
OUTPUT_NAME = markdown-presentation

files = $(METADATA) $(sort $(wildcard $(INPUT_DIR)/*.md))

PANDOC_OPTIONS= --standalone --number-sections

PANDOC_FILTERS=\
	--filter $(FILTERS)/graphviz_shell.py \
	--filter pandoc-citeproc \

PANDOC_BEAMER_OPTIONS=\
	-t beamer \
	--pdf-engine=pdflatex \
	--highlight-style zenburn \
	$(PANDOC_FILTERS)

PANDOC_HANDOUT_OPTIONS=\
	-V handout

.PHONY: all clean slides handout latex filtertest

all: slides handout

clean:
	rm out/*
	rm graphviz-images/*

slides: $(OUTPUT_DIR)/$(OUTPUT_NAME).slides.pdf
handout: $(OUTPUT_DIR)/$(OUTPUT_NAME).handout.pdf
latex: $(OUTPUT_DIR)/$(OUTPUT_NAME).tex
filtertest: $(OUTPUT_DIR)/$(OUTPUT_NAME).json $(OUTPUT_DIR)/$(OUTPUT_NAME).filtered.json

$(OUTPUT_DIR)/$(OUTPUT_NAME).json: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$^ \
		-o $@

$(OUTPUT_DIR)/$(OUTPUT_NAME).filtered.json: $(files)
	pandoc -t json \
		$(PANDOC_OPTIONS) \
		$(PANDOC_FILTERS) \
		$^ \
		-o $@


$(OUTPUT_DIR)/$(OUTPUT_NAME).tex: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(PANDOC_BEAMER_OPTIONS) \
		$^ \
		-o $@

$(OUTPUT_DIR)/$(OUTPUT_NAME).slides.pdf: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(PANDOC_BEAMER_OPTIONS) \
		$^ \
		-o $@

$(OUTPUT_DIR)/$(OUTPUT_NAME).handout.pdf: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(PANDOC_BEAMER_OPTIONS) \
		$(PANDOC_HANDOUT_OPTIONS) \
		$^ \
		-o $@

