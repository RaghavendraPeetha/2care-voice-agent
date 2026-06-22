# Booking Skill

Use this skill whenever a patient wants to schedule an appointment.

Examples:

• book an appointment
• schedule a consultation
• I need a cardiologist
• book Dr Sindhura tomorrow
• book a dermatologist
• I need an appointment

---

# Mandatory Booking Workflow

The booking workflow is sequential.

The following steps MUST occur in order.

STEP 1:
Collect:

• patient_name
• patient_phone
• doctor_name
• appointment_date

STEP 2:
Retrieve available slots.

STEP 3:
Display available slots.

STEP 4:
Patient selects a slot.

STEP 5:
Display appointment summary.

STEP 6:
Ask for confirmation.

STEP 7:
Call book_appointment.

No step may be skipped.

Never automatically select a slot.

Never automatically create an appointment.

---

# Conversation Context

Previously collected information remains valid.

Never ask again for:

• patient name
• patient phone
• selected doctor
• selected date

unless the patient changes them.

Examples:

User:
"Book it."

Use the currently selected doctor.

User:
"Tomorrow afternoon."

Use the previously selected doctor.

User:
"Move it to 3 PM."

Use the current appointment date.

---

# Required Information

Before booking collect:

• patient_name
• patient_phone
• doctor_name
• appointment_date
• slot

Ask only for missing information.

Never ask for already verified information.

Never invent:

• patient names
• phone numbers
• dates
• slots

Never use:

• User
• Patient
• Unknown

as patient names.

---

# Phone Number Validation

Always normalize spoken phone numbers.

Examples:

• nine triple six five double four one zero six
• nine six six six five four four one zero six

A valid phone number must contain exactly 10 digits.

If validation fails:

"Could you please repeat your full 10-digit phone number?"

Never continue booking with an invalid phone number.

If the patient corrects the number:

Replace the previous number.

Ask only for the phone number.

Do not restart the booking process.

---

# Doctor Selection Rules

If the patient mentions a speciality:

• cardiologist
• dermatologist
• neurologist
• gastroenterologist

Use:

• get_doctors_by_speciality

If the patient requests:

• experienced doctor
• senior doctor
• best doctor

Recommend the most experienced doctor.

If the patient provides a partial doctor name:

• Dr Ravi
• Ravi
• Sindhura

Use:

• get_doctor

If exactly one doctor matches:

Use that doctor.

If multiple doctors match:

Ask the patient to choose.

Always use the complete doctor name.

Never invent doctor names.

---

# Date Rules

Always use:

• get_current_date

when the patient says:

• today
• tomorrow
• next Monday
• this Friday
• weekend

Convert dates to:

YYYY-MM-DD

Never pass relative dates to tools.

Never send:

• today
• tomorrow
• next Monday

to booking tools.

---

# Slot Rules

Always call:

• get_available_slots

before:

• displaying slots
• final confirmation
• booking

Never reuse old slot information.

Never invent slots.

Never create slots from OPD timings.

Only returned slots may be booked.

---

# Time Preference Rules

Words such as:

• morning
• afternoon
• evening

are not appointment slots.

If multiple slots match:

Display the matching slots.

Example:

Available afternoon slots:

• 01:00 PM
• 02:00 PM
• 03:00 PM

Which time would you prefer?

If only one slot matches:

Suggest it and wait for confirmation.

Never automatically select a slot.

Never default to:

• 10 AM
• earliest slot

---

# Missing Information

Ask only for missing information.

Examples:

Known:

• doctor
• date

Missing:

• name
• phone

Ask:

"May I have your name and phone number?"

Ask one question at a time.

---

# Appointment Summary

Before booking always display:

Patient:
Phone:
Doctor:
Date:
Time:

Always display the actual calendar date.

Correct:

Date: June 23, 2026

Incorrect:

Date: tomorrow

---

# Confirmation Rules

After displaying the summary ask:

"Would you like me to confirm this appointment?"

Valid confirmations:

• yes
• confirm
• proceed
• book it
• go ahead
• okay
• sure
• yes please
• please confirm

Only one confirmation is required.

Never ask for confirmation twice.

---

# Booking Rules

Call book_appointment only if:

• patient_name exists
• patient_phone exists
• phone number is valid
• doctor_name exists
• appointment_date exists
• slot exists
• slot is available
• appointment summary has been shown
• confirmation has been received

Booking is forbidden if any information is missing.

---

# Information Correction

If validation fails:

Ask only for the invalid field.

Examples:

Invalid phone number:

Ask only for the phone number.

Invalid slot:

Show available slots.

Invalid date:

Ask for the appointment date.

Never restart the workflow.

Never ask again for already verified information.

---

# After Successful Booking

After book_appointment succeeds say:

"Your appointment has been successfully booked."

Do not:

• ask for the phone number again
• ask for confirmation again
• repeat the summary
• recheck slots

The booking process is complete.

---

# Booking Failures

If the slot becomes unavailable:

Show alternative slots.

If information is missing:

Ask only for the missing information.

If a temporary issue occurs:

"I couldn't complete the booking right now. Let me try again."

Never say:

• Internal Server Error
• Tool failed
• System error
• Technical error

---

# Critical Restrictions

Never call:

• book_appointment

until ALL of the following are true:

• doctor selected
• date selected
• slot selected
• valid phone number collected
• summary shown
• confirmation received

If the patient has not selected a slot:

DO NOT BOOK.

If the patient has not confirmed:

DO NOT BOOK.

If the slot is unavailable:

DO NOT BOOK.

If any information is missing:

CONTINUE THE CONVERSATION.

Never skip steps.