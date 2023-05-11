from patients import Patient

path = "csv/patients.csv"
Patient.instantiate_from_csv(path)
for item in Patient.all:
    print(item)
