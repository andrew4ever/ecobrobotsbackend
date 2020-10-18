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

Set the environment variables:
`export ENVIRONMENT={DEVELOPMENT or PRODUCTION}` and
`export PYTHONPATH=$(pwd)`

If `ENVIRONMENT` variable is set to `DEVELOPMENT` the `.env.dev` file will be used. Otherwise, the `.env` is used. `PYTHONPATH` is needed for `AQICalculator.py` to be executed on its own.

To start the server run:
`python run.py`

To start tests run:
`python -m unittest tests`

## For WSL users

I use WSL as my working system and I spent lots of time debugging this small thing: `cron` isn't started on WSL startup. You have to run `sudo service cron start` before working.

## [eco-project frontend](https://github.com/andrew4ever/ecobrobotsfrontend)
