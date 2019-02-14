from playsound import playsound
from gtts import gTTS
s = "escape with plane"
file = "file.mp3"
tts = gTTS(s, 'en')
tts.save(file)
playsound('file.mp3')
