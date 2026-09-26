
class Appointment:
    appointments = []

    def __init__(self, patient, practitioner, time):
        self.patient = patient
        self.practitioner = practitioner
        self.time = time

    @classmethod
    def is_available(cls, practitioner, time):
        for appointment in cls.appointments:
            if (appointment.practitioner == practitioner and
                    appointment.time == time):
                return False
        return True

    @classmethod
    def book(cls, patient, practitioner, time):
        if cls.is_available(practitioner, time):
            appointment = Appointment(patient, practitioner, time)
            cls.appointments.append(appointment)
            print("Appointment booked successfully.")
            return appointment
        else:
            print("That practitioner is already booked at that time.")
            return None

    @classmethod
    def get_available_times(cls, practitioner, all_times):
        available = []

        for time in all_times:
            if cls.is_available(practitioner, time):
                available.append(time)

        return available

    def cancel(self):
        Appointment.appointments.remove(self)
        print("Appointment cancelled.")

    def __str__(self):
        return (f"{self.patient} with "
                f"{self.practitioner} at {self.time}")




#practitioners = [
 #   Practitioner(101, "Dr Jones"),
  #  Practitioner(102, "Dr Wilson")
#]

available_slots = [
    "09:00",
    "10:00",
    "11:00",
    "13:00",
    "14:00",
    "15:00"
]


# Booking menu
#print("\nPractitioners:")
#for i, practitioner in enumerate(practitioners, start=1):
   # print(f"{i}. {practitioner}")

#practitioner_choice = int(input("Choose practitioner: ")) - 1
#selected_practitioner = practitioners[practitioner_choice]

#print("\nAvailable times:")
#times = Appointment.get_available_times(
   # selected_practitioner,
    #available_slots
#)

#for i, time in enumerate(times, start=1):
  #  print(f"{i}. {time}")

#time_choice = int(input("Choose time: ")) - 1
#selected_time = times[time_choice]

#name = input("Enter patient name: ")

#patient = Patient(len(patients) + 1, name)
#patients.append(patient)

#Appointment.book(
 #   patient,
  #  selected_practitioner,
  #  selected_time
#)

#print("\nCurrent Appointments")
#for appointment in Appointment.appointments:
 #   print(appointment)
