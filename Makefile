.PHONY: pdf verify clean

pdf:
	latexmk poisson-del-pezzo.tex

verify:
	python3 computations/verify_jacobi.py
	python3 computations/verify_families.py
	python3 computations/verify_cone.py

clean:
	latexmk -C poisson-del-pezzo.tex
