from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shut_down():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg = "blue")

r_btn = Button(st, text = "Restart", font = ("times new roman", 20, "bold"),
               relief = RAISED, cursor = "plus", command = restart)
r_btn.place(x = 150, y = 60, height = 50, width = 200)

rt_btn = Button(st, text = "Restart Time", font = ("times new roman", 20, "bold"),
                relief = RAISED, cursor = "plus", command = restart_time)
rt_btn.place(x = 150, y = 170, height = 50, width = 200)

lg_btn = Button(st, text = "Log Out", font = ("times new roman", 20, "bold"),
                relief = RAISED, cursor = "plus", command = log_out)
lg_btn.place(x = 150, y = 270, height = 50, width = 200)

st_btn = Button(st, text = "Shut Down", font = ("times new roman", 20, "bold"),
                relief = RAISED, cursor = "plus", command = shut_down)
st_btn.place(x = 150, y = 370, height = 50, width = 200)




st.mainloop()