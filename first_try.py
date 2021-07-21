# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %%

a = 2 + 2 

b = [1,2,3,4]

print("hello world")

# %%

# integer = 10 
# string = "a" "futbol" "nurgul farugu seviyor"

string = "faruğun yaşı"
integer = 30


# %% classes

employee1_name = "faruk"
employee1_age = 30
employee1_address = "akdljs askjajla"


class Employee:
    #attribute = age,address,...
    #behavior = pass
    pass

Employee1 = Employee()

# %% attribute

class Footballer:
    
    club = "barcelona"
    age = 30
    pass

Footballer1 = Footballer()

print(Footballer.age)
print(Footballer.club)

# %% methods

class Square: 
    
    edge = 5 #meter
    area = 0 
    
    def area1(self):
        
        self.area = self.edge * self.edge #5*5
        
        print("New area:", self.area)

s1 = Square()

print(s1.area1())

s1.edge = 7 

print(s1.area1())

# %% methods vs functions

#method example

class Emp(object):
    
    age = 25
    salary = 1000 #pounds
    
    def agesalaryRatio(self):
        a = self.age/self.salary
        print("The ratio is",a,".")
         
e1 = Emp()
e1.agesalaryRatio()
    
# method classa bağımlı bir fonksiyonu tanımlar 
# function bağımsız bir fonksiyonu tanımlar 
# functionda değişkenlerini yazarız tanımlarken 

# function örnegi

def ageSalaryRatio(age, salary):
    a = age / salary
    print("The new ratio is",a,".")
    
    
ageSalaryRatio(30, 3000)

# dairenin alanı

def areaOfcircle(a,b):
    area = a * b ** 2
    # print("Area of the circle is", area)
    return area

pi = 3.14
r = 5

result1 = areaOfcircle(pi, r)

result2 = areaOfcircle(pi, 10) 

print(result1 + result2)


# %% initializer and constructor

#__init__ ile yeni bir method yazdık. 
#Bunu classın attributelerini tanımlamak için kullanacağız
#Sonrasında tanımladığımız objectlerin özellikleri buraya atanacak.

class Animal():

    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
    def getAge(self): 
        return self.age
    
    def getName(self):
        return self.name
    
    
a1 = Animal("dog", 2)
a2 = Animal("cat", 4)
a3 = Animal("bird", 3)

print("Hayvanların isimleri ve yaşları aşağıda verilmiştir:\n", 
      a1.getName(), ":", a1.getAge(), "\n",
      a2.getName(), ":", a2.getAge(), "\n",
      a3.getName(), ":", a3.getAge())

# %% calculator project

class Calc(object):
    
    def __init__(self, x, y):
        self.value1 = x
        self.value2 = y 
        
    def add(self):
        result1 = self.value1 + self.value2
        return result1
    
    def multiply(self):
        result2 = self.value1 * self.value2
        return result2
    
    def division(self):
       result3 = self.value1 / self.value2
       return result3
    
    def subtraction(self):
       result4 = self.value1 - self.value2
       return result4
        
   
selection = input("Please select 1 for Add or 2 for Multiply or 3 for Division or 4 for Subtraction: ")

if selection in ["1", "2", "3", "4"]:
    print("Continue")
else:
    print("Lütfen geçerli bir işlem seçiniz.")
   
v1 = int(input("Please enter first value: "))
v2 = int(input("please enter second value: "))

i1 = Calc(v1,v2)

if selection == "1":
    print("Toplama işleminin sonucu: {}'dir.".format(i1.add()))
elif selection == "2":
    print("Çarpma işleminin sonucu: {}'dir.".format(i1.multiply()))
elif selection == "3":
    print("Bölme işleminin sonucu: {}'dir.".format(i1.division()))
elif selection == "4":
    print("Çıkarma işleminin sonucu {}'dir.".format(i1.subtraction()))


# tam bitmedi. While, for vs. öğrenince tekrar bak. Düzenle. 
    
    
# %% encapsulation
    
