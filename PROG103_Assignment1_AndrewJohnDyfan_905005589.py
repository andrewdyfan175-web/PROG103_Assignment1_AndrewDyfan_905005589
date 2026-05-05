# Clinic Queue Management System
# A simple program to manage patient check-ins and queue processing

import datetime

# Global Constants
CLINIC_NAME = "City Health Medical Center"
CONSULTATION_FEE = 50.00


def display_header():
    """Prints the system header."""
    print("-" * 40)
    print(f"{CLINIC_NAME.upper()}")
    print(f"Date: {datetime.date.today()}")
    print("-" * 40)


def calculate_priority(age):
    """
    Logic Processing: Determines if a patient is a priority (Senior/Child).
    Returns a string category.
    """
    if age >= 60:
        return "Priority (Senior Citizen)"
    elif age <= 12:
        return "Priority (Pediatric)"
    else:
        return "Regular"


def process_clinic_queue():
    """
    Main Logic: Handles multiple records using loops and decision structures.
    """
    patient_records = []

    while True:
        display_header()
        print("\n[1] Register New Patient")
        print("[2] View All Records & Exit")

        choice = input("\nSelect an option (1-2): ")

        if choice == '1':
            # 5.1 Input Requirements
            name = input("Enter Patient Name: ").strip()
            try:
                age = int(input("Enter Patient Age: "))
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue

            # 5.2 Processing: Logic and Functions
            category = calculate_priority(age)

            # Store data in a dictionary (Record)
            record = {
                "name": name,
                "age": age,
                "category": category
            }
            patient_records.append(record)

            print(f"\nSUCCESS: {name} added to {category} queue.")

            # Loop control: Ask to continue
            cont = input("\nAdd another patient? (y/n): ").lower()
            if cont != 'y':
                break

        elif choice == '2':
            break
        else:
            print("Invalid selection. Please try again.")

    # 5.3 Output: Display Processed Results
    print("\n" + "=" * 40)
    print(f"FINAL QUEUE SUMMARY - {CLINIC_NAME}")
    print("=" * 40)
    print(f"{'No.':<4} {'Name':<20} {'Age':<6} {'Category'}")
    print("-" * 40)

    # Iteration through records
    for i, patient in enumerate(patient_records, 1):
        print(f"{i:<4} {patient['name']:<20} {patient['age']:<6} {patient['category']}")

    total_revenue = len(patient_records) * CONSULTATION_FEE
    print("-" * 40)
    print(f"Total Patients: {len(patient_records)}")
    print(f"Estimated Revenue: Le1"
          f"{total_revenue:.2f}")
    print("=" * 40)


# Entry Point
if __name__ == "__main__":
    process_clinic_queue()