.PHONY: pdf verify clean

pdf:
	latexmk -lualatex -outdir=build papers/dp12_poisson.tex

verify:
	python3 computations/verify_jacobi.py

clean:
	latexmk -C -outdir=build papers/dp12_poisson.tex
