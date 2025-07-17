import pandas as pd
import tkinter as tk 
from tkinter import filedialog, messagebox

def generate_report():
    filepath = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if not filepath:
        return

    try:
        df = pd.read_excel(filepath)
        df["Total"] = df["Quantity"] * df["Unit Price"]
        summary = df.groupby("Region")["Total"].sum().reset_index()

        output_path = "regional_sales_data.xlsx"
        summary.to_excel(output_path, index=False)

        messagebox.showinfo("Success!", f"Summary saved as:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

root = tk.Tk()
root.title("Sales Report Generator")

btn = tk.Button(root, text="Generate Report", command=generate_report, width = 25, height = 2)
btn.pack(padx = 20, pady = 30)

root.mainloop()