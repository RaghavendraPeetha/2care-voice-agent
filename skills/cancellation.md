# Cancellation Skill

Use this skill whenever the patient wants to cancel appointments.

Examples:

* cancel my appointment
* cancel booking
* cancel tomorrow appointment
* cancel my latest appointment
* cancel all appointments
* cancel everything
* cancel all bookings

---

# Intent Preservation

Determine the cancellation intent immediately.

Possible intents:

* single appointment
* specific appointment
* latest appointment
* tomorrow appointment
* all appointments

Never forget the original intent.

Example:

User:

"Cancel all appointments."

The agent must continue the bulk cancellation flow even after verification.

---

# Patient Verification

Required:

* patient_name
* patient_phone

If already collected during the current conversation:

Do not ask again.

The verified patient identity remains valid during the session.

Ask only for missing information.

Examples:

"May I have your registered phone number?"

"May I have your name?"

---

# Appointment Lookup

After verification:

Use:

get_patient_appointments

Retrieve all active appointments.

If none exist:

"I couldn't find any active appointments."

Stop the flow.

---

# Display Appointments

Display:

Doctor:
Date:
Time:

Example:

1. Dr. Bharat Vijay Purohit
   June 22, 2026
   03:00 PM

2. Dr. Gopi Krishna Rayidi
   June 25, 2026
   11:00 AM

Never cancel immediately.

---

# Single Appointment

If only one active appointment exists:

Display the appointment.

Ask:

"Would you like me to cancel this appointment?"

Wait for confirmation.

---

# Specific Appointment Requests

Examples:

* cancel tomorrow appointment
* cancel the cardiologist appointment
* cancel the 3 PM appointment

If one appointment matches:

Display it.

Ask for confirmation.

If multiple appointments match:

Ask the patient which appointment they mean.

Never guess.

---

# Latest Appointment

Examples:

* cancel my latest appointment
* cancel my recent booking

Choose the most recent upcoming appointment.

Display it.

Ask:

"Would you like me to cancel this appointment?"

---

# Multiple Appointments

If several appointments exist and the patient did not specify one:

Display all appointments.

Ask:

"Which appointment would you like to cancel?"

Number the appointments.

---

# Bulk Cancellation

Examples:

* cancel all appointments
* cancel everything
* cancel all bookings

Steps:

1. Verify patient.
2. Retrieve appointments.
3. Display all appointments.
4. Ask:

"Would you like me to cancel all of these appointments?"

Only after confirmation may appointments be cancelled.

Never downgrade to a single appointment flow.

---

# Valid Confirmations

Only:

* yes
* confirm
* proceed
* cancel it
* cancel them
* go ahead

are valid confirmations.

---

# Invalid Confirmations

Not confirmations:

* okay
* ok
* fine
* maybe
* sure
* alright

Ask again.

Example:

"Please say yes or confirm to proceed."

---

# Mandatory Confirmation

Before cancellation:

Display:

Patient Name:
Doctor:
Date:
Time:

Ask:

"Would you like me to cancel this appointment?"

Only after confirmation may the tool be called.

---

# Tool Rules

Never call:

* cancel_patient_appointment

until:

* patient_name exists
* patient_phone exists
* doctor_name exists
* appointment_date exists
* slot exists
* confirmation exists

Required arguments:

* patient_name
* patient_phone
* doctor_name
* appointment_date
* slot

Never guess values.

---

# Privacy Rules

Never:

* reveal another patient's appointments
* search by name only
* search by phone only
* display all appointments
* expose database information

Verification is mandatory.

---

# Voice Recognition Rules

Examples:

* cancel tomorrow one
* cancel the afternoon one
* cancel cardiologist appointment

Use existing appointments to identify the correct booking.

If only one match exists:

Proceed.

If multiple matches exist:

Ask the patient.

Never guess.

---

# Cancellation Success

After successful cancellation:

"Your appointment with Dr. ______ on June 22, 2026 at 3:00 PM has been successfully cancelled."

Ask:

"Would you like any further assistance?"
