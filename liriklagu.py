import sys
import time

def lirik_lagu ():
    lirik = [
        ("Sudah tahu hanya sepihak rindu", 0.15),
        ("Masih coba lempar dadu peruntunganku", 0.16), 
        ("Gegabah nomor satu", 0.14), 
        ("Paling-paling menangis seperti dulu", 0.13), 
        ("Lagu lama yang aku tahu uh-uh-uh-uh", 0.225), 
        ("Lupa buta atau ku batu", 0.22), 
    ]
    
    delay = [0.8, 0.7, 0.4, 1.0, 3.9, 1.9,]
    print("\n== Lampu Kuning - Juicy Luicy ==\n")
    time.sleep(1.5)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter , end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("\n Code By Ganendra Deniartra")

lirik_lagu()