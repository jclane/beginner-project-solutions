import time
from random import randint
from tkinter import *
from tkinter import ttk

class tkWindow:
       
    def __init__(self, root):
    
        def timer():
            result.set("Let me consult with my friends on the other side...")
            root.after(1500, ask)
            
        def ask():
        
            ANSWERS = {1:"It is certain.", 2:"It is decidedly so.", 3:"Without a doubt.", \
                        4:"Yes - definitely.", 5:"You may rely on it.", 6:"As I see it, yes.", \
                        7:"Most likely.", 8:"Outlook good.", 9:"Yes.", 10:"Signs point to yes.", \
                        11:"Reply hazy, try again", 12:"Ask again later.", 13:"Better not tell you now.", \
                        14:"Cannot predict now.", 15:"Concentrate and ask again.", 16:"Don't count on it.", \
                        17:"My reply is no.", 18:"My sources say no.", 19:"Outlook not so good.", 20:"Very doubtful."}
            
            result.set("They spirits have answered!\n\n\tThey say: {}".format(ANSWERS[randint(1,20)]))
            
        def clear_window():
            question.set("")
            result.set("")           
            
        def play_again():
            clear_window()
            
        def close_window():
            root.destroy()
        
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
                
        resultframe = ttk.Frame(mainframe)
        resultframe.grid(column=1, row=1, sticky=(N, W, E))
        
        controlframe = ttk.Frame(mainframe)
        controlframe.grid(column=1, row=2, sticky=(W, E, S))
        
        question = StringVar()
        result = StringVar()
        
        ttk.Entry(controlframe, textvariable=question).grid(column=0, row=1, columnspan=3, sticky=W+E)
        ttk.Button(controlframe, text="Ask", command=timer).grid(column=4, row=1, pady=15, sticky=W+E)
        ttk.Button(controlframe, text="Clear", command=clear_window).grid(column=5, row=1, pady=15, sticky=W+E)
        ttk.Button(controlframe, text="Play Again", command=play_again).grid(column=0, row=3, sticky=W+E)
        ttk.Button(controlframe, text="Quit", command=close_window).grid(column=5, row=3, sticky=W+E)
        
        ttk.Label(resultframe, textvariable=result).grid(column=0, row=1, sticky=N+W+E+S)
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


root = Tk()
tkWindow(root)
root.mainloop()
