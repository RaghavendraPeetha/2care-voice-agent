# Date Reasoning Skill

Use this skill whenever the patient mentions:

• today
• tomorrow
• day after tomorrow
• next Monday
• next Friday
• next week
• same day
• same date
• previous date
• that day
• June 25
• 25 June
• 23rd this month
• tomorrow morning
• tomorrow afternoon
• next Monday evening

Never guess dates.

Always use:

• get_current_date

before resolving relative dates.

---

# Mandatory Tool Rule

Before resolving:

• today
• tomorrow
• day after tomorrow
• next Monday
• next Friday
• next week

Call:

• get_current_date

The returned dates are the source of truth.

Never use:

• model memory
• training dates
• previous conversations

---

# Supported Relative Dates

The current date tool may provide:

• today
• tomorrow
• day_after_tomorrow
• next_monday
• next_friday
• next_week

Examples:

today → 2026-06-21

tomorrow → 2026-06-22

day after tomorrow → 2026-06-23

next Monday → 2026-06-29

next Friday → 2026-06-26

---

# Conversation Context

Dates already selected during the conversation remain valid.

If an appointment is selected, remember:

• appointment date
• appointment slot

Examples:

User:

"Move it to the same day."

Use the selected appointment date.

User:

"Keep the same date."

Reuse the current appointment date.

User:

"Move it to 2 PM."

Use the selected appointment date.

Previously selected appointments have priority.

---

# Date Conversion Rules

All appointment tools require:

YYYY-MM-DD

Never send:

• today
• tomorrow
• next Monday
• same day

to:

• get_available_slots
• check_availability
• book_appointment
• reschedule_patient_appointment

Examples:

today → 2026-06-21

tomorrow → 2026-06-22

next Monday → 2026-06-29

---

# Same-Day Changes

Examples:

• same day
• same date
• later that day
• move it to 2 PM

Reuse the currently selected appointment date.

Do not ask for another date.

---

# Time Preferences

Patients may say:

• morning
• afternoon
• evening

These are preferences.

They are not appointment slots.

Morning:

before 12 PM

Afternoon:

12 PM to 4 PM

Evening:

after 4 PM

After retrieving available slots, display matching slots.

Never automatically choose a slot.

Example:

Patient:

"Tomorrow afternoon."

Agent:

"The available afternoon appointments on June 22, 2026 are 1 PM, 2 PM, and 3 PM. Which would you prefer?"

---

# Partial Dates

Examples:

• June 25
• 25 June
• 23rd this month

Convert to:

YYYY-MM-DD

Use the current year unless another year is specified.

---

# Unsupported Dates

Examples:

• weekend
• next weekend
• sometime next week
• later this month

Ask for clarification.

Examples:

"Would you prefer Saturday or Sunday?"

"Which day next week would you like?"

Never guess.

---

# Past Dates

Appointments cannot be:

• booked in the past
• rescheduled to the past

If the resolved date is earlier than today:

"Appointments cannot be scheduled for a past date."

Stop the workflow.

---

# Final Date Display

Never display:

• today
• tomorrow
• next Monday
• same day

in appointment summaries.

Always display:

Month Day, Year

Correct:

June 22, 2026

Incorrect:

Tomorrow

---

# Final Confirmation Rule

Before:

• book_appointment
• reschedule_patient_appointment

Display:

Patient:
Doctor:
Date:
Time:

Dates must always be displayed as:

Month Day, Year

Example:

Date: June 22, 2026

---

# Voice Conversations

Examples:

• tomorrow morning
• tomorrow afternoon
• next Monday evening

Workflow:

1. Resolve the date.
2. Retrieve available slots.
3. Filter slots using the time preference.
4. Ask the patient to choose.

Never create slots.

Always use:

• get_available_slots

---

# Tool Rules

Always pass dates as:

YYYY-MM-DD

Correct:

2026-06-22

Incorrect:

tomorrow

Incorrect:

next Monday

Incorrect:

same day

---

# Critical Restrictions

Never:

• guess dates
• invent dates
• assume weekends
• assume calendar dates
• create appointment slots

Previously selected appointments and get_current_date are the only sources of truth for relative dates.
