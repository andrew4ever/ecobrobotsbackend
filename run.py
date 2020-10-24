import os

from crontab import CronTab

from app import create_app

cron = CronTab(user=True)

job = cron.new(
    command='export ENVIRONMENT={1} && export PYTHONPATH={0} && cd {0} && {0}/venv/bin/python {0}/common/AQICalculator.py'.format(
        os.getcwd(), os.environ.get('ENVIRONMENT'))
)
job.minute.every(int(os.environ.get('DB_UPDATE_PERIOD_MINUTES')))
cron.write()

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080)
