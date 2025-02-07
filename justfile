# Default Python version to use
python_version := "3.12"

# List available commands
default:
    @just --list

# Create a new virtual environment
create-venv:
    uv venv create .venv --python={{python_version}}

# Install package in development mode with test dependencies
install:
    uv pip install -e ".[test]"

# Install development tools
install-dev:
    uv pip install build twine pytest

# Run tests
test:
    uv run pytest

# Clean build artifacts and cache
clean:
    rm -rf dist/
    rm -rf .pytest_cache/
    rm -rf **/__pycache__

# Build package
build: clean
    uv build

# Upload to PyPI
upload:
    uv run twine upload dist/*

# Tag a new release
tag-release:
    #!/usr/bin/env bash
    VERSION=$(grep -m1 'version = ' pyproject.toml | cut -d'"' -f2)
    git add pyproject.toml
    echo "Committing pyproject.toml with version \"$VERSION\""
    git commit -m "ver: $VERSION"
    COMMIT_ID=$(git rev-parse HEAD)
    echo "Tagging commit \"$COMMIT_ID\" as tag \"$VERSION\""
    git tag $VERSION
    echo "Pushing tag \"$VERSION\" to origin"
    git push origin $VERSION

# Build and tag a new release
release: build upload tag-release

# Setup a fresh development environment
setup: create-venv install install-dev 