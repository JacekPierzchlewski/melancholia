# Makefile for melancholia, v1.0 (13 Feb 2015)
pep8:
	pep8 --ignore=E501 *.py

clean:
	rm -f *.pyc
