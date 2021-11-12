# Otrium Sales price predictor

## Setting up your development environment

Set-up virtual environment:

```sh
python -m venv .venv
```


Install all (development) dependencies:

```sh
pip install -r requirements.txt
```

Install package 

```sh
pip install .
```

... and you should be all set up!

## Run assessment jupyter notebook

Jupyter notebook can be found in folder ./assessment. The original dataset needs to be saved into the ./assessment/data folder after which the otrium_assessment.ipynb can be run.

## Running tests, flake8 and mypy

To run tests use following command

```sh
tox
```

## Running the API from Python

Run the API directly with:

```sh
python -m otrium_model.main serve
```

Visit http://127.0.0.1:8000/docs for FastAPI docs.

## Test 

## Running the API with Docker

Make sure your Docker daemon is running and build the image:

```sh
docker build --tag otrium_model .
```

Run the container:

```sh
docker run --rm -p 8000:8000 otrium_model
```

## Test API

Run python file that tests API:
```sh
python ./assessment/test_api.py
```
This returns model predictions for test dataset.
