from langchain_core.tools import tool

from app.database import SessionLocal
from app.models import Doctor
from app.models import Appointment

from datetime import date, datetime, timedelta

from sqlalchemy import func


@tool
def get_doctors():
    """
    Retrieve all doctors available in the clinic.

    Use this tool when the patient asks:
    - Which doctors are available?
    - Who is the cardiologist?
    - Which departments exist?
    - Who is a dermatologist?
    - Which specialists are available?

    This tool is informational only.

    Never use this tool to create, update, or cancel appointments.
    """

    db = SessionLocal()

    try:

        doctors = db.query(Doctor).all()

        return [
            {
                "name": d.name,
                "speciality": d.speciality,
                "experience": d.experience,
                "languages": d.languages,
                "timings": d.opd_timings,
                "services": d.services,
                "location": d.location,
                "hospital": d.hospital
            }
            for d in doctors
        ]

    finally:
        db.close()

@tool
def get_doctor(doctor_name: str):
    """
    Retrieve a doctor using a partial or full doctor name.

    Use this tool whenever the patient mentions:

    - Dr Sindhura
    - Dr Ravi
    - Sindhura
    - Ravi Kumar

    This tool helps identify the correct doctor record.

    IMPORTANT:

    - Always use this tool before booking if the doctor name is incomplete.
    - If exactly one doctor matches, use the full doctor name.
    - If multiple doctors match, ask the patient to choose.
    - The returned doctor name becomes the official doctor name for the conversation.

    Never invent doctor names.

    Never shorten doctor names.

    The database doctor record is the source of truth.
    """
    db = SessionLocal()

    try:
        search_name = (
            doctor_name
            .replace("Dr.", "")
            .replace("Dr", "")
            .strip()
        )

        doctor = db.query(Doctor).filter(
            Doctor.name.ilike(f"%{search_name}%")
        ).first()

        if not doctor:
            return None

        return {
            "name": doctor.name,
            "speciality": doctor.speciality,
            "experience": doctor.experience,
            "languages": doctor.languages,
            "timings": doctor.opd_timings,
            "expertise": doctor.expertise,
            "services": doctor.services
        }

    finally:
        db.close()

@tool
def get_patient_appointments(
    patient_phone: str,
    patient_name: str
):
    """
    Retrieve ACTIVE appointments belonging to a verified patient.

    SECURITY RULES:

    This tool requires BOTH:

    - patient_name
    - patient_phone

    Never call this tool unless both values have
    been collected.

    Use this tool when the patient asks:

    - show my appointments
    - what appointments do I have
    - do I have any bookings
    - list my appointments
    - cancel my appointment
    - reschedule my appointment

    Never reveal another patient's appointments.

    Never use only the patient name.

    Never use only the phone number.

    Patient verification is mandatory.

    This tool returns only ACTIVE appointments.

    Returned statuses:

    - BOOKED

    Cancelled, completed, and no-show appointments
    are excluded.
    """

    db = SessionLocal()

    try:

        patient_name = patient_name.strip().title()
        patient_phone = patient_phone.strip()

        if not patient_name:
            return {
                "status": "failed",
                "message": "patient name required"
            }

        if not patient_phone:
            return {
                "status": "failed",
                "message": "phone number required"
            }

        if not patient_phone.isdigit():
            return {
                "status": "failed",
                "message": "invalid phone number"
            }

        if len(patient_phone) != 10:
            return {
                "status": "failed",
                "message": "phone number must contain 10 digits"
            }

        appointments = (
            db.query(Appointment)
            .filter(
                Appointment.patient_name.ilike(patient_name),
                Appointment.patient_phone == patient_phone,
                Appointment.status == "BOOKED"
            )
            .order_by(
                Appointment.appointment_date,
                Appointment.slot
            )
            .all()
        )

        if not appointments:
            return {
                "status": "failed",
                "message": "no active appointments found"
            }

        return [
            {
                "appointment_id": a.id,
                "doctor": a.doctor_name,
                "date": a.appointment_date,
                "slot": a.slot,
                "status": a.status
            }
            for a in appointments
        ]

    finally:
        db.close()

