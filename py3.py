import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import datetime
import os

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 290,
    "AMZN": 125
}

portfolio = {}
is_dark_mode = False

def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

def add_stock():
    stock = stock_entry.get().upper().strip()
    qty = qty_entry.get().strip()

    if not stock or not qty:
        messagebox.showwarning("Input Error", "Please enter both stock and quantity.")
        return

    if stock not in stock_prices:
        messagebox.showerror("Invalid Stock", f"'{stock}' is not in our stock list.\nAvailable: {', '.join(stock_prices.keys())}")
        return

    try:
        quantity = int(qty)
        if quantity < 0:
            messagebox.showerror("Invalid Quantity", "Quantity cannot be negative.")
            return
    except ValueError:
        messagebox.showerror("Invalid Quantity", "Please enter a valid integer quantity.")
        return

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    update_summary()
    stock_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)

def update_summary():
    summary_text.delete("1.0", tk.END)
    total = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = qty * price
        total += investment
        summary_text.insert(tk.END, f"{stock}: {qty} shares x ${price} = ${investment}\n")
    summary_text.insert(tk.END, "\n----------------------------\n")
    summary_text.insert(tk.END, f"💰 Total Investment: ${total}\n")
    summary_text.insert(tk.END, f"\n📅 {get_datetime()}")

def clear_portfolio():
    portfolio.clear()
    summary_text.delete("1.0", tk.END)

def save_to_csv():
    if not portfolio:
        messagebox.showinfo("Nothing to Save", "Portfolio is empty.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
        total = 0
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = qty * price
            total += investment
            writer.writerow([stock, qty, price, investment])
        writer.writerow(["", "", "TOTAL", total])
        writer.writerow(["", "", "DateTime", get_datetime()])

    messagebox.showinfo("Success", f"Portfolio saved to {file_path}")

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    bg = "#263238" if is_dark_mode else "#e1f5fe"
    fg = "white" if is_dark_mode else "black"
    title_bg = "#000000" if is_dark_mode else "#0288d1"

    root.configure(bg=bg)
    input_frame.configure(bg=bg)
    button_frame.configure(bg=bg)

    for widget in [title_label, *input_frame.winfo_children(), *button_frame.winfo_children()]:
        widget.configure(bg=bg, fg=fg)

    summary_text.configure(bg="black" if is_dark_mode else "white", fg="white" if is_dark_mode else "black")
    title_label.configure(bg=title_bg)

def show_help():
    help_text = (
        "📘 Instructions:\n"
        "- Enter Stock Symbol (e.g., AAPL) and Quantity.\n"
        "- Click 'Add to Portfolio' to record.\n"
        "- Use 'Save to CSV' to export.\n"
        "- 'Toggle Dark Mode' for dark/light themes.\n"
    )
    messagebox.showinfo("Help", help_text)

def confirm_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("📈 Simple Stock Portfolio Tracker")
root.geometry("550x700")
root.configure(bg="#e1f5fe")

title_label = tk.Label(root, text="📈 Stock Portfolio Tracker", font=("Helvetica", 20, "bold"), bg="#0288d1", fg="white", pady=10)
title_label.pack(fill="x")

welcome_label = tk.Label(root, text="Welcome! Start adding your stocks below.", font=("Helvetica", 12), bg="#e1f5fe")
welcome_label.pack()

input_frame = tk.Frame(root, bg="#e1f5fe")
input_frame.pack(pady=15)

tk.Label(input_frame, text="Stock Symbol:", font=("Helvetica", 12), bg="#e1f5fe").grid(row=0, column=0, padx=5, pady=5, sticky="e")
stock_entry = tk.Entry(input_frame, font=("Helvetica", 12))
stock_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Quantity:", font=("Helvetica", 12), bg="#e1f5fe").grid(row=1, column=0, padx=5, pady=5, sticky="e")
qty_entry = tk.Entry(input_frame, font=("Helvetica", 12))
qty_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add to Portfolio", font=("Helvetica", 12, "bold"), bg="#0288d1", fg="white", command=add_stock)
add_button.pack(pady=10)

summary_text = tk.Text(root, height=15, font=("Courier", 12), bg="white")
summary_text.pack(padx=10, pady=10, fill="both", expand=True)

button_frame = tk.Frame(root, bg="#e1f5fe")
button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Helvetica", 12), bg="#ff5252", fg="white", command=clear_portfolio)
clear_button.grid(row=0, column=0, padx=10)

save_button = tk.Button(button_frame, text="Save to CSV", font=("Helvetica", 12), bg="#43a047", fg="white", command=save_to_csv)
save_button.grid(row=0, column=1, padx=10)

theme_button = tk.Button(button_frame, text="Toggle Dark Mode", font=("Helvetica", 12), bg="#37474f", fg="white", command=toggle_theme)
theme_button.grid(row=1, column=0, columnspan=2, pady=5)

help_button = tk.Button(root, text="Help / Instructions", font=("Helvetica", 12), bg="#039be5", fg="white", command=show_help)
help_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), bg="#757575", fg="white", command=confirm_exit)
exit_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", confirm_exit)
root.mainloop()
