from storage import load_patients


def generate_report():

    patients = load_patients()

    if len(patients) == 0:

        print("No patient records found.")

        return

    patient_id = input(
        "Enter Patient ID for report: "
    )

    for patient in patients:

        if patient["patient_id"] == patient_id:

            print("\n")
            print("========================================")
            print("       MEDICAL HISTORY REPORT")
            print("========================================")

            print("\nPATIENT INFORMATION")
            print("----------------------------")

            print("Patient ID :", patient["patient_id"])
            print("Name       :", patient["name"])
            print("Age        :", patient["age"])
            print("Gender     :", patient["gender"])

            print("\nMEDICAL HISTORY")
            print("----------------------------")

            print(
                "Previous Medical Conditions:"
            )
            print(patient["conditions"])

            print("\nAllergies:")
            print(patient["allergies"])

            print("\nCurrent Medications:")
            print(patient["medications"])

            print("\nPrevious Surgeries:")
            print(patient["surgeries"])

            print("\nFamily Medical History:")
            print(patient["family_history"])

            print("\nCurrent Symptoms:")
            print(patient["symptoms"])

            print("\nLifestyle Information:")
            print(patient["lifestyle"])

            print("\n========================================")
            print("This report contains information")
            print("provided by the user.")
            print("It is not a medical diagnosis.")
            print("========================================")

            return

    print("Patient ID not found.")