# variable'a 2 tane alttan çizgi koyunca private oluyor.
# içerisindeki bilgiler dışarıdan görülemiyor ve değiştirilemiyor.  
# Böyle yapmadığımız tüm variablelar global oluyor.
    
    
# private variable alıp üzerinde değişiklik yapmak için 
# get ve set methodlarını kullanırım.Bunlar global methodlar.
# methodları da private yapabilmek için onların da başına 2 alttan çizgi koyulur.
    
class BankAccount(object):
    
    def __init__(self, name, money, address):
        self.name = name        #global
        self.__money = money     #private
        self.address = address
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
        
    def __increase(self):
        self.__money = self.money + 500
        
        
p1 = BankAccount("Faruk", 1000, "Gunnersbury")
p2 = BankAccount("Nurgul", 2000, "Halıcıoğlu")  

print(p1.__Money())

# %% inheritance

# inheritance daha önce yaratılan bir class içerisindeki 
# attribute veya methodları kullanarak yeni bir class yaratmaktır

# child class ve parent classlar var. 
#(super class parent class,child class subclass da deniyor)
# child class, parent classtan üretilmiş class oluyor
# parent class'tan istediğin kadar child class yaratabilirsin

#parent class
class Animal(object):
    
    def __init__(self):
        print("Animal is created.")

    def toString(self):
        print("Animal")
        
    def walk(self):
        print("Animals can walk.")

# parent classın ismini child classın içine yazıyorum.
# böylece içindekileri kullanabilirim bu classtada
#super() methodunda da parent classının initini kopyalamış 
# ve bu classtada kullanmış oldum. Direkt kullanacağın parentın adını da yazabilirsin.
# tüm hayvanların özelliği olmayan methodları (climb ve fly)
#child classında tanımlıyorum ayrıca.
# iki child classın birbiri ile ilişkisi olmaz.
# parentın childı baska bir childın parentı olabilir.
        
#child class
class Monkey(Animal):
    
    def __init__(self):
        super().__init__()
        print("Monkey is created.")
        
    def toString(self):
        print("Monkey")
        
    def climb(self):
        print("Monkey can climb.")
        
#child class
        
class Bird(Animal):
    
    def __init__(self):
        super().__init__()
        print("Bird is created.")
        
    def toString(self):
        print("Bird")

    def fly(self):
        print("Bird can fly.")
        

m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()

b1 = Bird()
b1.toString()
b1.walk()
b1.fly()

# %% inheritance project
    
# websitesi var isim ve soyisim gerektiriyor
# baska bir site id, baska bir site de email gerektiriyor.


class Website():
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
       
    def loginInfo(self):            
        print(self.name + " " + self.surname)
        
        
class Website1(Website):
    
    def __init__(self, name, surname, id):
        Website.__init__(self, name, surname) #buraya Website yazarak super() yerine spesifik konum belirttim.
        self.id = id
        
    def loginInfo(self):
        print(self.name + " " + self.surname + "-" + self.id)
        
class Website2(Website1):

    def __init__(self, name, surname, id, email):
        Website1.__init__(self, name, surname, id)
        self.email = email

    def loginInfo(self):
        print(self.name + " " + self.surname + "-" + self.id  + "-" + self.email)
        
    
        
w1 = Website("nurgul", "aygun")
w1.loginInfo()

w2 = Website1("nurgul", "aygun", "nrgl")
w2.loginInfo()

w3 =Website2("nurgul", "aygun", "nrgl", "nnnnnn@gmail")     
w3.loginInfo()
 
# %% abstract classes

# abstraxt classlar child classlar için şablon görevi görürler.
# nesne yönelimli programlarda nesnesi yaratılamayan sınıflara denirler
# kullanılacak ortak fonksiyonları kendi içlerinde tutarlar.
# abstract classlara kesinlikle object tanımlayamazsın. bu abstract class olma şartı
# bu classı yaratmak için python bir alt yapı sunmuyor ama open source old. için
# abc (abstract base class) ile abstract method decorater kullanacağız.
# ikinci abstract class olma koşulu ise abstracta yazılan methodların
# mutlaka child classlarda kullanılması.


