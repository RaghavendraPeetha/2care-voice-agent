# Date Reasoning Skill

Use this skill whenever the patient mentions:

• today
• tomorrow
• day after tomorrow
• next Monday
• this Friday
• next week
• weekend
• same day
• same date
• previous date
• that day
• June 25
• 25 June
• 23rd this month
• tomorrow morning
• next Tuesday afternoon

Never guess dates.

Always use get_current_date.

---

# Mandatory Tool Rule

Before resolving any relative date:

Call:

• get_current_date

This tool is the only source of truth.

Never use:

• model memory
• training dates
• previous conversations

---

# Conversation Context Rule

Dates already selected during the current conversation remain valid.

If an appointment has already been selected:

Remember:

• appointment date
• appointment slot

Examples:

User:
"Move it to the same day."

Use the selected appointment date.

User:
"Reschedule it for the afternoon."

Reuse the current appointment date.

Previously selected appointment information has priority.

---

# Date Conversion Rule

All tools require:

YYYY-MM-DD

Never send:

• tomorrow
• today
• next Monday
• same day
• this Friday

to tools.

Examples:

today → 2026-06-21

tomorrow → 2026-06-22

next Monday → 2026-06-29

---

# Relative Date Resolution

Examples:

• today
• tomorrow
• day after tomorrow
• next Monday
• this Friday
• next week

Always convert to:

YYYY-MM-DD

Example:

Current date:

2026-06-21

tomorrow

becomes

2026-06-22

---

# Time Periods

Patients may say:

• morning
• afternoon
• evening

These are NOT appointment times.

Morning:
before 12 PM

Afternoon:
12 PM to 4 PM

Evening:
after 4 PM

Use available slots.

Example:

Available:

• 12 PM
• 1 PM
• 2 PM
• 3 PM

Patient:

"Tomorrow afternoon."

Agent:

"The available afternoon slots are 12 PM, 1 PM, 2 PM, and 3 PM. Which would you prefer?"

Never choose automatically.

---

# Context Dates

When rescheduling:

• same day
• same date
• that day
• previous date

Use the currently selected appointment date.

Example:

Current appointment:

2026-06-22

User:

"Move it to 1 PM on the same day."

Result:

2026-06-22

---

# Partial Dates

Examples:

• June 25
• 25 June
• 23rd this month

Convert to:

YYYY-MM-DD

Always use the current year unless explicitly specified.

---

# Weekday Validation

Always verify:

• calendar date
• weekday

Example:

"Next Monday is June 22, 2026."

---

# Past Dates

Appointments cannot be:

• booked in the past
• rescheduled to the past

If the calculated date is earlier than today:

"Appointments cannot be scheduled for a past date."

Do not continue.

---

# Ambiguous Dates

Examples:

• sometime next week
• later this month
• weekend
• next weekend

Ask for clarification.

Examples:

"Would you prefer Saturday or Sunday?"

"Which day next week would you like?"

Never guess.

---

# Information Validation

Date information is not considered final until validated.

This applies to:

• relative dates
• partial dates
• spoken dates

If validation fails:

Ask only for the date information that needs correction.

Do not restart the workflow.

Do not ask again for already verified information.

---

# Final Confirmation Rule

Before:

• book_appointment
• reschedule_patient_appointment

The final summary MUST show:

Patient Name:
Phone Number:
Doctor:
Date:
Time:

Date must always be displayed as:

Month Day, Year

Correct:

June 22, 2026

Incorrect:

• tomorrow
• next Monday
• same day

---

# Final Date Display

Never display:

• today
• tomorrow
• next Monday
• same day

in appointment summaries.

Always display the actual calendar date.

Example:

Date: June 23, 2026

---

# Tool Rules

Before calling:

• get_available_slots
• check_availability
• book_appointment
• reschedule_patient_appointment

Always convert the date.

Correct:

2026-06-22

Incorrect:

tomorrow

---

# Voice Recognition

Patients may say:

• tomorrow morning
• tomorrow afternoon
• Monday evening

First resolve the date.

Then retrieve available slots.

Never create slots.

Always use:

• get_available_slots

---

# Selected Appointment Priority

If an appointment has already been selected:

Reuse:

• doctor
• appointment date
• slot

Examples:

User:

"Move it to 2 PM."

Use the selected appointment date.

User:

"Same day afternoon."

Use the selected appointment date.

Previously selected appointment information is more reliable than repeated speech recognition.

---

# Examples

Current date:

2026-06-21

today → 2026-06-21

tomorrow → 2026-06-22

day after tomorrow → 2026-06-23

same day → selected appointment date

23rd this month → 2026-06-23

next Monday → calculated calendar date

Always pass only YYYY-MM-DD values to tools.
