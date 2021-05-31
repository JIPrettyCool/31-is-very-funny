import string
import random
a = int(input("İlk Sayı: "))
b = int(input("İkinci Sayı: "))
final = a + b

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

komedi = random_char(21).upper()

if final == 31:
  print("{} + {} = {}".format(a,b,komedi))
else:
  print("{} + {} = {}".format(a,b,final))
