from tkinter import *
import time
import keyboard
from tkinter import filedialog



root = Tk()
#FUNCTIONS

    
def click():
    a = entry.get()
    while True:
        
        if len(a) == 0:
            wmessage1 = Tk()
            wlabel1 = Label(wmessage1, text = "Empty input field is not allowed.")
            wlabel1.pack()
            wmessage1.mainloop()
            del a
        elif len(a) < 20:
            
            while True:
                for i in a: 
                    keyboard.press(i)
                    time.sleep(0.05)
                    keyboard.release(i)
                    if keyboard.is_pressed("Esc"):
                        
                        Tmessage = Tk()
                        tlabel = Label(Tmessage, text = "Program terminated",fg = 'red')
                        tlabel.pack()
                        Tmessage.mainloop()
                        
                        time.sleep(1)
                        del a
                        break
        elif len(a)>20:
            wmessage2 = Tk()
            wlabel2 = Label(wmessage2, text = "Input length should be 20 characters or below.")
            wlabel2.pack()
            wmessage2.mainloop()
            del a
                    

def fclick():
    file = filedialog.askopenfilename(title = "Open script",filetypes = [('Text Files', '*.txt')])
    fileread = open(file,'rt')    
    a = fileread.read()
    fileread.close()
    while True:
        if len(a) == 0:
            wmessage1 = Tk()
            wlabel1 = Label(wmessage1, text = "Empty input field is not allowed.")
            wlabel1.pack()
            wmessage1.mainloop()
        
        elif len(a) < 20:
            
            while True:
                for i in a:   
                    keyboard.press(i)
                    time.sleep(0.05)
                    keyboard.release(i)
                    if keyboard.is_pressed("Esc"):
                        
                        Tmessage = Tk()
                        tlabel = Label(Tmessage, text = "Program terminated",fg = 'red')
                        tlabel.pack()
                        Tmessage.mainloop()
                        
                        time.sleep(1)
                        del a
                        break

        
                        
                    
        
        

            
            
    
    
    
            
#ENTRY
canvas = Canvas(root,width = 500, height = 500)
canvas.pack()
entry = Entry(root, width = 30,font =('Courier New', 10) )
entry.place(x = 125, y = 80)

#BUTTON
button = Button(root, text = "Open script...", command = fclick)
button.pack(side = 'left',padx = 10)
button.pack(pady = 10)

button = Button(root, text = "Start", command = click)
button.pack(side = 'left',padx = 10)
button.pack(pady = 10)

#LABEL
label = Label(root, text = "Press 'Esc' to stop program.",fg = 'red')
label.pack(side = 'left',pady=10)



root.wm_attributes('-toolwindow','True')
root.title('Macro')
root.mainloop()


