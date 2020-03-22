'''
Name: Jontavius Caston
Date: 5/15/2019
Course: DSC510-T301 - Intro to Python Programming
Assignment: Assignment 10
Desc: This program's purpose is to create a get request to a site that retrieves Chuck Norris jokes. We will parse the the
      the returned data to get the value and display it to the user. We will wrap this in a loop to keep displaying a new
      joke until the user exits the program.
'''

import json
import requests
from pprint import pprint

print('\nWelcome to Chuck Norris jokes! Laugh or he will find you!\n')

choice = int(input('select 1 to see a joke or 2 to close the application\n'))        #The input that allows the loop to run and exit

while choice != 2:                                                                   #while loop that runs until the user selects 2

    if (choice == 1):
        r = requests.get('https://api.chucknorris.io/jokes/random')                  #statement that gets the url that holds the jokes
        jokes_json = r.json()                                                        #I assigned the JSON to an object so I can call it later
        jokes_str = json.dumps(jokes_json, indent=2)                                 #This is where I cleaned my JSON up to be able to view and easily see the varible portion
        jokes = jokes_json['value']                                                  #Here I assigned the variable so that I could print only it
        pprint(jokes)                                                                #This is the print that handles the variable and prints only it
        print('\n')
    elif (choice == 2):
        exit()
    else:
        print('Improper selection please select 1 to see a joke or 2 to exit! \n')

    choice = int(input('select 1 to see a joke or 2 to close the application\n'))
