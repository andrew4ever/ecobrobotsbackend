# #brobots eco-project backend

This is a new Python back-end for #brobots eco-project. Previous version was written in PHP and had major flaws.

**#brobots eco-project** is a net of sensors that collect data about air quality in Brovary.

## What's used

Server is based on **Flask** and few extensions:

- Flask RESTful
- Flask SQLAlchemy

Database: **MySQL**

## Executing

First of all, create your virtual environment and activate it with:
`source venv/bin/activate`

    I highly recommend using `virtualenv`, not `python -m venv`, as it creates `activate_this.py` that is needed for CGI

Set the environment variables:
`export ENVIRONMENT={DEVELOPMENT or PRODUCTION}` and
`export PYTHONPATH=/path/to/project/root`

If `ENVIRONMENT` variable is set to `DEVELOPMENT` the `.env.dev` file will be used. Otherwise, the `.env` is used. `PYTHONPATH` is needed for loading config and `AQICalculator.py` to be executed on its own.

To start the server run:
`python run.py`

To start tests run:
`python -m unittest tests`

## When deploying as CGI

Make sure `app.cgi` has access permissons set to **750**.
Also in `app.cgi` change path to virtual environment.

Few helpful links:

- [Official Flask page](https://flask.palletsprojects.com/en/1.1.x/deploying/cgi/)
- [How to use with venv](https://homes.cs.washington.edu/~yjzhang/notes/python_web.html)

## For WSL users

I use WSL as my working system and I spent lots of time debugging this small thing: `cron` isn't started on WSL startup. You have to run `sudo service cron start` before working.

## For VS Code users

Don't use SSH connection feature in VS Code. It prevented my CGI app from working on server and made me spend hours of debugging.

## [eco-project frontend](https://github.com/andrew4ever/ecobrobotsfrontend)
