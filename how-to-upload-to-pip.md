Go through [this tutorial](https://packaging.python.org/tutorials/packaging-projects/)

Commands to run often:

* `python3 setup.py sdist bdist_wheel`: to build distribution
* `python3 -m twine upload --repository testpypi dist/*`: to upload to testpypi
* `python3 -m twine upload dist/*`: to upload to [pypi](https://pypi.org)

