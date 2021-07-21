# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:36:26 2020

@author: asus
"""
#%% 4

a = "1"
b = 2
print(int(a) + b)

#%% 5- 10

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


print(letters[1])
print(letters[3:6])
print(letters[:3])
print(letters[-2])
print(letters[-3:])
print(letters[::2])

#%% 11

l = range(1, 21)
print(list(l))

#%% 12

my_range = range(1, 21)

print([10*a for a in my_range])

# %% 13

my_range = range(1, 21)
print(list(map(str, my_range)))

# %% 14

name = "nurgul"
a = list(set(a for a in name))
print(a)

# %% 15 

# =============================================================================
# dict_a = {"a":1, "b":2}
# print(dict_a)
# =============================================================================

a = dict(a="nurgul", b=5)
print(a)


#%% 16

d = {"a": 1, "b": 2}
print(d["b"])

# %% 17

d = {"a": 1, "b": 2, "c": 3}

print(d["a"] + d["b"])

# %% 18 

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)


# %% 20 

d = {"a": 1, "b": 2, "c": 3}

a = sum(d.values())

print(a)

# %% 21

d = {"a": 1, "b": 2, "c": 3}

d = dict((key, value) for key, value in d.items() if value <= 1)

print(d)

# %% 22-23

from pprint import pprint
d = {"a": list(range(1, 11)), "b": list(range(11, 21)), "c": list(range(21, 31))}

pprint(d)

pprint(d["b"][2])

# %% 24

from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key, value in d.items():
    print("{} has value {}".format(key, value))

# %% 25 
    
    
import string
 
for letter in string.ascii_lowercase:
    print(letter)
 
# %% 26
    

for number in range(1, 11):
    print(number)
    

#%% 27 
    
def a(v1, v2, t1, t2):
    a = (v2 - v1)/(t2 - t1)
    print(a)
    
b = a(0, 10, 0, 20)    
       
# %% 28 

def foo(a, b):
    print(a + b)
    return a+b
 
x = foo(2, 3) * 10  
    
# %% 29 

from math import pi

def liquid_volume_in_sphere(h, r =10):
    liquid_volume = (4*pi*(r**3)/3) - (pi*(h**2)*((3*r)-h)/3)
    return liquid_volume
    
print(liquid_volume_in_sphere(2))  
    
    
# %% 34 

def foo(): 
    global c
    c = 1 
    return c 
foo() 
print(c)    
    
# %% 35 

def count_words(strng): 
    strng_list = strng.split() 
    return len(strng_list) 
 
print(count_words("Hey there it's me!"))
    

# %% 36   

mypath = "C:\\Users\\asus\\Desktop\\Python_nurgul"
myfilepath =  mypath + "/" + "words1.txt"

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print(count_words(myfilepath))


# %% aslında 36 ile aynı 

# file okuturken ismini yazarken sonuna slash ters olacak dikkat et

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print(count_words("C:\\Users\\asus\\Desktop\\Python_nurgul/words1.txt"))


# %% 38

mypath = 'C:\\Users\\asus\\Desktop\\Python_nurgul'
my_filepath = mypath + '/' + 'words2.txt'

def count_file(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        change = strng.replace(',', ' ')
        strng_list = change.split(" ") 
        return len(strng_list)
print(count_file(my_filepath))        
                 
# %% 38

import math

print(math.sqrt(9))
      
# %% 39

import math
print(math.cos(1))

# %% 40

import math
print(math.pow(2, 3))

# %% 41

import string
mypath = 'C:\\Users\\asus\\Desktop\\Python_nurgul'
my_file_path = mypath + '/' + 'words2.txt'

def write_alphabet(filepath):
    with open(filepath, 'w') as file:
        for letter in string.ascii_lowercase:
            file.write(letter + '\n')
        
write_alphabet(my_file_path)

# %% 42

a = [1, 2, 3]
b = (4, 5, 6)

for x, y in zip(a,b):
    print(x + y)

# %% 43 

import string
    
mypath = 'C:\\Users\\asus\\Desktop\\Python_nurgul'
my_file_path = mypath + '/' + 'words2.txt'

def write_alphabet_in_two(filepath):
    with open(filepath, 'w') as file:
        for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]): 
            file.write(letter1 + letter2 + '\n')
           
write_alphabet_in_two(my_file_path)
            
# %% 44

import string

myfilepath = 'C:\\Users\\asus\\Desktop\\Python_nurgul/words2.txt'
    

def write_alphabet_in3(filepath):
    with open(filepath, 'w') as file:
        for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase [1::3], string.ascii_lowercase[3::3]):
            file.write(letter1 + letter2 + letter3 + '\n')
     
write_alphabet_in3(myfilepath)


# %% 45

import string, os

if not os.path.exists('letters'):
    os.makedirs('letters')
for letter in string.ascii_lowercase:
    with open('letters/' + letter + '.txt', "w") as file:
        file.write(letter + "\n")
        
# %% 46

import glob

letters = []

file_list = glob.glob("letters/*.txt")  

for filename in file_list:
    with open(filename, "r") as file: 
        letters.append(file.read().strip("\n"))
        
print(letters)
     
# %% 47
        
import glob, string

letters = []

file_list = glob.glob("letters/*.txt") 

for filename in file_list:
    with open(filename, "r") as file:
        for i in file.read():
            if i in "python":
                letters.append(i)
        
print(letters)        
    

#%% 48

for letter in "Hello":
    if letter == "e":
        print(letter)

#%% 49
        
x = input("Please enter your password: ")

#%% 50

age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)

# %% 51

print(type("Hey".replace("ey","i")[-1]))


# %% 52

name = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % (name, secondname))

# %% 53

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

print(d['employees'][1]['lastName'])


# %% 54

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))

print(d)

#%% 55

import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company1.json", 'w') as file:
    json.dump(d, file, indent=2)
    

# %% 57
    
import json
from pprint import pprint     


with open("company1.json", "r") as file:
    pprint(json.loads(file.read()))

# %% 58 
    
import json

with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
    file.seek(0)
    json.dump(d, file, indent = 2, sort_keys= True)
    file.truncate()
    
    
# %% 59
    
a = [1, 2, 3]
   

for index, item in enumerate(a):
    print("item %s has index %s" % (index, item))
    
# %% 60
    
while True:
    print("Hello!")
    
# %% 61

import time
    
while True:
    print("Hello!")
    time.sleep(2)

# %% 62

import time

i = 0

while True:
    i = i + 1
    print("Hello!")
    time.sleep(i)

# %% 63
    
import time
    
i = 0

while True:
    i = i+1
    print("Hello!") 
    if i > 3 :
        print("End of the loop!")
        break
    time.sleep(i)

# %% 64

while True:
    print("Hello!")
    
    if 2>1: 
        pass
        print("Hi!")
    
# %%  65    
 
while True:
    print("Hello!")
    
    if 2>1: 
        continue
    
    print("Hi!")
    
# %% 66 
 
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def dictionary(word):
    return d[word]

word = input("Enter word: ")

print(dictionary(word))

# %% 67 
    
d = dict(weather = "clima", earth = "terra", rain = "chuva")
    
def vocabulay(word):
    if word in d:
        print(d[word])
    else:
        print("Sorry, this word cannot be found.")

word = input("Enter word: ")
    
vocabulay(word)   

# %% 67

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabul(word):
    try:
        return d[word]
    except KeyError:
        return "Sorry this word cannot be found!"
        
word = input("Enter word: ").lower()

print(vocabul(word))

# %% 69

import os

if not os.path.exists('requests'):
    os.makedirs('requests')

def filecreate():
    with open('request/' + '.py', "w") as file:
        file.write()


import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])

# %% 70

import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)

# %% 71

import requests
 
response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text
count_a = text.count("a")
print(count_a)

print(text)


# %% 72

import webbrowser
 
query = input("Input your query: ")
webbrowser.open("https://google.com/search?q=%s" % query)


# %% 72 Deneme

import webbrowser

query = input("Please enter your query: ")
webbrowser.open("https://www.bing.com/search?q=%s"% query)

# %% 73

import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data*2
data_2.to_csv("sample2.txt", index = None)


# %% 74

import pandas

file1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
file2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
final = pandas.concat([file1, file2])
final.to_csv("twofiles.txt", index = None)


# %% 75





                  

                       
                       
                       
                       
                       
                       
                       
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
                       
                       
                       
                       
                       
