# ServeMeBot

Chat Bot built using RASA NLU and RASA CORE, which the consumers can use on their phones to book a service appointment for their Appliances.
Rasa NLU version: 0.13.2
Rasa Core version: 0.11.3

![alt text](https://raw.githubusercontent.com/WonderboyWonderboyv/ServeMeBot/master/image.png)


Clone this repo to get started:

```
git clone https://github.com/WonderboyWonderboyv/ServeMeBot.git
```

After you clone the repository, a directory will be downloaded to your local machine. It contains all the files of this repo and you should refer to this directory as your 'project directory'.


## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt
```

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```


## What’s in the project directory?

It contains some training data and the main files which use as the basis of our custom assistant. It also has the usual file structure of the assistant built with Rasa Stack. This directory consists of the following files:

### Files for training the Rasa NLU model

- **data/nlu_data.json** file contains training examples of intents 
- **nlu_cofing.yml** file contains the configuration of the Rasa NLU pipeline:  

### Files for training the Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action.
- **endpoints.yml** file contains the webhook configuration for custom action.

## How to use this starter-pack?
1. You can train the Rasa NLU model by running:  
    ```sh
    $ python nlu_tf_model.py
    ```  
This will train the Rasa NLU model and store it inside the `/models/nlu_tf` folder of our project directory.

2. Train the Rasa Core model by running:  
    ```sh
    $ python train_bot_online.py
    ```   
This will train the Rasa Core model and store it inside the `/models/dialogue` folder of our project directory.

3. Start the server for the custom action by running:  
    ```sh
    $ python -m rasa_core_sdk.endpoint --actions actions
    ```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
    ```sh
    $ python dialogue_management_model.py
    ```  
This will load the assistant in your terminal for you to chat.

## What's next?
### Connecting a chatbot to Slack:
1. Configure the slack app. 
2. Make sure custom actions server is running  
3. Start the agent by running run_app.py file  
4. Start the ngrok on the port 5004  
5. Provide the url: https://your_ngrok_url/webhooks/slack/webhook to 'Event Subscriptions' page of the slack configuration.  
6. Talk to you bot. 


