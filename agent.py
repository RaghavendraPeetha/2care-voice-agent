import os

from pathlib import Path

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent

from tools.appointment_tools import (
    get_current_date,
    normalize_phone_number,

    get_doctors,
    get_doctors_by_speciality,
    get_doctor,

    get_available_slots,
    check_availability,

    get_patient_appointments,
    get_appointment_history,

    book_appointment,
    cancel_patient_appointment,
    reschedule_patient_appointment
)

load_dotenv()


# =====================================================
# LLM
# =====================================================

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
)


# =====================================================
# SYSTEM PROMPT
# =====================================================

SYSTEM_PROMPT = Path("AGENTS.md").read_text(
    encoding="utf-8"
)


# =====================================================
# SKILLS
# =====================================================

SKILLS = [
    Path("skills/booking.md").read_text(
        encoding="utf-8"
    ),

    Path("skills/cancellation.md").read_text(
        encoding="utf-8"
    ),

    Path("skills/reschedule.md").read_text(
        encoding="utf-8"
    ),

    Path("skills/appointment_lookup.md").read_text(
        encoding="utf-8"
    ),

    Path("skills/doctor_lookup.md").read_text(
        encoding="utf-8"
    ),

    Path("skills/date_reasoning.md").read_text(
        encoding="utf-8"
    ),

    Path("skills/emergency.md").read_text(
        encoding="utf-8"
    )
]


# =====================================================
# TOOLS
# =====================================================

TOOLS = [
    get_current_date,

    normalize_phone_number,

    get_doctors,
    get_doctors_by_speciality,
    get_doctor,

    get_available_slots,
    check_availability,

    get_patient_appointments,
    get_appointment_history,

    book_appointment,
    cancel_patient_appointment,
    reschedule_patient_appointment,
]


# =====================================================
# AGENT
# =====================================================

agent = create_deep_agent(
    model=llm,
    system_prompt=SYSTEM_PROMPT,
    skills=SKILLS,
    tools=TOOLS,
    debug=False
)