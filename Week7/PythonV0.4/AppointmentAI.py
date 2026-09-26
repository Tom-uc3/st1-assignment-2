
class Appointment:
    appointments = []

    def __init__(self, patient, practitioner, time):
        self.patient = patient
        self.practitioner = practitioner
        self.time = time

    @classmethod
    def is_available(cls, practitioner, time):
        import ast
        try:
            with open("appointments.txt", "r") as file:
                for line in file:
                    try:
                        data = ast.literal_eval(line)
                    except (ValueError, SyntaxError):
                        # Skip blank or old-format lines
                        continue
                    if (data["PractitionerID"] == practitioner.PractitionerID and
                            data["time"] == time):
                        return False
        except FileNotFoundError:
            pass
        return True


    @classmethod
    def book(cls, patient, practitioner, time):
        if cls.is_available(practitioner, time):

            appointment = Appointment(patient, practitioner, time)
            cls.appointments.append(appointment)
            # Save one appointment per line as a dict so it can be read back with ast.literal_eval
            record = {
                "patient": str(patient),
                "practitioner": practitioner.name,
                "PractitionerID": practitioner.PractitionerID,
                "time": time
            }
            with open("appointments.txt", "a") as file:
                file.write(f"{record}\n")
            print("Appointment booked successfully.")
            return appointment
        else:
            print("That practitioner is already booked at that time.")
            return None


    @classmethod
    def get_available_times(cls, practitioner,all_times):
        available = []
        #search = str(time)
        #file = open(f"appointments.txt", "r")
       # for line_number, line in enumerate(file, start=1):
          #  if search in line:
          #      print("time not available.")

            #else:
             #   return available

        for time in all_times:
            if cls.is_available(practitioner, time):
                available.append(time)

        return available

    @classmethod
    def view_appointments(cls):
        import ast
        found = False
        try:
            with open("appointments.txt", "r") as file:
                for line in file:
                    try:
                        data = ast.literal_eval(line)
                    except (ValueError, SyntaxError):
                        # Skip blank or old-format lines
                        continue
                    print(f"{data['patient']} with {data['practitioner']} "
                          f"(ID: {data['PractitionerID']}) at {data['time']}")
                    found = True
        except FileNotFoundError:
            pass
        if not found:
            print("No appointments booked.")

    def cancel(self):
        Appointment.appointments.remove(self)
        print("Appointment cancelled.")

    def __str__(self):
        return (f"{self.patient} with "
                f"{self.practitioner} at {self.time}")

available_slots = [
    "09:00",
    "10:00",
    "11:00",
    "13:00",
    "14:00",
    "15:00"
]
