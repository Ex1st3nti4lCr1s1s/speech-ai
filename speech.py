import speech_recognition as sr 
from tqdm import tqdm
import time,os
#import pyttsx3
from gtts import gTTS 
from playsound import playsound

# initialising
r = sr.Recognizer()

# importing audio file
'''
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
	audio = r.record(source)

# List Of Api's
recognize_bing(): Microsoft Bing Speech
recognize_google(): Google Web Speech API
recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
recognize_houndify(): Houndify by SoundHound
recognize_ibm(): IBM Speech to Text
recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
recognize_wit(): Wit.ai

# processing audio file
spt = r.recognize_sphinx(audio)
print(spt)
'''

#using mic
mic = sr.Microphone()

# list all devices
#print(sr.Microphone.list_microphone_names())

#using by index
#mic = sr.Microphone(device_index=1)

#recording audio

with mic as source:
	r.adjust_for_ambient_noise(source)
	print("Speak.....\n")
	audio = r.listen(source)

print("Processing......\n")
spt = r.recognize_google(audio)

print("Finished!\n")
print("was it:",spt)

'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
                       
engine.setProperty('rate', 100)     # setting up new voice rate


engine.say(spt)
engine.runAndWait()
'''

f = open("voices.txt", "r")
for x in f.readlines():
	try:
		y = x.strip()
		print(y)
		'''
		language = '{}'.format(y)
		print(language)
		myobj = gTTS(text=spt, lang='%s' %y, slow=False)
		print(spt)

		
		  
		#Playing the converted file
		playsound("welcome.mp3")
		time.sleep(1)

	except ValueError:
		pass
		
	
