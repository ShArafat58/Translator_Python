from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

def label_change():
    c = combol.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END).strip()
        if not text_:
            raise ValueError("No input text to translate")

        c2 = combol.get()
        c3 = combo2.get()

        translator = Translator()
        # Detect language of the input text
        detection = translator.detect(text_)
        source_lang = detection.lang

        # Find the target language code
        target_lang = None
        for key, value in language.items():
            if value == c3:
                target_lang = key
                break

        if target_lang is None:
            raise ValueError(f"Could not find language code for {c3}")

        # Translate text
        translated = translator.translate(text_, src=source_lang, dest=target_lang)
        text2.delete(1.0, END)
        text2.insert(END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

# Icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# Arrow
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# Languages
language = googletrans.LANGUAGES
languageV = list(language.values())

# Combobox for selecting languages
combol = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combol.place(x=110, y=20)
combol.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="salmon", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="salmon", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=460, y=350)

label_change()

root.configure(bg="coral")
root.mainloop()
