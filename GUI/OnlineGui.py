import tkinter as tk
from tkinter import *
import pickle
from tkinter import ttk
#from clientchartGUI import ChartRoomOnline
from SocketChatRoom import SocketChatRoomGUI
def OnlineGuiWindow(NameKey,port1,port2):
    
    window = tk.Tk()
    window.title("Online Gui")
    window.geometry('800x600')
   
    
    #canvas = tk.Canvas(window,height = 200,width=500,bg='white')
    #x0, y0, x1, y1= 250, 50, 260, 60
    #oval = canvas.create_oval(x0, y0, x1, y1, fill='green')
    #oval2 = canvas.create_oval(x0,y0+30,x1,y1+30,fill='green')
    #oval3 = canvas.create_oval(x0,y0+60,x1,y1+60,fill='green')
    #canvas.pack()
    
    with open('./usrs_info.pickle','rb') as usr_file:
        tot_name = pickle.load(usr_file)
        ydist = 0;
        for key in tot_name:
            if key == NameKey:
                continue
            #tk.Label(window,text=key,background='red').place(x=700,y=50+ydist)
            tk.Button(window,text=key,background='red').place(x=700,y=50+ydist)
            ydist += 30
        usr_file.close()
       
        messages = tk.Text(window)
        messages.pack()
        input_user = tk.StringVar()
        input_field = tk.Entry(window,text=input_user)
        input_field.pack(side=BOTTOM,fill=X)
        input_chartroom = input_field.get()
        def Entry_pressed(event):
            input_get = input_field.get()
            #print(input_get) #string
            #print(type(port1),type(port2))
            SocketChatRoomGUI(input_get,port1,port2) 
            messages.insert(INSERT,'%s\n' %input_get)
            #ChartRoomOnline(NameKey,input_get)
            input_user.set('')
            return "break"
        frame = tk.Frame(window)
        input_field.bind('<Return>',Entry_pressed)
        frame.pack()
        #ChartRoomOnline(NameKey)
        #For text 20191225 temporarily command
        #conversation_var = tk.StringVar()
        #conversation_var_label = tk.StringVar()
        #entry_con_var = tk.Entry(window,textvariable=conversation_var,width=50)
        #entry_con_var.place(x = 30,y = 550)
        #display = tk.Label(window,textvariable=conversation_var).place(x = 100,y=100)
        
        #display = tk.Label(window,textvariable=conversation_var_label).place(x = 100, y = 100)
        #def Go_String():
        #    s = conversation_var.get()
        #    conversation_var_label.set(s)
        #    display = tk.Label(window,textvariable=conversation_var_label).place(x = 100, y = 100)
        #    entry_con_var.delete(0,'end')
        #tk.Button(window,text="Go",command=Go_String).place(x = 600, y = 550)
    def logout():
        with open('./usrs_info.pickle','rb') as usrs_file:
            login = pickle.load(usrs_file)
            #for key in login:
            #    print(key)
            usrs_file.close()
        tk.messagebox.showinfo(title="Logout",message="Logout: ")
        window.destroy()
    
    #LogOutButton = tk.Button(window,text="Logout",command=logout).pack(anchor=tk.S)
    #LogOutButton = ttk.Button(window,text="Logout",command=logout).pack(anchor=tk.NE)
    ttk.Button(window,text="Logout",command=logout).place(x = 700, y = 550)

    window.mainloop()
