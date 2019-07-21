'''
issues
- control the location and size of the GUI

'''

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox # use this to see if the player would like to play again
import random

# backend of the MC game

def extractData(ffilename):

    fdicRow = {} # must define this within the function
    flstTable = [] # must define this within the function
    '''
    purpose:
    1. this function is to open any txt file with keyword and value pair separated by a dash
    and extract them into key/value pairs
    2. add the dictionary pairs into a list
    input: file name containing the xxx-xxxx list
    output: list containing key/value pairs
    '''
    with open(ffilename, "r") as f:
        for item in f:

            try:  # this loop here is to catch errors in the txt file
                fWord, fDefinition = item.split('-', 1) # problem as there are empty lines in the file
            except:
                print(item)

            fdicRow[fWord]=fDefinition.strip() # this .strip() gets rid of \n in the values
            # the line above acts as append for all subsequent dicRow key/value pairs
            flstTable=list(fdicRow.items()) # output = [('a', 'high'), etc]
    return fdicRow,flstTable

def browsefile():

    filename = filedialog.askopenfilename()
#    filename = r"C:\Users\robox\Google Drive\My_Python_programs (GD)\wordGame\word.txt"

    global dicRow
    global lstTable
    dicRow, lstTable = extractData(filename)
    # dicRow contains a list of words.  dicRow is a simple list.
    # lstTable contains ('word', 'meaning').  LstTable is a dictionary
    Popup()

def wordGen(fdicRow, fguess): # called by playgame() and takes dicRow, fguess as inputs from the Popup
    global MCW
    MCW = random.sample(fdicRow.keys(), int(fguess))  # MCW is a list of chosen words #
#    input (MCW)

def choiceGen(): # called by Mcgen() and return 4 random definitions
    global MCWpool # MCWpool is the pool of 4 choices
    MCWpool = []
    while (MCW[k] not in MCWpool):
        MCWpool = random.sample(dicRow.keys(), 4)  # MCWpool is a list of words for the random answers

def kcounter(): # called by Mcgen() and indicates the number of words being played

    global k
    k+=1

def kreset(): # called if playagain is true.

    global k
    k=-1

def scorereset():
    global score
    score = 0

def Quit(): # called by mcgen()
    root.destroy()
    playGame.destroy()

def scorecounter(): # this counting function must be outside of the main function that calls it
    global score
    score = score + 1

score = 0

def rightAnsfetch(): # called by userInput().  This prints the correct answer
    pp = MCWpool.index(MCW[k-1]) # this finds index of MCW[k-1] in MCWpool
    rightanswer.set(pp+1) # need to identify which one is the correct one
    #rightanswer.set(dicRow[MCW[k]]) # need to identify which one is the correct one

def userInput(value): # use this function to compare answers and print the result / score
    # the intake value ranges between 1 and 4

    global rightanswer
    global outputans
    global goodjob

    rightanswer = StringVar(frame_FB)

    # print(MCWpool[(value-1)]) #---- this line is to check the choice
    # print(MCW[k-1]) #---- this line is check the given word

    if (MCWpool[(value-1)] == MCW[k-1]): # MCWpool[value-1] is the word chosen by the user and MCW[i] is the given word
        # it is necessary to reduce the value by 1 as MCWpool starts at 0 instead of 1
        goodjob = ttk.Label(frame_FB, text = 'Correct.  Good job!!!')
        goodjob.grid(row=0)
        outputans = ttk.Label(frame_FB, textvariable =' ') # whatever the value inside textvariable is being treated as empty spaces
        outputans.grid(row=1)
        ttk.Label(frame_FB, text = "Your score is").grid(row=2)
        scorecounter()
        ttk.Label(frame_FB, text=score).grid(row=3)
        ttk.Label(frame_FB, text='out of '+ number_of_guess).grid(row=4)
    else:

        goodjob = ttk.Label(frame_FB, text = 'The correct answer is')
        goodjob.grid(row = 0)
        outputans = ttk.Label(frame_FB, textvariable = rightanswer, wraplength = 200)
        outputans.grid(row = 1)
        rightAnsfetch() # this function will put the correct definition reflecte by the variable rightanswer in the frame
        ttk.Label(frame_FB, text="Your score is").grid(row=2)
        ttk.Label(frame_FB, text=score).grid(row=3)
        ttk.Label(frame_FB, text='out of ' + number_of_guess).grid(row=4)

