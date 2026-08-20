# 📊 Week 4 - Day 5: System Analysis & UML Diagrams

Welcome to Day 5! Today's focus shifted from writing code to **Software Engineering and System Design**. Before building a system, it is crucial to understand its requirements, user interactions, and underlying architecture. 

In this folder, you will find the system design documentation for a **School Management System**, specifically detailing the "Add Student" feature.

## 🛠️ Diagrams Included

*   **Use Case Diagram:** 
    Visualizes the system's functional requirements from the user's perspective. It maps out how an `Admin` interacts with the system, including core actions like `Login` and `Add Student`, alongside `<<include>>` and `<<extend>>` relationships for validation and messaging.
    
*   **Activity Diagram:** 
    Illustrates the dynamic behavior and workflow of the "Add Student" process. It maps the step-by-step execution flow, from data entry to the decision node (checking if the information is valid), branching into either a successful save or an error state.
    
*   **Class Diagram:** 
    Defines the static structure and object-oriented architecture of the system. It breaks down the system into distinct entities (`Student`, `Admin`, `Course`, `Classroom`) and separates concerns by introducing structural classes like `Validator` (for data integrity) and `StudentRepository` (for database operations).

---
*Proper system design using UML ensures that the code we write is scalable, maintainable, and aligned with business logic.*