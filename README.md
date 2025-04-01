# Excel to CSV Converter

This Python script allows you to convert an Excel file (.xlsx/.xls) into multiple CSV files, with each sheet saved as a separate CSV file. It features a simple graphical user interface (GUI) for easy file selection.

## Features
- Splits each sheet from an Excel file into individual CSV files
- User-friendly GUI for file selection
- Supports UTF-8 encoding to maintain special characters
- Saves CSV files in a user-specified directory

## Requirements
Ensure you have Python installed. The required Python libraries are:
- `pandas`
- `tkinter`

You can install missing dependencies using:
```sh
pip install pandas
```

## How to Use
1. Run the script:
   ```sh
   python script.py
   ```
2. A file dialog will appear. Select the Excel file you want to convert.
3. Choose an output directory where the CSV files will be saved.
4. The script will process the file and save each sheet as a separate CSV.
5. A success message will be displayed after completion.

## Repository Setup
To clone this repository:
```sh
git clone https://github.com/YOUR-USERNAME/Excel-to-CSV-Converter.git
cd Excel-to-CSV-Converter
```

To update the repository with changes:
```sh
git add .
git commit -m "Updated script"
git push origin main
```

## License
This project is licensed under the MIT License.

---
Developed by [Your Name]

