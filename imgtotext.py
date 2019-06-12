import pytesseract
import cv2
from tkinter import *

frame = cv2.imread('image.jpg')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
frase = pytesseract.image_to_string(frame, lang='por')

janela = Tk()

lb = Label(janela, text=frase, font=('Times', 17) )
lb.pack(pady=int(janela.winfo_screenheight()/2)-100)

janela.state('zoomed')
janela.mainloop()
