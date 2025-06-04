import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import scrolledtext, messagebox

def analyze_titanic():
    try:
        file_path = 'tested.csv'
        df = pd.read_csv(file_path)
        required_cols = {'Survived', 'Sex', 'Pclass', 'Age', 'Embarked'}
        if not required_cols.issubset(df.columns):
            raise ValueError(f"CSV missing required columns: {required_cols - set(df.columns)}")

        df['Survived'] = df['Survived'].astype(int)
        df['Age'] = df['Age'].fillna(df['Age'].median())
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

        total_passengers = len(df)
        total_survived = df['Survived'].sum()
        survival_rate = total_survived / total_passengers * 100

        male_survival = df[df['Sex'] == 'male']['Survived'].mean() * 100
        female_survival = df[df['Sex'] == 'female']['Survived'].mean() * 100

        pclass_survival = df.groupby('Pclass')['Survived'].mean() * 100

        ages = df['Age'].values
        mean_age = np.mean(ages)
        median_age = np.median(ages)
        std_age = np.std(ages)

        avg_survivor_age = np.mean(df[df['Survived'] == 1]['Age'])
        avg_non_survivor_age = np.mean(df[df['Survived'] == 0]['Age'])

        text_area.config(state='normal')
        text_area.delete(1.0, tk.END)

        # Title
        text_area.insert(tk.END, "🚢 Titanic Survival Report\n\n", "title")

        # Overall stats
        text_area.insert(tk.END, f"Total Passengers: ", "header")
        text_area.insert(tk.END, f"{total_passengers}\n")
        text_area.insert(tk.END, f"Total Survivors: ", "header")
        text_area.insert(tk.END, f"{total_survived}\n")
        text_area.insert(tk.END, f"Overall Survival Rate: ", "header")
        text_area.insert(tk.END, f"{survival_rate:.2f}%\n\n")

        # Gender survival
        text_area.insert(tk.END, f"👨 Male Survival Rate: ", "header")
        text_area.insert(tk.END, f"{male_survival:.2f}%\n")
        text_area.insert(tk.END, f"👩 Female Survival Rate: ", "header")
        text_area.insert(tk.END, f"{female_survival:.2f}%\n\n")

        # Class survival
        text_area.insert(tk.END, "📊 Survival Rate by Class:\n", "header")
        for cls, rate in pclass_survival.items():
            text_area.insert(tk.END, f"  Class {cls}: ", "subheader")
            text_area.insert(tk.END, f"{rate:.2f}%\n")

        # Age statistics
        text_area.insert(tk.END, "\n📈 Age Statistics:\n", "header")
        text_area.insert(tk.END, f"  Mean Age: ", "subheader")
        text_area.insert(tk.END, f"{mean_age:.2f}\n")
        text_area.insert(tk.END, f"  Median Age: ", "subheader")
        text_area.insert(tk.END, f"{median_age:.2f}\n")
        text_area.insert(tk.END, f"  Std Deviation: ", "subheader")
        text_area.insert(tk.END, f"{std_age:.2f}\n\n")

        text_area.insert(tk.END, f"Average Age of Survivors: ", "header")
        text_area.insert(tk.END, f"{avg_survivor_age:.2f}\n")
        text_area.insert(tk.END, f"Average Age of Non-Survivors: ", "header")
        text_area.insert(tk.END, f"{avg_non_survivor_age:.2f}\n")

        text_area.config(state='disabled')
        status_var.set(f"Analysis completed on '{file_path}'")

    except FileNotFoundError:
        messagebox.showerror("Error", "File 'tested.csv' not found.")
        status_var.set("Error: File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")
        status_var.set("Error during analysis.")

def clear_text():
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    text_area.config(state='disabled')
    status_var.set("Ready")

def exit_app():
    root.destroy()

# --- Tkinter window setup ---
root = tk.Tk()
root.title("Titanic Survival Analysis")

root.geometry('650x520')
root.resizable(False, False)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_run = tk.Button(frame_buttons, text="Run Analysis", width=15, bg="#4CAF50", fg="white", command=analyze_titanic)
btn_run.pack(side='left', padx=10)

btn_clear = tk.Button(frame_buttons, text="Clear", width=15, bg="#f44336", fg="white", command=clear_text)
btn_clear.pack(side='left', padx=10)

btn_exit = tk.Button(frame_buttons, text="Exit", width=15, bg="#555555", fg="white", command=exit_app)
btn_exit.pack(side='left', padx=10)

text_area = scrolledtext.ScrolledText(root, width=75, height=25, font=("Consolas", 11), state='disabled')
text_area.pack(padx=10, pady=10)

# Define tags and their styles
text_area.tag_config("title", foreground="#003366", font=("Consolas", 14, "bold"))
text_area.tag_config("header", foreground="#006400", font=("Consolas", 12, "bold"))
text_area.tag_config("subheader", foreground="#228B22", font=("Consolas", 11, "italic"))

status_var = tk.StringVar(value="Ready")
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor='w', fg="red")
status_bar.pack(side='bottom', fill='x')

root.mainloop()