from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def walk(): pass

    @abstractmethod
    def run(): pass
    
class Monkey(Animal):
    
    def __init__(self):
        print("monkey")
    
    def walk(self):
        print("walk")
        
    def run(self):
        print("run")
        
class Bird(Animal):
    
    def __init__(self):
        print("bird")
        
    def run(self):
        print("run")
        
    def walk(self):
        print("walk")

a1 = Monkey()
a1.walk()

a2 = Bird()
a2.run()


# %% overriding

# Aşağıdaki kodda görüldüğü gibi eğer parent ve child classta iki aynı isimli method varsa
# Childdaki bir obje bu methodu çağırırsa kendi içerisindeki methodu çağırır.
# Bir diğer deyişle ikinci yazılan method ilk yazılan methodu geçersiz kılar
# kendi classındaki methodu uygular. Buna overriding denir.

class Animal():
     
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    
    def toString(self):
        print("monkey")
        
m1 = Monkey()
m1.toString()

# %% polymorphism (çok şekillilik, çok biçimlilik)

# super classın içine bir methodu tanımladıktan sonra oluşturduğumuz child classta da 
# aynı methodu kullanırsak (yukarıdaki overridig örnek de buna uyuyor)
# ve yine başka methodlarda da kullanırsak buna polymorphism denir.

class Employee(object):
           
    def zam(self, salary): 
        self.salary = salary
        a = self.salary*1.1  
        print(a, "is new salary of employee")

class CE(Employee):

    def zam(self, salary):
        self.salary = salary       
        a = self.salary*1.2  
        print(a, "is new salary of CE")
        
class EEE(Employee):

    def zam(self, salary):
        self.salary = salary 
        a = self.salary*1.3       
        print(a, "is new salary of EEE")    

e1 = Employee()

ce1 = CE()

eee1 = EEE()

e1.zam(2000)

ce1.zam(2000)

eee1.zam(2000)

employee_list = [eee1, e1]

for employee in employee_list:
    employee.zam(2000)
    
# %% list örneği

nurgul_list = ["a", "b", "c", "d", "e"]    
    
for harf in nurgul_list:
    print(harf)
    

# %% Final Projesi
    
# şekiller adında bir abstract class oluştur.
# içerisinde alan (area) ve çevre uzunluğu (perimeter) olsun.
# bir de toString methodu yaz. Bu da şeklin adını return etsin.
# iki farklı child class yazacağız. square ve circle için.
# 


from abc import ABC, abstractmethod

 
class Shapes(ABC):
    
    @abstractmethod
    def area(self): pass
     
    @abstractmethod 
    def perimeter(self): pass
        

    def toString(self): pass

class Square(Shapes):
    
    def __init__(self, a):
        self.__a = a

    def area(self): 
        
        Shapes.area(self)
        area = self.__a ** 2
        print("Bu karenin alanı {} santimdir.".format(area))

    def perimeter(self):
        
        Shapes.perimeter(self)
        perimeter = self.__a*4
        print("Bu karenin çevresi {} santimdir.".format(perimeter))
        
    def toString(self):
        print("a degeri:", self.__a)

class Circle(Shapes):
    
    pi = 3.14
    
    def __init__(self, r):
        self.__r = r
    
    def area(self):
        Shapes.area(self)
        area = self.pi * (self.__r**2)
        print("Bu dairenin alanı {} santimdir.".format(area))

    def perimeter(self):
        Shapes.perimeter(self)
        perimeter = (2) * self.pi * self.__r 
        print("Bu dairenin çevresi {} santimdir.".format(perimeter))
        
    def toString(self):
        print("r degeri:", self.__r)

k1 = Square(5)
k1.area()
k1.perimeter()
k1.toString()

d1 = Circle(5)
d1.area()
d1.perimeter()
d1.toString()






























