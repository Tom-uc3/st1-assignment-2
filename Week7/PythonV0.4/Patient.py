from contourpy.util import data


class Patient:
    # Initialize class
    def __init__(self, name, ContactDetails,PatientID):
        self.name = name
        self.ContactDetails = ContactDetails
        self.PatientID = PatientID
    #Creates a new patient
    def new_Patient(self):
        import json
        File = open("patient.txt","a",encoding="utf-8")
        patient_dict = {}
        while True:
             patient_dict["name"] =  input("Patient Name:")
             if any(char.isdigit() for char in patient_dict["name"]):
                print("Error: Names cannot contain numbers!")
             elif patient_dict["name"] == "":
                 print("Error: Patient Name not entered!")
             else:
                 break
        while True:
            patient_dict["ContactDetails"] = input("Contact Details:")
            if patient_dict["ContactDetails"] == "":
                print("Error: Contact Details not entered!")
            else:
                break

        while True:
            try:
                patient_dict["PatientID"] = int(input("Patient ID:"))
                break
            except ValueError:
                print("Error: Patient ID must be a number")

        json.dump(patient_dict, File)
        File.write(",")
        File.write("\n")
        File.close()

    #To be able to search for a patient
    def view_Patient(self):
        import ast
        search = input("Enter Patient Name or ID:")
        with open("patient.txt", "r") as file:
            try:
                for line_number, line in enumerate(file, start=1):
                     if search in line:
                        data = ast.literal_eval(line)
                for d in data:
                    print(f"Name: {d['name']} | Contact Details: {d['ContactDetails']} | Patient ID: {d['PatientID']}")
            except UnboundLocalError:
                print("Not found")

Patient.new_Patient(Patient)
Patient.view_Patient(Patient)
