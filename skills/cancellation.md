# Cancellation Skill

Use this skill whenever a patient wants to cancel an appointment.

Examples:

• cancel my appointment
• cancel tomorrow appointment
• cancel the cardiologist appointment
• cancel my latest appointment
• cancel it
• cancel that appointment

---

# Patient Verification

Required:

• patient_name
• patient_phone

If already verified during the conversation:

Do not ask again.

Ask only for missing information.

---

# Selected Appointment Priority

If an appointment has already been selected:

Reuse:

• doctor
• date
• slot

Examples:

• cancel it
• cancel that appointment
• cancel the same appointment

Use the selected appointment.

Do not ask again.

---

# Appointment Retrieval

If no appointment is currently selected:

Call:

• get_patient_appointments

Only BOOKED appointments may be cancelled.

If no appointments exist:

"I couldn't find any active appointments."

Stop the workflow.

---

# Multiple Appointments

If multiple appointments exist:

Display:

1. Doctor — Date — Time
2. Doctor — Date — Time

Ask:

"Which appointment would you like to cancel?"

Never guess.

The selected appointment becomes:

• selected doctor
• selected date
• selected slot

---

# Date Resolution

If the patient says:

• tomorrow appointment
• today's appointment
• Monday appointment

Always use:

• get_current_date

Resolve the actual calendar date.

Match against appointment dates.

---

# Cancellation Summary

Before cancellation display:

Patient:
Doctor:
Date:
Time:

Always display actual calendar dates.

Example:

Doctor: Dr. Ravi Kumar

Date: June 22, 2026

Time: 03:00 PM

Ask:

"Would you like me to cancel this appointment?"

---

# Confirmation Rules

Valid confirmations:

• yes
• confirm
• proceed
• cancel it
• go ahead
• yes please

Only one confirmation is required.

---

# Tool Rules

Call:

• cancel_patient_appointment

only after:

• patient verified
• doctor selected
• appointment date selected
• appointment slot selected
• summary shown
• confirmation received

Required arguments:

• patient_name
• patient_phone
• doctor_name
• appointment_date
• slot

Never guess values.

Use the selected appointment values.

---

# Tool Failure

If cancellation fails:

"I couldn't cancel that appointment right now."

If the appointment still exists:

Retry using the selected appointment.

---

# Success Response

"Your appointment with Dr. ______ on June 22, 2026 at 3:00 PM has been successfully cancelled."

Ask:

"Would you like any further assistance?"

---

# Restrictions

Never:

• ask for verification twice
• ask for the doctor again
• ask for the appointment date again
• ask for the slot again
• expose another patient's appointments
• reveal internal information

Previously selected appointments always have priority.