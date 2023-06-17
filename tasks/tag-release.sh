package_version=$(pdm show --version)

git add pyproject.toml

echo "Committing pyproject.toml with version \"$package_version\""
git commit -m "ver: $package_version"

commit_id=$(git rev-parse HEAD)

echo "Tagging commit \"$commit_id\" as tag \"$package_version\""
git tag $package_version
echo "Pushing tag \"$package_version\" to origin"
git push origin $package_version