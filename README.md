# RASA employee-crud - About bot

Rasa employee- crud is based on an open source machine learning framework to automate text-and voice-based conversations. With Rasa, we have build contexual assistants that fetches, saves, update and delete information from employee database (basically a google sheet). It can be easily deployed on:
```
Facebook Messenger

Slack

Google Hangouts

Microsoft Bot Framework

Telegram

Twilio

Your own custom conversational channels

or voice assistants as:

Alexa Skills

Google Home Actions
```
# RASA employee-crud - instruction to follow

This bot contains some training data and the main files needed to build an assistant on your local machine. The employee-crud consists of the following files:
```
data/nlu.md contains training examples for the NLU model
```
```
data/stories.md contains training stories for the Core model
```
```
actions.py contains some custom actions
```
```
config.yml contains the model configuration
```
```
domain.yml contains the domain of the assistant
```
```
endpoints.yml contains the webhook configuration for the custom action
```
# How to use this locally?

First clone this repo by : 
```
git clone https://github.com/zyllu/employee-bot-crud.git
```
Enter the folder: 
```
cd employee-bot-crud
```
To train your employee-crud locally, execute
```
rasa train
```
This will store a zipped model file in models/.


There are two ways to chat with bot:

1)To chat with the bot on the command line, run
```
rasa shell
```
and parallely you have to start an action server plus a Rasa server by
```
rasa run actions
```

2)To run bot in visual integration Rasa-X, run following in commnad line:
```
rasa x
```
and parallely you have to start an action server plus a Rasa server by
```
rasa run actions
```

# Sharing with real tester
To share with real tester use [ngrok](https://ngrok.com). Download ngrok from this [link](https://ngrok.com/download)

step 1>
open two command prompts and cd into working directory using:
```
cd employee-bot-crud
```
step 2>
After this in one terminal run:
```
rasa x
```
using this command you will get a link like this:
```
http://localhost:5002/login?username=me&password=SXcli1c45YAg
```
remember this password(it will be different for you).

step 3>
Then run following in the other terminal:
```
rasa run actions
```
step 4>
Lastly open up ngrok and run:
```
ngrok http 5002
```
remember this 5002 is the port used when we run the rasa x command above. If yours is different run ngrok http <your port address>

Now you will get two links like this: 

```
https://68434d17.ngrok.io
http://68434d17.ngrok.io
```
Copy any and open in a browser. Voila! the bot is ready to share.

Remember the password is the one we got in rasa x step.


Rasa Version trained on : 1.4.5

Rasa X version: 0.25.5

Operating System : Windows
