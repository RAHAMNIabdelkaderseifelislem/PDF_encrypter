from tkinter.filedialog import *
from PyPDF2 import PdfFileWriter,PdfFileReader 
import random
from random import randint

def encrypt(source):

    out = PdfFileWriter()

    file_path = "".join(source)
    file = PdfFileReader(file_path)

    num = file.numPages

    for i in range(num):
        page = file.getPage(i)
        out.addPage(page)
    
    password = passgen()

    out.encrypt(password)

    with open("encrypted_file.pdf", "wb") as f:
        out.write(f)


def passgen():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "&#{}()[]|-_ç@=+*/-.;!?$£,"
    all = lower + upper + numbers + symbols
    length = randint(8,32)
    print("Your Password Length :")
    print(length)
    password = "".join(random.sample(all,length))
    print("Your Password :")
    print(password)
    return password

source = askopenfilenames(filetypes = (("PDF Files", "*.pdf;"),("All files", "*.*")))

encrypt(source)