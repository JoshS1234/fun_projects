# # Chinese word of the day
# 
# - Import words from a HTML file online
# - Pick a random one
# - Ask the user for the translation
# - Give a nice friendly message 

import requests
import pandas as pd
import random

url = 'https://www.digmandarin.com/80-basic-chinese-words-and-phrases-to-help-you-survive.html'
html = requests.get(url).content

# Read in the html to dataframe
df_list = pd.read_html(html)

# Get the table - which is the last thing in the web page
df = df_list[-1]
length = df.shape[0]

print('Hello! Your Chinese phrase of the day is ...')

# Get random words until the user enters no
answer = "yes"
while answer == "yes":
	random_num = random.randint(0, length)
	# Get the random Chinese phrase
	chinese_word = df['Chinese'].iloc[random_num]
	english_word = df['English'].iloc[random_num]
	pinyin_word = df['Pinyin'].iloc[random_num]

	print ('\033[1m' + chinese_word + '\033[0m')
	print('What is the English Translation?')

	guess = input()
	if guess == english_word:
	    print('You da man')
	else:
	    print("You suck")
	    print("the correct translation was \"{}\"".format(english_word))
	
	print('What is the Pinyin version?')
	guess = input()
	if guess == pinyin_word:
	    print('You da man')
	else:
	    print("You suck")
	    print("the correct translation was \"{}\"".format(pinyin_word))
	    
	print('Do you want to try another word?')
	answer = input("please enter yes or no: ")

print('Good stuff, have a nice day')



