rm -rf dist/
echo "Building package"
pdm build

echo "Uploading package to index"
twine upload dist/*