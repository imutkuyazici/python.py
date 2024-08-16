import os

def sag_yıldız():


    terminal_width = os.get_terminal_size().columns

    yildiz_sayisi = 10

    for i in range(yildiz_sayisi):
        print(" " * (terminal_width - 1) + "*")

sag_yıldız()

