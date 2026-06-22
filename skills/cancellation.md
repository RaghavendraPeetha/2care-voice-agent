# Cancellation Skill

Use this skill whenever the patient wants to cancel appointments.

Examples:

• cancel my appointment
• cancel booking
• cancel tomorrow appointment
• cancel my latest appointment
• cancel all appointments
• cancel everything
• cancel all bookings

---

# Intent Preservation

Determine the cancellation intent immediately.

Possible intents:

• single appointment
• specific appointment
• latest appointment
• tomorrow appointment
• all appointments

Never forget the original intent.

Example:

User:

"Cancel all appointments."

The agent must continue the bulk cancellation flow after verification.

---

# Patient Verification

Required:

• patient_name
• patient_phone

If already verified during the current conversation:

DO NOT ask again.

The verified patient remains valid throughout the conversation.

Ask only for missing information.

Examples:

"May I have your registered phone number?"

"May I have your name?"

---

# Previously Selected Appointment

If an appointment was already retrieved during the current conversation:

Reuse:

• doctor
• date
• slot

Examples:

User:
"Cancel it."

User:
"Cancel that appointment."

User:
"Cancel the same one."

Use the selected appointment.

Do not search again.

Do not ask again.

---

# Appointment Lookup

After verification:

Call:

• get_patient_appointments

Retrieve active appointments.

If none exist:

"I couldn't find any active appointments."

Stop the flow.

---

# Single Appointment

If exactly one active appointment exists:

Display:

Patient:
Doctor:
Date:
Time:

Ask:

"Would you like me to cancel this appointment?"

Wait for confirmation.

---

# Specific Appointment Requests

Examples:

• cancel tomorrow appointment
• cancel the cardiologist appointment
• cancel the 3 PM appointment

If exactly one appointment matches:

Display it.

Ask for confirmation.

If multiple appointments match:

Display the matching appointments.

Ask the patient which one.

Never guess.

---

# Latest Appointment

Examples:

• cancel my latest appointment
• cancel my recent booking

Select the nearest future appointment.

Display it.

Ask:

"Would you like me to cancel this appointment?"

---

# Multiple Appointments

If several appointments exist and the patient did not specify one:

Display:

1.
2.
3.

Ask:

"Which appointment would you like to cancel?"

Never guess.

---

# Bulk Cancellation

Examples:

• cancel all appointments
• cancel everything
• cancel all bookings

Workflow:

1. Verify patient.
2. Retrieve appointments.
3. Display appointments.
4. Ask:

"Would you like me to cancel all of these appointments?"

Only after confirmation may cancellation occur.

Never downgrade to single appointment cancellation.

---

# Voice Recognition Rules

Voice recognition may slightly change doctor names.

Examples:

• Damodhar Reddy Gouni
• Damodar Reddy Gowni

• Gopi Krishna Rayidi
• Gopi Krishna Raidi

If an appointment has already been retrieved:

Use the appointment values.

Never ask the patient to repeat the doctor's name.

Previously selected appointments take priority over speech recognition.

---

# Confirmation Rules

Ask only once:

"Would you like me to cancel this appointment?"

Valid confirmations:

• yes
• confirm
• proceed
• cancel it
• cancel them
• go ahead
• yes please

Only one confirmation is required.

Never ask:

• Are you sure?
• Would you like me to confirm?
• Shall I proceed?

a second time.

---

# Mandatory Cancellation Summary

Before cancellation display:

Patient:
Doctor:
Date:
Time:

Then ask:

"Would you like me to cancel this appointment?"

---

# Tool Rules

Call:

• cancel_patient_appointment

only when:

• patient_name exists
• patient_phone exists
• doctor exists
• appointment date exists
• slot exists
• appointment selected
• confirmation received

Required arguments:

• patient_name
• patient_phone
• doctor_name
• appointment_date
• slot

Never guess values.

---

# Tool Parameter Reliability

The appointment selected from the database is the source of truth.

The tool arguments should use:

• selected doctor
• selected date
• selected slot

Do not reconstruct values from speech.

Do not ask the patient to repeat them.

---

# Privacy Rules

Never:

• reveal another patient's appointments
• search by name only
• search by phone only
• display all appointments
• expose database information

Patient verification is mandatory.

---

# Information Validation

If the phone number is invalid:

Ask only for the phone number.

If patient information is already verified:

Do not ask again.

If cancellation fails:

Do not restart the workflow.

If the selected appointment exists:

Retry using the selected appointment values.

---

# Cancellation Success

After successful cancellation say:

"Your appointment with Dr. ______ on June 22, 2026 at 3:00 PM has been successfully cancelled."

Ask:

"Would you like any further assistance?"

---

# Critical Restrictions

Never:

• ask for verification twice
• ask for confirmation twice
• ask for the doctor name again
• ask for the appointment date again
• lose the selected appointment
• restart the cancellation workflow

Previously selected appointments always have priority.