def wordfetch(): # call by mcgen().  This function is mandatory so the new and old words do not overlap each other
    word.set(f'Word # {str(k+1)} is {MCW[k]}')

def choicefetch(): # called by mcgen().  This function sets the definitions of the four choices

    choice1.set(dicRow[MCWpool[0]])
    choice2.set(dicRow[MCWpool[1]])
    choice3.set(dicRow[MCWpool[2]])
    choice4.set(dicRow[MCWpool[3]])
    # choice1.set(MCWpool[0])
    # choice2.set(MCWpool[1])
    # choice3.set(MCWpool[2])
    # choice4.set(MCWpool[3])

def mcgen():

    #print (f'value of k at the beginning of mcgen is {k}')

    if (k < int(number_of_guess)):

        global word

        word = StringVar(frame_MC)

        ttk.Label(frame_MC, textvariable = word).grid(row=0, columnspan = 2, sticky = W)  # the variable word comprises of a number and the word
        ttk.Label(frame_MC, text="Please select one of the definitions below:  ").grid(row=1, columnspan = 2, sticky = W)

        wordfetch() # this puts the MCW[i] word in the GUI

        choiceGen() # this function generates 4 MC according to the MCW[i]

        global choice1
        global choice2
        global choice3
        global choice4

        user = IntVar(frame_MC) # it is extremely important to put frame_MC inside IntVar as else you will always get zero

        choice1 = StringVar(frame_MC)
        choice2 = StringVar(frame_MC)
        choice3 = StringVar(frame_MC)
        choice4 = StringVar(frame_MC)

# The Radiobutton just shows the choice # while the label to its right shows the actual choice

        # ttk.Radiobutton(frame_MC, textvariable = choice1, variable=user, value=1,
        #                         command=lambda :userInput(user.get())).grid(row=2, column = 0, sticky=E)
        # ttk.Radiobutton(frame_MC, textvariable = choice2, variable=user, value=2,
        #                         command=lambda: userInput(user.get())).grid(row=3, column = 0, sticky=E)
        # ttk.Radiobutton(frame_MC, textvariable = choice3, variable=user, value=3,
        #                         command=lambda: userInput(user.get())).grid(row=4, column = 0, sticky=E)
        # ttk.Radiobutton(frame_MC, textvariable = choice4, variable=user, value=4,
        #                         command=lambda: userInput(user.get())).grid(row=5, column = 0, sticky=E)
        ttk.Radiobutton(frame_MC, text = "1 ", variable=user, value=1,
                                command=lambda :userInput(user.get())).grid(row=2, column = 0, sticky=E)
        ttk.Radiobutton(frame_MC, text = "2 ", variable=user, value=2,
                                command=lambda: userInput(user.get())).grid(row=3, column = 0, sticky=E)
        ttk.Radiobutton(frame_MC, text = "3 ", variable=user, value=3,
                                command=lambda: userInput(user.get())).grid(row=4, column = 0, sticky=E)
        ttk.Radiobutton(frame_MC, text = "4 ", variable=user, value=4,
                                command=lambda: userInput(user.get())).grid(row=5, column = 0, sticky=E)

        ttk.Label(frame_MC, textvariable=choice1, wraplength=200).grid(row=2, column=1, sticky=W)
        ttk.Label(frame_MC, textvariable=choice2, wraplength=200).grid(row=3, column=1, sticky=W)
        ttk.Label(frame_MC, textvariable=choice3, wraplength=200).grid(row=4, column=1, sticky=W)
        ttk.Label(frame_MC, textvariable=choice4, wraplength=200).grid(row=5, column=1, sticky=W)

        choicefetch() # this puts the 4 MC in the GUI
    else:
        playAgain = messagebox.askyesno("Game Over", "Do you want to play again")
        if playAgain == True:
            kreset() # resets the k value in mcgen to 0
            scorereset()
            playGame.destroy() # cloese the previous multiple choice window
            Popup() # at this point, the value of k = number of guesses previously entered

        else:
            Quit() # this is not working either

    kcounter() # defines k for the words.  Once the user clicks the choice, this immediates acts.

