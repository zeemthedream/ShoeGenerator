import tkinter as tk
from tkinter import font as tkfont
import random
import os
from PIL import ImageTk, Image #make sure to import this library


class ShoeGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.count = 3 #timer
        self.myfont = tkfont.Font(family='arial', size=30, weight='bold', slant='italic')


    def start(self):
        self.create_screen()

    def create_screen(self):
        self.root.title("Shoe of the Day")
        canvas = tk.Canvas(self.root, width=600, height=600, bd=7)
        canvas.pack()

        background_img = tk.PhotoImage(file='') #enter file and make sure img is a png file in the same directory as this python file
        background = tk.Label(self.root, image=background_img)
        background.place(relwidth=1, relheight=1)

        frame = tk.Frame(self.root)
        frame.place(relx=0.1, rely=0.1, relwidth= 0.8, relheight=0.65)

        button_frame = tk.Frame(self.root, bd=7)
        button_frame.place(relx= 0.5, rely=0.8, relwidth=0.4, relheight=0.075, anchor='n')

        generate_button = tk.Button(button_frame, text='Generate Shoes', command=self.button_action, font=self.myfont)
        generate_button.pack()

        self.root.mainloop()

    def button_action(self):
        if self.count != 0: #while counter is still going
            frame = tk.Label(self.root, text=str(self.count), font=self.myfont)
            frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.65)
            self.count -= 1
            self.root.after(1000,self.button_action)
        else: #when counter is finished
            #getting a random shoe to choose
            shoe_folder = r'' #enter path of this shoe folder
            shoe_list = os.listdir(shoe_folder)
            index = random.randint(0, len(shoe_list)-1)
            while shoe_list[index] == ".Ds_Store":
                index = random.randint(0, len(shoe_list) - 1)

            #opening the image on the tkinter window
            shoe_image = Image.open(r'/{}'.format(shoe_list[index])) #enter the shoe folder path
            shoe_image = shoe_image.resize((450, 350), Image.ANTIALIAS) #resizing to fit in shoe box
            shoe = ImageTk.PhotoImage(shoe_image)

            chosen_shoe = tk.Label(self.root, image=shoe)
            chosen_shoe.image = shoe    #this is to set image on window
            chosen_shoe.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.65)
            self.count = 3

shoeGen = ShoeGenerator()
shoeGen.start()





















