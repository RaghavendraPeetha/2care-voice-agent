# Reschedule Appointment Skill

Use this skill whenever a patient wants to modify an existing appointment.

Examples:

• reschedule my appointment
• change my appointment
• move my appointment
• change booking
• change the time
• move it to tomorrow
• reschedule tomorrow appointment
• change to afternoon
• move it to 2 PM

---

# Security Rules

Appointments are private.

Never reveal another patient's appointments.

Patient verification is mandatory.

Never reschedule appointments without verification.

---

# Patient Verification

Required:

• patient_name
• patient_phone

If already verified during the current conversation:

DO NOT ask again.

Verified patient information remains valid for the entire session.

Ask only for missing information.

---

# Previously Selected Appointment

If an appointment has already been retrieved:

Reuse:

• doctor
• date
• slot

Examples:

User:
"Reschedule it."

User:
"Move that appointment."

User:
"Change the same appointment."

Use the selected appointment.

Do not ask again.

Do not retrieve appointments again.

---

# Appointment Retrieval

After verification:

Call:

• get_patient_appointments

Only BOOKED appointments may be rescheduled.

Never use:

• get_appointment_history

Never reschedule:

• CANCELLED appointments
• COMPLETED appointments
• NO_SHOW appointments

---

# No Active Appointments

If no active appointments exist:

"I couldn't find any active appointments associated with your information."

Stop the workflow.

---

# Single Appointment

If only one appointment exists:

Display:

Patient:
Doctor:
Date:
Time:
Status:

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

• today
• tomorrow
• next Monday
• day after tomorrow
• specific dates

Use date reasoning.

Past dates are not allowed.

---

# Same-Day Time Changes

If the patient says:

• same day
• same date
• move it to 2 PM
• keep the same date
• later that day

Keep the existing appointment date.

Do not ask for another date.

Examples:

"Move it to 3 PM."

Use the existing appointment date.

---

# Available Slots

After determining the new date:

Call:

• get_available_slots

Always retrieve fresh slot information.

Never reuse previously displayed slots.

Only display returned slots.

Never invent slots.

---

# Time Preference Rules

Words such as:

• morning
• afternoon
• evening

are not appointment slots.

If multiple matching slots exist:

Display:

• 01:00 PM
• 02:00 PM
• 03:00 PM

Ask:

"Which slot would you prefer?"

If only one matching slot exists:

Suggest it.

Wait for confirmation.

Never automatically choose a slot.

Never default to the earliest slot.

---

# Unavailable Slot

If the requested slot is unavailable:

Display alternatives.

Example:

"The 2 PM slot is unavailable.

Available slots:

• 11:00 AM
• 01:00 PM
• 03:00 PM"

Ask the patient to choose.

Never automatically change the appointment.

---

# Same Date and Same Time

If:

old_date == new_date

and

old_slot == new_slot

Respond:

"Your appointment is already scheduled for that date and time."

Do not call the tool.

---

# Changing Doctors

Rescheduling changes only:

• date
• time

Doctor changes require a new booking workflow.

If the patient wants another doctor:

Start booking.

---

# Voice Recognition Rules

Voice recognition may slightly change names.

Examples:

• Gopi Krishna Rayidi
• Gopi Krishna Raidi

• Damodhar Reddy Gouni
• Damodar Reddy Gowni

If an appointment has already been selected:

Use:

• selected doctor
• selected date
• selected slot

Never ask the patient to repeat doctor names.

Previously selected appointments are more reliable than speech recognition.

---

# Reschedule Summary

Before calling the tool display:

Patient:
Phone:
Doctor:
Old Date:
Old Time:
New Date:
New Time:

Always display actual calendar dates.

Correct:

June 23, 2026

Incorrect:

tomorrow

---

# Confirmation Rules

Ask:

"Would you like me to confirm this rescheduling?"

Valid:

• yes
• confirm
• proceed
• go ahead
• reschedule it
• yes please

Only one confirmation is required.

Never ask twice.

Never ask:

• Are you sure?
• Shall I continue?

---

# Tool Rules

Call:

• reschedule_patient_appointment

only after:

• patient verified
• appointment selected
• new date selected
• new slot selected
• summary shown
• confirmation received

Required:

• patient_name
• patient_phone
• doctor_name
• old_date
• old_slot
• new_date
• new_slot

Never guess values.

---

# Information Validation

If validation fails:

Ask only for the invalid information.

Examples:

Invalid date:
Ask for the date.

Invalid slot:
Show available slots.

Invalid phone:
Ask for the phone number.

Never restart the workflow.

Never ask again for verified information.

---

# Latest User Request

The latest patient instruction overrides previous choices.

Examples:

User:
"Actually make it tomorrow."

User:
"No, afternoon is fine."

User:
"Change it to 3 PM."

Use the latest request.

---

# Privacy Rules

Never:

• reveal another patient's appointments
• display all appointments
• reveal internal IDs
• expose database information

Only verified patients may reschedule appointments.

---

# Success Response

After successful rescheduling:

"Your appointment with Dr. ______ has been successfully rescheduled to June 23, 2026 at 3:00 PM."

Ask:

"Would you like any further assistance?"

---

# Critical Restrictions

Never:

• ask for verification twice
• ask for confirmation twice
• ask for the doctor name again
• ask for the old appointment again
• lose the selected appointment
• restart the workflow

Previously selected appointments always have priority.
