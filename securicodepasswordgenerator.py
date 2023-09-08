from tkinter import *
import random

def show_pw():
  pw = ""
  special_chars = ["!", "@", "#", "$", "%", "^", "&", "*"]
  uppercase_letters = [
      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
      "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
  ]
  lowercase_letters = [
      "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
      "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
  ]

  if numbers_var.get() == "checked":
    random_num = str(random.randint(0, 9))
    pw += random_num
  if special_char_var.get() == "checked":
    random_char = random.choice(special_chars)
    pw += random_char
  if upper_var.get() == "checked":
    random_upper = random.choice(uppercase_letters)
    pw += random_upper
  if lower_var.get() == "checked":
    random_lower = random.choice(lowercase_letters)
    pw += random_lower

  #add extra characters to meet length requirement
  missing = length_var.get() - len(pw)
  for x in range(missing):
    pw += random.choice(lowercase_letters)

  #shuffle all characters
  char_list = list(pw)
  random.shuffle(char_list)
  pw_string = ''.join(char_list)
  pw_display_var.set(pw_string)

def hide_pw():
  pw_display_var.set(str("*****"))

def save_pw():
  global password_list

  new_pw = pw_display_var.get()

  if new_pw != "" and new_pw != "*****":
    password_list.append(new_pw)
    password_var.set(password_list)
    
    pw_display_var.set("")
    
    password_listbox.selection_clear(0,len(password_list))
    password_listbox.selection_set(len(password_list)-1)
                                    
def delete_pw():
  global password_list
  index = password_listbox.curselection()[0]
  password_list.pop(index)
  password_var.set(password_list)

root = Tk()
root.title("Securicode: Password Generator")
mainframe = Frame(root, padx=30, pady=50, background = "#595358") 
mainframe.pack_propagate(False) 
criteria_frame = Frame(mainframe,
                       highlightthickness=0, highlightbackground="#F1F7ED", bg="#595358")
image = PhotoImage(file="C:/Users/anuny/Downloads/lock.png")
image = image.subsample(4)
global password_list

#widgets
image1_label = Label(mainframe, image=image, bg="#595358")
image2_label = Label(mainframe, image=image, bg="#595358")
securicode_var = StringVar()
securicode_var.set("securicode")
securicode_label = Label(mainframe,fg = "white", background="#595358", textvariable=securicode_var,
                         font=("Arial", 30))

subline_var = StringVar()
subline_var.set("your free customizable password generator!")
subline_label = Label(mainframe, textvariable=subline_var, font=("Arial", 10), fg = "white", background="#595358")

pw_display_var = StringVar()
pw_display_var.set(str("*****"))
pw_display_label = Label(mainframe, width=30, textvariable=pw_display_var, fg = "white", background="#595358", font=("Arial", 10), highlightthickness=1)

length_var = IntVar()
length_scale = Scale(mainframe,
                     from_=4,
                     to=30,
                     variable=length_var,
                     orient=HORIZONTAL,
                     width=20,
                     length=220, fg = "white", highlightthickness=0, background="#595358", troughcolor="#F1F7ED", activebackground = "#595358")

length_label = Label(mainframe, text="Length", fg = "white", background="#595358")
criteria_label = Label(mainframe, text="Criteria", fg = "white", background="#595358")

numbers_var = StringVar()
numbers_var.set("unchecked")
numbers_check = Checkbutton(criteria_frame,
                            text="numbers",
                            variable=numbers_var,
                            onvalue="checked",
                            offvalue="unchecked", bg="#595358", 
                    activebackground="#F1F7ED", 
                          fg="white", 
                          selectcolor="#595358", highlightthickness=0)

special_char_var = StringVar()
special_char_var.set("unchecked")
special_char_check = Checkbutton(criteria_frame,
                                 text="special characters", variable=special_char_var, onvalue="checked", offvalue="unchecked", bg="#595358", 
                    activebackground="#F1F7ED", 
                          fg="white", 
                          selectcolor="#595358", highlightthickness=0)

upper_var = StringVar()
upper_var.set("unchecked")
upper_check = Checkbutton(criteria_frame,
                          text="uppercase",
                          variable=upper_var,
                          onvalue="checked",
                          offvalue="unchecked",
                          bg="#595358", 
                    activebackground="#F1F7ED", 
                          fg="white", 
                          selectcolor="#595358", highlightthickness=0)

lower_var = StringVar()
lower_var.set("unchecked")
lower_check = Checkbutton(criteria_frame,
                          text="lowercase",
                          variable=lower_var,
                          onvalue="checked",
                          offvalue="unchecked", bg="#595358", 
                    activebackground="#F1F7ED", 
                          fg="white", 
                          selectcolor="#595358", highlightthickness=0)

show_button = Button(mainframe, text="SHOW", command=show_pw, bg="#595358", fg="white", activebackground="#F1F7ED")
hide_button = Button(mainframe, text="HIDE", command=hide_pw, bg="#595358", fg="white", activebackground="#F1F7ED")

save_button = Button(mainframe, text="SAVE", command=save_pw, bg="#595358", fg="white", activebackground="#F1F7ED")
delete_button = Button(mainframe, text="DELETE", command=delete_pw, bg="#595358", fg="white", activebackground="#F1F7ED")

password_list = ["safepassword1", "safepassword2"]
password_var = StringVar()
password_var.set(password_list)
password_listbox = Listbox(mainframe, listvariable = password_var, selectmode = SINGLE, background = "#595358", fg = "white", height=5,foreground="white", highlightcolor="#F1F7ED", relief="ridge")

#gridding
image1_label.grid(row = 1, column = 1, rowspan = 2)
image2_label.grid(row = 1, column = 3, rowspan = 2)

securicode_label.grid(row=1, column=2)
subline_label.grid(row=2, column=2, pady = 10, sticky = N)
length_scale.grid(row=3, column=2, sticky = N)
length_label.grid(row=3, column=1, pady = 10, sticky = S)
pw_display_label.grid(row=5, column=2, ipady = 20)
show_button.grid(row=5, column=1, ipadx = 20, ipady = 17)
hide_button.grid(row=5, column=3, ipadx = 20, ipady = 17, sticky=W)

criteria_label.grid(row=4, column=1, sticky=N, pady=15)
numbers_check.grid(row=1, column=1, sticky=W)
special_char_check.grid(row=2, column=1, sticky=W)
upper_check.grid(row=1, column=2, sticky=W)
lower_check.grid(row=2, column=2, sticky=W)

mainframe.grid(row=0, column=0)
criteria_frame.grid(row=4, column=2, pady = 15)
password_listbox.grid(row = 6, column = 2, pady = 10, ipadx = 55, ipady = 2)

save_button.grid(row = 6, column = 1, ipadx = 25, ipady = 30, sticky = N, pady = 10)
delete_button.grid(row = 6, column = 3, ipadx=13, ipady = 30, sticky = N, pady = 10)

root.mainloop()
