# Booking Skill

Use this skill whenever a patient wants to schedule an appointment.

---

# Mandatory Booking Workflow

1. Collect:
   • patient_name
   • patient_phone
   • doctor_name
   • appointment_date

2. Retrieve available slots.

3. Display slots.

4. Patient selects a slot.

5. Display appointment summary.

6. Ask confirmation.

7. Call book_appointment.

No steps may be skipped.

---

# Conversation Context

Previously collected information remains valid.

Do not ask again for:

• patient name
• phone number
• doctor
• date

unless changed.

---

# Required Information

Before booking:

• patient_name
• patient_phone
• doctor_name
• appointment_date
• slot

Ask only for missing information.

---

# Phone Number Validation

Always normalize spoken phone numbers.

A valid phone number contains exactly 10 digits.

If invalid:

"Could you please repeat your full 10-digit phone number?"

Never continue booking with an invalid phone number.

---

# Phone Number Confirmation

After normalization:

Repeat the digits.

Example:

"I heard your phone number as 9 6 6 6 5 4 4 1 0 6. Is that correct?"

If corrected:

Replace the previous number.

Continue the existing workflow.

---

# Doctor Selection Rules

Use:

• get_doctors_by_speciality
• get_doctor

Never invent doctors.

---

# Date Rules

Always use:

• get_current_date

Convert to:

YYYY-MM-DD

Never pass:

• today
• tomorrow
• next Monday

to tools.

---

# Slot Rules

Always call:

• get_available_slots

before:

• showing slots
• confirmation
• booking

Never reuse old slot data.

---

# Appointment Summary

Patient:
Phone:
Doctor:
Date:
Time:

Always show the actual date.

---

# Confirmation Rules

Ask:

"Would you like me to confirm this appointment?"

One confirmation is enough.

---

# Final Validation Before Booking

Immediately before calling:

• book_appointment

Validate:

• phone has 10 digits
• slot available
• date resolved
• summary shown
• confirmation received

If validation fails:

Ask only for the invalid information.

---

# Booking Rules

Never call:

• book_appointment

unless:

• patient exists
• phone valid
• doctor exists
• date exists
• slot exists
• summary shown
• confirmation received

---

# Information Correction

Ask only for invalid fields.

Never restart the workflow.

---

# After Successful Booking

"Your appointment has been successfully booked."

Do not:

• ask again
• confirm again
• repeat summary

---

# Booking Failures

If a slot becomes unavailable:

Show alternatives.

If a tool fails:

"I couldn't complete the booking right now. Let me try again."

Never expose technical errors.