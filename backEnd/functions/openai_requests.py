import openai;
from decouple import config;

#Retrieve environment variables
openai.organization = config("OPENAI_ORG")
openai.api_key = config("OPENAI_APIKEY")


#openai whisper
#convert audion to text
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1",audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return
    

