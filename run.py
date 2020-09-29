import os

from crontab import CronTab

from app import create_app

cron = CronTab(user=True)

job = cron.new(
    command='{0}/venv/bin/python {0}/common/run_calculator.py'
    .format(os.getcwd())
)
job.minute.every(int(os.environ.get('DB_UPDATE_PERIOD_MINUTES')))
cron.write()

app = create_app()
app.run(host='0.0.0.0', port=8080)