@tool
def get_appointment_history(
    patient_phone: str,
    patient_name: str
):
    """
    Retrieve all appointments belonging to a verified patient.

    Includes:

    - BOOKED
    - CANCELLED
    - COMPLETED
    - NO_SHOW
    """

    db = SessionLocal()

    try:

        appointments = (
            db.query(Appointment)
            .filter(
                Appointment.patient_name.ilike(
                    patient_name.strip().title()
                ),
                Appointment.patient_phone == patient_phone.strip()
            )
            .order_by(
                Appointment.appointment_date,
                Appointment.slot
            )
            .all()
        )

        if not appointments:
            return {
                "status": "failed",
                "message": "no appointment history found"
            }

        return [
            {
                "appointment_id": a.id,
                "doctor": a.doctor_name,
                "date": a.appointment_date,
                "slot": a.slot,
                "status": a.status
            }
            for a in appointments
        ]

    finally:
        db.close()

@tool
def get_available_slots(
    doctor_name: str,
    appointment_date: str
):
    """
    Retrieve the currently available appointment slots.

    IMPORTANT:

    - Always call this tool before booking.
    - Always call this tool before rescheduling.
    - Always call this tool before displaying available slots.
    - Never reuse previously displayed slots.
    - Never create slots from OPD timings.
    - Only returned slots may be booked.

    The returned slots are the source of truth.
    """

    db = SessionLocal()

    try:
        search_name = (
            doctor_name
            .replace("Dr.", "")
            .replace("Dr", "")
            .strip()
        )

        doctor = db.query(Doctor).filter(
            Doctor.name.ilike(f"%{search_name}%")
        ).first()

        if not doctor:
            return []

        timing = doctor.opd_timings

        # Example:
        # MON – SAT : 11:00 AM – 03:00 PM

        import re

        match = re.search(
            r'(\d{1,2}:\d{2}\s*[AP]M).*?(\d{1,2}:\d{2}\s*[AP]M)',
            timing
        )

        if not match:
            return []

        start_time = datetime.strptime(
            match.group(1),
            "%I:%M %p"
        )

        end_time = datetime.strptime(
            match.group(2),
            "%I:%M %p"
        )

        slots = []

        current = start_time

        while current < end_time:

            slots.append(
                current.strftime("%I:%M %p")
            )

            current += timedelta(hours=1)

        booked = db.query(Appointment).filter(
            Appointment.doctor_name == doctor.name,
            Appointment.appointment_date == appointment_date,
            Appointment.status == "BOOKED"
        ).all()

        booked_slots = [a.slot for a in booked]

        available = [
            slot
            for slot in slots
            if slot not in booked_slots
        ]

        return available

    finally:
        db.close()

@tool
def check_availability(
    doctor_name: str,
    appointment_date: str,
    slot: str
):
    """
    Check whether a doctor's appointment slot is available.

    Use this tool before booking appointments.

    IMPORTANT:

    - This tool does not create appointments.
    - This tool only checks availability.
    - If the slot is unavailable, suggest alternatives.
    - Never promise unavailable slots.

    This tool may be called before the patient confirms the booking.

    Return availability information to the patient.
    """

    db = SessionLocal()

    try:
        available_slots = get_available_slots.invoke(
            {
                "doctor_name": doctor_name,
                "appointment_date": appointment_date
            }
        )

        return slot in available_slots

    finally:
        db.close()

