.PHONY: pdf verify clean

pdf:
	latexmk papers/poisson-del-pezzo.tex

verify:
	python3 computations/verify_jacobi.py
	python3 computations/verify_families.py
	python3 computations/verify_cone.py
	python3 computations/verify_coarse.py

clean:
	latexmk -C papers/poisson-del-pezzo.tex
