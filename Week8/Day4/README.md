# Medical Appointment System - Database Design Lab

## Overview
This repository documents the Entity-Relationship (ER) modeling and logical database design for a clinic or hospital appointment system[cite: 14]. The project showcases the progression from an initial schema to a refined, normalized architecture[cite: 14].

## Phase 1: Initial Database Schema
The foundational architecture consists of four primary entities and their relationships[cite: 14]:

### 1. Patient Entity
*   **PatientID**: Primary Key (PK)[cite: 14].
*   **Name**: Requires a value (Not Null)[cite: 14].
*   **Phone**: Must be unique[cite: 14]. *Note: The documentation highlights that phone numbers are unstable attributes because they can change at any time*[cite: 14].
*   **DOB**: Date of Birth[cite: 14].
*   *Example Record*: PatientID: 101, Name: Maha, Phone: 0551234567, DOB: 12/05/2000[cite: 14].

### 2. Doctor Entity
*   **DocID**: Primary Key (PK)[cite: 14].
*   **Name**: Requires a value (Not Null)[cite: 14].
*   **Speciality**: Initially designed as a simple attribute because it directly describes the doctor and did not require independent records in the first scenario[cite: 14].

### 3. Appointment Entity
*   **Appointment_No**: Primary Key (PK)[cite: 14].
*   **Date** and **Time**[cite: 14].
*   **Status**: Requires a value (Not Null)[cite: 14].
*   **PatientID**: Foreign Key (FK) linking the appointment to a specific patient[cite: 14].
*   **DocID**: Foreign Key (FK) linking the appointment to a specific doctor[cite: 14].

### 4. Medical Profile Entity
*   **Medical_profile_id**: Primary Key (PK)[cite: 14].
*   **PatientID**: Foreign Key (FK) linking the profile to a patient[cite: 14].

## Relationships & Business Rules
The logical flow of the system is governed by the following rules[cite: 14]:
*   **Patient to Appointments (1 to 0..*)**: A single patient may book several appointments (zero to many)[cite: 14]. Conversely, each appointment belongs to exactly one patient[cite: 14].
*   **Doctor to Appointments (1 to 0..*)**: One doctor can be assigned to zero or many appointments[cite: 14]. Each appointment belongs to exactly one doctor[cite: 14].
*   **Patient to Medical Profile (1 to 0..1)**: One patient can have up to one (zero or one) medical profile[cite: 14].
*   **Core Logic**: Every appointment is strictly defined as an event between one patient and one doctor[cite: 14].

## Phase 2: Schema Normalization (Exercise 2)
In the second exercise, the schema is refined to reduce redundancy and improve structure[cite: 14]. 

**Extracting Specialities:**
Instead of storing the specialty as a simple text attribute in the Doctor table, it is extracted into a dedicated table[cite: 14]:
*   **sepcialities Table**: Created with `sepciality_ID` as the Primary Key (PK) and `sepciality_name` as an attribute[cite: 14].
*   **Updated Doctors Table**: The `DocID` remains the Primary Key (PK), and `Name` remains Not Null[cite: 14]. However, it now uses `sepciality_ID` as a Foreign Key (FK) to link to the new specialities table[cite: 14].