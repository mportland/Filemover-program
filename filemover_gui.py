#       Version         Python 3.6
#
#       Author          Mathew Perrow
#
#       Description     Program to select a folder
#                       and iterate through files in folder
#                       and copy any files that have been 
#                       created or modified in the last 24 hours
#                       to another selected folder
#

from tkinter import *
import tkinter as tk

import filemover_main
import filemover_func

def load_gui(self):
    #Create Labels for text boxes
    self.lbl_foldscan = tk.Label(self.master,text='Folder to be scanned')
    self.lbl_foldscan.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_foldrec = tk.Label(self.master,text='Folder to copy into')
    self.lbl_foldrec.grid(row=1,column=2,padx=(27,0),pady=(10,0),sticky=N+W)
    

    #Text boxes for filepath entry
    self.txt_foldscan = tk.Entry(self.master,text='',)
    self.txt_foldscan.grid(row=2,column=0,rowspan=1,columnspan=1,padx=(27,20),pady=(0,0),sticky=N+E+W)
    self.txt_foldrec = tk.Entry(self.master,text='')
    self.txt_foldrec.grid(row=2,column=2,rowspan=1,columnspan=1,padx=(27,20),pady=(0,0),sticky=N+E+W)
    #Create buttons to navigate directory
    self.btn_selectfile1 = tk.Button(self.master,width=10,height=1,text='Select Folder',command=lambda: filemover_func.ask_destination(self))
    self.btn_selectfile1.grid(row=3,column=2,padx=(27,0),pady=(10,10),sticky=N+W)
    self.btn_selectfile = tk.Button(self.master,width=10,height=1,text='Select Folder',command=lambda: filemover_func.ask_directory(self))
    self.btn_selectfile.grid(row=3,column=0,padx=(27,0),pady=(10,10),sticky=N+W)
    #Create buttons to reset, close or commence scan and copy
    self.btn_scncpy = tk.Button(self.master,width=12,height=2,text='Scan and Copy',command=lambda: filemover_func.begin_Scan(self))
    self.btn_scncpy.grid(row=8,column=0,padx=(25,0),pady=(30,10),sticky=W)
    self.btn_reset = tk.Button(self.master,width=12,height=2,text='Reset',command=lambda: filemover_func.reset(self))
    self.btn_reset.grid(row=8,column=1,padx=(15,0),pady=(30,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: filemover_func.ask_quit(self))
    self.btn_close.grid(row=8,column=2,columnspan=1,padx=(15,0),pady=(30,10),sticky=E)



    



if __name__ == "__main__":
    pass