@tool
def book_appointment(
patient_name: str,
patient_phone: str,
doctor_name: str,
appointment_date: str,
slot: str
):
    """
    Create a hospital appointment.

    ```
    CRITICAL RULES:

    This tool MUST NOT be called immediately.

    This tool may only be called AFTER ALL of the following information
    has been collected:

    - patient_name
    - patient_phone
    - doctor_name
    - appointment_date
    - slot

    Before calling this tool, the agent MUST:

    1. Show the appointment summary.

    Patient Name:
    Phone Number:
    Doctor:
    Date:
    Time:

    2. Ask:

    "Would you like me to confirm this appointment?"

    3. Wait for explicit confirmation.

    Valid confirmations:

    - Yes
    - Confirm
    - Proceed
    - Book it
    - Go ahead

    Never invent:

    - patient names
    - phone numbers
    - dates
    - times

    Never use:

    - User
    - Patient
    - Unknown

    If information is missing,
    continue asking the patient.

    If confirmation has not been received,
    DO NOT call this tool.
    """

    required_fields = {
        "patient_name": patient_name,
        "patient_phone": patient_phone,
        "doctor_name": doctor_name,
        "appointment_date": appointment_date,
        "slot": slot
    }

    invalid_values = [
        "user",
        "patient",
        "unknown",
        "[your name]",
        "[your phone number]",
        ""
    ]

    normalized_name = patient_name.strip().title()

    if normalized_name.lower() in invalid_values:
        return {
            "status": "failed",
            "message": "valid patient name required"
        }

    if patient_phone.lower().strip() in invalid_values:
        return {
            "status": "failed",
            "message": "valid phone number required"
        }

    missing = [
        field
        for field, value in required_fields.items()
        if not value
    ]

    if missing:
        return {
            "status": "failed",
            "message": f"Missing required fields: {', '.join(missing)}"
        }

    # Phone validation
    if not patient_phone.isdigit() or len(patient_phone) != 10:
        return {
            "status": "failed",
            "message": "phone number must contain 10 digits"
        }

    # Date validation
    try:
        appointment_dt = datetime.strptime(
            appointment_date,
            "%Y-%m-%d"
        ).date()

        if appointment_dt < date.today():
            return {
                "status": "failed",
                "message": "cannot book appointments in the past"
            }

    except ValueError:
        return {
            "status": "failed",
            "message": "invalid appointment date"
        }

    db = SessionLocal()

    try:

        doctor = db.query(Doctor).filter(
            Doctor.name.ilike(
                f"%{doctor_name.replace('Dr.', '').replace('Dr', '').strip()}%"
            )
        ).first()

        if not doctor:
            return {
                "status": "failed",
                "message": "doctor not found"
            }

        doctor_name = doctor.name

        # Prevent duplicate bookings
        existing_patient_booking = (
            db.query(Appointment)
            .filter(
                Appointment.patient_name == normalized_name,
                Appointment.patient_phone == patient_phone,
                Appointment.doctor_name == doctor_name,
                Appointment.appointment_date == appointment_date,
                Appointment.slot == slot,
                Appointment.status == "BOOKED"
            )
            .first()
        )

        if existing_patient_booking:
            return {
                "status": "failed",
                "message": "you already have this appointment booked"
            }

        available_slots = get_available_slots.invoke(
            {
                "doctor_name": doctor_name,
                "appointment_date": appointment_date
            }
        )

        if slot not in available_slots:
            return {
                "status": "failed",
                "message": (
                    f"Invalid slot. Available slots: "
                    f"{', '.join(available_slots)}"
                )
            }

        available = check_availability.invoke(
            {
                "doctor_name": doctor_name,
                "appointment_date": appointment_date,
                "slot": slot
            }
        )

        if not available:
            return {
                "status": "failed",
                "message": "slot unavailable"
            }

        appointment = Appointment(
            patient_name=normalized_name,
            patient_phone=patient_phone,
            doctor_name=doctor_name,
            appointment_date=appointment_date,
            slot=slot,
            status="BOOKED"
        )

        db.add(appointment)
        db.commit()

        return {
            "status": "success",
            "message": "appointment booked"
        }

    finally:
        db.close()


       
