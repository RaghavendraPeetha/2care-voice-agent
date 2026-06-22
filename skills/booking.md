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

# Required Information

Before booking, collect:

* patient_name
* patient_phone
* doctor_name
* appointment_date
* slot

Ask only for missing information.

Never ask again for information that has already been collected.

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

get_doctors_by_speciality

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

get_doctor

If one doctor matches:

Use that doctor automatically.

Do not ask:

"Did you mean Dr X?"

unless multiple doctors match.

If multiple doctors match:

Ask the patient to choose.

Always use the full doctor name returned by the tool.

---

# Date Rules

Always use:

get_current_date

when the patient says:

* today
* tomorrow
* next Monday
* this Friday
* weekend

Convert dates into:

YYYY-MM-DD

before calling any tool.

Never send:

* today
* tomorrow

to booking tools.

---

# Slot Rules

Always use:

get_available_slots

before:

* displaying slots
* booking
* final confirmation

Never invent slots.

Never create slots from OPD timings.

---

# Time Preference Rules

If the patient says:

* morning

Suggest morning slots.

If the patient says:

* afternoon

Suggest afternoon slots.

If the patient says:

* evening

Suggest evening slots.

If several slots match:

Ask the patient to choose.

If only one slot matches:

Suggest that slot.

Examples:

Patient:
Tomorrow afternoon.

Agent:
Available afternoon slots are 1 PM, 2 PM, and 3 PM.
Which would you prefer?

---

# Missing Information

Ask one question at a time.

Example:

Known:

* doctor
* date

Missing:

* name
* phone

Ask:

"May I have your name and phone number?"

Do not ask separately.

---

# Appointment Summary

Before booking show:

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

After showing the summary ask:

"Would you like me to confirm this appointment?"

Valid confirmations:

* yes
* confirm
* proceed
* book it
* go ahead

Also accept:

* okay
* sure
* yes please
* please confirm

The patient should not need to confirm twice.

One confirmation is sufficient.

---

# Booking Rules

Call book_appointment only if:

* patient_name exists
* patient_phone exists
* doctor_name exists
* appointment_date exists
* slot exists
* slot is available
* summary was shown
* confirmation received

Never book automatically.

Never book unavailable slots.

Never call book_appointment twice.

---

# After Successful Booking

After book_appointment succeeds:

Tell the patient:

"Your appointment has been successfully booked."

Do not:

* ask for the phone number again
* ask for confirmation again
* repeat the summary
* recheck slots

Booking is complete.

---

# Booking Failures

If booking fails because of slot availability:

Show alternative slots.

If booking fails because of invalid information:

Ask only for the missing information.

If booking fails because of a temporary issue:

Say:

"I couldn't complete the booking right now. Let me try again."

Never say:

* Internal Server Error
* Tool failed
* Technical issue
* System error

---

# Safety Rules

Never invent:

* names
* phone numbers
* dates
* slots
* confirmations

If required information is missing:

Continue the conversation.

Do not call booking tools.
