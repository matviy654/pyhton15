import tkinter as tk

clicks = 0
best_scores_file = "best_scores.txt"
best_scores = []

def load_best_scores():
    global best_scores
    try:
        with open(best_scores_file, "r") as file:
            lines = file.readlines()
            best_scores = [int(line.strip()) for line in lines]
    except FileNotFoundError:
        best_scores = []

def save_best_scores():
    with open(best_scores_file, "w") as file:
        for score in best_scores:
            file.write(f"{score}\n")

def update_best_scores(new_score):
    global best_scores
    best_scores.append(new_score)
    best_scores = sorted(best_scores, reverse=True)[:10]

def update_scores_listbox():
    scores_listbox.delete(0, tk.END)
    for score in best_scores:
        scores_listbox.insert(tk.END, score)

def on_click():
    global clicks
    clicks += 1
    score_label.config(text=f"Натискання: {clicks}")
    

    if len(best_scores) < 10 or clicks > best_scores[-1]:
        update_best_scores(clicks)
        save_best_scores()
        update_scores_listbox()
        best_score_label.config(text=f"Найкращий результат: {best_scores[0]}")

root = tk.Tk()
root.title("Clicker Game")

score_label = tk.Label(root, text="Натискання: 0", font=("Helvetica", 16))
score_label.pack(pady=10)

load_best_scores()
best_score_label = tk.Label(root, text=f"Найкращий результат: {best_scores[0] if best_scores else 0}", font=("Helvetica", 16))
best_score_label.pack(pady=10)

button = tk.Button(root, text="Натисни тут", font=("Helvetica", 16), command=on_click)
button.pack(pady=20)

scores_label = tk.Label(root, text="Топ 10 результатів:", font=("Helvetica", 16))
scores_label.pack(pady=10)

scores_listbox = tk.Listbox(root, font=("Helvetica", 14))
scores_listbox.pack(pady=10)
update_scores_listbox()

root.mainloop()
