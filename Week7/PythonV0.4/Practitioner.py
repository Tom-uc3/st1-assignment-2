

#Create Class
class Practitioner:
    # Initialize class
    def __init__(self, name,specialty, PractitionerID):
        self.name = name
        self.specialty = specialty
        self.PractitionerID = PractitionerID


    #Creates a view practitioner method
    def __repr__(self):
        return f"Practitioner Name: '{self.name}',Specialty: {self.specialty},Practitioner ID: {self.PractitionerID}"

    def view_Practitioners(Practitioner):
        Practitioners = [Practitioner("Dave", "Colons", 35),
                     Practitioner("Steve", "Alcohol abuse", 36)]
        print("\nPractitioners:")
        for i, Practitioner in enumerate(Practitioners, start=1):
            print(f"{i}. {Practitioner}")

    def choose_Practitioner(Practitioner):
        practitioner_choice = int(input("Choose practitioner: ")) - 1
        selected_practitioner = Practitioner[practitioner_choice]

        return Practitioner

