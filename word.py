from tkinter import *
import random

window = Tk()

window.title("Random generated words")
window.geometry("500x500")
window.config(background="yellow")

label = Label(window)

def random_word():
    
    alpha_list = ['A' , 'B' , ' C ',  'D ',  'E' , ' F ' ,  'G ' , 'H' , ' I' , ' J ' , 'K '  ,'L' , ' M' , ' N'  , ' O' , ' P' , ' Q ' , ' R'  , ' S ' , 'T' , ' U' , ' V' , ' W' , ' X'  , ' Y' , ' Z']


    alpha_list.place(relx = 0.5 , rely= 0.5 , anchor = CENTER )

    random_no1 = random.randint(1 , 5)
    random_no2 = random.randint(1 ,7)
    random_no3 = random.randint(1 , 15)
    random_no4 = random.randint(1 , 8)
    random_no5 = random.randint(1 , 20)

    alpha_random1 = alpha_list[random_no1]
    alpha_random2 = alpha_list[random_no2]
    alpha_random3 = alpha_list[random_no3]
    alpha_random4 = alpha_list[random_no4]
    alpha_random5 = alpha_list[random_no5]

    label["text"]= alpha_random1 + alpha_random2 + alpha_random3 + alpha_random4 + alpha_random5


btn = Button(window , text = "Generate Random Words" , command = random_word)
btn.place(relx=0.5 , rely=0.7 , anchor=CENTER)








window.mainloop()