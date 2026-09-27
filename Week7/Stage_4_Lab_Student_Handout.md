# Assignment 2-Case Study

# Stage 4 Lab Activities

#  Implementing the SmartCare Domain Layer 

DESIGN FIRST \-\> AI PAIR PROGRAMMING \-\> REVIEW \-\> VERIFY | 1hour

# **A \- Revisit Approved UML**

Confirm responsibilities, attributes and relationships before coding.

# **B \- Implement Patient: AI OFF**

Implement Patient with type hints and basic validation. 

# **C \- Implement Practitioner: AI OFF**

Implement Practitioner with identifier, name and specialty; no database logic.

# **D \- Implement Appointment: AI ON**

Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception.

# **E \- Review Generated Code**

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling.

# **F \- Manual Behaviour Checks**

Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition.

# **G \- Refactor**

Remove unnecessary code and make implementation simpler and design-consistent.

# **H \- AI Engineering Log**

Record prompt, generated contribution, decisions and verification evidence.

# **Suggested AI prompt**

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

# **Reflection**

**Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?**

I rejected the first appointment class code as it was effectively a class skeleton, and was missing all the key features I asked it to make. The second generated appointment class had the key features however it didn’t store the appointments so I modified it.

The approved design constrained the AI to only thinking in the box of the brief however it still wanted to change things unnecessarily to incorporate different appointment attributes outside of the scope of the assignment. 