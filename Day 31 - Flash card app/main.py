from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
french_words = data.to_dict(orient="records")
current_card ={}


def next_card():
    global current_card
    current_card = random.choice(french_words)
    print(current_card["French"])
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])


def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word,text=current_card["English"])



window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

window.after(3000,func=flip_card)


canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150,text="French",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
button_right_img = PhotoImage(file="images/right.png")
button_wrong_img = PhotoImage(file="images/wrong.png")
button_right = Button(image=button_right_img, highlightthickness=0,command=next_card)
button_wrong = Button(image=button_wrong_img, highlightthickness=0,command=next_card)
button_right.grid(row=1,column=1)
button_wrong.grid(row=1,column=0)


next_card()

card_back = PhotoImage(file="images/card_back.png")








canvas.mainloop()