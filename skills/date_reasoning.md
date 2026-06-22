# Date Reasoning Skill

Use this skill whenever the patient mentions:

* today
* tomorrow
* day after tomorrow
* next Monday
* this Friday
* next week
* weekend
* same day
* same date
* previous date
* that day
* June 25
* 25 June
* 23rd this month
* tomorrow morning
* next Tuesday afternoon

Never guess dates.

Always use get_current_date.

---

# Mandatory Tool Rule

Before resolving any relative date:

Call:

get_current_date

This tool is the only source of truth.

Never use:

* model memory
* training dates
* previous conversations

---

# Date Conversion Rule

All tools require:

YYYY-MM-DD

Never send:

* tomorrow
* today
* next Monday
* same day
* this Friday

to tools.

Examples:

today → 2026-06-21

tomorrow → 2026-06-22

next Monday → 2026-06-29

---

# Relative Date Resolution

Examples:

today

tomorrow

day after tomorrow

next Monday

this Friday

next week

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

* morning
* afternoon
* evening

These are NOT appointment times.

Morning:
before 12 PM

Afternoon:
12 PM to 4 PM

Evening:
after 4 PM

Use available slots.

Examples:

Available:

12 PM
1 PM
2 PM
3 PM

Patient:

"Tomorrow afternoon."

Agent:

"The available afternoon slots are 12 PM, 1 PM, 2 PM, and 3 PM. Which would you prefer?"

Never choose automatically.

---

# Context Dates

When rescheduling:

same day

same date

that day

previous date

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

June 25

25 June

23rd this month

Convert to:

YYYY-MM-DD

Always use the current year unless explicitly specified.

---

# Weekday Validation

Always verify:

* calendar date
* weekday

Example:

"Next Monday is June 22, 2026."

---

# Past Dates

Appointments cannot be:

* booked in the past
* rescheduled to the past

If calculated date is earlier than today:

Respond:

"Appointments cannot be scheduled for a past date."

Do not continue booking.

---

# Ambiguous Dates

Examples:

* sometime next week
* later this month
* weekend
* next weekend

Ask for clarification.

Examples:

"Would you prefer Saturday or Sunday?"

"Which day next week would you like?"

Never guess.

---

# Final Confirmation Rule

Before:

* book_appointment
* reschedule_patient_appointment

The final summary MUST show:

Patient Name:
Phone Number:
Doctor:
Date:
Time:

Date must always be:

Month Day Year

Example:

June 22, 2026

Never show:

* tomorrow
* next Monday
* same day

during final confirmation.

---

# Tool Rules

Before calling:

* get_available_slots
* check_availability
* book_appointment
* reschedule_patient_appointment

Always convert the date.

Correct:

2026-06-22

Incorrect:

tomorrow

---

# Voice Recognition

Patients may say:

* tomorrow morning
* tomorrow afternoon
* Monday evening

First resolve the date.

Then determine matching slots.

Never create slots.

Use get_available_slots.

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
