Hello Everyone,

This file conatains the basic steps of how to deploy your chatbot with required dependencies on GCP. Similarly can be done to other AWS as well.

# Step1 
Create a Virtual instance with following process:
```
Log in to your GCP Console and navigate to Compute Engine>VM instances. Click Create.
```
```
On the configuration page, specify a name for the instance. We’ll call ours rasax-server. Then, choose a region near where you are located.
```
```
Under Machine configuration>Machine type, choose the standard option with 2 CPUs:
n1-standard-2 (2 vCPU, 7.5 GB memory)
```
```
Next, specify the boot disk. You’ll need to be running a modern Linux distribution that can run Docker, like Debian 9 or Ubuntu 16.04 / 18.04. We’ll go with Ubuntu 16.04 LTS. Increase the disc size to 100 GB.
```
```
Finally, under the Firewall settings, check the boxes to allow both HTTP and HTTPS traffic, and click Create.
```
# Step 2

# Installation of Rasa X

We’ve created our VM, but right now, it’s empty. Let’s connect to the new instance using SSH, so we can download and install Rasa.

Click the SSH button next to your newly created instance to start a new shell session and connect.
In your terminal, run the install script using the following commands. First, run:
```
curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.23.3/install.sh
```
Note that i have specified version 0.23.3.You can choose any other latest version as well. Rasa latest versions are not always stable so i prefer to choose some earlier version

Then, run:
```
sudo bash ./install.sh
```
The installation will take a few minutes to complete. Agree to the terms and conditions when prompted in the terminal.

By default, the installation folder for Rasa X is the /etc/rasa directory. Navigate into this directory using the following command:
```
cd /etc/rasa
```
run the ls command to take a look at the files contained in this directory.
It contains all the neccessary files.

Let’s start Rasa X with the following command:
```
sudo docker-compose up -d
```
The above command will pull everything from rasa containers and Once the container is up and running, set the password for the admin user with the following command. In this example, we’re setting the password to 12345, choose your as you want.
```
sudo python rasa_x_commands.py create --update admin me 12345
```

# Launch Rasa X

Now that you have everything up you can see your Rasa x instance in browser by going to 
```
http://<your host external ip>
```
Remember do not use https here as we have not connected it to a secured url.

As we open up the Rasa X instance we can see that it is empty. There are two methods to add NLU.md, Stories.md, domain.md etc by uploading them manually.

Or

We can use Integrated Version Control of rasa.

# Integrated Version Control

upload all your codes except any secreat keys to your public github repository.
Structure should Looks like this

# Activate Integrated Version Control
At the time this video was released, Integrated Version Control is an experimental feature that must be manually toggled on. Let’s go ahead and activate it.

In the Rasa X dashboard, click on the user icon in the lower left hand corner and select Experimental. Check the box next to Integrated Version Control.

Next, we’ll authenticate our server with GitHub to establish the connection, by generating an SSH key on the server, saving the public key in our GitHub repository settings, and sending the private key to Rasa X via an API call.

# Generate SSH keys
Navigate back to your SSH terminal. 
If you’ve closed the connection to your VM instance, log back in.

Make sure you’re in the /etc/rasa directory, where Rasa X is installed on your server. Then, run the following command to generate a public and private SSH key.
```
ssh-keygen -t rsa -b 4096 -f git-deploy-key
```

When prompted, do not set a passphrase. 
After the key has finished generating, you can run the 
```ls``` 
command in the ```/rasa/etc``` directory to see the newly created keys: ```git-deploy-key``` (the private key) and ```git-deploy-key.pub``` (the public key).

# Save the public key in GitHub

We’ll print the public key to the terminal so we can copy and save it in our GitHub settings.

Run the following command to view the public key:
```
cat git-deploy-key.pub
```
Copy the entire contents.
In your GitHub repository, navigate to Settings>Deploy keys. Click the Add deploy key button and paste your public key into the Key box. Give the key a title to identify it, like medicare-rasax, and be sure to check the box to Allow write access. Click Add key.

# Connect the repository to Rasa X

create a repository.json file in /etc/rasa folder in your SSH terminal:
```
touch repository.json
```
then nano into it:
```
nano repository.json
```

and the following content.
```
{
    "repository_url": "<your repository's SSH clone url>",
    "target_branch": "<the default branch Rasa X will use>",
    "ssh_key": "<your generated private SSH key>",
}
```
repository_url - The SSH URL for your GitHub repository, e.g. git@github.com:RasaHQ/rasa-demo.git

To get the URL for your repo, click the Clone or download button on your GitHub repository and select the Use SSH link.

target_branch - The GitHub repository branch where Rasa X should push and pull changes, e.g. master
ssh_key - The private SSH key generated on your server. use cat git-deploy-key & copy the full key including "BEGIN PRIVATE KEY" and "END PRIVATE KEY" and paste in ssh_key in repository. json file.

We’ll establish the connection between the Rasa X instance and GitHub repository by making a POST request to this Rasa X API endpoint:
```
https://<your server host>/api/projects/default/git_repositories?api_token=<your api token>
```
The JSON request body contains three pieces of information are as mentioned above in repository.json.

We need one more thing before we can send the cURL request: the Rasa X API token. The easiest way to get the token is to launch Rasa X in the browser and navigate to the Models screen. Click the Upload model button and copy the api_token from the URL.

ead back to the terminal. Still in the /etc/rasa directory, run the following cURL command, replacing the Rasa X server URL and API key values with your own:
```
curl --request POST \
--url http://<Rasa X server host>/api/projects/default/git_repositories?api_token=<your api token> \
--header 'content-type: application/json' \
--data-binary @repository.json
```

Finally, Check the connection by navigating back to the Rasa X dashboard in your browser and checking the Integrated Version Control icon in the bottom left corner. If the connection was successful, you’ll see either a green indicator, meaning Rasa X is up to date with the GitHub repository, or a yellow indicator, meaning Rasa X has changes that need to be pushed to GitHub.

Important: Read the [Readme_action_server.md](https://github.com/zyllu/employee-bot-crud/blob/master/Readme_action_server.md) for more details about how to create your action server for custom dependencies.
Like in our case pandas, gspread etc are need to be on a seprate custom server image.


