# Reschedule Appointment Skill

Use this skill whenever a patient wants to reschedule an appointment.

Examples:

* reschedule my appointment
* change my appointment
* move my appointment
* change booking
* reschedule tomorrow appointment

---

# Security Rule

Appointment information is private.

Never reveal appointments belonging to other patients.

Never reschedule appointments without patient verification.

---

# Patient Verification

Before accessing appointments, collect:

* Patient Name
* Phone Number

If either is missing, ask for it.

Examples:

* "Please provide your name and registered phone number."
* "May I have your registered phone number?"

Never continue without verification.

---

# Appointment Retrieval

After verification:

* call get_patient_appointments

This tool returns only active BOOKED appointments.

Never use:

* get_appointment_history

for rescheduling.

Never show:

* CANCELLED appointments
* COMPLETED appointments
* NO_SHOW appointments

---

# No Active Appointments

If no active appointments exist:

"I couldn't find any active appointments associated with your information."

Stop the flow.

---

# Single Active Appointment

Display:

* Doctor
* Date
* Time
* Status

Ask:

"Would you like to reschedule this appointment?"

---

# Multiple Active Appointments

Display all active appointments.

Example:

1. Dr. Sindhura Mandava — 2026-06-21 — 02:00 PM
2. Dr. Ravi Kumar — 2026-06-25 — 11:00 AM

Ask:

"Which appointment would you like to reschedule?"

Never guess.

Never assume.

---

# New Appointment Date

Ask:

"What date would you like to reschedule to?"

Accept:

* today
* tomorrow
* day after tomorrow
* specific date

Past dates are not allowed.

---

# Same-Day Time Change

If the patient asks:

* change only the time
* same day
* same date
* move to 1 PM
* reschedule to 2 PM

Then:

* keep the existing appointment date
* ask only for the new slot if needed

Example:

User:
"Reschedule to 2 PM."

Agent:
"The appointment date will remain 2026-06-22.

Available slots:

* 11:00 AM
* 02:00 PM

Would you like 02:00 PM?"

Do not ask for a new date if the patient only wants to change the time.

---

# Available Slots

After receiving the new date:

* call get_available_slots

Display only available slots.

Example:

Available slots:

* 11:00 AM
* 12:00 PM
* 02:00 PM

Ask:

"Which slot would you prefer?"

---

# Reschedule Summary

Before calling the tool, display:

* Patient Name
* Phone Number
* Doctor
* Old Date
* Old Time
* New Date
* New Time

Ask:

"Would you like me to confirm this rescheduling?"

---

# Valid Confirmations

Valid confirmations:

* yes
* confirm
* proceed
* go ahead
* reschedule it

Invalid confirmations:

* okay
* fine
* sure
* maybe

If unclear, ask again.

---

# Tool Rules

Never call:

* reschedule_patient_appointment

until:

* patient identity is verified
* active appointment is selected
* new date is collected
* new slot is selected
* summary has been shown
* explicit confirmation has been received

Never:

* reschedule CANCELLED appointments
* reschedule COMPLETED appointments
* reschedule NO_SHOW appointments
* guess appointment IDs
* assume patient identity
* reveal another patient's appointments

Only active BOOKED appointments may be rescheduled.
