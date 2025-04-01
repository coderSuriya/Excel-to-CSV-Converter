import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def split_excel_to_csv(excel_file, output_dir="csv_output"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the Excel file
    xls = pd.ExcelFile(excel_file)
    
    # Iterate through each sheet and save as CSV
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        csv_filename = os.path.join(output_dir, f"{sheet_name}.csv")
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')  # Use utf-8-sig for proper encoding
        print(f"Saved: {csv_filename}")
    
    messagebox.showinfo("Success", "Excel file has been successfully split into CSV files.")

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    excel_file = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if not excel_file:
        return
    
    output_dir = filedialog.askdirectory(title="Select Output Folder")
    if not output_dir:
        return
    
    split_excel_to_csv(excel_file, output_dir)

if __name__ == "__main__":
    select_file()
