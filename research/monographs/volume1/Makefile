all: volume1.pdf

volume1.pdf: volume1.tex appendices/*.tex
	pdflatex -interaction=nonstopmode -halt-on-error volume1.tex
	pdflatex -interaction=nonstopmode -halt-on-error volume1.tex

clean:
	rm -f *.aux *.log *.toc *.out *.pdf
