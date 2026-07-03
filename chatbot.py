import random
import datetime
import difflib
import json
import os


class MemoryManager:
    FILE = "memory.json"

    def __init__(self):
        self.data = self.load()

    def load(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                return json.load(f)
        return {}

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key):
        return self.data.get(key)


class ChatBot:
    def __init__(self):
        self.memory = MemoryManager()

        # ---------------- INTENTS ----------------
        self.intents = {
            "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
            "bye": ["bye", "goodbye", "see you", "exit", "quit"],
            "how_are_you": ["how are you", "how are you doing"],
            "thanks": ["thanks", "thank you", "thx"],
            "name": ["your name", "who are you"],
            "help": ["help", "what can you do"],
            "time": ["time", "current time", "what time"],
            "joke": ["joke", "tell me a joke", "make me laugh"],
        }

        # ---------------- BIG KNOWLEDGE BASE ----------------
        self.knowledge = {
            # Python
            "python": "Python is a high-level programming language used in AI, web development, automation and data science.",
            "loop": "Loops are used to repeat code. Python has for loop and while loop.",
            "function": "Functions are reusable blocks of code defined using def keyword.",
            "list": "Lists store multiple items like [1,2,3]. They are mutable.",
            "dictionary": "Dictionaries store data in key-value pairs like {'a': 1}.",
            "oop": "OOP means Object-Oriented Programming using classes and objects.",
            "class": "Class is a blueprint for creating objects in Python.",

            # Tech
            "computer": "A computer is an electronic device that processes data.",
            "internet": "The internet is a global network connecting millions of computers.",
            "ai": "AI stands for Artificial Intelligence which allows machines to think and learn.",

            # General
            "india": "India is a country in South Asia known for culture and technology growth.",
            "earth": "Earth is the third planet from the Sun.",
            "sun": "The Sun is a star at the center of our solar system.",

            # Daily life
            "hello": "Hi there! How can I help you today?",
            "good morning": "Good morning! Have a productive day 😊",
            "good night": "Good night! Sleep well 🌙",
            "how are you": "I'm doing great! What about you?",
        }

        self.jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs 😄",
            "I told my computer to stop freezing… it didn’t listen 🥶",
            "Why do programmers hate nature? Too many bugs 🐛"
        ]

    # ---------------- INTENT ----------------
    def detect_intent(self, text):
        for intent, patterns in self.intents.items():
            for p in patterns:
                if p in text:
                    return intent
        return None

    # ---------------- MEMORY ----------------
    def handle_memory(self, text):
        if "my name is" in text:
            name = text.split("my name is")[-1].strip().title()
            self.memory.set("name", name)
            return f"Nice to meet you, {name}!"

        if "what is my name" in text:
            name = self.memory.get("name")
            return f"Your name is {name}" if name else "I don't know your name yet."

        return None

    # ---------------- SMART SEARCH ----------------
    def smart_search(self, text):
        keys = list(self.knowledge.keys())
        match = difflib.get_close_matches(text, keys, n=1, cutoff=0.5)

        if match:
            return self.knowledge[match[0]]

        # keyword partial match (better than before)
        for key in self.knowledge:
            if key in text:
                return self.knowledge[key]

        return None

    # ---------------- RESPONSE ENGINE ----------------
    def get_response(self, user_input):
        text = user_input.lower().strip()

        # memory
        mem = self.handle_memory(text)
        if mem:
            return mem

        # time
        if "time" in text:
            return datetime.datetime.now().strftime("Current time: %H:%M:%S")

        # joke
        if "joke" in text:
            return random.choice(self.jokes)

        # intent
        intent = self.detect_intent(text)

        if intent == "greeting":
            return random.choice(["Hello! 👋", "Hi there!", "Hey!"])

        if intent == "how_are_you":
            return "I'm doing great! What about you?"

        if intent == "thanks":
            return "You're welcome! 😊"

        if intent == "name":
            return "I'm a smart rule-based chatbot built with Python."

        if intent == "help":
            return "I can answer questions about Python, general knowledge, and daily chat."

        if intent == "bye":
            return "Goodbye! 👋"

        # knowledge base
        answer = self.smart_search(text)
        if answer:
            return answer

        # final fallback
        return "Sorry, I don't know that yet. Try asking about Python, tech, or general topics."

    # ---------------- CHAT LOOP ----------------
    def chat(self):
        print("=" * 55)
        print("🤖 Chatbot")
        print("Type 'bye' to exit")
        print("=" * 55)

        while True:
            user_input = input("\nYou: ")

            if not user_input.strip():
                print("Bot: Please type something.")
                continue

            response = self.get_response(user_input)
            print("Bot:", response)

            if "bye" in user_input.lower():
                break


if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()