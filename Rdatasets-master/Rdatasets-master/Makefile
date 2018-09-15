gh:
	git rm -r csv
	git rm -r doc
	mkdir csv
	mkdir doc
	R CMD BATCH Rdatasets.R
	cd doc
	../rst.sh
	cd ..
	git add csv
	git add doc
	git add datasets.html
	git add datasets.csv
	git add Rdatasets.R
	vim datasets.csv
	vim README.rst
	git add README.rst

ghpages:
	git checkout master csv
	git checkout master doc
	git checkout master Rdatasets.R
	git checkout master README.rst
	git checkout master datasets.html
	git checkout master datasets.csv
	git checkout master Makefile
	sed -i '.bak' 's/https:\/\/raw.github.com\/vincentarelbundock\/Rdatasets\/master\///g' datasets.html 
	git add csv
	git add doc
	git add datasets.html
	git add datasets.csv
	git add Rdatasets.R
	git add Makefile
	vim README.rst
	vim index.html
	git add README.rst
	git add index.html

