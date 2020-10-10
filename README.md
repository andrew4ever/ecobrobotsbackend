# #brobots eco-project backend

This is a new Python back-end for #brobots eco-project. Previous version was written in PHP and had major flaws.

**#brobots eco-project** is a net of sensors that collect data about air quality in Brovary.

## Note

Currently the project depends on older back-end as it's receiving data from sensors. In future new version will fully replace older back-end.

## What's used

Server is based on **Flask** and few extensions:

- Flask RESTful
- Flask SQLAlchemy

Database: **MySQL**

## Executing

First of all, activate virtual environment with:

`source venv/bin/activate`

To start the server run:

`python run.py`

To start tests run:

`python -m unittest discover`

## [eco-project frontend](https://github.com/andrew4ever/ecobrobotsfrontend)
