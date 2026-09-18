

#appointment class creation
class Appointment:
    #Initialize class
    def __init__(self, Date, Time, Practitioner, Patient):
        self.Date = Date
        self.Time = Time
        self.Practitioner = Practitioner
        self.Patient = Patient
        self.Status = True

    #Create a cancel method
    def cancel(self):
        self.Status = False

    #creates a View appointment method
    def view_appointment(self):
        pass

