.PHONY: thumbs quick_publish template publish

default:
	exit 1

template: maskify.js.mustache maskify.xml.mustache
	mkdir -p build
	cat values.yml maskify.js.mustache | mustache >build/maskify.js
	cat values.yml maskify.xml.mustache | mustache >build/maskify.xml

quick_publish: template
	cd build && aws put --public maskify maskify.js
	cd build && aws put --public maskify maskify.xml

thumbs:
	./manage_masks.py thumbs

publish: thumbs quick_publish
	aws put --public maskify red_x.png
	./manage_masks.py publish

