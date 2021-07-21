# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:14:12 2020

@author: asus
"""
from rent import BikeRent, CarRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              *****Vehicle Rental Shop*****
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        main_menu = False  
    
        choice = input("Enter your choice: ").strip().lower()        
        
    if choice == "a":
            
        print("""
              ***** Bike Menu *****
              1. Display available bikes
              2. Request a bike on hourly basis £5
              3. Request a bike on daily basis £84
              4. Return a bike
              5. Main Menu
              6. Exit
              """)
              
        choice = input("Enter your choice: ")
        
        try: 
            choice = int(choice)
        except ValueError:
            print("It is not an integer.")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "a"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True 
            print("----------------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------------")
        elif choice == 4:
            bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6: ")
            
    elif choice == "b":
        
        print("""
              ***** Car Menu *****
              1. Display available cars
              2. Request a car on hourly basis £10
              3. Request a car on daily basis £192
              4. Return a car
              5. Main Menu
              6. Exit
              """)
        main_menu = False
              
        choice = input("Please enter your choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not an integer.")
            continue
        
        if choice == 1:
            car.displayStock() 
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car")) 
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car")) 
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------------")
        elif choice == 4: 
            car.returnVehicle(customer.returnVehicle("car"), "car")
            car.rentalBasis_c, car.rentalTime_c, car.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6: ")
    
    elif choice == "q":
        break
    else: 
        print("Please enter A, B or Q: ")
        main_menu = True
            
print("Thank you for using Vehicle Rental Shop.")
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    