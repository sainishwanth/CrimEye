
from cgitb import text
from fileinput import filename
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import down, width
from webbrowser import get
from PIL import Image, ImageTk
import detect_knives
from tkinter import filedialog as fd
import threading as th




check = 0
choice = ''
src_choice = ''
def open_popup(txt):
   top= Toplevel(tk_Window)
   top.geometry("700x150")
   top.title("Error!")
   Label(top, text= txt, font=('Mistral 18 bold')).place(x=150,y=40)

def btn_list(clicked):
    global choice
    if choice == 'Face Detection':
        choice = 'best_face.pt'
    else:
        choice = 'best_weapons.pt'
    if(clicked.lower() == 'webcam'):
        opt1 = detect_knives.parse_opt(choice,'0')
        detect_knives.main(opt1)
    elif(clicked.lower() == 'image'):
        filename = fd.askopenfilename()
        fn = ''
        fn2 = ''
        for c in filename[::-1]:
            if(c == '/'):
                break
            else:
                fn += c
        for c in fn[::-1]:
            fn2 += c
        print(fn2)
        opt1 = detect_knives.parse_opt(choice, filename, fn2)
        detect_knives.main(opt1)
    
def img_window(choice_ ):
    global choice
    choice = choice_
    tk_choice = Tk()
    tk_choice.geometry('400x400')
    options = ['Webcam', 'Image']
    clicked = StringVar()
    clicked.set('Webcam')
    drop = OptionMenu(tk_choice, clicked, *options)
    drop.pack()
    print(f"It is: {clicked.get()}")
    btn3 = Button(tk_choice, text='Submit', command=lambda: btn_list(clicked.get())).pack()
    tk_choice.mainloop()

def choice_window(user_text, pass_text):
    if(user_text.get() == '') or (pass_text.get() ==  ''):
        open_popup("Username or Password Fields cannot be empty!")
        return
    tk_choice = Tk()
    tk_choice.geometry('400x400')
    tk_choice.title("Choice Window")
    options = ['Weapon Detection', 'Face Detection']
    clicked = StringVar()
    clicked.set(' ')
    drop = OptionMenu(tk_choice, clicked, *options)
    drop.pack()
    btn3 = Button(tk_choice, text='Submit', command=lambda: img_window(clicked.get())).pack()
    tk_choice.mainloop()

def sign_up_return():
    global check
    check = 1
def sign_up():
    tk_signup = Tk()
    tk_signup.geometry('800x800')
    tk_signup.title("Sign Up")
    while check == 0:
        Label(tk_signup, text='Sign Up',font=('Arial', 50)).pack()
        frame_2 = ttk.Frame(tk_signup)
        frame_2.pack()
        frame_2.place(x=300,y=300)
        Label(frame_2, text='Username').pack()
        signup_user = StringVar()
        Entry(frame_2, textvariable=signup_user).pack()
        Label(frame_2, text='Password').pack()
        signup_pass = StringVar()
        Entry(frame_2, textvariable=signup_pass,show='*').pack()
        signup_repass = StringVar()
        Label(frame_2, text = "Re Enter Your Password").pack()
        Entry(frame_2, textvariable=signup_repass, show='*').pack()
        btn_signup = Button(frame_2, text='Sign up', width=3, command=sign_up_return).pack()
        tk_signup.mainloop()
    tk_signup.destroy()
    
    
    

tk_Window = Tk()
tk_Window.geometry('800x800')
tk_Window.title('Login')
Label(tk_Window, text='Login',font=('Arial', 50)).pack()
frame_ = ttk.Frame(tk_Window)
frame_.pack()
frame_.place(x=300,y=300)
Label(frame_, text="").pack()
Label(frame_, text='Username', font=('Arial', 20)).pack()
user_text = StringVar()
Username = Entry(frame_, textvariable=user_text).pack()
Label(frame_, text='Password', font=('Arial', 20)).pack()
pass_text = StringVar()
Password = Entry(frame_,textvariable=pass_text, show='*').pack()
Label(frame_, text="").pack()
btn_submit = Button(frame_, text='Submit', command=lambda: choice_window(user_text, pass_text)).pack()
btn_signup = Button(frame_, text='Sign Up', width=3, command=sign_up).pack(side=LEFT)
Label(frame_, text="")
btn_frgtpass = Button(frame_, text='Forgot Password', width=10).pack(side=RIGHT)
tk_Window.mainloop()

