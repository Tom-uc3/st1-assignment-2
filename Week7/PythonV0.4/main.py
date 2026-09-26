import Patient
import Practitioner
import AppointmentAI

def main():
    while True:
        import Patient
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
         # for i, Practitioner in enumerate(practitioners, start=1):
         #      print(f"{i}. {practitioner}")
     # Practitioners = [Practitioner.Practitioner("Dave", "Colons", 35),
           #          Practitioner.Practitioner("Steve", "Alcohol abuse", 36)]

    #Practitioner.view_Practitioners(Practitioner.Practitioner)
        print("Welcome to smartcare menu")
        print("1.Book appointment\n"
            "2.Find patient\n"
            "3.View appointment\n"
            "4.New Patient\n"
            "5.Exit")
        Menu = input("Choose action")
        if Menu == "1":
            global Practitioner

            Practitioners = [Practitioner.Practitioner("Dave", "Colons", 35),
                            Practitioner.Practitioner("Steve", "Alcohol abuse", 36)]
            print("\nPractitioners:")
            for i, practitioner in enumerate(Practitioners, start=1):
                print(f"{i}. {practitioner}")

            practitioner_choice = int(input("Choose practitioner: ")) - 1
            # selected_practitioner = Practitioner.objects.get(id=practitioner_choice)
            index_choice = practitioner_choice
            selected_practitioner = Practitioners[index_choice]

            print("\nAvailable times:")
            times = AppointmentAI.Appointment.get_available_times(
                selected_practitioner,
                available_slots
            )

            for i, time in enumerate(times, start=1):
                print(f"{i}. {time}")

            while True:
                try:
                    time_choice = int(input("Choose time use index number: ")) - 1
                    selected_time = times[time_choice]
                    break
                except IndexError:
                    print("Not found")

            from Patient import Patient

            #Patient.view_Patient(Patient)

            AppointmentAI.Appointment.book(
                Patient.view_Patient(Patient),
                selected_practitioner,
                selected_time
            )

            print("\nCurrent Appointments")
            for appointment in AppointmentAI.Appointment.appointments:
                print(appointment)
        elif Menu == "2":
            Patient.Patient.view_Patient(Patient)
            return
        elif Menu == "3":
            print("\nCurrent Appointments")
            for appointment in AppointmentAI.Appointment.appointments:
                print(appointment)
        elif Menu == "4":\
            Patient.Patient.new_Patient(Patient)
        elif Menu == "5":
            print("Exit")
            break



if __name__ == "__main__":
    main()
