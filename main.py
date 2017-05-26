#!/usr/bin/python

from Tkinter import *
from PIL import Image, ImageTk
from RollDice import RollDice

dice = RollDice(6)

#Create main screen
screen = Tk()
screen.configure(background="#a1dbcd")
screen.title("Roll Dice Game")
screen.geometry("500x500")

#Change label's background every time you roll the dice
setColor = 1

def printImage(filename,label,labelbg):
    #Open and resize image
    photo = Image.open(filename)
    resizePhoto = photo.resize((100,100),Image.BILINEAR)
    
    #Update label
    photoimg = ImageTk.PhotoImage(resizePhoto)
    label.configure(image=photoimg,bg=labelbg,bd=5)
    label.photo = photoimg
    label.pack(side = LEFT)
    
    #Close image file
    photo.close()
    resizePhoto.close()

def insertText():
    global setColor
    
    #Get random number
    rand_num1 = dice.rollDice()
    rand_num2 = dice.rollDice()

    labelbg = ""
    if(setColor == 1):
        setColor = 0
        labelbg = "#299617"
    else:
        setColor = 1
        labelbg = "#f0422e"

    printImage("Die-%d.gif" % rand_num1,label1,labelbg)
    printImage("Die-%d.gif" % rand_num2,label2,labelbg)

    s = str(rand_num1)+" "+str(rand_num2)
    if(rand_num1 == rand_num2): s = s+", Lucky!"
    text.insert(END,s+"\n")

#Create Button widget
button = Button(screen,text="Roll dice",height=2,width=10,command=insertText)
button.pack()

#Create Frame widget
frame = Frame(screen)
frame.pack()

bottomFrame = Frame(screen)
bottomFrame.pack(side=BOTTOM)

scrollbar = Scrollbar(bottomFrame)
scrollbar.pack(side=RIGHT,fill=Y)

#Create Label widget within frame
label1 = Label(frame)
label2 = Label(frame)

printImage("diceimg.jpeg",label1,"#299617")
printImage("diceimg.jpeg",label2,"#299617")

#Create Label widget within bottomFrame
text = Text(bottomFrame)
text.pack(side = BOTTOM,fill = BOTH)
text.config(yscrollcommand=scrollbar.set)
text.insert(END,"Your Record:\n")
scrollbar.config( command = text.yview )

screen.mainloop()

