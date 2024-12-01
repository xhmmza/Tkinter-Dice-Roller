import tkinter as tk
import random
def roll_dice():
    dice_value = random.randint(1, 6)
    result_label.config(text=f"🎲 {dice_value}")
root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x200")  
result_label = tk.Label(root, text="🎲 Roll the Dice!", font=("Arial", 24))
result_label.pack(pady=20)
roll_button = tk.Button(root, text="Roll", font=("Arial", 18), command=roll_dice)
roll_button.pack(pady=10)
root.mainloop()
