build: clean
	python setup.py sdist bdist_wheel
	make test

test:
	twine check dist/*

clean:
	-rmdir build /s/q
	-rmdir dist /s/q
	-rmdir COVID19_ES_Py.egg-info /s/q
	-rmdir htmlcov /s/q
	-rmdir .pytest_cache /s/q
	-rmdir __pycache__ /s/q

publish_test: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: clean build
	twine upload dist/*
