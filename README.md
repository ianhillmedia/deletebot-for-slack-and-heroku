# deletebot-for-slack-and-heroku

Basic Slackbot: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

Added to Heroku: https://github.com/ianhillmedia/slackbot-for-heroku

Delete old files: https://gist.github.com/thesoftwarejedi/d78af9ee12b7f7a9d3e7

# HOW TO DEPLOY

Download and install the Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli

# Heroku: 

Create new app


# Slack:

Configure Apps > Build > Make a Custom Integration > Bots

Name it

Add bot integration

Copy API token



# Terminal:

cd to your bot folder

`virtualenv botname`

`source botname/bin/activate`

Result: (tegnasocialbot) ladmins-MacBook-Pro:TEGNASOCIAL ihill$ 

`pip install slackclient`

`export SLACK_BOT_TOKEN='your slack token pasted here’`

Create print_bot_id.py (https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

Change BOT_NAME to the name of your bot from Slack

`python print_bot_id.py`

Copy your BOT_ID from the response.

Close Terminal


# Heroku:

Settings > Reveal Config Vars

Add vars:

Key = BOT_ID

Value = Bot ID

Add



# Slack: 

Go to https://api.slack.com/docs/oauth-test-tokens

Create token

Copy token


# IDLE or your development environment:

Code: Open run.py

Set _token to your token for testing and development

Set _domain to the first work in your Slack domain tegnasocial



# Terminal: 

cd to your bot folder

`echo "API_TOKEN = Your bot API token” > .env`

Hit enter. Nothing should happen in your command line, and you probably won't see a new file in your Slackbot Directory. That's OK!


# Heroku:

Deploy tab

Follow instructions to deploy in terminal


# Terminal:

`heroku ps:scale worker=1`


# Update in Terminal:

`git init`

`heroku git:remote -a <APP NAME>`

`git add .`

`git commit -m “comment with updates”`

`git push heroku master`

`heroku ps:scale worker=1`
