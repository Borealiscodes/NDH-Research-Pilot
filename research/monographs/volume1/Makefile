all: volume1.pdf

volume1.pdf: volume1.tex references.bib appendices/*.tex
	pdflatex -interaction=nonstopmode -halt-on-error volume1.tex
	bibtex volume1
	pdflatex -interaction=nonstopmode -halt-on-error volume1.tex
	pdflatex -interaction=nonstopmode -halt-on-error volume1.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.toc *.out *.pdf
