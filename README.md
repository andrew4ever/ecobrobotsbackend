# #brobots eco-project backend

This is a new Python back-end for #brobots eco-project. Previous version was written in PHP and had major flaws.

**#brobots eco-project** is a net of sensors that collect data about air quality in Brovary.

## What's used

Server is based on **Flask** and few extensions:

- Flask RESTful
- Flask SQLAlchemy

Database: **MySQL**

## Executing

First of all, activate virtual environment with:
`source venv/bin/activate`

Set the environment variable:
`export ENVIRONMENT={DEVELOPMENT or PRODUCTION}`

If `ENVIRONMENT` variable is set to `DEVELOPMENT` the `.env.dev` file will be used. Otherwise, the `.env` is used

To start the server run:
`python run.py`

To start tests run:
`python -m unittest tests`

## [eco-project frontend](https://github.com/andrew4ever/ecobrobotsfrontend)
