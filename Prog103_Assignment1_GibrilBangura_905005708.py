# Constants
AVERAGE_CONSULTATION_TIME = 15  # Minutes per patient


def calculate_wait_time(queue_position):
    """Calculates estimated wait time based on position in queue."""
    return queue_position * AVERAGE_CONSULTATION_TIME


def display_header():
    """Displays the system branding and SDG alignment."""
    print("\n" + "~" * 47)
    print(" HEALSYNC: SDG 3  'Good Health & Well-beinng'")
    print(" CITING SYSTEM: Clinic QUEUE MANAGEMENT SYSTEM")

    print("  Goal: Ensure Healthy Lives & Well-being")
    print("~" * 47)


def main():
    patients = []

    display_header()

    while True:
        print("\nMain Menu:")
        print("1. Register New Patient")
        print("2. View Current Queue")
        print("3. Exit System")

        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            # Input: Multiple records are possible via the loop
            name = input("Enter Patient Name: ")
            try:
                age = int(input("Enter Patient Age: "))
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue

            print("Urgency Levels: 1. Emergency | 2. Urgent | 3. Routine")
            urgency = input("Select Urgency Level: ")

            # Logic Processing: Decision structures
            if urgency == "1":
                status = "Emergency"
                # Logic: Emergencies go to the front
                patients.insert(0, {"name": name, "age": age, "status": status})
            elif urgency == "2":
                status = "Urgent"
                patients.append({"name": name, "age": age, "status": status})
            else:
                status = "Routine"
                patients.append({"name": name, "age": age, "status": status})

            print(f"\n[Success] {name} has been added to the queue.")

        elif choice == "2":
            # Output: Formatted results
            if not patients:
                print("\nNo patients currently in the queue.")
            else:
                print("\n--- CURRENT PATIENT LIST ---")
                print(f"{'Pos':<5} {'Name':<20} {'Status':<15} {'Wait (min)':<10}")

                # Iteration: Processing the list of records
                for index, patient in enumerate(patients):
                    wait_time = calculate_wait_time(index)
                    print(f"{index + 1:<5} {patient['name']:<20} {patient['status']:<15} {wait_time:<10}")

                print(f"\nTotal patients waiting: {len(patients)}")

        elif choice == "3":
            print("System shutting down. Stay healthy!")
            break

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()