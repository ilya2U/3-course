import time
import os
import base64
import random
from cryptography.fernet import Fernet
import time
import math



def generate_key():
    file = open('key.bin', 'wb')
    file.write(base64.urlsafe_b64encode(os.urandom(32)))
    
generate_key()    

def encrypt_message(message):
    file = open('key.bin', 'r')
    key = file.readline()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    file.close()
    return encrypted_message

# Зашифровать файл

def encrypt_file(file_name):
    with open(file_name, 'r') as file:
        phrases = file.readlines()
        encrypt_file = open('encrypt_phrases.bin', 'wb')

        for phase in phrases:
            encrypt_phrase = encrypt_message(phase)
            encrypt_file.write(encrypt_phrase + '\n'.encode('utf-8'))

        file.close

encrypt_file('phrases.txt')

#Decrypt function

def decrypt_message(message):
  file = open('key.bin', 'r')
  key = file.readline()
  f = Fernet(key)
  decrypt = f.decrypt(message)
  return decrypt.decode('utf-8')[:-1]

def read_file_encrypt(file_name):
  with open(file_name, 'rb') as file:
    phrases = file.readlines()
    return phrases 

def get_random_item(phrases):
  return random.choice(phrases)

def get_register_user_from_file(file_name):
  register_users = {}

  file = open(file_name, 'r')
  if not file:
    return register_users

  users = file.readlines()
  users = [user.split(' ') for user in users]

  for user in users:
    person = {'perfect': user[1], 'deviation': user[2], 'phrases_index': user[3]}
    register_users[user[0]] = person

  return register_users      


def register(user_name):
  global phrases
  global registered_users

  count = 0
  try_count = 0
  random_phrases = get_random_item(phrases)
  dectypt_random_phrases = decrypt_message(random_phrases)
  try_mass = []

  while not count == 4:
    print("Input phrases: " + dectypt_random_phrases)
    current_time = time.time()
    user_try = input("Input " + str(try_count) + ':\n')
    end_time = time.time()
    if user_try == dectypt_random_phrases:
      count += 1
      try_mass.append((end_time - current_time) / len(dectypt_random_phrases))
      try_count += 1
    else:
      try_count += 1
      print("Not valid input, try again")

  perfect = 0

  for i in try_mass:
    perfect += i
  perfect /= 4

  deviation = 0

  for i in try_mass:
    deviation += abs((i - perfect))
  deviation /= 4

  file = open('user.txt', 'a')
  file.write(user_name + " " + str(perfect) + " " + str(deviation) + " " + str(phrases.index(random_phrases)) + '\n')
  file.close()
  registered_users = get_register_user_from_file('user.txt')

def login(user_name):
  global logined_users
  global registered_users

  current_encrypt_phrases = phrases[int(registered_users[user_name]['phrases_index'])]
  current_decrypt_phrases = decrypt_message(current_encrypt_phrases)
  current_perfect = registered_users[user_name]['perfect']
  current_deviation = registered_users[user_name]['deviation']

  while True:
    print("Input phrases: " + current_decrypt_phrases)
    current_time = time.time()
    user_try = input("Try input: " + '\n')
    end_time = time.time()
    if user_try == current_decrypt_phrases:
      try_time = (end_time - current_time) / len(current_decrypt_phrases) 
      if float(current_perfect) - float(current_deviation) <= try_time and try_time <= float(current_perfect) + float(current_deviation):
        print('Login success')
        logined_users[user_name] = time.time()
        break
      else:
        print('Try again')     
    else:
      print('Not valid input, try again')

try:  
  file = open('user.txt', 'r')
  file.close()
except e:
  file = open('user.txt', 'w')
  file.close()

registered_users = get_register_user_from_file('user.txt')
phrases = read_file_encrypt('encrypt_phrases.bin')
logined_users = {}

while True:
  current_user = input('Input username ')
  if current_user in registered_users:
    if current_user in logined_users:
      if float(logined_users[current_user]) + 30 >= float(time.time()):
        logined_users[current_user] = time.time() 
        print("Already login")
      else:
        login(current_user)  
    else:
      login(current_user)
  else:
    register(current_user)  
