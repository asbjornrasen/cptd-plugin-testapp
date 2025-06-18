
def run(argv):
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Тест CPTD", "✅ The program has been successfully installed as an application!")
    except Exception as e:
        print("[⛔] Error on startup tkinter:", e)
