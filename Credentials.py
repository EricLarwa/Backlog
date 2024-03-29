import keyring as kr
attempts = 0
registered_users = {}
#Register Function

def register():
        username = user_entry.get()
        password = user_pass.get()
        registered_users[username] = password
        kr.set_password("Backlog",username,password)
        tkmb.showinfo(title="Registration Successful",message="You have registered a new user successfully. You may now login.")

#Login Function
def login(): 
        global attempts
        cred = kr.get_credential("Backlog","")
        username = cred.username
        password = cred.password

        while attempts < 5:
            if user_entry.get() == username and user_pass.get() == password: 
                onLogin()
                break

            elif user_entry.get() == username and user_pass.get() != password: 
                tkmb.showwarning(title='Wrong password',message='Please check your password')
                print(attempts)
                attempts += 1
                return attempts

            elif user_entry.get() != username and user_pass.get() == password: 
                tkmb.showwarning(title='Wrong username',message='Please check your username') 
                print(attempts)
                attempts += 1
                return attempts

            else: 
                tkmb.showerror(title="Login Failed",message="Invalid Username and password") 
                print(attempts)
                attempts += 1
                return attempts
        else:
            tkmb.showerror(title="Login Failed",message = 'You have been locked out of your account. Please contact the system administrator.')
            exit()

def onLogin():
    tkmb.showinfo(title="Login Successful",message="You have logged in Successfully") 
    new_window = ctk.CTkToplevel(app)
    new_window.title("New Window") 
    new_window.geometry("400x400")

#UI Interface Setup
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
