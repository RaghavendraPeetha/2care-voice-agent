# Reschedule Appointment Skill

Use this skill whenever the patient wants to modify an appointment.

Examples:

• reschedule my appointment
• move my appointment
• change my appointment
• move it to tomorrow
• move it to 2 PM
• change to afternoon

---

# Patient Verification

Required:

• patient_name
• patient_phone

If already verified:

Do not ask again.

Ask only for missing information.

---

# Selected Appointment Priority

If an appointment has already been selected:

Reuse:

• doctor
• old date
• old slot

Examples:

• reschedule it
• move that appointment
• change the same appointment

Do not ask again.

---

# Appointment Retrieval

If no appointment is selected:

Call:

• get_patient_appointments

Only BOOKED appointments may be rescheduled.

If none exist:

"I couldn't find any active appointments."

Stop the workflow.

---

# Multiple Appointments

If multiple appointments exist:

Display:

1. Doctor — Date — Time
2. Doctor — Date — Time

Ask:

"Which appointment would you like to reschedule?"

Never guess.

The selected appointment becomes:

• doctor
• old date
• old slot

---

# Date Resolution

Always use:

• get_current_date

Resolve:

• today
• tomorrow
• next Monday
• next week

Convert to:

YYYY-MM-DD

Past dates are not allowed.

---

# Same-Day Changes

Examples:

• move it to 2 PM
• same day afternoon
• later that day

Reuse the selected appointment date.

Do not ask for another date.

---

# Available Slots

After determining the new date:

Call:

• get_available_slots

Always retrieve fresh slots.

Only returned slots may be shown.

Never invent slots.

---

# Time Preferences

Morning:

before 12 PM

Afternoon:

12 PM to 4 PM

Evening:

after 4 PM

Display matching slots.

Never automatically choose.

---

# Unavailable Slots

If the requested slot is unavailable:

Display available slots.

Ask the patient to choose.

Never automatically change the appointment.

---

# Reschedule Summary

Display:

Patient:
Doctor:
Old Date:
Old Time:
New Date:
New Time:

Always display actual dates.

Example:

Old Date: June 22, 2026

New Date: June 24, 2026

New Time: 02:00 PM

Ask:

"Would you like me to confirm this rescheduling?"

---

# Confirmation Rules

Valid confirmations:

• yes
• confirm
• proceed
• go ahead
• reschedule it
• yes please

Only one confirmation is required.

---

# Tool Rules

Call:

• reschedule_patient_appointment

only after:

• patient verified
• doctor selected
• old date selected
• old slot selected
• new date selected
• new slot selected
• summary shown
• confirmation received

Required arguments:

• patient_name
• patient_phone
• doctor_name
• old_date
• old_slot
• new_date
• new_slot

Never guess values.

Always use the selected appointment.

---

# Same Date And Same Time

If:

old_date == new_date

and

old_slot == new_slot

Respond:

"Your appointment is already scheduled for that date and time."

Do not call the tool.

---

# Success Response

"Your appointment with Dr. ______ has been successfully rescheduled to June 24, 2026 at 2:00 PM."

Ask:

"Would you like any further assistance?"

---

# Restrictions

Never:

• ask for verification twice
• ask for the doctor again
• ask for the old appointment again
• ask for confirmation twice
• lose the selected appointment
• reveal internal information

Previously selected appointments always have priority.