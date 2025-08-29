def vacuum_world():
    # Initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum (A or B): ").strip().upper()
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ").strip()
    status_input_complement = input("Enter status of the other room (0 for Clean, 1 for Dirty): ").strip()

    print("Initial Location Condition:", goal_state)

    if location_input == 'A':
        print("Vacuum is placed in Location A")

        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            cost += 1
            print("Sucking dirt... Location A has been Cleaned.")
            print("Cost for CLEANING A:", cost)
        else:
            print("Location A is already clean.")

        if status_input_complement == '1':
            print("Location B is Dirty.")
            print("Moving RIGHT to Location B.")
            cost += 1
            print("Cost for moving RIGHT:", cost)

            goal_state['B'] = '0'
            cost += 1
            print("Sucking dirt... Location B has been Cleaned.")
            print("Cost for SUCK:", cost)
        else:
            print("Location B is already clean.")
            print("No action. Current Cost:", cost)

    elif location_input == 'B':
        print("Vacuum is placed in Location B")

        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1
            print("Sucking dirt... Location B has been Cleaned.")
            print("Cost for CLEANING B:", cost)
        else:
            print("Location B is already clean.")

        if status_input_complement == '1':
            print("Location A is Dirty.")
            print("Moving LEFT to Location A.")
            cost += 1
            print("Cost for moving LEFT:", cost)

            goal_state['A'] = '0'
            cost += 1
            print("Sucking dirt... Location A has been Cleaned.")
            print("Cost for SUCK:", cost)
        else:
            print("Location A is already clean.")
            print("No action. Current Cost:", cost)

    else:
        print("Invalid vacuum location input. Please enter 'A' or 'B'.")
        return

    print("\nGOAL STATE:", goal_state)
    print("Performance Measurement (Total Cost):", cost)


# To run the function:
vacuum_world()
