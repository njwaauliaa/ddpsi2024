import math
def l_kubus(s):
  hitung=6*s**2
  print(f"Luas kubus adalah {hitung}")

def l_balok(p, l, t):
  hitung=2*(p*l+p*t+l*t)
  print(f"Luas balok adalah {hitung}")

def l_limas_segitiga(la, ls):
  hitung=la+ls
  print(f"Luas limas segitiga adalah {hitung}")

def l_prisma(la, ls):
  hitung=(2*la)+ls
  print(f"Luas prisma adalah {hitung}")

def l_tabung(pi, r, t):
  hitung=2*pi*r*(r+t)
  print(f"Luas tabung adalah {hitung}")