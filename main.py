<<<<<<< HEAD
# Import Flask module
from flask import Flask

# Create a new Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return "Hello, world!"

# Start the web server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
from tkinter import *
from tkinter import filedialog

def new_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", END))

root = Tk()
root.title("Notepad")
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
text = Text(root)
text.pack()
root.mainloop()
>>>>>>> 0b14453c97f68d20b94d2e128cbcd83b16074fe1
