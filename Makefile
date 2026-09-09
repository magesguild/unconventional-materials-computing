all: pdf epub

pdf:
	mkdir -p build
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	bibtex build/main
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	cp build/main.pdf unconventional-material-substrates.pdf

epub:
	pandoc /home/magesguild/research/02-regulus-and-hardware/analysis/2026-09-09-unconventional-material-substrates-and-stratospheric-mesh.md \
		-o unconventional-material-substrates.epub \
		--metadata title="Computing Beyond the Circuit Board: Sub-Milliwatt Silicon, Unconventional Material Substrates, and Stratospheric Mesh Networks" \
		--metadata author="Magus Gaius Mycelius (David Hayden) & Gemini (The Point of Stillness)" \
		--metadata date="September 9, 2026" \
		--metadata publisher="Mage's Guild Research Laboratories & Basin Game Studios" \
		--toc

clean:
	rm -rf build *.pdf *.epub
