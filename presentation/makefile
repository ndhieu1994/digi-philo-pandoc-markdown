# Makefile
# converts multiple markdown files
# to standalone pdf files: article, beamer


INPUT_DIR = sections
METADATA = metadata.yaml
FILTERS = filters
OUTPUT_DIR = out
OUTPUT_NAME = markdown-presentation

files = $(sort $(wildcard $(INPUT_DIR)/*.md))

PANDOC_OPTIONS= --standalone

PANDOC_PDF_OPTIONS=

PANDOC_FILTERS=\
	--filter $(FILTERS)/graphviz2.py \
	--filter $(FILTERS)/latex_env_div.py \
	--filter pandoc-citeproc \
	# --filter $(FILTERS)/run_programm.py \

PANDOC_BEAMER_OPTIONS=\
	-t beamer \
	--pdf-engine=pdflatex \
	--highlight-style zenburn \
	$(PANDOC_FILTERS)

PANDOC_NOTES_OPTIONS=\
	-V notes \
	--template=notes.beamer

PANDOC_HANDOUT_OPTIONS=\
	-V handout

.PHONY: all clean

all: slides notes handout

clean:
	rm out/*
	rm graphviz-images/*

document: $(OUTPUT_NAME).pdf
slides: $(OUTPUT_NAME).slides.pdf
notes: $(OUTPUT_NAME).slides.notes.pdf
handout: $(OUTPUT_NAME).handout.pdf
latex: $(OUTPUT_NAME).tex
filtertest: $(OUTPUT_NAME).json $(OUTPUT_NAME).filtered.json

$(OUTPUT_NAME).pdf: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(PANDOC_FILTERS) \
		$(METADATA) \
		$^ \
		-o $(OUTPUT_DIR)/$@

$(OUTPUT_NAME).json: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(METADATA) \
		$^ \
		-o $(OUTPUT_DIR)/$@

$(OUTPUT_NAME).filtered.json: $(files)
	pandoc -t json \
		$(PANDOC_OPTIONS) \
		$(PANDOC_FILTERS) \
		$(METADATA) \
		$^ \
		-o $(OUTPUT_DIR)/$@


$(OUTPUT_NAME).tex: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(METADATA) \
		$(PANDOC_BEAMER_OPTIONS) \
		$^ \
		-o $(OUTPUT_DIR)/$@

$(OUTPUT_NAME).slides.pdf: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(METADATA) \
		$(PANDOC_BEAMER_OPTIONS) \
		$^ \
		-o $(OUTPUT_DIR)/$@

$(OUTPUT_NAME).slides.notes.pdf: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(METADATA)\
		$(PANDOC_BEAMER_OPTIONS) \
		$(PANDOC_NOTES_OPTIONS) \
		$^ \
		-o $(OUTPUT_DIR)/$@

$(OUTPUT_NAME).handout.pdf: $(files)
	pandoc \
		$(PANDOC_OPTIONS) \
		$(METADATA) \
		$(PANDOC_BEAMER_OPTIONS) \
		$(PANDOC_HANDOUT_OPTIONS) \
		$^ \
		-o $(OUTPUT_DIR)/$@


