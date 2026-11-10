all: volume1.pdf

volume1.pdf: volume1.md references.bib appendices/*.md
	pandoc volume1.md appendices/*.md \
		--citeproc \
		--bibliography=references.bib \
		--toc \
		--number-sections \
		-V geometry:margin=1in \
		-o volume1.pdf

clean:
	rm -f volume1.pdf
