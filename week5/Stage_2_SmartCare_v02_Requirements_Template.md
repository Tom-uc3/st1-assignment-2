# SmartCare v0.2 \- Requirements Specification Template

# **1\. Problem and Scope**

The main issue is that smartcare uses paper and spreadsheets to keep track of all their data and it is difficult to find this way. So patients and the receptionists don’t know which practitioners are free and when. Management also can’t find the required information for operational reports.

&nbsp;

| In scope |  |
| ----- | :---- |
| Practitioner booking time availabilities |  |
| Booking system with times and availability including error handling. |  |
| Data storage for the required data for operational reports. |  |
| Search system to help find patient information. |  |
| Practitioner information (ex what they specialize in) | provisional |
| Patient information (ex medical record) | Provisional |

&nbsp;

# **2\. Stakeholders**

| Stakeholder | Need | Evidence |
| :---- | :---- | :---- |
| Practitioners | To easily find patient information | Currently they are struggling to find it. So the patient's history is unknown. |
| patients | To easily be able to see practitioner availability and book appointments. | Can’t see practitioner availability and has to call up to book appointments. |
| management | To be able to view appointment history for producing operational reports. | Since multiple different forms of data keeping are being used it is extremely difficult for them to find appointment history |
| receptionists | To be able to cancel appointments and have consistent appointment status | Since multiple different forms of appointment tracking are being used it is difficult to know when appointments are and if they have been canceled or not |
|  |  |  |

# **3\. Functional Requirements**

FR-01: Patient Database (be able to add/remove patient information and search for patients)

FR-02: Practitioner database

FR-03: appointment database

FR-04: To be able to book appointments

FR-05:to be able to select which practitioner when booking

FR-06: to be able to cancel bookings

FR-07: view Booking times

FR-08: error handling so theres no duplicate bookings

FR-09: error handling so theres no bookings missing information

FR-10: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FR-11: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FR-12: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# **4\. Non-Functional Requirements**

NFR-01: All the databases are encrypted

NFR-02: receptionist, management and practitioners to be able to view which bookings are for which patients and practitioners.

NFR-03: view booking history

NFR-04: The software being able to produce operational reports.

NFR-05: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NFR-06: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# **5\. User Stories**

US-01: As a Practitioner, I want patient information, so that I can prepare prior to seeing them.

US-02: As a patient, I want to be able to see when my practitioner is available, so that i can find a suitable time to book an appointment.

US-03: As a manager, I want to be able to see the appointment history, so that I can write operational reports.

US-04: As a receptionist, I want patients to have to enter all their information for booking, so that when they show up for their appointment I know who there seeing and what time the appointment is.

US-05: As a \_\_\_\_\_\_\_\_\_\_, I want \_\_\_\_\_\_\_\_\_\_, so that \_\_\_\_\_\_\_\_\_\_.

US-06: As a \_\_\_\_\_\_\_\_\_\_, I want \_\_\_\_\_\_\_\_\_\_, so that \_\_\_\_\_\_\_\_\_\_.

# **6\. Acceptance Criteria**

GIVEN patient information  
WHEN their about to show up for there booking  
THEN the practitioner can read up on the patients past visits to ask questions on how things are going.

GIVEN practitioner availability&nbsp;  
WHEN trying to book  
THEN booking becomes straightforward

Failure scenario

GIVEN patient booking records  
WHEN patients attend appointments  
THEN I can only see there records and not there name or appointment time.

# **7\. Assumptions and Open Questions**

Who can create, move and cancel bookings? What booking history data needs to be retained for operational reports?

&nbsp;

&nbsp;

# **8\. AI Requirements Review Record**

| AI suggestion | Evidence? | Decision | Reason | Verification |
| :---- | :---- | :---- | :---- | :---- |
| Clearly state what the patient database has to store and what the system can do to it. | Yes I wasn’t overly clear on what it had to store or what it had to do. | Clearly define what the system has to do to the database. | Without defining this I may end up coding a program that can’t store or remove content. | Accepted&nbsp; |
| Figure out what needs to go into management's operational reports so it can be stored. | Yes, Not very clear from the task what management needs for their reports. | Figure out what data they need to store for their reports so the software can ensure it's stored. | Not knowing what they need to store makes it difficult to know what information we need to keep | Accepted&nbsp; |
| Follow governing regulators for encryption process | Yes no one wants there details for medical issues being leaked and there are regulations for privacy. | Find out what these regulation are and encrypt data based on them. | Not encrypting data could lead to data leaks and smart care could get into a lot of trouble | Accepted |
| Clarify which actor does what with the system. | Yes it is not very clear from the brief what actor is going to be doing what with the system. | Get this clarified | Without having this clarified it’s difficult to code a system as I’m basically going in blind. | Accepted |
|  |  |  |  |  |

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

# **Reflection**

In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence?

AI noticed that I have not explained the requirements thoroughly and who the requirements actually concerned however from the client brief this is also not very clear. Using the recommended prompt AI did not invent anything or overreach on anything it mainly told me what I could clarify more and if it was a testable requirement or not. None of my requirements changed all that much after the review as I’ll need to ask the client more questions.&nbsp;

&nbsp;

Requirements must have evidence as without evidence, is it really a problem the client is running into? Or are you just wasting your time with a non-problem?. It is always better to go and clarify the exact requirements with the client prior to wasting time and making the system more complex.