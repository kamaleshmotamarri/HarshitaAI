#Harshita AI
import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
from PIL import Image, ImageTk  
import google.generativeai as genai
import time


genai.configure(api_key="PUT YOUR API KEY HERE")



model = genai.GenerativeModel('gemini-1.5-flash')


def chat_with_bot(prompt):
    if prompt.lower().replace(" ", "")== "areyougoodatchemistry":
        return "NO Who you think I am 😂"
    elif prompt.lower().replace(" ", "")== "whoisyourcrush":
        return "I dont know ive had plenty in the past and Ill have more in the future."
    else:
        try:
            response = model.generate_content(prompt + " this ")
            return response.text
        except Exception as e:
            print(f"Error: {e}")  
            return "Sorry, I couldn't process your request."


def send_message():
    user_input = user_entry.get()
    print(f"User Input: {user_input}")  
    if user_input.lower() == 'exit':
        root.quit()
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        chat_window.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)
        
        bot_response = chat_with_bot(user_input)
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "Harshita AI: " + bot_response + "\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.see(tk.END)


root = tk.Tk()
root.title("Harshita AI")
image = Image.open(r"c:\Users\Kamalesh\Downloads\PHOTO-2025-01-13-21-00-01.jpg")  
image = image.resize((100, 100))  
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)  


chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_entry = tk.Entry(root, width=80)
user_entry.pack(padx=10, pady=10, side=tk.LEFT, expand=True, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)


root.mainloop()

