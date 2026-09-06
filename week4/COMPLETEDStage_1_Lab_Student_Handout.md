# Stage 1 Lab \- Human vs AI: Building Your First SmartCare Prototype

# **Learning objectives**

* Create and run a simple Python file with basic input, output, and processing statements  
* Use lists, dictionaries and functions to enhance the Python file  
* Build a small SmartCare appointment prototype.  
* Use AI as a tutor rather than a replacement.  
* Compare human-written and AI-generated code.  
* Verify AI-generated code through execution and test inputs.  
* Document a short AI-use reflection.

# **Files to create and commit in GitHub**

stage01/  
  smartcare\_v01.py  
  comparison.md  
  reflection.md  
  ai\_usage.md

# **Part A \- Understand the Problem: AI OFF**

SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each appointment records patient name, practitioner name and appointment time.

What data must be stored?

Patients name, appointment times and practitioner names.

What functions might be useful?

Being able to book and see appointment times, as well as patient and practitioner names.

What could go wrong?

Someone not entering a section of needed input data; the program not showing all relevant data when checking appointments. 

What requirements are unclear?

Wether or not they want a version of the software for clients to book appointmentstments.

# **Part B \- Build a Human-Written Prototype: AI OFF**

**\#task 1**

**\# Create and run a simple Python file with basic input,output statements**

**print("Welcome to SmartCare: Community Clinic Appointment Booking System\!")**

**\# First Appointment**  
**patient1\_name \= 'Alice Smith'**  
**practitioner1\_name \= 'Dr. John Doe'**  
**appointment1\_time \= '2024-07-20 10:00 AM'**  
**print(f"Patient: {patient1\_name} | Practitioner: {practitioner1\_name} | Time: {appointment1\_time}")**

**\# Second Appointment**  
**patient2\_name \= 'Bob Johnson'**  
**practitioner2\_name \= 'Dr. Jane Roe'**  
**appointment2\_time \= '2024-07-20 11:30 AM'**  
**print(f"Patient: {patient2\_name} | Practitioner: {practitioner2\_name} | Time: {appointment2\_time}")**

**\#task1enhanced**  
**\# Use lists, dictionaries and functions to enhance the Python file**

**appointments \= \[\]**

**def book\_appointment(patient\_name, practitioner\_name, appointment\_time):**  
**    if not patient\_name:**  
**        raise ValueError("Patient name cannot be empty")**  
**    appointment \= {**  
**        "patient": patient\_name,**  
**        "practitioner": practitioner\_name,**  
**        "time": appointment\_time**  
**    }**  
**    appointments.append(appointment)**

**def display\_appointments():**  
**    if not appointments:**  
**        print("No appointments recorded.")**  
**        return**  
**    for appointment in appointments:**  
**        print(f"Patient: {appointment\['patient'\]} | Practitioner: {appointment\['practitioner'\]} | Time: {appointment\['time'\]}")**

**print("Welcome to SmartCare: The Clinical Appointment Booking System\!")**  
**book\_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')**  
**book\_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')**  
**display\_appointments()**

^ Now, run  both programs , and identify at least five limitations.

limitations: 

1. No user input  
2. It doesn’t necessarily store any of the appointment details  
3. Still complex to add appointments (seeing as the receptionist would have to code them in  
4. No error handling for not having an appointment time  
5. No error handling for if someone was trying to book an appointment at the same time as another one

# **Part C \- Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot)**

Suggested prompt structure:  
Act as a Python tutor.  
I am learning introductory software technology.  
Here is a small appointment-booking function.  
1\. Explain what the code does.  
2\. Identify three limitations.  
3\. Suggest improvements.  
4\. Do not rewrite the whole application.  
5\. Ask me two questions to test my understanding.

# **Part D \- Generate an Alternative: AI ON**

Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI.

# **Part E \- Compare Human and AI Versions**

| Question | Human version | AI version |
| :---- | :---- | :---- |
| Easy to understand? | yes | No comments to explain |
| Runs successfully? | yes | yes |
| Uses only required features? | No, it doesn't have any required features  | Yes  |
| Adds assumptions? | no | no |
| Handles errors? | no | no |
| Could I explain it? | yes | yes |

# **Part F \- Verify Behaviour**

* Normal appointment  
* Blank patient name  
* Two appointments for the same practitioner/time  
* Strange input such as patient\_name=None or appointment\_time=None

# **Part G \- Improve One Thing**

Choose exactly one controlled improvement, for example: if not patient\_name: raise ValueError("Patient name cannot be empty")

I added error handling for practitioner and time so it cannot be left blank

# **Part H \- Reflection (150-250 words)**

What did you build before using AI?

My code prior to using AI would make you repeat the patient's name until you actually entered in a name.

What did AI help you understand?

Nothing at all; I already understood how the code functioned.

Did AI make assumptions?

With the prompts I used, it did not, as I told it specifically what I wanted.

How did you verify the AI output?

I verified it by testing all the possible inputs to see if it would work and handle errors appropriately. 

What engineering work remained for you?

Adding comments to the code so it all made sense, and adding some more error handling.

# **Submission checklist \[GitHub Commit\]**

* Python file runs.  
* Comparison table completed.  
* Normal and unusual inputs tested.  
* AI assistance documented.  
* Reflection completed.  
* I can explain my code.