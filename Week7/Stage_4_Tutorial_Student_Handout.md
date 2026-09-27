# Assignment 2 – Case Study

# Stage 4 Tutorial Activities 

# Object-Oriented Design Decisions

Week 7 | 60 minutes

# **Activity 1 \- Encapsulation Review**

| Class | Protected state/invariant | Public operations |
| :---- | :---- | :---- |
| Patient | No information can be left blank | new\_Patient |
| Practitioner | List of practitioners | view\_practitioner |
| Appointment | View\_appointment to find and view list of appointments | View\_appointment  |

# **Activity 2 \- Composition or Inheritance?**

Appointment and Patient \-\> Composition/association  Reason: as Appointment has a patient.

Appointment and Practitioner \-\> □ Composition/association Reason: as appointment has a practitioner

Doctor and Practitioner (hypothetical) \-\> □ Inheritance  Reason: As a doctor and a practitioner are effectively the same and both employees of a General practice or hospital. So one would be a child class

Clinic and Appointment \-\> □ Composition/association  Reason: as a clinic would have appointments but isn’t one.

# **Activity 3 \- Responsibility Allocation**

**Who decides whether SCHEDULED can become CANCELLED?**

In the code it is the appointment class however in real life for this particular practice and design brief it would be the Clinic/ receptionist.

**Who validates a patient name?**

Whoever is entering it in for the code which would most likely be the receptionist.

**Should Appointment execute SQL? Why?**

Yes it should as SQL is database code and all the appointments need to be stored and kept for operational reports and SQL would make it easier to pull all the appointments for a particular day.

**Should the UI decide whether a status transition is legal?**

No it shouldn’t as that would make it way easier to acces sensitive data.

# **Activity 4 \- AI Code Critique**

**AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.**

1. The appointment class should’nt be a child class of PatientRecord, they should have a composition relationship. An Appointment should have a patient.  
2. If the appointment class is an inheritance from patient record, I don’t beleive it would stop you from viewing every patients personal details when booking an appointment.   
3. Appointment class should’nt have a dependency for the Notification Manager. They should both be able to run separately.  
4. Sql shouldn’t be directly in the cancel function it should have a separate file that the cancel function can access and modify.  
5. The appointment class shouldn’t have public status mutation from smartcares brief, I also believe public status mutation is for html not for python code. 

# **Exit question**

**Why can code be object-oriented syntactically but still have poor object-oriented design?**

Code can be Object-oriented syntactically but still have poor Object-oriented design as coding a good design requires coding to the desired architecture for the code. Python doesn’t enforce good design just the coding mechanics so its upto the software engineer to actually enforce the architecture for there design.