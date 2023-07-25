from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text pad')
# root.iconbitmap()
root.geometry('1200x660')

global open_status_name
open_status_name = False

global selected
selected = False

def  new_file():
    my_text.delete("1.0",END)
    root.title('New file - TextPad!')
    status_bar.config(text ='New File        ')
    
def open_file():
    my_text.delete("1.0", END)
    
    text_file = filedialog.askopenfilename(initialdir= "C:/gui/",title="open file", filetypes=(("Text Files","*.txt"),("HTML Files", ".*html"),("PYTHON Files",".*py"), ("ALL Files","*.*")))
    name = text_file
    status_bar.config(text= f'{name}'        )
    name = name.replace("C:/gui/","")
    root.title(f'{name} - TextPad!')
    
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
       
     
   
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/",title="Save File", filetypes=(("Text Files", "*.txt"),("HTML Files", "*.html"),("Python Files","*.py" ),("All Files","*.*")))
    
    if text_file:
       name = text_file
       status_bar.config(text = f'Saved {name}       ')
       name = name.replace("C:/gui/","")
       root.title(f'{name} - TextPad!')
       
       text_file = open(text_file, 'w')
       text_file.write(my_text.get(1.0, END))
       text_file.close()
       
def cut_text(e):
    global selected
    if my_text.selection_get():
     selected = my_text.selection_get()
    my_text.delete("sel.first", "sel.last")
               
                      
def copy_text(e):
    global selected
    
    if my_text.selection_get():
        selected = my_text.selection_get()
      
       
def paste_text(e):
    if selected:
        position = my_text.index(INSERT)
        my_text.insert(position, selected)       
              
       
my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(my_frame, width=97, height=25, font= ('Hevetica',16), selectbackground = 'lightgreen',selectforeground='black',undo= True, yscrollcommand = text_scroll.set)
my_text.pack()

text_scroll.config(command = my_text.yview)




my_menu = Menu(root)
root.config(menu= my_menu)

file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command= open_file)
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)


edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label= 'Cut', command=lambda:cut_text(False))
edit_menu.add_command(label= 'Copy',command=lambda: copy_text(False))
edit_menu.add_command(label= 'Paste',command=lambda:paste_text(False))



status_bar = Label(root,text= 'Ready', anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady= 5)

root.mainloop()