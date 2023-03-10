import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import pic_input


def templateinput(vision):
    my_w = tk.Tk()
    my_w.geometry("1000x900")  # Size of the window 
    my_w.title('Template Upload')
    my_w['background'] = '#DFDDD1'
    my_font1=('Sans', 22, 'bold')

    def nextPage():
        my_w.destroy()
        pic_input.picinput(vision)


    def upload_file():
        f_types = [('Jpg Files', '*.jpg'),
        ('PNG Files','*.png'), ('Jpeg Files','*.jpeg')]   # type of files to select 
        filename = askopenfilename(multiple=False,filetypes=f_types)
        print(filename)
        vision.set_good_image(filename)  

    l1 = tk.Label(my_w,text='Upload Template Image',width=30,font=my_font1,bg= '#DFDDD1') 
    l1.place(relx=0.5, rely=0.1, anchor=CENTER) 
    b1 = tk.Button(my_w, text='Upload Files', font=('Sans', 22, 'bold'), padx=50, pady=20,command = lambda:upload_file())
    b1.place(relx=0.4, rely=0.5, anchor=CENTER)

    NextPage = tk.Button(my_w, text="Next Page", font=('Sans', 22, "bold"), padx=50, pady=20,command= lambda:nextPage())
    NextPage.place(relx=.75, rely=0.5, anchor=CENTER)
            
    my_w.mainloop()  # Keep the window open