Hello Everyone,

This file conatains the basic steps of how to connect your Cloud Deployed bot to slack

# Step 1

To create the app go to https://api.slack.com/apps and click on Create New App.

# Step 2

Go to OAuth & Permissions and add folowing to Bot Token Scopes
Scopes that govern what your app can access.
```
chat:write.public
chat:write
```

# Step 3

On the very same page, Install app to workspace button will give you, your Bot User OAuth Access Token.

Something like this :
```
xoxb-1123355240483-1133112129958-XXXXxxxxxxxxXXXXXXX
```
# Step 4

Copy this to your credentials.yml file on your cloud by following process:
```
cd /etc/rasa
```
```
nano credentials.yml
```
Now add these to credentials.yml file

```
slack:
  slack_token: "<your slack token found in last step>"
```
Save the file

# Step 5
 Goto Event subscription and enable events
 
# Step 6

Most important Step, as rasa is wrong about this in documents :

add this in Request URL:
```
http://<your host ip>/core/webhooks/slack/webhook
```
Please confirm that verified pops up automatically.
# Step 7

On the events subscription page, subscribe to following bot events:
```
message.channels
channels:history
groups:history
message.im
im:history
message.mpim
```
# Step 8 
Reinstall the app if needed. 

# Important things :
remember to add slack connector in docker-compose.override.yml file.

Please read [Readme_GCP_deployement.md](https://github.com/zyllu/employee-bot-crud/blob/master/Readme_GCP_deployment.md) for more details.

In case of any issue read the solutions on [rasa forums](https://forum.rasa.com/t/rasa-slack-bot-issue-again/28860/4) written by me:
