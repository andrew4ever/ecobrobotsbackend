import os

from crontab import CronTab

from app import create_app


cron = CronTab(user=True)

job = cron.new(
    command='{}/venv/bin/python common/run_calculator.py'
    .format(os.getcwd())
)

job.minute.every(15)
cron.write()
x = job.run()
print(x)

app = create_app()
app.run(host='0.0.0.0', port=8080)
