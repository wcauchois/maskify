
all: maskify.js.mustache maskify.xml.mustache
	mkdir -p build
	cat values.yml maskify.js.mustache | mustache >build/maskify.js
	cat values.yml maskify.xml.mustache | mustache >build/maskify.xml

publish: all
	aws put --public maskify walken_cutout.png
	cd build && aws put --public maskify maskify.js
	cd build && aws put --public maskify maskify.xml
