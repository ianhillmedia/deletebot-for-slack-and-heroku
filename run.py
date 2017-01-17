import os
import time
import json
import calendar
import requests
from slackclient import SlackClient
from datetime import datetime, timedelta

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
COMMAND_DELETE = "deletefiles"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

# tokens and domains
_token = "YOUR SLACK TOKEN FOR TESTING AND DEVELOPMENT"
_domain = "THE FIRST WORD IN YOUR SLACK SUBDOMAIN"

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
        
    if command.startswith(COMMAND_DELETE):
        response_three = "OK! This may take a few moments. I will tell you when I am done..."
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response_three, as_user=True)
        if __name__ == '__main__':
            while 1:
                files_list_url = 'https://slack.com/api/files.list'
                date = str(calendar.timegm((datetime.now() + timedelta(-1))
                    .utctimetuple()))
                data = {"token": _token, "ts_to": date}
                response = requests.post(files_list_url, data = data)
                if len(response.json()["files"]) == 0:
                    break
                for f in response.json()["files"]:
                    timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
                    delete_url = "https://" + _domain + ".slack.com/api/files.delete?t=" + timestamp
                    requests.post(delete_url, data = {
                        "token": _token, 
                        "file": f["id"], 
                        "set_active": "true", 
                        "_attempts": "1"})
            message = "Done!"
            slack_client.api_call("chat.postMessage", channel=channel,
                                  text=message, as_user=True)




def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None
s
if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
