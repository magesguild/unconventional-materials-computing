all: pdf

pdf:
	mkdir -p build
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	bibtex build/main
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	cp build/main.pdf unconventional-material-substrates.pdf

clean:
	rm -rf build *.pdf
