#Importing the Tkinter and Random libraries
from tkinter import *
import tkinter as tk
import random

#Configuring the window for Tkinter
window = Tk()
window.geometry("390x450")
window.title('Password Generator')
window.configure(background='#DBE2EF')

#Creating lists with letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+']

#Declaring variables to randomly pick a letter, number, and symbol
randomLetters = random.choice(letters)
randomNumbers = random.choice(numbers)
randomSymbol = random.choice(symbols)

#Setting password to an empty string
passwordText = '' 

#Creating the function using length as a parameter to randomize the password using the user's entries
def passwordFunction(length):
    if wordEntry.get() != '' and nameEntry.get() != '':
        password = ''
        for num in range(length):
            randomLetters = random.choice(nameEntry.get())
            randomLetters2 = random.choice(wordEntry.get())
            randomNumbers = random.choice(numbers)
            randomNumbers2 = random.choice(numbers)
            randomSymbol = random.choice(symbols)
            randomSymbol2 = random.choice(symbols)
            randomSymbol3 = random.choice(symbols)
            password += randomLetters + nameEntry.get() + randomNumbers + randomSymbol + wordEntry.get() + randomNumbers2 + randomSymbol2 + randomLetters2 + randomSymbol3
        passwordText = password 
        passwordLabel.configure(text=passwordText)
    else:
        passwordText = 'Error, please try again'
        passwordLabel.configure(text=passwordText)

#Heading for the password generator
headLine = tk.Label(window, text='Password Generator', bg='#DBE2EF', fg='black', font='none 30 bold')
headLine.pack()

#Spacer for content
spacer = tk.Label(window, text=' ', bg='#DBE2EF')
spacer.pack()

#Label asking user to input their name
nameQuestion = tk.Label(window, text='What is your first name?', bg='#DBE2EF', fg='black', font='none 15')
nameQuestion.pack()

#Box for user to input their name
nameEntry = tk.Entry(window, text='enter a name', bg='white', fg='black', font='none 15')
nameEntry.pack()

#Label asking user to input a word
wordQuestion = tk.Label(window, text='Enter a word', bg='#DBE2EF', fg='black', font='none 15' )
wordQuestion.pack()

#Box for user to input a word
wordEntry = tk.Entry(window, text='enter a word', bg='white', fg='black', font='none 15')
wordEntry.pack()

#A submit button which runs passwordFunction when it is clicked and generates a randomized password
submitButton = tk.Button(window, text='Randomize', bg='#DBE2EF', command=lambda: passwordFunction(2))
submitButton.pack()

#Spacer for content
spacer2 = tk.Label(window, text=' ', bg='#DBE2EF')
spacer2.pack()

#Label with text before showing password
yourPassword = tk.Label(window, bg='#DBE2EF', fg='black', text='Your Randomly Generated Password is:', font='none 15 bold')
yourPassword.pack()

#Label to display the password
passwordLabel = tk.Label(window, text=passwordText, bg='#DBE2EF', fg='black')
passwordLabel.pack()

#Creating a button to exit the app
end = Button(window, text='Close Program', bg='#DBE2EF', fg='black', command=window.destroy)
end.pack(side=BOTTOM)

#Running the Tkinter window
window.mainloop()