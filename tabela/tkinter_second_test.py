# tkinter_second_test
# source: https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
# the fist part was sucessfull, but the second was wrong.





# from tkinter import *
# root=Tk()
# def retrieve_input():
#     inputValue=textBox.get("1.0","end-1c")
#     print(inputValue)

# textBox=Text(root, height=2, width=10)
# textBox.pack()
# buttonCommit=Button(root, height=1, width=10, text="Commit", 
#                     command=lambda: retrieve_input())
# #command=lambda: retrieve_input() >>> just means do this when i press the button
# buttonCommit.pack()

# mainloop()


# ######################################################

#Imports all (*) classes,
#atributes, and methods of tkinter into the
#current workspace

from tkinter import *

#***********************************
#Creates an instance of the class tkinter.Tk.
#This creates what is called the "root" window. By conventon,
#the root window in Tkinter is usually called "root",
#but you are free to call it by any other name.

root = Tk()
root.title('how to get text from textbox')


#**********************************
mystring = StringVar()

####define the function that the signup button will do
def getvalue():
##    print(mystring.get())
#*************************************

Label(root, text="Text to get").grid(row=0, sticky=W)  #label
Entry(root, textvariable = mystring).grid(row=0, column=1, sticky=E) #entry textbox

WSignUp = Button(root, text="print text", command=getvalue).grid(row=3, column=0, sticky=W) #button


############################################
# executes the mainloop (that is, the event loop) method of the root
# object. The mainloop method is what keeps the root window visible.
# If you remove the line, the window created will disappear
# immediately as the script stops running. This will happen so fast
# that you will not even see the window appearing on your screen.
# Keeping the mainloop running also lets you keep the
# program running until you press the close buton
root.mainloop()