from storage import load_patients


def view_patients():

    patients = load_patients()

    if len(patients) == 0:

        print("No patient records found.")

        return

    print("\n========== PATIENT RECORDS ==========")

    for patient in patients:

        print("\nPatient ID:", patient["patient_id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Medical Conditions:", patient["conditions"])
        print("Allergies:", patient["allergies"])
        print("Medications:", patient["medications"])
        print("Surgeries:", patient["surgeries"])
        print("Family History:", patient["family_history"])
        print("Symptoms:", patient["symptoms"])
        print("Lifestyle:", patient["lifestyle"])
