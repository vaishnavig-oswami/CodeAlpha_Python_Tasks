import tkinter as tk
from tkinter import scrolledtext
import random

# Responses dictionary
chatbot_responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just code, but I'm running smoothly 😄",

    "what is your name": "I am CodeAlpha Bot, your Python assistant 🤖",
    "bye": "Goodbye! Have a nice day!",
    "thank you": "You're welcome!",
    "who created you": "I was created by a passionate coder during an internship.",
    "what is python": "Python is a popular programming language known for its simplicity.",
    "what can you do": "I can answer basic questions and simulate conversation!",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "what is ai": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines.",
    "what is your purpose": "I am here to assist you with your queries.",
    "who are you": "I am CodeAlpha Bot, a simple chatbot.",
    "how old are you": "I was created recently, so I'm quite young.",
    "what is the time": "I don't have a clock, but you can check your device's time.",
    "what is the date": "I don't track real-time dates, sorry.",
    "what is the weather": "I'm not connected to the internet, so I can't check the weather.",
    "can you help me": "Of course! Just ask your question.",
    "tell me about python": "Python is great for web development, data science, AI, and more.",
    "tell me about java": "Java is an object-oriented programming language, widely used in enterprise applications.",
    "how to learn programming": "Start with the basics, practice a lot, and build small projects.",
    "what is machine learning": "Machine learning is teaching computers to learn from data.",
    "what is data science": "Data science combines statistics, coding, and domain knowledge to extract insights.",
    "can you code": "I can't write code by myself, but I can help you understand code!",
    "do you like me": "Of course! I'm here to assist you.",
    "good morning": "Good morning! Hope you have a wonderful day.",
    "good night": "Good night! Sweet dreams.",
    "what are you doing": "I'm waiting to help you.",
    "motivate me": "Believe in yourself! You can achieve anything you set your mind to. 💪",
    "tell me a fun fact": "Did you know? Honey never spoils. Archaeologists found edible honey in ancient Egyptian tombs!",
    "give me a tip": "Stay consistent in your learning—small efforts every day lead to big results.",
    "how to start learning python": "Try online tutorials, interactive coding platforms, or books like 'Automate the Boring Stuff with Python'.",
}

# ChatBot App class
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 CodeAlpha AI ChatBot")
        self.root.geometry("650x700")
        self.root.configure(bg="#e8eaf6")

        # Title label
        self.title_label = tk.Label(
            root, text="💬 CodeAlpha AI ChatBot",
            font=("Helvetica", 22, "bold"),
            bg="#3f51b5", fg="white", pady=10
        )
        self.title_label.pack(fill="x")

        # Chat history area
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD,
            font=("Arial", 13),
            bg="white",
            state="disabled",
            relief="sunken",
            bd=2
        )
        self.chat_area.pack(padx=10, pady=10, fill="both", expand=True)

        # Input frame
        self.input_frame = tk.Frame(root, bg="#e8eaf6")
        self.input_frame.pack(padx=10, pady=10, fill="x")

        # Entry field
        self.entry = tk.Entry(
            self.input_frame, font=("Arial", 14)
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(
            self.input_frame, text="Send",
            font=("Arial", 12, "bold"),
            bg="#3f51b5", fg="white",
            padx=20, pady=5,
            command=self.send_message
        )
        self.send_button.pack(side="right")

        # Greet message
        self.insert_message("Bot", "Hi! I'm your assistant. How can I help you today?")

    def insert_message(self, sender, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_message = self.entry.get().strip()
        if not user_message:
            return

        self.insert_message("You", user_message)
        self.entry.delete(0, tk.END)

        # Process response
        lower_message = user_message.lower()
        response = chatbot_responses.get(
            lower_message,
            random.choice([
                "Sorry, I didn't understand that.",
                "Hmm, I'm not sure about that.",
                "Can you rephrase your question?",
                "I'm still learning. Try asking something else!"
            ])
        )
        self.insert_message("Bot", response)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
