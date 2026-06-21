# Date Reasoning Skill

Use this skill whenever the patient says:

* today
* tomorrow
* day after tomorrow
* next Monday
* this Friday
* this weekend
* next week
* same day
* same date
* previous date
* that day
* the same appointment day
* 23rd this month
* June 25
* next Tuesday afternoon

Always use the current system date.

---

# Current Date

Always determine:

* today's date
* current year
* current month
* current weekday

Never use memorized dates.

Never use training dates.

Always use the system date.

---

# Relative Dates

Examples:

* today
* tomorrow
* day after tomorrow
* next Monday
* this Friday
* next week

Convert these to actual calendar dates.

Example:

Today: 2026-06-20

* tomorrow → 2026-06-21
* day after tomorrow → 2026-06-22

---

# Appointment Context

When rescheduling:

If the patient says:

* same day
* same date
* previous date
* that day

Use the currently selected appointment date.

Example:

Current appointment:

Date: 2026-06-22

Patient:

"Move it to 1 PM on the same day."

New Date:

2026-06-22

---

# Partial Dates

Examples:

* 23rd this month
* June 25
* 25 June

Convert to:

YYYY-MM-DD format.

Example:

23rd this month

Current month: June 2026

Result:

2026-06-23

---

# Weekday Verification

Always verify:

1. calendar date
2. weekday

Example:

"Next Monday is 2026-06-22."

---

# Past Dates

Appointments cannot be:

* booked in the past
* rescheduled to the past

If the calculated date is earlier than today:

Respond:

"Appointments cannot be scheduled for past dates."

---

# Ambiguous Dates

If the date is unclear:

Examples:

* next weekend
* later this month
* sometime next week

Ask the patient for clarification.

Never guess.

---

# Confirmation

Before booking or rescheduling, always display:

Doctor:
Date:
Time:

Example:

"Your appointment date will be June 22, 2026."

---

# Tool Rules

Always resolve dates before calling:

* get_available_slots
* book_appointment
* reschedule_patient_appointment

Never pass:

* tomorrow
* next Monday
* same day

to tools.

Tools must receive:

YYYY-MM-DD format only.

---

# Examples

Today = 2026-06-20

* tomorrow → 2026-06-21
* day after tomorrow → 2026-06-22
* same day → currently selected appointment date
* 23rd this month → 2026-06-23
* next Monday → calculated calendar date

Always verify the final date before confirmation.
