from ListenAndSpeak import listen
from ListenAndSpeak import speak


while True:
    listen.listenActive()
    speak(listen.transcribe())
