import asyncio
import certifi
import os
import tkinter as tk
from tkinter import filedialog
from werk24 import Hook, W24TechreadClient, W24AskVariantMeasures

# Set the SSL certificate
os.environ['SSL_CERT_FILE'] = certifi.where()

def get_drawing_bytes(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

async def print_measures_of_drawing(drawing_bytes):
    hooks = [Hook(ask=W24AskVariantMeasures(), function=print)]
    async with W24TechreadClient.make_from_env() as session:
        await session.read_drawing_with_hooks(drawing_bytes, hooks)

def select_file():
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)

def process_file():
    drawing_file = file_path_label.cget("text")
    drawing_bytes = get_drawing_bytes(drawing_file)
    asyncio.run(print_measures_of_drawing(drawing_bytes))

# Create the main window
root = tk.Tk()
root.title("Werk24 Drawing Reader")

# Add a label and button to select a file
file_path_label = tk.Label(root, text="No file selected")
file_path_label.pack()
select_button = tk.Button(root, text="Select Drawing", command=select_file)
select_button.pack()

# Add a button to process the file
submit_button = tk.Button(root, text="Process Drawing", command=process_file)
submit_button.pack()

# Run the application
root.mainloop()