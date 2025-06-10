class Fruits:
    def __init__(self): 
        self.fav_fruit = {}
  
    def Add(self):
        name = input("Enter the person's name: ")
        fruit = input("Enter their favourite fruit: ")
        self.fav_fruit[name] = fruit
        print(f"{name}'s favourite fruit has been added.\n") 

    def View(self):
        if self.fav_fruit:
            print("\nFavourite Fruits List:")
            for name, fruit in self.fav_fruit.items():
                print(f"{name}: {fruit}")
            print()
        else:
            print("No favourite fruits added yet.\n")

def main():
    fruits_manager = Fruits()
    
    while True:
        print("1. Add favourite fruits")
        print("2. View favourite fruits")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                fruits_manager.Add()
            elif choice == 2:
                fruits_manager.View()
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice.Enter again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()
