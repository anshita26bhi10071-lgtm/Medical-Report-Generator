from patient import (
    add_patient,
    update_patient,
    delete_patient
)

from display import view_patients

from report import generate_report

from config import APP_NAME


print("==========================================")
print(APP_NAME)
print("==========================================")


while True:

    print("\n========== MAIN MENU ==========")

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Generate Medical Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_patient()

    elif choice == "2":

        view_patients()

    elif choice == "3":

        update_patient()

    elif choice == "4":

        delete_patient()

    elif choice == "5":

        generate_report()

    elif choice == "6":

        print("Thank you for using the system!")

        break

    else:

        print("Invalid choice. Please try again.")
