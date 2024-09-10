import pandas as pd
import numpy as np
import PyPDF2
import os
from platform import system
if system() == "Linux":
    os.system("clear")
pdfDoc = input("pdf dosyasını giriniz:")

with open(pdfDoc, 'rb') as pdf:
    read = PyPDF2.PdfReader(pdf)
    m = ''
    
    for page in read.pages:
        print(page.extract_text())
   

exceldosyası = input("excel dosyasını giriniz: ")
dosya = pd.read_excel(exceldosyası)
sütun = input("sütunu giriniz: ")
aranan_kelime = input("aranan kelimeyi giriniz : ")
sd = dosya[dosya[sütun] == aranan_kelime]


arananYer = input("eger girdiginiz kelimde örn: sınav listesi payaşılmış olsun ordan x bölümünde okuyan kişinin numarasını almak istiyorsunuz eger öyle bi şey istiyorsanız burdaki numara örneklemisendeki veriyi griniz (yoksa n diyiniz): ")
if arananYer == "n":
    for page in read.pages:
        m += page.extract_text()

    for a in sd:
        if a in list(m):
            
            print(f'bulundu!{a}')
        else:
            print(f'{a} bulunamadı.')
else:
    z= sd[arananYer]
    for page in read.pages:
        m += page.extract_text()
        
    for a in z:
        if a in list(m):
            
            print(f'bulundu!{a} girmiş')
        else:
            print(f'{a} numara bulunamadı.')