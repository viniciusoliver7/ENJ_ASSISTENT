import pyttsx3


class listen():
    import speech_recognition as sr #biblioteca base para captura de audio

    __inicilize = False #saber se foi iniado o microfone
    __microphone= False #obj microfone
    __audio= False #espaço resevado para o audio, já quardado


    def __init__(self):
        ...



    @classmethod
    def listenActive(cls):



        cls.inicilize=True
        sr=cls.sr
        microfone=sr.Recognizer()
        with sr.Microphone() as mic:
            microfone.adjust_for_ambient_noise(mic)
            audio = microfone.listen(mic)
            cls.microphone=microfone
            cls.audio=audio


    @classmethod
    def transcribe(cls):
        if  cls.inicilize == False:
            print("tente inicializar o microfone primeiro, com a função 'listenActive()'")
        else:
            fala=cls.microphone.recognize_google(cls.audio,language="pt-BR")
            return fala

class speak():
    def __init__(self,fala):
        import gtts
        from playsound import playsound
        frase = gtts.gTTS(fala, lang="pt-br")
        frase.save("frase.mp3")
        playsound("frase.mp3")