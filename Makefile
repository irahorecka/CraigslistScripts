black:
	black -l 120 *.py ./craigsearch/*.py;
	rm -rf ./__pycache__/ ./craigsearch/__pycache__/

flake8:
	flake8 *.py ./craigsearch/*.py;