import json;
import random;

#get recent messages
def get_recent_messages():

    #Define the filename and learn instructions
    file_name = "stored_data.json"
    learn_instructions = {
        "role" : "system",
        "content" : "You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior position. Your name is Jerry. The user is called Mahi. Keep your answers to under 30 words"
    }


#initialise messages
