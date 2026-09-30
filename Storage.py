import csv
import os


FILE_NAME = "patients.csv"


def load_patients():

    patients = []

    if not os.path.exists(FILE_NAME):

        file = open(FILE_NAME, "w", newline="")

        writer = csv.writer(file)

        writer.writerow([
            "patient_id",
            "name",
            "age",
            "gender",
            "conditions",
            "allergies",
            "medications",
            "surgeries",
            "family_history",
            "symptoms",
            "lifestyle"
        ])

        file.close()

        return patients

    file = open(FILE_NAME, "r", newline="")

    reader = csv.DictReader(file)

    for row in reader:
        patients.append(row)

    file.close()

    return patients


def save_patients(patients):

    file = open(FILE_NAME, "w", newline="")

    writer = csv.writer(file)

    writer.writerow([
        "patient_id",
        "name",
        "age",
        "gender",
        "conditions",
        "allergies",
        "medications",
        "surgeries",
        "family_history",
        "symptoms",
        "lifestyle"
    ])

    for patient in patients:

        writer.writerow([
            patient["patient_id"],
            patient["name"],
            patient["age"],
            patient["gender"],
            patient["conditions"],
            patient["allergies"],
            patient["medications"],
            patient["surgeries"],
            patient["family_history"],
            patient["symptoms"],
            patient["lifestyle"]
        ])

    file.close()
