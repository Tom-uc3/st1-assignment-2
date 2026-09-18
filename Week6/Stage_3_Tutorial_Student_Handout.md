# Assignment 2-Case Study

# Stage 3 Tutorial Activities

# From Requirements to Domain Models

Week 6 | 60 minutes

# **Candidate Concepts**

| Candidate | Class? | Reason |
| :---- | :---- | :---- |
| Patient | Patient | They correlate |
| Practitioner | Practitioner | They correlate |
| Appointment | Appointment | They correlate |
| Name | Patient, practitioner | Both classes need a name for each patient and practitioner |
| Clinic | Clinic |  |
| Database | Patient, practitioner, appointment | Each of these classes need a database |
| Cancellation | appointment | As it is an appointment being cancelled |
| Status | appointment | As its the appointment status being checked. |

# **CRC Cards**

## **Patient**

| Responsibilities | Collaborators |
| :---- | :---- |
| identity/state | Appointment \+ patient Information |
| Basic validation | Appointment&nbsp;&nbsp; |

## **Practitioner**

| Responsibilities | Collaborators |
| :---- | :---- |
| Identity/specialty&nbsp; | appointment |
| Check appointments | appointment |

## **Appointment**

| Responsibilities | Collaborators |
| :---- | :---- |
| Time&nbsp; | Patient \+ practitioner&nbsp; |
| Status and state change | Patient \+practitioner |

# 

# **Relationship Reasoning**

Patient to Appointment: which relationship and why?

Patient to appointment Has a relationship as each appointment needs one patient.

Practitioner to Appointment: what multiplicity?

Practitioner 1 \------- 0..\*Appointment. As each appointment needs one practitioner but a practitioner can have multiple appointments booked for different dates and times.

Should Appointment inherit from the Patient?

No, as an appointment does not have a first name or date of birth. The appointment being booked has just one patient and the patient has all the details of the patient.

Does the Clinic need to own every object?

No, as then the clinic becomes a god class. This isn’t good practice and makes code harder to debug.

# **AI Model Critique**

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

All of these proposals will make the software over complicated, and harder to debug if any issues arise. The smartcare clinic just wants a simple software for now that works and is simpler than their current processes.