def clearall():

    outputans.config(textvariable=' ') # the program treats whatever content inside as empty characters
    goodjob.config(text='                       ') # the number of empty spaces only need to cover the sentence "Correct.  Good job!!!"
    mcgen()

def PlayGame():

    popup.withdraw() # command is to close the popup window after the user submits the number of guesses.
    # must have the () after withdraw.

    global number_of_guess
    number_of_guess = guess.get()  # it is ok to call a variable from another function
    wordGen(dicRow, number_of_guess)  # this function generates a list of words according to the number of guesses

    global playGame

    k = 0 # this line effectively resets the value of k to 0 for subsequent plays.
    # however, this k is independent from the k in mcgen.

    playGame = Tk()

    #value of k here equals to the number of guesses from the previous game for the next game

    #print(f'value of k in Playgame equals to {k}')
    frame_header = ttk.Frame(playGame)
    frame_header.grid(row=0, columnspan=2)
    ttk.Label(frame_header, text="Let's play!!!").pack()

    global frame_MC # this line is required in order to reference it in other functions

    frame_MC = ttk.Frame(playGame)
    frame_MC.grid(row=1, column = 0)

    global frame_FB

    frame_FB = ttk.Frame(playGame)
    frame_FB.grid(row=1, column = 1)

    mcgen()

    # the following step only get called once
    ttk.Button(frame_MC, text='Continue', command=clearall).grid(row=6, column = 0, sticky = E)
    ttk.Button(frame_MC, text='Quit', command=Quit).grid(row=6, column = 1, sticky = W)

    playGame.mainloop()

def Popup():

    # when the first starts, k = 0
    # when popup is called subsequently, k equals to the number of previous guesses
    global popup # this would allow the PlayGame function to close this window
    popup = Toplevel(root)  # this creates the top-level pop-up window to ask the user about the number of words
    popup.title("Let's begin")
    label = ttk.Label(popup, text="How many words would you like to play?")
    label.pack()
    global guess # defines this as a global variable so it could be used by the function PlayGame
    guess = ttk.Entry(popup, width=3)
    guess.pack()
    popup.lift(root)  # this puts the popup window over the root window
    guessButton = ttk.Button(popup, text="Submit", command = PlayGame)
    guessButton.pack()


def AddWord():
    pass

# this is the main window with drop-down menu calling different options.

# will eventually turn the following as an input so it is more versatile

k = 0 # this variable is associated with mcgen and keeps track of the number of word being played.  1 is being added immediately after the user selects
# the radiobutton and the addition is via the kcounter function.

root = Tk() # this is to use tkinter class to initiate the object called root

menu_obj = Menu(root) # Menu is a method in tkinter.  this is to create the menu_obj using the tkinter class.
# but what about the root inside Menu?

root.config(menu=menu_obj) #

subMenu_obj = Menu(menu_obj) # creating the subMenu inside the object menu

menu_obj.add_cascade(label="Options", menu=subMenu_obj)

subMenu_obj.add_command(label="Play Game", command=browsefile) # changing command to browsefile in order for user to select the file first
subMenu_obj.add_command(label="Add word", command=AddWord)
subMenu_obj.add_separator()
subMenu_obj.add_command(label="Exit", command = root.destroy)

root.mainloop()
