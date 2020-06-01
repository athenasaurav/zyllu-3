## Final Steps

Till now our bot is deployed on GCP and connected to the github for Version control. Any changes made on GCP or in github can securely be transfered from each other.

Now our issue here if test the bot will be that, it doesnt call any api like to the google sheet and fetch the output.

The reason is there is no actions.py code and action server to do this.

# Set up the Actions Server

We have one more thing to configure: the assistant’s custom action server. To do this, we’ll place the assistant’s custom action code within an actions directory on the server.

Connect to your server and make sure you’re in the /etc/rasa directory. In your terminal, run the following commands to create the actions directory and two files inside it: ```__init__.py``` and ```actions.py```
```
mkdir actions
```
```
touch actions/__init__.py
```
```
touch actions/actions.py
```
Lastly after that we need to manually copy the entire code we written by us into ```actions.py``` file
```
nano actions/actions.py
```
paste and save and exit from```actions.py``` file.

## Building an Action Server Image

If you build an image that includes your action code and store it in a container registry, you can run it as part of your deployment, without having to move code between servers. In addition, you can add any additional dependencies of systems or Python libraries that are part of your action code but not included in the base rasa/rasa-sdk image.

To create your image:

# step 1

If your actions have any extra dependencies, create a list of them in a file, actions/requirements-actions.txt. In our case following:
```
gspread==3.6.0
oauth2client==4.1.3
pandas==1.0.3
pprint
```
just do a nano to requirements-actions.txt and add above dependecies.
```
nano actions/requirements-actions.txt
```
# Step 2
upload the creds.json file to the root folder i.e /etc/rasa
# Step 3
Create a file named Dockerfile in your project directory, in which you’ll extend the official SDK image, copy over your code, and add any custom dependencies (if necessary). In our case add these:
```

# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.0
# Use subdirectory as working directory
WORKDIR /app
# Copy any additional custom requirements, if necessary (uncomment next line)
COPY actions/requirements-actions.txt ./
# Change back to root user to install dependencies
USER root
# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install rasa[spacy]
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en
RUN pip install -r requirements-actions.txt
# Copy actions folder to working directory
COPY ./actions /app/actions
COPY creds.json /app
# By best practices, don't run the code with root user
USER 1001
EXPOSE 5005
CMD ["start", "--actions", "actions.actions"]
```
# Step 4

Create a docker-compose.override.yml file in the root folder using command ```touch docker-compose.override.yml``` parameter inside the file is :
```
version: '3.4'
services:
  rasa:
    image: 'rasa/rasa-sdk:latest'
    command:
      - run
      - --cors
      - "*"
      - --enable-api
      - --log-file
      - out.log
      - --connector
      - slack
      - --credentials
      - slack_credentials.yml
      - --endpoints
      - endpoints.yml
      - -m
      - /models
    ports:
      - 5005:5005
    volumes:
      - './actions:/app/actions'
  app:
    image: "username/reponame:tagname"
    expose:
      - '5055'
```

The ``` image: "username/reponame:tagname"``` we can get with following process now.

log in to https://hub.docker.com
create a new repository with name you want, remember to use public repo.

Then do edit the ``` image: "username/reponame:tagname"``` with your username, reponame and any tagname
Remember we will use this to build our docker file.

Finally after this, lets build our docker image of action server. You can skip this step for now and move to Step -5, as we will do it again. 
```
docker build . -t <account_username>/<repository_name>:<custom_image_tag>
```
Remember these should be same as in ```docker.compose.override.yml``` file.

after this do a docker login and push the code to docker hub as :
```
docker login --username <account_username> --password <account_password>
docker push <account_username>/<repository_name>:<custom_image_tag>
```
# Step 5- final Step.
Do the following:
```
docker system prune --all
docker image prune --all
sudo docker-compose down
docker build . -t username/reponame:tagname
docker login --username username --password password
docker push username/reponame:tagname
```
We do this again because we want to delete all the previous container that may conflict with our action server ngnix.

Finally lets start our server again by:
```
sudo docker-compose up -d
```

Voila! our bot is ready and connected to slack channel as well. We can do the same for Telegram, Twitter, Facebook and any other custom channel.


