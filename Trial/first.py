# from tkinter import *
# from tkinter.ttk import *
# from tkinter import messagebox
# import tkinter
# window = tkinter.Tk()
# window.title("GUI")
# window.geometry('350x200') #used to resize the windows

# l1 = Label(window,text = "Ashutosh",font=("Arial Bold",50))
# l1.grid(column=0,row=0)

# txt = Entry(window,width=10)
# txt.grid(column=1,row=0)

# def clicked():
#     l1.config(text=txt.get())
# bt = Button(window,text = "Enter",command=clicked)#clickable buttom and command help in giving function
# bt.grid(column=0,row=1)

# combo = Combobox(window)
# combo['values'] = (1,2,3,4,"ashu")
# combo.current(3)
# combo.grid(column=0,row = 2)

# def clickedAgain():
#     messagebox.showinfo('Message title','Message content')
# btn = Button(window,text='Enter',command=clickedAgain)
# btn.grid(column=0,row=3)

# window.mainloop()


from tkinter import *
import win32api
from tkinter import filedialog
  
# Create Tkinter Object
root = Tk()
  
# Set Title and geometry
root.title('Print Hard Copies')
root.geometry("200x200")
  
# Print File Function
def print_file():
    
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
      initialdir="/", title="Select file", 
      filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
      
    if file_to_print:
        
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
  
# Make Button
Button(root, text="Print FIle", command=print_file).pack()
  
# Execute Tkinter
root.mainloop()