@tool
def cancel_patient_appointment(
patient_name: str,
patient_phone: str,
doctor_name: str,
appointment_date: str,
slot: str
):
    """
    Cancel exactly one appointment.

    ```
    Required:
    - patient_name
    - patient_phone
    - doctor_name
    - appointment_date
    - slot

    The patient must already be verified.

    This tool only cancels one appointment.

    Never use this tool until:
    - patient identity is verified
    - appointment is identified
    - confirmation is received

    Valid confirmations:
    - yes
    - confirm
    - proceed
    - cancel it

    Never cancel multiple appointments with one call.
    """

    db = SessionLocal()

    try:

        appointment = (
            db.query(Appointment)
            .filter(
                Appointment.patient_name.ilike(patient_name),
                Appointment.patient_phone == patient_phone,
                Appointment.doctor_name == doctor_name,
                Appointment.appointment_date == appointment_date,
                Appointment.slot == slot
            )
            .first()
        )

        if not appointment:
            return {
                "status": "failed",
                "message": "appointment not found"
            }

        if appointment.status == "CANCELLED":
            return {
                "status": "failed",
                "message": "appointment already cancelled"
            }

        if appointment.status == "COMPLETED":
            return {
                "status": "failed",
                "message": "completed appointments cannot be cancelled"
            }

        if appointment.status == "NO_SHOW":
            return {
                "status": "failed",
                "message": "no-show appointments cannot be cancelled"
            }

        appointment.status = "CANCELLED"

        db.commit()

        return {
            "status": "success",
            "message": "appointment cancelled"
        }

    finally:
        db.close()

@tool
def reschedule_patient_appointment(
patient_name: str,
patient_phone: str,
doctor_name: str,
old_date: str,
old_slot: str,
new_date: str,
new_slot: str
):
    """
    Reschedule exactly one verified appointment.

    ```
    Required:
    - patient_name
    - patient_phone
    - doctor_name
    - old_date
    - old_slot
    - new_date
    - new_slot

    The patient must already be verified.

    Never use this tool without explicit confirmation.

    This tool only reschedules one appointment.
    """

    db = SessionLocal()

    try:

        normalized_name = patient_name.strip().title()

        # Validate new date
        try:
            new_dt = datetime.strptime(
                new_date,
                "%Y-%m-%d"
            ).date()

            if new_dt < date.today():
                return {
                    "status": "failed",
                    "message": "cannot reschedule to a past date"
                }

        except ValueError:
            return {
                "status": "failed",
                "message": "invalid date"
            }

        appointment = (
            db.query(Appointment)
            .filter(
                func.lower(Appointment.patient_name)
                == normalized_name.lower(),
                Appointment.patient_phone == patient_phone,
                Appointment.doctor_name == doctor_name,
                Appointment.appointment_date == old_date,
                Appointment.slot == old_slot,
                Appointment.status == "BOOKED"
            )
            .first()
        )

        if not appointment:
            return {
                "status": "failed",
                "message": "appointment not found"
            }

        if appointment.status == "CANCELLED":
            return {
                "status": "failed",
                "message": "cancelled appointments cannot be rescheduled"
            }

        if appointment.status == "COMPLETED":
            return {
                "status": "failed",
                "message": "completed appointments cannot be rescheduled"
            }

        if appointment.status == "NO_SHOW":
            return {
                "status": "failed",
                "message": "no-show appointments cannot be rescheduled"
            }

        # Prevent same appointment rescheduling
        if (
            appointment.appointment_date == new_date
            and appointment.slot == new_slot
        ):
            return {
                "status": "failed",
                "message": "appointment is already scheduled for this date and time"
            }

        # Check whether new slot is already booked
        existing = (
            db.query(Appointment)
            .filter(
                Appointment.id != appointment.id,
                Appointment.doctor_name == doctor_name,
                Appointment.appointment_date == new_date,
                Appointment.slot == new_slot,
                Appointment.status == "BOOKED"
            )
            .first()
        )

        if existing:
            return {
                "status": "failed",
                "message": "slot unavailable"
            }

        appointment.appointment_date = new_date
        appointment.slot = new_slot

        db.commit()

        return {
            "status": "success",
            "message": "appointment rescheduled"
        }

    finally:
        db.close()
