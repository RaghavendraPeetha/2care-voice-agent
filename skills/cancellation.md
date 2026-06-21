# Cancellation Skill

Use this skill whenever a patient wants to cancel appointments.

Examples:

* cancel my appointment
* cancel booking
* cancel tomorrow appointment
* cancel all appointments
* cancel everything
* cancel all bookings

---

# Intent Preservation

Determine whether the user intends:

* Single appointment cancellation
* Multiple appointment cancellation
* Cancel all appointments

Once identified, preserve this intent throughout the conversation.

Never forget the original request.

Examples:

User: "Cancel all appointments."

Even after collecting name and phone number, the intent remains:

* cancel all appointments

Do not downgrade a bulk cancellation request into a single appointment cancellation.

---

# Patient Verification

Before accessing or cancelling any appointment, the patient's identity must be verified.

Required information:

* Patient Name
* Phone Number

If either is missing, ask for it.

Examples:

* "Please provide your name and phone number to locate your appointments."
* "May I have your registered phone number?"

Never retrieve, display, or cancel appointments without patient verification.

---

# Appointment Lookup

After receiving:

* Patient Name
* Phone Number

Use:

* get_patient_appointments

Retrieve all appointments belonging to the patient.

If no appointments are found:

* inform the patient
* stop the cancellation flow

Example:

"I couldn't find any appointments associated with this name and phone number."

---

# Appointment Display

Display:

* Patient Name
* Doctor
* Date
* Time
* Status

Never cancel immediately.

---

# Single Appointment Cancellation

If only one appointment exists:

Display the appointment details.

Ask:

"Would you like me to cancel this appointment?"

Only after confirmation may cancellation occur.

---

# Multiple Appointments

If multiple appointments exist and the user did NOT request bulk cancellation:

* display all appointments
* assign numbers

Example:

1. Dr. Sindhura — June 21 — 12:00 PM
2. Dr. Ravi Kumar — June 25 — 11:00 AM

Ask:

"Which appointment would you like to cancel?"

Never guess.

Never assume.

---

# Bulk Cancellation

If the original request was:

* cancel all appointments
* cancel everything
* cancel all bookings

Always:

1. Verify patient identity.
2. Retrieve all appointments.
3. Display all appointments.
4. Ask:

"Would you like me to cancel all of these appointments?"

Only after explicit confirmation:

* yes
* confirm
* proceed
* cancel them
* go ahead

may all appointments be cancelled.

Never ask which appointment to cancel.

Never downgrade to a single appointment flow.

---

# Valid Confirmations

Valid confirmations:

* yes
* confirm
* proceed
* cancel it
* cancel them
* go ahead

---

# Invalid Confirmations

These are NOT confirmations:

* ok
* okay
* fine
* sure
* maybe

Ask again.

Example:

"Please reply with 'yes' or 'confirm' to proceed."

---

# Security Rules

Never:

* cancel another patient's appointment
* reveal appointment information without verification
* guess appointment IDs
* assume patient identity
* display all patients' appointments

Patient verification is mandatory.

---

# Tool Rules

Never call:

- get_patient_appointments
- cancel_patient_appointment

until:

- patient name has been collected
- phone number has been collected

Never call cancel_patient_appointment until:

- appointment has been identified
- appointment details have been shown
- explicit confirmation has been received

Required arguments:

- patient_name
- patient_phone
- doctor_name
- appointment_date
- slot

Never guess values.

Never cancel multiple appointments with one tool call.
