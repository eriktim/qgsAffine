VERSION := $(shell cat qgsAffine/metadata.txt | sed -n 's/version=\(.*\)/\1/p')
PY_VERSION := $(shell cat qgsAffine/__init__.py | sed -n 's/.*"Version \(.*\)"/\1/p')



default: zip

build: build_res build_ui
	@:

build_res:
	pyrcc4 -o qgsAffine/resources.py qgsAffine/resources.qrc

build_ui:
	pyuic4 -o qgsAffine/ui.py qgsAffine/ui.ui

zip: build
	zip -qr qgsAffine-$(VERSION).zip qgsAffine

lint: build
	pylint --ignore=resources.py,ui.py --rcfile=.pylintrc qgsAffine/

test:
	@:

ci: lint test
	@:

clean:
	rm -f *.zip
	rm -f qgsAffine/resources.py
	rm -f qgsAffine/ui.py
