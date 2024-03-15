#if True is used to collapse the code for easier navigation and can be deleted if not needed

import keyring as kr

registered_users = {}
#New Users
if True:
    def register():
        while True:
            #print("Please input intended username:")
            #new_user = input()
            #new_user_confirmation = input("Is " + new_user + " correct? (yes/no)\n")
            #if new_user_confirmation == "yes":
            #    break
            #else: 
            #    continue
        #while True:
            print("Please input a password for the new user:")
            new_password = input()
            new_password_confirmation = input("Is " + new_password + " correct? (yes/no)\n")
            if new_password_confirmation == "yes":
                kr.set_password("Backlog",new_user,new_password)
                break
            else: 
                continue
        registered_users[new_user] = new_password
        tkmb.showinfo(title="Registration Successful",message="You have registered a new user successfully")

#Login Function
if True:
    def login(): 
        cred = kr.get_credential("Backlog","")
        username = cred.username
        password = cred.password
        new_window = ctk.CTkToplevel(app) 

        new_window.title("New Window") 

        new_window.geometry("350x150") 

        if user_entry.get() == username and user_pass.get() == password: 
            tkmb.showinfo(title="Login Successful",message="You have logged in Successfully") 
            #ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack() 
        elif user_entry.get() == username and user_pass.get() != password: 
            tkmb.showwarning(title='Wrong password',message='Please check your password') 
        elif user_entry.get() != username and user_pass.get() == password: 
            tkmb.showwarning(title='Wrong username',message='Please check your username') 
        else: 
            tkmb.showerror(title="Login Failed",message="Invalid Username and password") 

#UI Interface Setup
if True:
    import customtkinter as ctk 
    import tkinter.messagebox as tkmb 


    # Selecting GUI theme - dark, light , system (for system default) 
    ctk.set_appearance_mode("dark") 

    # Selecting color theme - blue, green, dark-blue 
    ctk.set_default_color_theme("blue") 

    app = ctk.CTk() 
    app.geometry("400x400") 
    app.title("User Backlog Program") 

    frame = ctk.CTkFrame(master=app) 
    frame.pack(pady=20,padx=40,fill='both',expand=True) 

    label = ctk.CTkLabel(master=frame,text='User Login') 
    label.pack(pady=12,padx=10) 


    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
    user_entry.pack(pady=12,padx=10) 

    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
    user_pass.pack(pady=12,padx=10) 


    button = ctk.CTkButton(master=frame,text='Login',command=login) 
    button.pack(pady=12,padx=10) 

    button = ctk.CTkButton(master=frame,text='Register',command=register) 
    button.pack(pady=12,padx=10) 

    checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
    checkbox.pack(pady=12,padx=10) 

    app.mainloop()

#Password Retrieval
if True:
    print("Please input your username to retreive your password:")
    username_retrieval = input()
    print(kr.get_password("Backlog", username_retrieval))

#Login Attempts
if True:
    attempts = 0
    while attempts < 3:
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        if username == 'user123' and password == 'password123':
            print('You have successfully logged in.')
            break
        else:
            print('Incorrect credentials. Check if you have Caps lock on and try again.')
            attempts += 1
            continue
    else:
        print('You have been locked out of your account. Please contact the system administrator.')
        exit()