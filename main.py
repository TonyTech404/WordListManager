import pandas as pd
import tkinter as tk

root = tk.Tk()
root.title("Word List Manager")
root.geometry("410x600")

df = pd.DataFrame()


def read_csv_file():
    global df
    file_path = file_entry.get()
    df = pd.read_csv(file_path, header=None, names=["Word"])
    df = df.sort_values("Word")
    word_listbox.delete(0, tk.END)
    for index, row in df.iterrows():
        word_listbox.insert(tk.END, row["Word"])


def search_word():
    search_term = search_entry.get()
    search_results_listbox.delete(0, tk.END)
    search_df = df[df["Word"].str.contains(search_term, case=False)]
    for index, row in search_df.iterrows():
        search_results_listbox.insert(tk.END, row["Word"])


def add_word():
    global df
    new_word = add_entry.get().strip()
    if new_word != "":
        df = pd.concat([df, pd.DataFrame({"Word": [new_word]})], ignore_index=True)
        df = df.sort_values("Word")
        word_listbox.delete(0, tk.END)
        for index, row in df.iterrows():
            word_listbox.insert(tk.END, row["Word"])
        add_entry.delete(0, tk.END)


def remove_word():
    global df
    selected_word = word_listbox.get(word_listbox.curselection())
    df = df[df["Word"] != selected_word]
    word_listbox.delete(tk.ACTIVE)


file_label = tk.Label(root, text="File:")
file_entry = tk.Entry(root)
read_file_button = tk.Button(root, text="Read File", command=read_csv_file)

search_label = tk.Label(root, text="Search:")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_word)
search_results_listbox = tk.Listbox(root, width=30, height=5, font=("Arial", 12), borderwidth=2, relief="groove")

add_label = tk.Label(root, text="Add:")
add_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add", command=add_word)

remove_button = tk.Button(root, text="Remove", command=remove_word)
word_listbox = tk.Listbox(root, width=30, height=25, font=("Arial", 12), borderwidth=2, relief="groove")

file_label.grid(row=0, column=0, padx=2, pady=2)
file_entry.grid(row=0, column=1, padx=2, pady=2)
read_file_button.grid(row=0, column=2, padx=2, pady=2)

search_label.grid(row=1, column=0, padx=2, pady=2)
search_entry.grid(row=1, column=1, padx=2, pady=2)
search_button.grid(row=1, column=2, padx=2, pady=2)
search_results_listbox.grid(row=2, column=1, padx=2, pady=2)

add_label.grid(row=3, column=0, padx=2, pady=2)
add_entry.grid(row=3, column=1, padx=2, pady=2)
add_button.grid(row=3, column=2, padx=2, pady=2)

remove_button.grid(row=4, column=0, padx=2, pady=2)
word_listbox.grid(row=5, column=1, padx=2, pady=2)


root.mainloop()
