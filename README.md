# email_tracker.py

This updates a beeminder goal with the number of emails you have in your inbox. I'm running this on a linux server with a cronjob that runs every hour. You can configure the included crontab file to automatically update your beeminder goal at any interval you choose.

This is an alternative to the gmailzero project on beeminder:
https://www.beeminder.com/gmailzero

_What's the difference, you ask?_

gmailzero updates your beeminder with the number of _read_ messages in your inbox. I don't know about you, but I need to process all of those unloved, unread emails rotting away in my inbox as well. So email_tracker keeps you accountable for **all** your messages in your inbox.

_Where's this headed?_

I'll expand this to start tracking the lifetime of each email in my inbox as well. I want to kill my emails more efficiently. Suggestions, feedback and collaboration are all encouraged!


## Beeminder Setup

1. You will need to make a beeminder account:
https://www.beeminder.com/

2. Create a goal and choose goal type **"inbox fewer"**. Name your goal something like _"emailzero"_

3. While logged into beeminder, visit https://www.beeminder.com/api/v1/auth_token.json to get your personal auth token

You will need your **username**, **goal_name**, and **personal authorization token** so keep those handy for deploying.

## Deploying

### Environment Setup

Files included:
- [ ] requests folder (_a dependency: http://bit.ly/requests_py_)
- [ ] email_tracker.py
- [*] email_tracker_config.json
- [/] crontab.txt

[*] must edit, [/] optional to edit

1. Put those files into the same directory.

2. Update email_tracker_config.json file with your credentials.

    You will need to supply your:
    - email address
    - email password
    - beeminder username
    - the name of your beeminder goal
    - beeminder authorization token

3. _Optional:_ If you want to customize when/how frequently your cronjob runs, read steps 1-5 to change your crontab.txt file: http://bit.ly/cron_config

### How to deploy

Upload your directory folder to a linux web server. Then, invoke crontab to start running your cronjob on email_tracker.py. 

You can follow the directions here, starting from step 6 for how to run this on a remote server:
http://bit.ly/cron_invoke

##Contribute
Use GitHub issues and Pull Requests.
