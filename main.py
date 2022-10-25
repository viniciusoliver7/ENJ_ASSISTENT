from ListenAndSpeak import listen
from ListenAndSpeak import speak

#vamos dev
while True:
    listen.listenActive()
    speak(listen.transcribe())
