
template: maskify.js.mustache maskify.xml.mustache
	mkdir -p build
	cat values.yml maskify.js.mustache | mustache >build/maskify.js
	cat values.yml maskify.xml.mustache | mustache >build/maskify.xml

quick_publish: template
	cd build && aws put --public maskify maskify.js
	cd build && aws put --public maskify maskify.xml

publish: quick_publish
	./masks.py publish

