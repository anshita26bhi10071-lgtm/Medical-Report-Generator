from storage import load_patients, save_patients
from validation import valid_name, valid_age


def add_patient():

    patients = load_patients()

    print("\n========== ADD PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    name = input("Enter patient name: ")

    if not valid_name(name):
        print("Invalid name.")
        return

    age = input("Enter age: ")

    if not valid_age(age):
        print("Invalid age.")
        return

    gender = input("Enter gender: ")

    conditions = input(
        "Previous medical conditions: "
    )

    allergies = input(
        "Allergies: "
    )

    medications = input(
        "Current medications: "
    )

    surgeries = input(
        "Previous surgeries: "
    )

    family_history = input(
        "Family medical history: "
    )

    symptoms = input(
        "Current symptoms: "
    )

    lifestyle = input(
        "Lifestyle information: "
    )

    patient = {

        "patient_id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "conditions": conditions,
        "allergies": allergies,
        "medications": medications,
        "surgeries": surgeries,
        "family_history": family_history,
        "symptoms": symptoms,
        "lifestyle": lifestyle
    }

    patients.append(patient)

    save_patients(patients)

    print("\nPatient information saved successfully!")


def update_patient():

    patients = load_patients()

    if len(patients) == 0:

        print("No patient records found.")

        return

    patient_id = input("Enter Patient ID to update: ")

    for patient in patients:

        if patient["patient_id"] == patient_id:

            print("\nEnter new information.")

            patient["name"] = input("Name: ")
            patient["age"] = input("Age: ")
            patient["gender"] = input("Gender: ")

            patient["conditions"] = input(
                "Previous medical conditions: "
            )

            patient["allergies"] = input(
                "Allergies: "
            )

            patient["medications"] = input(
                "Current medications: "
            )

            patient["surgeries"] = input(
                "Previous surgeries: "
            )

            patient["family_history"] = input(
                "Family medical history: "
            )

            patient["symptoms"] = input(
                "Current symptoms: "
            )

            patient["lifestyle"] = input(
                "Lifestyle information: "
            )

            save_patients(patients)

            print("Patient updated successfully!")

            return

    print("Patient ID not found.")


def delete_patient():

    patients = load_patients()

    patient_id = input("Enter Patient ID to delete: ")

    for patient in patients:

        if patient["patient_id"] == patient_id:

            patients.remove(patient)

            save_patients(patients)

            print("Patient deleted successfully!")

            return

    print("Patient ID not found.")
