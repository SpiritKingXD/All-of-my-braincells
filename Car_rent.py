class Car:
    def __init__(self):
        self.rented_cars = []  

    def rent_a_car(self):
        car = input('What car do you want to rent? ')
        rental_details = {'car': car}  
        self.rented_cars.append(rental_details)  
        return f'So, you want to rent the {car}.'

    def rent_period(self):
        if not self.rented_cars:
            return "You need to rent a car first before setting the rental period."
        
        _from = input('From when do you need the car? ')
        to = input('To when do you need the car? ')
        
      
        self.rented_cars[-1]['rental_period'] = f'From {_from} to {to}'
        return f'You will rent the car from {_from} to {to}.'

    def show_rented_cars(self):
        if self.rented_cars:
            print("\nList of rented cars and their details:")
            for i, rental in enumerate(self.rented_cars, 1):
                car_info = rental['car']
                rental_period = rental.get('rental_period', 'Not set yet')
                print(f"{i}. Car: {car_info}, Rental Period: {rental_period}")
        else:
            print("No cars have been rented yet.")

def main():
    car_rental = Car() 
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Rent a car")
        print("2. Set rental period")
        print("3. View rented cars")
        print("4. Exit")
        
        choice = input("Please enter your choice (1/2/3/4): ")
        
        if choice == '1':
            print(car_rental.rent_a_car())
        elif choice == '2':
            print(car_rental.rent_period())
        elif choice == '3':
            car_rental.show_rented_cars()
        elif choice == '4':
            print("Thank you for using the car rental service!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
