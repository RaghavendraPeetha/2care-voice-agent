# Booking Skill

Use this skill whenever a patient wants to schedule an appointment.

Examples:

• book an appointment
• schedule a consultation
• book tomorrow
• I need an appointment
• book a cardiologist
• book Dr. Sindhura

---

# Mandatory Booking Workflow

1. Collect missing information.
2. Identify the doctor.
3. Resolve the appointment date.
4. Retrieve available slots.
5. Patient selects a slot.
6. Show appointment summary.
7. Ask for confirmation.
8. Call book_appointment.

No workflow steps may be skipped.

Never automatically select a slot.

Never automatically create an appointment.

---

# Conversation Context

Previously collected information remains valid.

Remember:

• patient_name
• patient_phone
• selected_doctor
• appointment_date
• appointment_slot

Examples:

User:
"Book it tomorrow."

Use the selected doctor.

User:
"Move it to afternoon."

Use the selected doctor and date.

User:
"Book 4 PM."

Use the current doctor and date.

Do not ask again for information that already exists.

---

# Required Information

Before booking:

• patient_name
• patient_phone
• doctor_name
• appointment_date
• slot

Ask only for missing information.

Never invent:

• names
• phone numbers
• doctors
• dates
• slots

---

# Missing Information Rules

If both name and phone are missing:

"May I have your name and phone number?"

If only one field is missing:

Ask only for that field.

Never restart the booking process.

---

# Phone Number Rules

Always use:

• normalize_phone_number

before validating the phone number.

The normalized result must contain exactly 10 digits.

If invalid:

"Could you please repeat your full 10-digit phone number?"

Never guess digits.

Never continue booking with an invalid number.

---

# Phone Number Confirmation

After normalization:

Repeat the digits.

Example:

"I heard your phone number as 9 5 4 2 4 2 0 5 5 0. Is that correct?"

The phone number becomes verified only after confirmation.

If corrected:

Replace the previous number.

Do not continue booking until the phone number has been confirmed.

Continue the existing workflow.

---

# Doctor Selection

If the patient mentions a specialty:

Use:

• get_doctors_by_speciality

If the patient mentions a doctor name:

Use:

• get_doctor

If exactly one doctor matches:

Use that doctor.

If multiple doctors match:

Display the matching doctors.

Ask the patient to choose.

Never invent doctor names.

---

# Doctor Availability

If the selected doctor has no available slots:

Inform the patient.

Example:

"Dr. Sagari Gullapalli does not have any available appointments on June 22, 2026."

The patient may:

• choose another date
• choose another doctor

Do not automatically select another doctor.

---

# Date Rules

Always use:

• get_current_date

for:

• today
• tomorrow
• next Monday
• next week

Convert all dates to:

YYYY-MM-DD

Never pass relative dates to tools.

---

# Slot Rules

Always call:

• get_available_slots

before:

• showing slots
• confirmation
• booking

Never reuse previously shown slots.

Only returned slots may be booked.

---

# Time Preference Rules

Patients may say:

• morning
• afternoon
• evening

These are preferences, not appointment times.

Morning:
before 12 PM

Afternoon:
12 PM to 4 PM

Evening:
after 4 PM

If multiple slots match:

Display the matching slots.

Example:

Available afternoon slots:

• 01:00 PM
• 02:00 PM
• 03:00 PM

Which time would you prefer?

Never automatically choose a slot.

---

# Unavailable Slot

If the requested slot is unavailable:

Show available alternatives.

Example:

"The 10:00 AM slot is unavailable.

Available slots:

• 11:00 AM
• 12:00 PM
• 02:00 PM"

Ask the patient to choose.

Never automatically change the appointment.

---

# Appointment Summary

Before booking, always display:

Patient:
Doctor:
Date:
Time:

Example:

Patient: Raghavendra

Doctor: Dr. Sagari Gullapalli

Date: June 22, 2026

Time: 04:00 PM

Would you like me to confirm this appointment?

Always display actual dates.

Never display:

• tomorrow
• next Monday

in the final summary.

---

# Confirmation Rules

Ask:

"Would you like me to confirm this appointment?"

One confirmation is sufficient.

Valid confirmations:

• yes
• confirm
• proceed
• book it
• go ahead
• yes please

Do not ask for confirmation twice.

---

# Final Validation

Before calling:

• book_appointment

Verify:

• patient exists
• phone number is valid
• doctor exists
• date exists
• slot exists
• slot is available
• summary has been shown
• confirmation has been received

---

# Information Correction

If validation fails:

Ask only for the invalid information.

Examples:

Invalid phone:
Ask for the phone number.

Invalid date:
Ask for the date.

Invalid slot:
Show available slots.

Never restart the workflow.

Never ask again for verified information.

---

# Booking Success

After a successful booking:

"Your appointment has been successfully booked."

Ask:

"Would you like any further assistance?"

Do not:

• ask for confirmation again
• repeat the summary
• ask for the phone number again

---

# Booking Failures

If a slot becomes unavailable:

Show alternative slots.

If a temporary problem occurs:

"I couldn't complete the booking right now. Let me try again."

Never expose:

• technical errors
• tool failures
• internal messages

---

# Critical Restrictions

Never call:

• book_appointment

unless:

• patient verified
• phone validated
• doctor selected
• date selected
• slot selected
• summary shown
• confirmation received

Never:

• choose a slot automatically
• create appointments silently
• skip workflow steps
