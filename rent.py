# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:05:41 2020

@author: asus
"""
# %% Arsa kiralama projesi (RentAVehicle)

# Araç kiralama olacak bunun içinde araba ve bisiklet kiralama bölümü olacak
# Müşteri araç kiralama talebinde bulunabilir (request)
# Müşteri kiraladığı aracı iade edebilir (return) edebilir
# Araç kiralama firması aracları görselleştirmeli (display)
# Saatlik ve günlük kiralama olsun (rent/day, rent/hour)
# Müşterinin iade ettiği arabayı tekrar kiralanabilir duruma getirsin (return vehicle)
# Arabanın kendine özel bir indirim yapma özelliği ekleyeceğiz. (discount)

import datetime

class VehicleRent(): 
    
    def __init__(self, stock):
        self.stock = stock
        self.now = 0
        
    def displayStock(self): 
        print("{} vehicles are available for renting.".format(self.stock))
        return self.stock
        
    def rentHourly(self, n): 
        
        if n > self.stock:
            print("Sorry, there is only {} vehicle available.".format(self.stock))
            return None
        elif n <= 0: 
            print("Number should be positive.")       
            return None
        else: 
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours".format(n, self.now.hour))
            
            self.stock -= n
            return self.now
            
    def rentDaily(self, n): 
                
        if n > self.stock: 
            print("Sorry, there is only {} vehicles available.".format(self.stock))
            return None
        
        elif n <= 0:
            print("Number should be positive.")
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicles for daily at {} hours.".format(n, self.now.hour))
            
            self.stock -= n
            return self.now
    
    def returnVehicle(self, request, brand): 
        
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand == "car":
            
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: 
                    bill = car_h_price*rentalPeriod.seconds/3600*numOfVehicle
               
                elif rentalBasis == 2:
                    bill = car_d_price*rentalPeriod.seconds/(3600*24)*numOfVehicle
                
                if 5 <= numOfVehicle:
                    print("You have extra %20 discount.")
                    bill = bill*0.8
                
                print("Thank you for returning your vehicle.")
                print("Price is £{}.".format(bill))
                return bill
        
        elif brand == "bike":
            
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle
                
                if numOfVehicle >= 5:
                    print("You have extra %20 discount.")
                    bill = bill*0.8                    
                    
                print("Thank you for returning your vehicle.")
                print("Price is {}.".format(bill))
                
                return bill
            
        else:
            print("You do not rent a vehicle.")
            return None
    
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b): 
        
        bill = b - (b*discount_rate)/100
        
        return bill
    
class BikeRent(VehicleRent): 
    
    def __init__(self, stock):
        super().__init__(stock)
    
class Customer(): 
    
    def __init__(self): 
        
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self, brand): 
        
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
           
            try:
                bikes = int(bikes)
            except ValueError:
                print("Value should be number.")
                return -1        
            
            if bikes < 1:
                print("Number of bikes should be greater than zero.")
                return -1
            else:
                self.bikes = bikes
            return self.bikes
                            
        elif brand == "car":
            cars = input("How many cars would you like to rent?")
            
            try:
                cars = int(cars)                
            except ValueError:
                print("Value should be number.")
                return -1
            
            if cars < 1:
                print("Number of cars should be greater than zero.")
                return -1
            else: 
                self.cars = cars
            return self.cars
                        
        else:
            print("Request vehicle error!")
    
    def returnVehicle(self, brand): 
        
        if brand == "bike":
            if self.rentalBasis_b and self.rentalTime_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
        
        elif brand == "car":
            if self.rentalBasis_c and self.rentalTime_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else: 
                return 0,0,0
            
        else:
            print("Return vehicle Error!")
        
    
    
    
    
    
    
    
    
    
    
    
    























    
    
    
    
    
    
    

