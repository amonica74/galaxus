# galaxus

To setup a job in cron, run:

crontab -e

vi opens with a list of your scheduled jobs.

Enter this line:

`* * * * * /Users/vcz/galaxus/get.sh`

then save. Your job is now scheduled to run once per minute.
