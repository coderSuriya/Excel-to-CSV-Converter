import pandas as pd
import os

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

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Split an Excel file into multiple CSV files.")
    parser.add_argument("excel_file", help="Path to the Excel file")
    parser.add_argument("--output_dir", default="csv_output", help="Directory to save CSV files")
    
    args = parser.parse_args()
    split_excel_to_csv(args.excel_file, args.output_dir)
