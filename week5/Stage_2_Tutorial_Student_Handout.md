# Assignment 2 Case Study&nbsp;

# Stage 2 Tutorial From Problems to Requirements

Week 5 | 60 minutes

# **Learning goals**

* Analyse stakeholders.  
* Distinguish functional and non-functional requirements.  
* Recognise ambiguity and unsupported requirements.  
* Define scope.  
* Develop user stories and acceptance criteria.  
* Critique AI-generated requirements.

# **Activity 1 \- Stakeholder Map**

| Stakeholder | Need | Potential conflict |
| :---- | :---- | :---- |
| Practitioners | To easily find patient information and to know when there next appointment is. | none |
| patients | To easily be able to see practitioner availability and book appointments. | Practitioner lunch breaks |
| management | To be able to view appointment history for producing operational reports. | Showing management sensitive patient information |
| Receptionist&nbsp; | To be able to cancel appointments and have consistent appointment status | If the patient can also do this, it needs to load onto the system so the receptionist knows |
|  |  |  |

# **Activity 2 \- Functional or Non-Functional?**

□ Functional    The system shall allow staff to cancel an appointment.

□ Functional The system should remain responsive for the course-scale dataset.

□ Non-functional   The system shall retain cancelled appointments.

□ Functional   Core business logic should be independently testable.

□ Non-functional   The system shall search for a patient by ID.

# **Activity 3 \- Repair Ambiguous Requirements**

The system should be easy to use.

Problem: The current system is paper and spreadsheets so it is difficult to find any information.

Clarification question: What about the system needs to be easy to use?

Patient search should be fast.

Problem: no patient search function with current systems.&nbsp;&nbsp;

Clarification question: How do you want it to search fast? (ex Patient ID, names on search function alphabetically ordered?)

The system should securely manage data.

Problem: It is difficult to keep data secure when it is either on paper or on a spreadsheet.

  Clarification question: Where do you want it to store information?

Appointments should normally be easy to cancel.

Problem: difficult to cancel appointments as its difficult to even now when and who an appointment is with.  Clarification question: which stakeholders do you want to be able to cancel appointments using the system?

# **Activity 4 \- AI Requirements Audit**

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion | Classification | Evidence / reason |
| :---- | :---- | :---- |
| Patients receive SMS reminders. | Assumption requiring validation&nbsp; | This would be very useful so no one misses appointments. However it is probably out of scope. |
| Facial recognition login. | Out of scope | The company wants something simple prior to upscaling it. |
| Receptionists create appointments. | Confirmed | In scope and confirmed as that is what currently happens and this software will make it easier for this to happen. |
| Online payment. | Out of scope | People usually pay for GP appointments at the reception. |
| Practitioners view schedules. | Confirmed | Practitioners need to know when their next appointment is, so they can be available at the office. |
| AI recommends treatments. | Out of scope | Personally I wouldn't trust Ai to recommend me any type of treatment or medical advice. |
| Cancelled appointments remain in history. | Assumption requiring validation | The client brief is not clear on what information needs to be retained for operation reports. |

# **Exit question**

Why is 'AI suggested it' not sufficient evidence for a requirement?

As AI isn’t a person and hasn’t used similar apps or procedures for things, it will also try and come up with other useful things that are not in the scope of certain systems. Usually the other useful things it comes up with will also be difficult to code and create for a system that is supposed to be kept simple.