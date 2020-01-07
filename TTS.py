import os
import sys
from gtts import gTTS

mytext = ""
language = 'en'

with open(sys.argv[1], 'r') as f:
   mytext = f.read()

myobj = gTTS(text=mytext, lang = language, slow=False)

myobj.save("test.mp3")








    