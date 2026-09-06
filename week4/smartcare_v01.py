# SmartCare Appointment Booking System

appointments = []

def book_appointment(): #for booking appoinments

    patient = input("Enter patient name: ")
    #Patient error handling
    while not patient:
            print("Patient name cannot be empty")
            return

    #Practitioner error handling
    practitioner = input("Enter practitioner name: ")
    while not practitioner:
        print("Practitioner name cannot be empty")
        return

    #Time error handling
    time = input("Enter appointment time: ")
    while not time:
        print("Appointment time cannot be empty")
        return

    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!\n")


def display_appointments(): #for showing appointments once booked
    if not appointments:
        print("No appointments recorded.\n")
        return

    print("\nAppointments:")
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )
    print()


# Main Program
print("Welcome to SmartCare Appointment Booking System")

book_appointment()
book_appointment()

display_appointments()