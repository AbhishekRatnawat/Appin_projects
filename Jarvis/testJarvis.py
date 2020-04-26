import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule
from gtts import gTTS
i=0
n=0
doss = os.getcwd()

while (i<1):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.adjust_for_ambient_noise(source)
		n=(n+1)     
		print("Say something!")
		audio = r.listen(source)
	
	try:
		s = (r.recognize_google(audio))
		message = (s.lower())
		print (message)
		x=[message]
		    
		if ('goodbye') in message:                          
			
			break
		if ('hello') in message or ('hi') in message:
			rand = ['Wellcome to Jarvis.']
			speekmodule.speek(rand,n,mixer)
		
		if ('music') in message:
			mus = random.choice(glob.glob
			(doss + "\\music" + "\\*.mp3"))
			os.system('chown -R user-id:group-id mus')
			os.system('start ' + mus)
			rand = ['start playing']
			speekmodule.speek(rand,n,mixer)
			
		if ('install') in message:
			query = message
			stopwords = ['install']
			querywords = query.split()
			resultwords  = [word for word in querywords if word.lower() not in stopwords]
			result = ' '.join(resultwords)
			rand = [('installing '+result)]
			speekmodule.speek(rand,n,mixer)
			os.system('python -m pip install ' + result)
		if ('what time') in message:
			tim = strftime("%X", localtime())
			rand = [tim]
			speekmodule.speek(rand,n,mixer)
		if ('.com') in message :
			rand = ['Opening' + message]         
			Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s") # webbrowser.get('/usr/bin/google-chrome %s').open('http://google.com')
			speekmodule.speek(rand,n,mixer)
			webbrowser.get(Chrome).open('http://www.'+message)
			print ('')
       
	except sr.UnknownValueError:
		print("$could not understand audio")
	except sr.RequestError as e:
		print("Could not request results$; {0}".format(e))
