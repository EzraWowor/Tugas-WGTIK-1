#Bantulah Prof Stark dengan membuat sebuahprogram sederhana indexing nilai mahasiswa,dengan aturan sebegaiberikut:85 –100 -> A 80–84-> AB 75–79-> B 70–74-> BC 65–69-> C 0–65-> D

nilaikuliah=0;
while nilaikuliah!=1:
  print('masukan nilai : ')
  nilai = int(input())

  if nilai >=85: 
    print("A")
  elif nilai >=80:
    print("AB")
  elif nilai >=75:
    print("B")
  elif nilai >=70:
    print("BC")
  elif nilai >=65:
    print("C") 
  else:
    print("D")
  
  print(nilai)
  print(" 0. untuk lanjut indexing")
  print(" 1. untuk Berhenti indexing")
  nilaikuliah=int(input())