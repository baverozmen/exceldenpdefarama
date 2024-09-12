import pandas as pd
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def select_pdf():
    pdf_path = filedialog.askopenfilename(title="PDF dosyasını seçin", filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, pdf_path)

def select_excel():
    excel_path = filedialog.askopenfilename(title="Excel dosyasını seçin", filetypes=[("Excel files", "*.xlsx")])
    if excel_path:
        excel_entry.delete(0, tk.END)
        excel_entry.insert(0, excel_path)

def search_pdf_excel():
    try:
        pdfDoc = pdf_entry.get()
        exceldosyası = excel_entry.get()
        sütun = column_entry.get()
        aranan_kelime = term_entry.get()
        arananYer = arananYer_entry.get()

        with open(pdfDoc, 'rb') as pdf:
            read = PyPDF2.PdfReader(pdf)
            m = ''
            for page in read.pages:
                m += page.extract_text()

        dosya = pd.read_excel(exceldosyası)

        if sütun not in dosya.columns:
            messagebox.showerror("Hata", "Geçersiz sütun adı.")
            return

        sd = dosya[dosya[sütun] == aranan_kelime]

        if sd.empty:
            result_text.set(f"Excel dosyasında '{aranan_kelime}' bulunamadı.")
            return

        if arananYer == "n":
            result = ""
            for a in sd[sütun]:
                result += f"Bulundu! {a}\n" if str(a) in m else f"{a} bulunamadı.\n"
            result_text.set(result)
        else:
            z = sd[arananYer]
            result = ""
            for a in z:
                result += f"Bulundu! {a} girmiş\n" if str(a) in m else f"{a} numara bulunamadı.\n"
            result_text.set(result)

    except Exception as e:
        messagebox.showerror("Hata", f"Hata oluştu: {e}")

root = tk.Tk()
root.title("PDF-Excel Arama Aracı")

pdf_label = tk.Label(root, text="PDF dosyası:")
pdf_label.grid(row=0, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)
pdf_button = tk.Button(root, text="Gözat", command=select_pdf)
pdf_button.grid(row=0, column=2, padx=10, pady=10)

excel_label = tk.Label(root, text="Excel dosyası:")
excel_label.grid(row=1, column=0, padx=10, pady=10)
excel_entry = tk.Entry(root, width=50)
excel_entry.grid(row=1, column=1, padx=10, pady=10)
excel_button = tk.Button(root, text="Gözat", command=select_excel)
excel_button.grid(row=1, column=2, padx=10, pady=10)

column_label = tk.Label(root, text="Sütun:")
column_label.grid(row=2, column=0, padx=10, pady=10)
column_entry = tk.Entry(root, width=50)
column_entry.grid(row=2, column=1, padx=10, pady=10)

term_label = tk.Label(root, text="Aranan kelime:")
term_label.grid(row=3, column=0, padx=10, pady=10)
term_entry = tk.Entry(root, width=50)
term_entry.grid(row=3, column=1, padx=10, pady=10)

arananYer_label = tk.Label(root, text="diger aramalar (örn: n):")
arananYer_label.grid(row=4, column=0, padx=10, pady=10)
arananYer_entry = tk.Entry(root, width=50)
arananYer_entry.grid(row=4, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Sonuçlar:")
result_label.grid(row=5, column=0, padx=10, pady=10)
result_text = tk.StringVar()
result_output = tk.Label(root, textvariable=result_text, width=60, height=10, anchor="nw", justify="left")
result_output.grid(row=5, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Ara", command=search_pdf_excel)
search_button.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()