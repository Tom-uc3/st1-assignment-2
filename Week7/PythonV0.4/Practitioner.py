

#Create Class
class Practitioner:
    # Initialize class
    def __init__(self, name,specialty, PractitionerID):
        self.name = name
        self.specialty = specialty
        self.PractitionerID = PractitionerID


    #Creates a view practitioner method
    def view_Practitioner(self):
        return{
            "Practitioner Name": self.name,
            "Specialty": self.specialty,
            "Practitioner ID": self.PractitionerID
        }



Practitioner1 = Practitioner("Dave", "Colons", 35)

info = Practitioner1.view_Practitioner()

for key, value in info.items():
    print(f"{key}: {value}")

