# BRICKSLMSAI
In this we will be creating a feature in which the students can talk to AI voice bots in their teacher's voice like a call..

The PipeLine for data flow will be like this:
 
 - Speech to Text:
     - We will be creating a websocket connection for the realtime transcription of student's voice using OpenAI whisper model
 - Text to Text:
     - The transcribed data will be send to Google gemini with the context to get ai response
 - Text to Speech:
     - The ai response will be then passed to ElevenLabs in which, we have already created our voice clone model and it will give us response



Mainly we are using API's for our current project but later on we will try to create our own.
