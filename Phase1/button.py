import tkinter as tk
import os
    
def write_slogan():
    os.system('export FLASK_APP=%s' % (tk.Entry.get(inputapp)))
    print("The app is %s " % (tk.Entry.get(inputapp)))
    os.system('flask run')

#def create_button():
window = tk.Tk()
frame = tk.Frame(window)
frame.pack()
window.title("Phase1")
window.geometry("100x100")

label = tk.Label(window, text = "Please enter the application to run in docker")
entry_var = tk.StringVar()
inputapp = tk.Entry(window,textvariable=entry_var)
inputapp.pack()



button = tk.Button(frame,
                    text="QUIT",
                    fg="red",
                    command=quit)
slogan = tk.Button(frame,
                    text="Build",
                    command=write_slogan)

label.pack()
button.pack()
slogan.pack()

print("Am I reaching here")
window.mainloop()

