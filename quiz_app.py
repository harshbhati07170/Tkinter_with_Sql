import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
import random

all_questions = [
    {"question": "What is the SI unit of force?", "options": ["Newton", "Joule", "Pascal", "Watt"], "answer": "Newton"},
    {"question": "Who discovered gravity?", "options": ["Einstein", "Newton", "Tesla", "Edison"], "answer": "Newton"},
    {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Rajasthan ki rajdhani kya hai?", "options": ["Jaipur", "Jodhpur", "Udaipur", "Ajmer"], "answer": "Jaipur"},
    {"question": "हिंदी का पहला उपन्यास कौन सा था?", "options": ["गोदान", "चंद्रकांता", "सेवासदन", "कर्मभूमि"], "answer": "चंद्रकांता"},
    {"question": "What is H2O commonly known as?", "options": ["Water", "Oxygen", "Hydrogen", "Salt"], "answer": "Water"},
    {"question": "Which is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": "2"},
    {"question": "Rajasthan ka lok nritya kya hai?", "options": ["Ghoomar", "Bharatnatyam", "Kathak", "Odissi"], "answer": "Ghoomar"},
    {"question": "Who is known as the Father of Computers?", "options": ["Charles Babbage", "Alan Turing", "Tim Berners-Lee", "Steve Jobs"], "answer": "Charles Babbage"},
    {"question": "हिंदी दिवस कब मनाया जाता है?", "options": ["14 अगस्त", "15 अगस्त", "14 सितंबर", "2 अक्टूबर"], "answer": "14 सितंबर"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "Who invented the telephone?", "options": ["Bell", "Newton", "Tesla", "Edison"], "answer": "Bell"},
    {"question": "India’s national animal is?", "options": ["Elephant", "Tiger", "Lion", "Peacock"], "answer": "Tiger"},
    {"question": "What is the capital of India?", "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "answer": "New Delhi"},
    {"question": "Which festival is known as the festival of colors?", "options": ["Diwali", "Holi", "Eid", "Baisakhi"], "answer": "Holi"},
]

random.shuffle(all_questions)
questions = all_questions[:15]

score = 0
question_index = 0
timer_seconds = 20
progress = None
timer_running = False
user_name = ""

root = tk.Tk()
root.title("Smart Quiz App - Divyanshu Sahu")
root.geometry("1400x600")
root.resizable(False, False)

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

def start_timer():
    global timer_running
    timer_running = True
    for sec in range(timer_seconds):
        if not timer_running:
            return
        time.sleep(1)
        progress['value'] += 100 / timer_seconds
    timeout()

def show_login():
    global user_name
    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.config(bg="#222831")
    tk.Label(main_frame, text="🧠 Welcome to Quiz Master", font=("Arial", 32, "bold"),
             bg="#222831", fg="#00ADB5").pack(pady=40)
    tk.Label(main_frame, text="Enter your name", font=("Arial", 16), bg="#222831", fg="white").pack(pady=10)
    name_entry = tk.Entry(main_frame, font=("Arial", 16), width=30)
    name_entry.pack(pady=10)

    def proceed():
        global user_name
        entered = name_entry.get().strip()
        if not entered:
            messagebox.showwarning("Name Required", "Please enter your name to continue.")
            return
        user_name = entered
        show_welcome()

    tk.Button(main_frame, text="Continue ▶", font=("Arial", 18, "bold"), bg="#00ADB5", fg="white",
              padx=20, pady=10, command=proceed).pack(pady=30)

def show_welcome():
    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.config(bg="#393E46")
    tk.Label(main_frame, text=f"👋 Hello {user_name}!", font=("Arial", 26, "bold"), bg="#393E46", fg="#00ADB5").pack(pady=40)
    tk.Label(main_frame, text="Welcome to the Ultimate Quiz Challenge!", font=("Arial", 18),
             bg="#393E46", fg="white").pack(pady=10)
    tk.Button(main_frame, text="Start Quiz 🧠", font=("Arial", 20, "bold"), bg="#00ADB5", fg="white",
              padx=20, pady=10, command=start_quiz).pack(pady=40)

def start_quiz():
    global question_index, score
    question_index = 0
    score = 0
    show_question()

def show_question():
    global progress, timer_running
    for widget in main_frame.winfo_children():
        widget.destroy()
    question = questions[question_index]
    main_frame.config(bg="#222831")
    tk.Label(main_frame, text=f"Question {question_index+1}/{len(questions)}",
             font=("Arial", 20, "bold"), bg="#222831", fg="#00ADB5").pack(pady=20)
    tk.Label(main_frame, text=question['question'], font=("Arial", 22),
             wraplength=700, bg="#222831", fg="white").pack(pady=20)
    for option in question['options']:
        tk.Button(main_frame, text=option, font=("Arial", 18), width=30,
                  command=lambda opt=option: check_answer(opt)).pack(pady=5)
    progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
    progress.pack(pady=20)
    progress['value'] = 0
    threading.Thread(target=start_timer, daemon=True).start()

def check_answer(selected_option):
    global score, question_index, timer_running
    timer_running = False
    question = questions[question_index]
    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.config(bg="#222831")
    if selected_option == question['answer']:
        result = "Correct! ✅"
        score += 1
        color = "green"
    else:
        result = f"Wrong! ❌\nCorrect Answer: {question['answer']}"
        color = "red"
    tk.Label(main_frame, text=result, font=("Arial", 24, "bold"), bg="#222831", fg=color).pack(pady=40)
    tk.Button(main_frame, text="Next ▶", font=("Arial", 16), bg="#00ADB5", fg="white",
              command=next_question).pack(pady=20)

def timeout():
    global timer_running
    timer_running = False
    question = questions[question_index]
    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.config(bg="#222831")
    tk.Label(main_frame, text="⏰ Time's up!", font=("Arial", 24, "bold"),
             bg="#222831", fg="orange").pack(pady=40)
    tk.Label(main_frame, text=f"Correct Answer: {question['answer']}", font=("Arial", 20),
             bg="#222831", fg="white").pack(pady=10)
    tk.Button(main_frame, text="Next ▶", font=("Arial", 16), bg="#00ADB5", fg="white",
              command=next_question).pack(pady=20)

def next_question():
    global question_index
    question_index += 1
    if question_index < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.config(bg="#393E46")
    tk.Label(main_frame, text=f"✅ Quiz Completed, {user_name}!", font=("Arial", 30, "bold"),
             bg="#393E46", fg="#00ADB5").pack(pady=40)
    tk.Label(main_frame, text=f"{user_name}, your score is {score} / {len(questions)}",
             font=("Arial", 22), bg="#393E46", fg="white").pack(pady=10)
    tk.Button(main_frame, text="Play Again 🔁", font=("Arial", 16, "bold"), bg="#00ADB5", fg="white",
              command=start_quiz).pack(pady=20)
    tk.Button(main_frame, text="Exit ❌", font=("Arial", 16), bg="red", fg="white",
              command=root.destroy).pack(pady=10)

show_login()
root.mainloop()
