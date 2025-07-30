def career_expertsystem():
    print("Welcome to the Simple Career Advisor!")
    print("Please answer the following questions with yes or no.\n")

    like_math = input("Do you enjoy math and numbers? (yes/no): ").strip().lower()
    like_physics = input("Do you enjoy physics? (yes/no): ").strip().lower()
    like_programming = input("Are you interested in computers and technology? (yes/no): ").strip().lower()
    like_chemistry = input("Do you like experimenting with chemicals? (yes/no): ").strip().lower()
    like_circuits = input("Do you like experimenting with gadgets? (yes/no): ").strip().lower()

    if like_math == "yes" and like_programming == "yes":
        print("\nSuggested Career: computer engineering")
    elif like_math == "yes" and like_physics == "yes":
        print("\nSuggested Career: mechanical engineering")
    elif like_chemistry == "yes" and like_biology == "yes":
        print("\nSuggested Career: biotechnology")
    elif like_circuits== "yes" and like_programming== "yes":
        print("\nSuggested Career: electronic engineering")
    else:
        print("\n call for more advice")
    


career_expertsystem()
