from tkinter.filedialog import *
import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("Password.txt")]

file = askopenfilenames(filetypes = (("PDF Files", "*.pdf;"),("All files", "*.*")))

for password in tqdm(passwords,"Decrypting PDF"):
   try:
      with pikepdf.open("".join(file),password=password) as pdf:
         print("\n[+] Password found : ",password)
         break
   except pikepdf._qpdf.PasswordError as e :
      continue