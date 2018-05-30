mkdir output
pandoc main.md -o output/main.pdf # create latex article
pandoc main.md -o output/main-beamer-presentation.pdf -t beamer # create latex beamer presentation
#pandoc main.md -o main.docx # for ms word users
#pandoc main.md -o main.odt # for libreoffice writer users
