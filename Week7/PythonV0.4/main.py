



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

        #Start up menu
        print("Welcome to smartcare menu")
        print("1.Book appointment\n"
            "2.Find patient\n"
            "3.View appointment\n"
            "4.New Patient\n"
            "5.Cancel appointment\n"
            "6.Exit\n")

        Menu = input("Choose action:")
        #Menu item 1 code = book appointment
        if Menu == "1":
            import Practitioner
            global Practitioner

            Practitioners = [Practitioner.Practitioner("Dave", "Colons", 35),
                            Practitioner.Practitioner("Steve", "Alcohol abuse", 36)]

            print("\nPractitioners:")
            for i, practitioner in enumerate(Practitioners, start=1):
                print(f"{i}. {practitioner}")

            practitioner_choice = int(input("Choose practitioner: ")) - 1
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
            AppointmentAI.Appointment.book(
                Patient.view_Patient(Patient),
                selected_practitioner,
                selected_time
            )


            print("\nCurrent Appointments")
            for appointment in AppointmentAI.Appointment.appointments:
                print(appointment,'\n')

        #menu item 2 code = View patients
        elif Menu == "2":
            print("\n")
            Patient.Patient.view_Patient(Patient)
            print("\n")
        #Menu item 3 code = View appointments
        elif Menu == "3":
            print("\nCurrent Appointments")
            AppointmentAI.Appointment.view_appointments()
        #Menu item 4 code = Create a new patient
        elif Menu == "4":\
            Patient.Patient.new_Patient(Patient)
        #Menu item 6 code = Exit
        elif Menu == "6":
            print("Exit")
            break
        #Menu item 5 code = Cancel appointment
        elif Menu == "5":
            AppointmentAI.Appointment.cancel()



#Main code
if __name__ == "__main__":
    main()
