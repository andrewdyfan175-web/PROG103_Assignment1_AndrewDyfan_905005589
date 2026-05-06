#  I'm learning Python
print("Hello World")
num1, num2, num3 = 3, 4, 5
print(num1, num2, num3)
age = 18
if  age < 18:
    print("You are too young to attend this party.")
else:
    print("You required to attend this party.")
    message = 34
    print(message)

    count = 8.6
    print(count)
    #count = count + 2
    count += 3
    print(count)
person_name ='ALICE'
print(person_name)
alice_food = ("""no one should eat alice's food
               it's ok to be awesome
               stop !!""" )
print(alice_food)
POEM = ("""ALHAMDULILLAHI RABIL ALAMIN
REMIND ME OF HOW I USED TO BE 5 YEARS AGO
""")
print(POEM)
Freetown = "The capital city of Sierra Leone"
Age = 20
is_adult = age >= 18
print(is_adult)

#Truthly and Falsely Values
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hi"))
int(90.11)
print(int(90.11))
a = float(23.33)
print(a)



# Constants
AVERAGE_CONSULTATION_TIME = 15  # Minutes per patient


def calculate_wait_time(queue_position):
    """Calculates estimated wait time based on position in queue."""
    return queue_position * AVERAGE_CONSULTATION_TIME


def display_header():
    """Displays the system branding and SDG alignment."""
    print("\n" + "=" * 45)
    print("  HEALSYNC: SDG 3 QUEUE MANAGEMENT SYSTEM")
    print("  Goal: Ensure Healthy Lives & Well-being")
    print("=" * 45)


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
             age = int(input("Enter Patient Age:"))
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