from fastapi import FastAPI
from pydantic import BaseModel

from tools.appointment_tools import (
    get_doctors,
    get_doctor,
    get_available_slots,
    check_availability,
    book_appointment,
    cancel_patient_appointment,
    reschedule_patient_appointment,
    get_patient_appointments,
    get_appointment_history
)

app = FastAPI(
    title="2Care Voice AI API",
    description="Voice AI Hospital Receptionist Backend",
    version="1.0.0"
)


# -------------------------
# Request Models
# -------------------------

class PatientRequest(BaseModel):
    patient_name: str
    patient_phone: str


class DoctorRequest(BaseModel):
    doctor_name: str


class SlotRequest(BaseModel):
    doctor_name: str
    appointment_date: str


class AvailabilityRequest(BaseModel):
    doctor_name: str
    appointment_date: str
    slot: str


class BookRequest(BaseModel):
    patient_name: str
    patient_phone: str
    doctor_name: str
    appointment_date: str
    slot: str


class CancelRequest(BaseModel):
    patient_name: str
    patient_phone: str
    doctor_name: str
    appointment_date: str
    slot: str


class RescheduleRequest(BaseModel):
    patient_name: str
    patient_phone: str
    doctor_name: str
    old_date: str
    old_slot: str
    new_date: str
    new_slot: str


# -------------------------
# Doctor APIs
# -------------------------

@app.get("/")
def home():
    return {"message": "2Care Voice AI API Running"}


@app.get("/doctors")
def doctors():
    return get_doctors.invoke({})


@app.post("/doctor")
def doctor(data: DoctorRequest):
    return get_doctor.invoke({
        "doctor_name": data.doctor_name
    })


# -------------------------
# Slot APIs
# -------------------------

@app.post("/available-slots")
def available_slots(data: SlotRequest):
    return get_available_slots.invoke({
        "doctor_name": data.doctor_name,
        "appointment_date": data.appointment_date
    })


@app.post("/check-availability")
def availability(data: AvailabilityRequest):
    return check_availability.invoke({
        "doctor_name": data.doctor_name,
        "appointment_date": data.appointment_date,
        "slot": data.slot
    })


# -------------------------
# Patient APIs
# -------------------------

@app.post("/appointments")
def appointments(data: PatientRequest):
    return get_patient_appointments.invoke({
        "patient_name": data.patient_name,
        "patient_phone": data.patient_phone
    })


@app.post("/appointment-history")
def history(data: PatientRequest):
    return get_appointment_history.invoke({
        "patient_name": data.patient_name,
        "patient_phone": data.patient_phone
    })


# -------------------------
# Appointment APIs
# -------------------------

@app.post("/book")
def book(data: BookRequest):
    return book_appointment.invoke(data.model_dump())


@app.post("/cancel")
def cancel(data: CancelRequest):
    return cancel_patient_appointment.invoke(
        data.model_dump()
    )


@app.post("/reschedule")
def reschedule(data: RescheduleRequest):
    return reschedule_patient_appointment.invoke(
        data.model_dump()
    )