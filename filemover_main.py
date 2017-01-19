#       Version         Python 3.6
#
#       Author          Mathew Perrow
#
#       Description     Program to select a folder
#                       and iterate through files in folder
#                       and move any files that have been 
#                       created or modified in the last 24 hours
#                       to another selected folder
#

from tkinter import *
import tkinter as tk
                        #Importing both gui and function scripts for parent window
import filemover_gui    
import filemover_func
 



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(500,200) 
        self.master.maxsize(500,200)
                                               #Defining the dimensions of parent window and making it static
        filemover_func.center_window(self,500,200)
        self.master.title('New and modified file scanner')
        self.master.configure(bg='#F0F0F0')
        self.master.protocol('WM_DELETE_WINDOW', lambda: filemover_func.ask_quit(self))     
        arg = self.master

        filemover_gui.load_gui(self)
                
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)     #Creating menubar bar for parent window
        filemenu.add_separator()
        filemenu.add_command(label='Exit', underline=1,accelerator='Ctrl+Q',command=lambda: filemover_func.ask_quit(self))
        menubar.add_cascade(label='File', underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label='How to use filemover')
        helpmenu.add_separator()
        helpmenu.add_command(label='About filemover') 
        menubar.add_cascade(label='Help', menu=helpmenu) 
        self.master.config(menu=menubar, borderwidth='1')

        
if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
