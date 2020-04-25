build: clean
	python setup.py sdist bdist_wheel
	make test

pytest:
	pytest --cov=./ --disable-pytest-warnings

update_docs:
	sphinx-apidoc -o . ..\COVID19_ES_Py --force

test:
	twine check dist/*

clean:
	rm -rf dist
	rm -rf build
	rm -rf dist
	rm -rf COVID19_ES_Py.egg-info
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm -rf __pycache__

publish_test: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: clean build
	twine upload dist/*
