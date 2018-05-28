Pandoc
======

Pandoc
------

-   Created in 2006 by John MacFarlane
-   Commandline tool for converting document formats
-   Intention:
    -   Markdown originally designed for HTML generation
    -   Pandoc is designed for different output formats
    -   Initial document should be written in Markdown


Pandoc: Universal Converter
---------------------------

\normalsize
Input: 28 formats (6 markdown flavours)

\tiny
commonmark (CommonMark Markdown), creole (Creole 1.0), docbook (DocBook), docx (Word
docx), epub (EPUB), fb2 (FictionBook2 e-book), gfm (GitHub-Flavored Markdown), haddock
(Haddock markup), html (HTML), jats (JATS XML), json (JSON version of native AST), latex
(\latex), markdown (Pandoc's Markdown), markdown\_mmd (MultiMarkdown), markdown\_phpextra
(PHP Markdown Extra), markdown\_strict (original unextended Markdown), mediawiki
(MediaWiki markup), muse (Muse), native (native Haskell), odt (ODT), opml (OPML), org
(Emacs Org mode), rst (reStructuredText), t2t (txt2tags), textile (Textile), tikiwiki
(TikiWiki markup), twiki (TWiki markup), vimwiki (Vimwiki)

\normalsize
Output: 45 formats

\tiny
asciidoc (AsciiDoc), beamer (\latex beamer slide show), commonmark (CommonMark Markdown),
context (ConTeXt), docbook or docbook4 (DocBook 4), docbook5 (DocBook 5), docx (Word
docx), dokuwiki (DokuWiki markup), epub or epub3 (EPUB v3 book), epub2 (EPUB v2), fb2
(FictionBook2 e-book), gfm (GitHub-Flavored Markdown), haddock (Haddock markup), html or
html5 (HTML, i.e. HTML5/XHTML polyglot markup), html4 (XHTML 1.0 Transitional), icml
(InDesign ICML), jats (JATS XML), json (JSON version of native AST), latex (\latex), man
(groff man), markdown (Pandoc's Markdown), markdown\_mmd (MultiMarkdown),
markdown\_phpextra (PHP Markdown Extra), markdown\_strict (original unextended Markdown),
mediawiki (MediaWiki markup), ms (groff ms), muse (Muse), native (native Haskell), odt
(OpenOffice text document), opml (OPML), opendocument (OpenDocument), org (Emacs Org
mode), plain (plain text), pptx (PowerPoint slide show), rst (reStructuredText), rtf (Rich
Text Format), texinfo (GNU Texinfo), textile (Textile), slideous (Slideous HTML and
JavaScript slide show), slidy (Slidy HTML and JavaScript slide show), dzslides (DZSlides
HTML5 + JavaScript slide show), revealjs (reveal.js HTML5 + JavaScript slide show), s5 (S5
HTML and JavaScript slide show), tei (TEI Simple), zimwiki (ZimWiki markup)

\normalsize

How Pandoc works
----------------

`\only<1>{\begin{center}`{=latex}

``` {.graphviz width="90%" #workflow}
digraph workflow {

    graph [dpi = 250, bgcolor = "#FAFAFA"];

    rankdir = LR;

    pandoc [shape=box];
    filters [shape=box];
    {rank = same; filters pandoc}

    externals
    [
        margin=0,
        shape = none,
        label = <<table border="0" cellspacing="0">
                    <tr><td port="port0" colspan="2" border="1">external files</td></tr>
                    <tr>
                        <td port="port1" border="1" >png</td>
                        <td port="port2" border="1" >bib</td>
                    </tr>
                </table>>
    ]

    styles
    [
        margin=0,
        shape = none,
        label = <<table border="0" cellspacing="0">
                    <tr><td port="port0" colspan="3" border="1">styles and templates</td></tr>
                    <tr>
                        <td port="port1" border="1" >CSL</td>
                        <td port="port2" border="1" >CSS</td>
                        <td port="port3" border="1" >tex-template</td>
                    </tr>
                </table>>
    ]

    {rank = same; externals styles}

    Markdown -> pandoc;
    externals -> pandoc;
    styles -> pandoc;

    pandoc -> filters -> pandoc [dir=back, minlen=2.0];

    pandoc -> DOCX;
    LaTeX;
    pandoc -> LaTeX;
    PDF;
    pandoc -> PDF;
    pandoc -> HTML;
}
```

`\end{center}}`{=latex}
`\only<2|handout:0>{\begin{center}`{=latex}

``` {.graphviz width="90%"}
digraph workflow {

    graph [dpi = 250, bgcolor = "#FAFAFA"];

    rankdir = LR;

    pandoc [shape=box, color=red];
    filters [shape=box, color=red];
    {rank = same; filters pandoc}

    externals
    [
        shape = none,
        margin=0,
        label = <<table border="0" cellspacing="0">
                    <tr><td port="port0" colspan="2" border="1">external files</td></tr>
                    <tr>
                        <td port="port1" border="1" >png</td>
                        <td port="port2" border="1" ><font color="red">bib</font></td>
                    </tr>
                </table>>
    ]

    styles
    [
        shape = none,
        margin=0,
        label = <<table border="0" cellspacing="0">
                    <tr><td port="port0" colspan="3" border="1">styles and templates</td></tr>
                    <tr>
                        <td port="port1" border="1" >CSL</td>
                        <td port="port2" border="1" >CSS</td>
                        <td port="port3" border="1" ><font color="red">tex-template</font></td>
                    </tr>
                </table>>
    ]

    {rank = same; externals styles}

    Markdown [color = red];
    Markdown -> pandoc;
    externals -> pandoc;
    styles -> pandoc;

    pandoc -> filters -> pandoc [dir=back, minlen=2.0];

    pandoc -> DOCX;
    LaTeX [color = red];
    pandoc -> LaTeX;
    PDF [color = red];
    pandoc -> PDF;
    pandoc -> HTML;
}
```

`\end{center}}`{=latex}

Requirements
------------

-   Text editor: Notepad++, Geany
-   Commandline Terminal
    -   Windows: Powershell
    -   MacOS: Terminal, iTerm
    -   Linux: Terminal(gnome-terminal), Konsole, xterm
-   Pandoc: <https://pandoc.org/installing.html>
-   \latex:
    -   Windows: MiKTeX (<http://miktex.org/>)
    -   MacOS: MacTeX (<http://www.tug.org/mactex/>)
    -   Linux: \tex Live (<http://www.tug.org/texlive>)

Command
-------

To generate PDF documents:

``` {.sh}
# for articles
pandoc input.md -o output.pdf
# for beamer presentations
pandoc -t beamer input.md -o output.pdf
```

. . .

Additional flags:

-   `-s`, `--standalone`
-   `--filters` \[FILE\]
-   `--highlight-style=`\[FILE\]
-   `--template=`\[FILE\]
-   `-t` \[TARGET FORMAT\]

For more: `man pandoc`

Pandoc: YAML-Header
-------------------

In Pandoc metadata for a document are written in YAML\
(usually at the top of Markdown documents):

``` {.yaml}

---
title: Title of your work
author: Name of Author
date: 11.11.2011
tags: [markdown, writing]
abstract: |
  Abstract text here.
---
```

Raw \tex (1)
------------

Inline \tex commands will be preserved\
and passed unchanged to the \latex writers:

``` {.md}
You can use \LaTeX\ to create 
\textbf{bold} or \textit{italic} text.
```

Renders:

You can use \LaTeX\ to create \textbf{bold} or \textit{italic} text.

Raw \tex (2)
------------

Detailed \tex Tables are easily added if necessary:

::: {.columns}
::: {.column width="55%"}

``` {.md}
\begin{tabular}{|r|l|}
  \hline
  7C0 & hexadecimal \\
  3700 & octal \\ \cline{2-2}
  11111000000 & binary \\
  \hline \hline
  1984 & decimal \\
  \hline
\end{tabular}
```

:::
::: {.column width="45%"}

\begin{tabular}{|r|l|}
  \hline
  7C0 & hexadecimal \\
  3700 & octal \\ \cline{2-2}
  11111000000 & binary \\
  \hline \hline
  1984 & decimal \\
  \hline
\end{tabular}

:::
:::

\tex Math
---------

TeX Math is written between two `$`-signs

``` {.md}
<!-- Inline math -->
Here we see some inline math: $a^2 + b^2 = c^2$
<!-- displayed equation -->
And some displayed equation:
$$ \sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$
```

both render:

Here we see some inline math: $a^2 + b^2 = c^2$

And some displayed equation:
$$ \sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$

Footnotes (1)
-------------

``` {.md}
The next sentence has a note.
To look up about footnotes:[^1]
Another sentence that has a long note.[^longnote]

[^1]: <https://pandoc.org/MANUAL.html#footnotes>

[^longnote]: 
    Note with multiple blocks.
    { some.code }
    The whole paragraph can be indented, 
    or just the first line. 
    In this way, multi-paragraph footnotes work like
    multi-paragraph list items.
```

Footnotes (2)
-------------

The next sentence has a note. To look up about footnotes:[^1] Another sentence that has a long note.[^2]

[^1]: <https://pandoc.org/MANUAL.html#footnotes>

[^2]: Note with multiple blocks. 
    { some.code } 
    The whole paragraph can be indented, or just the first line. In this way,
    multi-paragraph footnotes work like multi-paragraph list items.



Citations (1)
-------------

Bibliographies are managed with Bib-files.

``` {.bib}
# mybib.bib
@article{macfarlane2013pandoc,
    title={Pandoc: a universal document converter},
    author={MacFarlane, John},
    url={http://pandoc.org},
    year={2013}
}
```

To use it in your document:

``` {.md}
John MacFarlane's Pandoc [@macfarlane2013pandoc]
```

Citation (2)
------------

Citations are generated through an external filter: `pandoc-citeproc`

``` {.sh}
pandoc --filter pandoc-citeproc input.md -o output.pdf
```

Bibliographies are either added as metadata into YAML

``` {.yaml}

---
bibliography: mybib.bib
---
```

Or are added as argument:

``` {.sh}
pandoc --bibliography mybib.bib ...
```

Intermediate features
=====================

Templates
---------

Generate default templates for further customization:

``` {.bash}
pandoc -D [FORMAT] > [filename]
pandoc -D latex > template.tex
pandoc -D beamer > template.beamer
```

To use it: `--template my-template.tex`

### Reuse for multiple projects move to:

-   Unix, Linux, macOS: `~/.pandoc/templates/`
-   Windows XP:\
    `C:\Documents And Settings\USERNAME\Application Data\pandoc`
-   Windows Vista or later:\
    `C:\Users\USERNAME\AppData\Roaming\pandoc`

Filters
-------

Filters:
:   Programs for manipulating Pandoc's representation of the document:
    AST -- the "Abstract syntax tree". Users can create their own for
    their specific needs.

`\begin{center}`{=latex}

``` {.graphviz width=100%}
digraph filter {

    graph [dpi = 250, bgcolor = "#FAFAFA"];
    rankdir=LR

    input [label=INPUT]
    ast [shape=box, label=AST]
    ast_filtered [shape=box, label=AST]
    output [label=OUTPUT]

    input -> ast [label="reader"]
    ast -> ast_filtered [label="filter"]
    ast_filtered -> output [label="writer"]
}
```

`\end{center}`{=latex}

Use them with `--filter`:

```{.sh}
pandoc --filter filter.py input.md -o output.pdf
```

Limitations of Markdown
-----------------------

-   No further customization of Tables
    -   cannot add lines between rows and columns
    -   cannot span over rows and columns
-   Free nesting of \latex and Markdown not possible
-   Pandoc generates cross references with hyperlinks instead of `\label` and `\ref`
-   Math is only inline or display expressions (latter as `\displaymath`)
    -   not possible to specify other environments: `equation`, `gather` etc.


