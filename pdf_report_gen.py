"""
-----------------------------------------------------------------------
PROJECT: Automated University Grade Report Generator
TASK: 02 (Automated Report Generation)
AUTHOR: Aditya Santosh Adhav
-----------------------------------------------------------------------
"""

import pandas as pd
from fpdf import FPDF

# --- CONFIGURATION ---
CSV_FILE = "student_scores.csv"
OUTPUT_FILENAME = "Class_Performance_Report.pdf"
PASS_MARK = 40

def analyze_data(df):
    """
    Calculates Total, Average, Grade, and Status for each student.
    """
    # 1. Calculate Total and Average
    df['Total'] = df['Maths'] + df['Science'] + df['English']
    df['Average'] = df['Total'] / 3

    # 2. Determine Grade and Status (Pass/Fail)
    grades = []
    statuses = []
    
    for avg in df['Average']:
        if avg >= 90: grades.append("A+")
        elif avg >= 80: grades.append("A")
        elif avg >= 60: grades.append("B")
        elif avg >= 40: grades.append("C")
        else: grades.append("F")
        
        if avg >= PASS_MARK:
            statuses.append("PASS")
        else:
            statuses.append("FAIL")

    df['Grade'] = grades
    df['Status'] = statuses
    return df

class PDFReport(FPDF):
    def header(self):
        # Title
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'University Class Performance Report', 0, 1, 'C')
        self.ln(5)
        # Subtitle
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Automated Generated Report', 0, 1, 'C')
        self.line(10, 30, 200, 30) # Draw a line
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf(df):
    """
    Creates the formatted PDF using FPDF.
    """
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    # --- TABLE HEADER ---
    pdf.set_font("Arial", 'B', 10)
    pdf.set_fill_color(200, 220, 255) # Light Blue Background
    
    # Define column widths
    cols = [20, 40, 20, 20, 20, 20, 15, 20]
    headers = ["ID", "Name", "Math", "Sci", "Eng", "Avg", "Grd", "Status"]

    # Print Header Row
    for i in range(len(headers)):
        pdf.cell(cols[i], 10, headers[i], 1, 0, 'C', fill=True)
    pdf.ln()

    # --- TABLE ROWS ---
    pdf.set_font("Arial", size=10)
    
    for index, row in df.iterrows():
        # Choose color for Status (Green for Pass, Red for Fail)
        if row['Status'] == "FAIL":
            pdf.set_text_color(255, 0, 0) # Red
        else:
            pdf.set_text_color(0, 0, 0)   # Black

        # Print Data
        pdf.cell(cols[0], 10, str(row['RollNo']), 1, 0, 'C')
        pdf.cell(cols[1], 10, str(row['Name']), 1, 0, 'L')
        pdf.cell(cols[2], 10, str(row['Maths']), 1, 0, 'C')
        pdf.cell(cols[3], 10, str(row['Science']), 1, 0, 'C')
        pdf.cell(cols[4], 10, str(row['English']), 1, 0, 'C')
        pdf.cell(cols[5], 10, f"{row['Average']:.1f}", 1, 0, 'C')
        pdf.cell(cols[6], 10, str(row['Grade']), 1, 0, 'C')
        pdf.cell(cols[7], 10, str(row['Status']), 1, 1, 'C')

    # Reset text color
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    
    # --- SUMMARY SECTION ---
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Class Analysis Summary:", 0, 1)
    
    pdf.set_font("Arial", size=11)
    top_student = df.loc[df['Average'].idxmax()]
    avg_score = df['Average'].mean()
    
    pdf.cell(0, 8, f"1. Class Average Score: {avg_score:.2f}%", 0, 1)
    pdf.cell(0, 8, f"2. Top Performer: {top_student['Name']} ({top_student['Average']:.1f}%)", 0, 1)
    pdf.cell(0, 8, f"3. Total Students Processed: {len(df)}", 0, 1)

    # Save
    pdf.output(OUTPUT_FILENAME)
    print(f"Success! Report generated: {OUTPUT_FILENAME}")

def main():
    print("Reading data...")
    try:
        # Read the CSV
        df = pd.read_csv(CSV_FILE)
        
        print("Analyzing performance...")
        df_analyzed = analyze_data(df)
        
        print(df_analyzed) # Show in console
        
        print("Generating PDF report...")
        generate_pdf(df_analyzed)
        
    except FileNotFoundError:
        print(f"Error: Could not find {CSV_FILE}. Make sure it is in the same folder.")

if __name__ == "__main__":
    main()