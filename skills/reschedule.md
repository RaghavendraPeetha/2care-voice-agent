# Reschedule Appointment Skill

Use this skill whenever a patient wants to modify an existing appointment.

Examples:

* reschedule my appointment
* change my appointment
* move my appointment
* change booking
* change the time
* move it to tomorrow
* reschedule tomorrow appointment
* change to afternoon
* move it to 2 PM

---

# Security Rules

Appointments are private.

Never reveal appointments belonging to other patients.

Patient verification is mandatory.

Never reschedule appointments without verification.

---

# Patient Verification

Collect:

* patient_name
* patient_phone

If either is missing:

"Please provide your name and registered phone number."

Never continue without verification.

---

# Appointment Retrieval

After verification:

Call:

* get_patient_appointments

Only BOOKED appointments may be rescheduled.

Never use:

* get_appointment_history

Never reschedule:

* CANCELLED appointments
* COMPLETED appointments
* NO_SHOW appointments

---

# No Active Appointments

If no active appointments exist:

"I couldn't find any active appointments associated with your information."

Stop the workflow.

---

# Single Appointment

If only one active appointment exists:

Display:

* Doctor
* Date
* Time
* Status

Ask:

"Would you like to reschedule this appointment?"

---

# Multiple Appointments

If multiple active appointments exist:

Display:

1. Doctor — Date — Time
2. Doctor — Date — Time

Ask:

"Which appointment would you like to reschedule?"

Never guess.

---

# Date Changes

Ask:

"What date would you like to reschedule to?"

Accept:

* today
* tomorrow
* next Monday
* day after tomorrow
* specific dates

Use date reasoning.

Past dates are not allowed.

---

# Same-Day Time Changes

If the patient says:

* change only the time
* same day
* move it to 2 PM
* keep the same date
* later that day

Keep the existing appointment date.

Do not ask for another date.

---

# Available Slots

After determining the new date:

Call:

* get_available_slots

Only display returned slots.

Never invent slots.

Never use OPD timings.

---

# Time Expressions

Patients may say:

* morning
* afternoon
* evening
* any slot
* earliest slot
* latest slot

Rules:

If multiple matching slots exist:

Display them.

Example:

Afternoon slots:

* 01:00 PM
* 02:00 PM
* 03:00 PM

Ask:

"Which slot would you prefer?"

If only one matching slot exists, suggest it.

Never automatically select a slot.

---

# Unavailable Slot

If the requested slot is unavailable:

Display available alternatives.

Example:

"The 2 PM slot is unavailable.

Available slots:

* 11:00 AM
* 01:00 PM
* 03:00 PM"

Ask the patient to choose.

Never automatically change appointments.

---

# Same Date and Same Time

If the patient selects the same date and same time:

Respond:

"Your appointment is already scheduled for that date and time."

Do not call the rescheduling tool.

---

# Changing the Doctor

Rescheduling changes only:

* date
* time

Doctor changes require a new booking.

If the patient wants another doctor:

Start a new booking workflow.

---

# Reschedule Summary

Before calling the tool display:

Patient Name:
Phone Number:
Doctor:
Old Date:
Old Time:
New Date:
New Time:

Ask:

"Would you like me to confirm this rescheduling?"

---

# Valid Confirmations

Valid:

* yes
* confirm
* proceed
* go ahead
* reschedule it

Invalid:

* okay
* fine
* sure
* maybe

If unclear:

"Please reply with yes or confirm."

---

# Tool Rules

Never call:

* reschedule_patient_appointment

until:

* patient verified
* appointment selected
* new date selected
* new slot selected
* summary shown
* confirmation received

Required:

* patient_name
* patient_phone
* doctor_name
* old_date
* old_slot
* new_date
* new_slot

Never guess values.

---

# User Changes Mind

If the patient changes:

* doctor
* date
* slot

Use the newest information.

The latest patient request overrides previous choices.

---

# Privacy Rules

Never:

* reveal another patient's appointments
* display all appointments
* guess patient identity
* reveal internal IDs
* expose database information

Only verified patients may reschedule their appointments.

---

# Voice Examples

Examples:

"Move it to tomorrow afternoon."

"Change it to 2 PM."

"Keep the same doctor."

"Move it to the next available slot."

"Any afternoon slot is fine."

Handle these naturally while still requiring explicit confirmation before rescheduling.
