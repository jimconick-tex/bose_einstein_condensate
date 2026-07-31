from src.plotting import plot_bec_density
from src.solver import split_step


while True:
    print("\n========== 1D Bose-Einstein Condensate ==========")
    print("1. Plot BEC density")
    print("2. Exit")

    option = input("\nSelect an option: ")

    match option:
        case "1":
            try:
                g = float(input("Interaction strength g = "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            x, psi = split_step(g)
            plot_bec_density(x, psi, g)

        case "2":
            print("Goodbye!")
            break

        case _:
            print("Invalid option. Please try again.")