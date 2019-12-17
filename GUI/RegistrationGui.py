import tkinter as tk 
from tkinter import messagebox
import pickle
#EncryptofRegitration.py with EncryptionPassword function
from EncryptofRegitraion import EncryptionPassword
from OnlineGui import OnlineGuiWindow

#Build a window with tkinter
window = tk.Tk()
window.title('Registration')
window.geometry('500x300')

##Prepare to decorate my gui
#canvas = tk.Canvas(window,height=200,width=550)
#image_file = tk.PhotoImage(file='welcome.gif')
#image = canvas.create_image(0,0,anchor='nw',image=image_file)
#canvas.pack(side='top')

tk.Label(window,text='User name: ').place(x=50,y=50)
tk.Label(window,text='Password: ').place(x=50,y=80)

##StringVar is a "class", you can use any function to imporve the original string##

#For user name 
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=150,y=50)

#For password
var_usr_passwd = tk.StringVar()
entry_usr_passwd = tk.Entry(window,textvariable=var_usr_passwd,show='*')
entry_usr_passwd.place(x=150,y=80)


def usr_login():
    usrs_name = var_usr_name.get()
    usrs_passwd = var_usr_passwd.get()

    #If the "*.pickle" file is already done
    try:
        with open('usrs_info.pickle','rb') as usrs_file:
            usrs_info = pickle.load(usrs_file)

    #else
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usrs_file:
            usrs_info = {}
            pickle.dump(usrs_info,usrs_file)
    #If the user name in login equal to user name in pickle file
    if usrs_name in usrs_info:
        if (usrs_passwd == usrs_info[usrs_name]):
            tk.messagebox.showinfo(title="Login",message="Successfully login")
            window.quit()
        else:
            tk.messagebox.showinfo(title="Login",message="Error, Please sign login again")
    else:
        is_signed_up = tk.messagebox.askyesno('Welcome','You may not sign up, please sign up at first')
        # 'is_signed' is 'true'
        if(is_signed_up):
            usr_signup()
        
#Sign up 
def usr_signup():
    def Registration_signup():
        np = new_passwd.get()
        npf = new_passwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle','rb') as usrs_file:
            exist_usr_info = pickle.load(usrs_file)
        
        if(np!=npf):
            tk.messagebox.showerror(title='Sign up',message='Error! Your password and confirm password is not the same')
        elif(nn in exist_usr_info):
            tk.messagebox.showerror(title='Sign up',message='Error! The sign up information has already existed')
        else:
            #password from pickle file
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usrs_file:
                pickle.dump(exist_usr_info,usrs_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_signup.destroy()


        
    window_signup = tk.Toplevel(window)
    window_signup.geometry("350x200")
    window_signup.title('Sign up window')

    new_name = tk.StringVar()
    tk.Label(window_signup,text='User name: ').place(x=10,y=10)
    entry_new_name = tk.Entry(window_signup,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_passwd = tk.StringVar()
    tk.Label(window_signup,text='Password: ').place(x=10,y=50)
    enetry_new_passwd = tk.Entry(window_signup,textvariable=new_passwd,show="*")
    enetry_new_passwd.place(x=150,y=50)

    new_passwd_confirm = tk.StringVar()
    tk.Label(window_signup,text='Confirm Password: ').place(x=10,y=90)
    entry_new_conf_passwd = tk.Entry(window_signup,textvariable=new_passwd_confirm,show="*")
    entry_new_conf_passwd.place(x=150,y=90)

    btn_commfirm_sign_up = tk.Button(window_signup,text="Submit",command=Registration_signup)
    btn_commfirm_sign_up.place(x=150,y=130)
    
    #destroy 'window_signup'
    def signup_exitquit():
        window_signup.destroy()

    btn_exit = tk.Button(window_signup,text="Exit",command=signup_exitquit)
    btn_exit.place(x=250,y=130)

#Exit if all the login is finish 
def exitquit():
    if (var_usr_name.get() == "" or var_usr_passwd.get() == ""):
        pass
    else:
        EncryptionPassword(var_usr_name.get())
    window.quit()

btn_login = tk.Button(window,text="Login",command=usr_login)
btn_login.place(x=100,y=200)

btn_signup =  tk.Button(window,text="Sign up",command=usr_signup)
btn_signup.place(x=200,y=200)

btn_exit = tk.Button(window,text="Exit",command=exitquit)
btn_exit.place(x=300,y=200)

window.mainloop()
OnlineGuiWindow(var_usr_name)
#window.quit()

#EncryptionPassword(var_usr_name.get())


