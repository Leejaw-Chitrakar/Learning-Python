animal_list =[]

while True:
  print("""
        1. Add Animal
        2. View Animals
        3. Calculate total food
        4. End program
        """)
  user_option = input("What do you want to do? please choose the number: ")
  if user_option =="1":
        animal_name = input("Enter the name and food cost (e.g., Monkey, 120): ")
        if ", " in animal_name:
            animal, cost = animal_name.split(", ")
            cost = float(cost)
            animal_list.append({"animal": animal, "cost": cost})
            print("Done!")
        else:
            print("Invalid input formate.\nPlease use: Animal, Cost")
  elif user_option == "2":
      print("\nAnimals:")
      for i, animal in enumerate(animal_list):
        print(f"{i + 1}. {animal["animal"]}: ${animal["cost"]:.22"
              f"f}")
  elif user_option =="3":
     total_cost = sum(animal["cost"] for animal in animal_list)
     print(f"\nTotal Cost: ${total_cost:.2f}")
  elif user_option == "4":
      print("Thank you!")
      break
  else:
      print("Invalid option")