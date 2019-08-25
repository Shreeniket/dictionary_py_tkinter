from tkinter import *
from tkinter import font
import json
from difflib import get_close_matches

window = Tk()
#window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
def findMeaning():
    try:
        toAppend = ""
        t1.delete('1.0', END)
        result = ''
        w = e1_value.get()
        data = json.load(open("data.json"))
        if w[0].isupper():
            pass
        else:
            toCheck = get_close_matches(w,data.keys())[0]
            if(toCheck[0].isupper()):
                result = data[toCheck]
            else:
                w.lower()
        if w in data.keys():
            if result is '':
                result = data[w]
        else:
            w = get_close_matches(w,data.keys())[0]
            if w is None:
                toAppend = "Sorry no such word in this dictionary."
            if result is '':
                result = data[w]
                toAppend = "Showing results for \""+w+"\" instead.\n\n"

        t1.insert(END, toAppend)
        r = result
        for i in range(0, len(result)):
            result = "Meaning "+str(i+1)+":"
            t1.insert(END, result)
            result = "\n"
            t1.insert(END, result)
            result = r[i]
            t1.insert(END, result)
            result = "\n"
            t1.insert(END, result)
            result = "----------"
            t1.insert(END, result)
            result = "\n"
            t1.insert(END, result)

    except:
        result = "Sorry, error occurred or word not found."
        t1.insert(END, result)

l1 = Label(window, text="Shreeniket's Dictionary", height =1, width = 20)
l1.grid(row = 0, column=1, sticky=W)

l2 = Label(window, text="Enter word to search:", height =1, width = 20)
l2.grid(row = 1, column=1)

e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row=1, column=2)

b1 = Button(window, text = "Search", command = findMeaning)
b1.grid(row = 1,column=3)

l3 = Label(window, text="Result:", height =1, width = 20)
l3.grid(row = 2, column=1)

t1 = Text(window, height =10, width = 20, wrap=WORD)
t1.grid(row=2,column=2)

f = font.Font(l1,l1.cget("font"))
f.configure(underline=True)
l1.configure(font=f)

window.mainloop()
