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
import filemover_main
import filemover_gui
import shutil
import time
import datetime
import os
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import sqlite3




def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
                                                                                #Begins scan and catches user imput error
def begin_Scan(self):
    create_db(self)                                                             #Begins scan process, first creating the database if none exists
    remind_user(self)                                                           #then fetching the last timestamp saved in the database 
    try:                                                                        
        lst_files(self)                                                         #lst_files, grabs the directory and destination paths from text boxes
    except OSError:                                                             #and iterates through files in folder, copying those modified in the last 24 hours
        tk.messagebox.showerror('Invalid entry','Please check filepath')
        reset(self)
    pass
    make_time_stamp(self)
        
def remind_user(self):                                                          #Displays lastchk for user
    try:
        check_timestamp(self)
        answer = tk.messagebox.askquestion("Last Scan", 'Last scan was done {}. Do you wish to continue?'
                                       .format(time.ctime(float(self.lastchk[0]))))
        if answer == 'yes':
            pass
        else:
            ask_quit(self)
    except TypeError:
        pass
    
    
    
def check_timestamp(self):                                                      #Grabs last entry of the tbl_timestamp
    conn = sqlite3.connect('lastscan.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_lastscan FROM tbl_timestamp ORDER BY ID DESC LIMIT 1")
        self.lastchk = cur.fetchone()
    conn.commit()
    conn.close()
    

def create_db(self):                                                            #Creates database, table and table contents
    conn = sqlite3.connect('lastscan.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_timestamp(ID INTEGER PRIMARY KEY AUTOINCREMENT,col_lastscan TEXT);")
    conn.commit()
    conn.close()
    
def make_time_stamp(self):                                                      #Makes epoch timestamp and inputs into tbl_lastscan
    unix = time.time()
    conn =sqlite3.connect('lastscan.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_timestamp (col_lastscan)VALUES(?)", ([unix]))
    conn.commit()
    conn.close()


def ask_directory(self):                                                        #Initiates folder selection and inserts selected folder into text box
    directory = filedialog.askdirectory(initialdir = 'C:/Users/Student/Desktop/Python' ,title='Select Folder')
    self.txt_foldscan.insert(1,directory)
    

def ask_destination(self):
    directory1 = filedialog.askdirectory(initialdir = 'C:/Users/Student/Desktop/Python' ,title='Select Folder')
    self.txt_foldrec.insert(1,directory1)
       
    
def lst_files(self):                                                            #Grabbing strings in text boxes 
    dir_folder= self.txt_foldscan.get()                                         #making list of files in dir_folder 
    dest_folder= self.txt_foldrec.get()
    dirlist = os.listdir(dir_folder)               
    for i in range(len(dirlist)):                                               #Iterating through list and running find_mod_files by index for length of index
        find_mod_files(self,dir_folder + '/{}'.format(dirlist[i]),dest_folder)

                                                                            
def find_mod_files(self,path,dest_folder):                                      #Using current seconds since epic and seconds since last modification since epic
    epic = time.time()
    self.yest_epic = epic - 86400                                               #if seconds since last epic 24 hours ago (yest_epic) is less than modification time
    mod_time = os.path.getmtime(path)                                           #seconds since last epic(mod_time) than copy file
    if mod_time > self.yest_epic:        
        copy_file(self,path,dest_folder)                        
    return

def copy_file(self,path,dest_folder):                                           #Copies file modified or created in last 24 hours to destination folder
    shutil.copy(path,dest_folder)            
    return
    
def reset(self):                                                                #Clears text boxes 
    self.txt_foldscan.delete(0,END)
    self.txt_foldrec.delete(0,END)


def ask_quit(self):
    answer = tk.messagebox.askquestion("Exit program", "Okay to exit application?")
    if answer == 'yes':
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
