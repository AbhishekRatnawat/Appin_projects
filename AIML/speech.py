import aiml
import pyttsx3
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
        #load = kernel.respond(input("Enter your message >> ")) #version 3
		load = kernel.respond(raw_input("Enter your message >> "))#version 2
		print load
        engine = pyttsx3.init()
        engine.say(load) # Answer in voice
        engine.runAndWait()
     

