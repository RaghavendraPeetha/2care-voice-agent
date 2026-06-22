# Booking Skill

Use this skill whenever a patient wants to schedule an appointment.

Examples:

* book an appointment
* schedule a consultation
* I need a cardiologist
* book Dr Sindhura tomorrow
* book a dermatologist
* I need an appointment

---

# Mandatory Booking Workflow

The booking workflow is sequential.

The following steps MUST occur in order.

STEP 1:
Collect:

* patient_name
* patient_phone
* doctor_name
* appointment_date

STEP 2:
Call:

* get_available_slots

STEP 3:
Display available slots.

STEP 4:
Wait for the patient to select a slot.

STEP 5:
Display the appointment summary.

STEP 6:
Ask for confirmation.

STEP 7:
Call book_appointment.

No step may be skipped.

Never automatically select a slot.

Never automatically create an appointment.

---

# Required Information

Before booking, collect:

* patient_name
* patient_phone
* doctor_name
* appointment_date
* slot

Ask only for missing information.

Do not ask for information that has already been collected.

Remember information throughout the conversation.

Never invent:

* patient names
* phone numbers
* dates
* slots

Never use:

* User
* Patient
* Unknown

as patient names.

---

# Doctor Selection Rules

If the patient mentions a speciality:

* cardiologist
* dermatologist
* neurologist
* gastroenterologist

Use:

* get_doctors_by_speciality

If the patient requests:

* best doctor
* experienced doctor
* senior doctor

Recommend the most experienced doctor.

If the patient provides a partial doctor name:

* Dr Ravi
* Ravi
* Sindhura

Use:

* get_doctor

If one doctor matches:

Use that doctor.

If multiple doctors match:

Ask the patient to choose.

Always use the complete doctor name returned by the database.

Never invent doctor names.

---

# Date Rules

Always use:

* get_current_date

when the patient says:

* today
* tomorrow
* next Monday
* this Friday
* weekend

Convert dates to:

YYYY-MM-DD

Never send relative dates to tools.

Never pass:

* today
* tomorrow
* next Monday

to booking tools.

---

# Slot Rules

Always call:

* get_available_slots

before:

* displaying slots
* final confirmation
* booking

Never invent slots.

Never create slots from OPD timings.

Slots returned by the tool are the only source of truth.

---

# Time Preference Rules

If the patient says:

* morning

Show only morning slots.

If the patient says:

* afternoon

Show only afternoon slots.

If the patient says:

* evening

Show only evening slots.

If multiple slots match:

Ask the patient to choose.

Example:

Available afternoon slots:

* 01:00 PM
* 02:00 PM
* 03:00 PM

Which time would you prefer?

If only one slot matches:

Suggest it and wait for confirmation.

Never automatically choose a slot.

---

# Missing Information

Ask only for missing fields.

Examples:

Known:

* doctor
* date

Missing:

* name
* phone

Ask:

"May I have your name and phone number?"

Do not ask separately.

Ask one question at a time.

---

# Appointment Summary

Before booking, always display:

Patient:
Phone:
Doctor:
Date:
Time:

Example:

Patient: Raghavendra
Phone: 9666544106
Doctor: Dr Bharat Vijay Purohit
Date: 2026-06-22
Time: 03:00 PM

---

# Confirmation Rules

After displaying the summary ask:

"Would you like me to confirm this appointment?"

Valid confirmations:

* yes
* confirm
* proceed
* book it
* go ahead
* okay
* sure
* yes please
* please confirm

Only one confirmation is required.

Never ask for confirmation twice.

---

# Booking Rules

Call book_appointment only if:

* patient_name exists
* patient_phone exists
* doctor_name exists
* appointment_date exists
* slot exists
* slot is available
* appointment summary has been shown
* confirmation has been received

Booking is forbidden if any information is missing.

Never:

* assume the earliest slot
* choose 10 AM automatically
* create appointments silently

---

# After Successful Booking

After book_appointment succeeds:

Say:

"Your appointment has been successfully booked."

Do not:

* ask for the phone number again
* ask for confirmation again
* display the summary again
* recheck slots

The booking process is complete.

---

# Booking Failures

If a slot becomes unavailable:

Show alternative slots.

If information is missing:

Ask only for the missing information.

If a temporary issue occurs:

Say:

"I couldn't complete the booking right now. Let me try again."

Never say:

* Internal Server Error
* Tool failed
* System error
* Technical error

---

# Critical Restrictions

Never call:

* book_appointment

until ALL of the following are true:

* doctor selected
* date selected
* slot selected
* summary shown
* confirmation received

If the patient has not selected a slot:

DO NOT BOOK.

If the patient has not confirmed:

DO NOT BOOK.

If the slot is unavailable:

DO NOT BOOK.

If any information is missing:

CONTINUE THE CONVERSATION.

Never skip steps.
