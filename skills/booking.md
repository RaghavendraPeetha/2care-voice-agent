# Booking Skill

Use this skill whenever a patient wants to book an appointment.

Examples:

* book an appointment
* book Dr Sindhura tomorrow
* schedule a consultation
* I need an appointment
* book a cardiologist
* book a dermatologist

---

# Required Information

Before booking an appointment, the following information MUST be known:

* patient_name
* patient_phone
* doctor_name
* appointment_date
* slot

If any information is missing:

* ask only for the missing information
* never ask for information already collected
* never invent values

Never use:

* User
* Patient
* Unknown

as patient names.

---

# Doctor Resolution Rules

If the patient provides a partial doctor name:

Examples:

* Dr Sindhura
* Dr Ravi
* Sindhura

Use get_doctor.

If one doctor matches:

Ask:

"Did you mean Dr. Sindhura Mandava?"

Only after confirmation should the doctor be considered resolved.

Always use the doctor's full name returned by the database.

Never shorten doctor names.

Incorrect:

* Dr. Sindhura
* Dr. Ravi

Correct:

* Dr. Sindhura Mandava
* Dr. Ravi Kumar

---

# Date Rules

Use date reasoning whenever the patient says:

* today
* tomorrow
* next Monday
* this Friday
* weekend

Always use the current system date.

Never invent dates.

Always verify the final appointment date.

---

# Slot Availability Rules

Always use get_available_slots.

Available slots must come only from the tool.

Never invent appointment slots.

Never create slots from OPD timings.

Before booking:

1. Call get_available_slots.
2. Display the slots.
3. Ask the patient to choose one.

Example:

Available slots:

* 11:00 AM
* 12:00 PM
* 01:00 PM
* 02:00 PM

Which time would you prefer?

---

# Mandatory Slot Refresh

Always call get_available_slots before:

* booking
* displaying available slots
* final confirmation

Appointments may change during the conversation.

Never reuse old slot information.

---

# Time Selection Rules

Valid appointment times must exactly match available slots.

Never interpret:

* morning
* afternoon
* evening
* night
* anytime
* after lunch
* before lunch
* later

as appointment times.

If the patient says:

"afternoon"

and multiple afternoon slots exist:

Example:

* 01:00 PM
* 02:00 PM
* 03:00 PM

Ask:

"Which slot would you prefer?"

If only one matching slot exists, that slot may be suggested, but the patient must still confirm it.

Never automatically select a slot.

---

# Missing Information Rules

If information is missing:

Ask only for the missing fields.

Example:

Known:

* doctor
* date

Missing:

* patient name
* phone number
* slot

Ask only for the missing information.

Never display placeholders such as:

* [Your Name]
* [Your Phone Number]

---

# Appointment Summary Rules

Before booking:

Display:

* Patient Name
* Phone Number
* Doctor
* Date
* Time

The doctor name must exactly match the database.

Never display shortened doctor names.

---

# Confirmation Rules

Before calling book_appointment:

Ask:

"Would you like me to confirm this appointment?"

Only the following responses are valid confirmations:

* yes
* confirm
* proceed
* book it
* go ahead

---

# Invalid Confirmations

The following are NOT confirmations:

* ok
* okay
* fine
* sure
* alright
* maybe

If the response is ambiguous:

Ask again.

Example:

User:
ok

Agent:

"Would you like me to confirm this appointment?

Please answer:

* Yes
* Confirm
* Proceed"

Never assume confirmation.

---

# Booking Tool Rules

The booking tool may only be called when:

* patient_name is known
* patient_phone is known
* doctor_name is known
* appointment_date is known
* slot is known
* slot is available
* appointment summary has been shown
* explicit confirmation has been received

Never call book_appointment before confirmation.

Never create appointments automatically.

Never book unavailable slots.

Never book outside available slots.

---

# Safety Rules

Never invent:

* names
* phone numbers
* dates
* slots
* confirmations

Never create appointments with:

* User
* Patient
* Unknown

as patient names.

If information is missing:

Continue the conversation.

Do not call tools.
