import tkinter as tk
from tkinter import messagebox
import pickle
def OnlineGuiWindow(NameKey):
    
    window = tk.Tk()
    window.title("Online Gui")
    window.geometry('500x300')
    with open('./usrs_info.pickle','rb') as usr_file:
        tot_name = pickle.load(usr_file)
        ydist = 0;
        for key in tot_name:
            tk.Label(window,text=key).place(x=150,y=50+ydist)
            ydist += 30
            
    #tk.Label(window,text='John').place(x=150,y = 50)
    #tk.Label(window,text='Jack').place(x=150,y = 80)
    #tk.Label(window,text='Matt').place(x=150,y = 110) 
    
    window.mainloop()
