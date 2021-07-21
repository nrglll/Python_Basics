# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:10:35 2020

@author: asus
"""

# %%

# class oluştur car, 
# attribute brand, speed, time
# method ekle getdistance hız*time
# constractor ekle dışarıdan attributeleri alacak 
# mercedes ... km/s gitti gibi yazsın
#

class Car(object):
    brand = "mercedes"
    speed = 100 #km
    time = 3 #hour
    
    def getDistance(self):
        sonuc = self.speed * self.time
        return sonuc
      

c1 = Car()
c1.getDistance()

c2 = Car()
c2.speed = 200 #km
print(c2.brand, c2.getDistance(), "km/sa yol gitti.")

# %% 

# 3 farklı cıktı olacak
# class olacak taksit miktarını hesaplayacak
# 


class Taksit(object):
    kreditutari = 1000
    faiz = 0.01 #%
    vade = 6
    
    def taksittutari(self):
       
        taksittutari = self.kreditutari * ((self.faiz*((1+self.faiz)**self.vade))/(((1+self.faiz)**self.vade)-1))
        
        return taksittutari
        
ing1 = Taksit()
ing1.faiz = 0.01

yapi1 = Taksit()
yapi1.faiz = 0.02

is1 = Taksit()
is1.faiz = 0.03

print("Almak istediğiniz kredinin aylık taksit tutarları bankalar için şu şekildedir:",
      "\nIng:", ing1.taksittutari(), 
      "\nYapıkredi:", yapi1.taksittutari(),
      "\nİş Bankası:", is1.taksittutari())


# %%
    
    
































