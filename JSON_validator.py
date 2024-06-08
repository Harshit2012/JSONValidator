import tkinter as tk
from tkinter import ttk, messagebox
import json

class JSONValidator:
    def __init__(self, root):
        self.root = root
        self.root.title("JSONValidator")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.heading_label = tk.Label(root, text="JSONValidator", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        self.heading_label.pack(pady=10)

        self.subheading_label = tk.Label(root, text="Paste your JSON below and click 'Lint JSON' to validate.", font=("Helvetica", 14), bg="#f0f0f0")
        self.subheading_label.pack(pady=5)

        self.json_text = tk.Text(root, height=10, width=70, font=("Helvetica", 12))
        self.json_text.pack(pady=10)

        self.progress = ttk.Progressbar(root, orient="horizontal", mode="determinate", maximum=100)
        self.progress.pack(fill=tk.X, padx=20, pady=10)
        self.progress["value"] = 0

        self.lint_button = tk.Button(root, text="Lint JSON", font=("Helvetica", 14), command=self.lint_json, bg="#4CAF50", fg="white", padx=10, pady=5)
        self.lint_button.pack(pady=20)

    def lint_json(self):
        json_data = self.json_text.get("1.0", tk.END).strip()
        self.progress["value"] = 0
        self.root.update_idletasks()

        try:
            self.progress["value"] = 50
            self.root.update_idletasks()
            parsed_json = json.loads(json_data)
            self.progress["value"] = 100
            self.root.update_idletasks()
            messagebox.showinfo("Success", "JSON is valid and well-formed.")
        except json.JSONDecodeError as e:
            self.progress["value"] = 100
            self.root.update_idletasks()
            messagebox.showerror("Error", f"Invalid JSON:\n{e}")

        self.progress["value"] = 0
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONValidator(root)
    root.mainloop()