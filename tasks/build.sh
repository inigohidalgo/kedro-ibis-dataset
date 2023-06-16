rm -rf dist/
pdm build
twine upload dist/*