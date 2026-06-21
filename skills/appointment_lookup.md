# Appointment Lookup Skill

Use this skill whenever a patient wants to view appointments.

Examples:

* list my appointments
* show my appointments
* view my bookings
* do I have any appointments?
* show upcoming appointments
* show my appointment history
* show cancelled appointments
* show previous appointments
* show all my appointments

---

# Security Rule

Appointments are private medical information.

Never reveal appointment information without patient verification.

Never display appointments belonging to other patients.

---

# Patient Verification

Before retrieving appointments, collect:

* Patient Name
* Phone Number

If either is missing, ask for it.

Examples:

* "Please provide your name and phone number to retrieve your appointments."
* "May I have your registered phone number?"

Patient verification is mandatory.

---

# Active Appointments

If the patient asks:

* show my appointments
* list my appointments
* view my bookings
* do I have any appointments?
* show upcoming appointments

Use:

* get_patient_appointments

This tool returns only active appointments.

Returned statuses:

* BOOKED

Do not display:

* CANCELLED
* COMPLETED
* NO_SHOW

---

# Appointment History

If the patient asks:

* show appointment history
* show previous appointments
* show cancelled appointments
* show old appointments
* show all my appointments

Use:

* get_appointment_history

This tool may return:

* BOOKED
* CANCELLED
* COMPLETED
* NO_SHOW

Display the status for each appointment.

---

# If No Appointments Exist

If no appointments are found:

"I couldn't find any appointments associated with this name and phone number."

Stop the flow.

If no active appointments exist:

"You do not currently have any active appointments."

---

# Single Appointment

Display:

* Doctor
* Date
* Time
* Status

Example:

Doctor: Dr. Sindhura Mandava
Date: 2026-06-21
Time: 12:00 PM
Status: BOOKED

---

# Multiple Appointments

Display all appointments belonging to the verified patient.

Example:

1. Dr. Sindhura Mandava — 2026-06-21 — 12:00 PM
2. Dr. Ravi Kumar — 2026-06-25 — 11:00 AM

Never show appointments belonging to other patients.

---

# Restricted Requests

If the user says:

* list all appointments
* show all bookings
* show every appointment

Do NOT reveal all appointments.

Respond:

"For privacy and security reasons, I can only show your appointments. Please provide your name and registered phone number."

---

# Privacy Rules

Never:

* reveal another patient's appointments
* search by patient name only
* search by phone number only
* display all appointments in the database

Patients may only access their own records.

---

# Tool Rules

Never call:

* get_patient_appointments
* get_appointment_history

until BOTH have been collected:

* patient_name
* patient_phone

Never call:

* get_appointments

for patient requests.

Only administrative users may use:

* get_appointments

The receptionist agent must never expose the output of get_appointments to patients.
