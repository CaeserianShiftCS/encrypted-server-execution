#this file will be a self encrypting file, this will use a engine that decrypts encryted code on this file and executes it
#imports
import os, re, subprocess
from cryptography.fernet import Fernet
import numpy as np
#functions
def cleanhtml(raw_html):    #cleans up html from string
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

local_com = subprocess.check_output("curl http://127.0.0.1/file/more.html", shell=True)
key = b'jCIAMFGlu2hosFNLzq-S4cog0aVlhxO9kBMVUXYHsfI=' # have to write the right key for it to be decrypted then it can only execute with the engine under
f = Fernet(key)
for x in range(len(local_array)):
    ((f.decrypt((local_array[x]).encode("utf-8"))).decode("utf-8"))  # takes each element and decrypts them, this could be used to send encrypted python code and then be executed

# this is a test to run script from localhost server
clean_local_com = cleanhtml((local_com.decode("utf-8"))
local_array_com = np.array(clean_local_com.split("\n"))
local_array_com = np.delete(local_array_com, -1)         
for x in range(len(local_array_com)):
    print((f.decrypt((local_array_com[x]).encode("utf-8"))).decode("utf-8"))
    exec((f.decrypt((local_array_com[x]).encode("utf-8"))).decode("utf-8")) # executes the local_array_com decrypted

