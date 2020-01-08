import os
import sys
from gtts import gTTS

mytext = ""
language = sys.argv[2]
fileName = sys.argv[3]

with open(sys.argv[1], 'r') as f:
   mytext = f.read()

myobj = gTTS(text=mytext, lang = language, slow=False)

myobj.save(fileName)









    