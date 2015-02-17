# Makefile for melancholia, v1.2 (17 Feb 2015)
htmldoc:
	make -C docs html

pep8:
	pep8 --ignore=E501 *.py

clean:
	rm -f *.pyc
