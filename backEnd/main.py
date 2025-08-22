# uvicorn main:app  initialsising app which doesn't reload on every save event
# uvicorn main:app --reload - initialsising app which reload on every save event


# main imports
from fastapi import FastAPI, File, UploadFile, HTTPException;
from fastapi.responses import StreamingResponse;
from fastapi.middleware.cors import CORSMiddleware;
from decouple import config;


#Custom functions import
from functions.openai_requests import convert_audio_to_text


#Initialise app
app = FastAPI()


#CORS : Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174"
    "http://localhost:3000"
]

#CORS : middlewear
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


#Check health
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}


#get audio
@app.get("/post-audio-get")
async def get_audio():

    #get saved audio
    audio_input = open('voice.mp3','rb');

    #decode audion
    decoded_message = convert_audio_to_text(audio_input)
    
    print(decoded_message)

    return 'Done'

# #Post bot response
# #Note: not playing in browser when using post request
# @app.post("/post-audio")
# async def post_audio(file: UploadFile= File(...)):
#     print("Hello")