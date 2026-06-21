import pandas as pd

from app.database import SessionLocal
from app.models import Doctor

df = pd.read_csv("data/doctors.csv")

db = SessionLocal()

for _, row in df.iterrows():

    doctor = Doctor(
        name=row["name"],
        qualification=row["qualification"],
        speciality=row["speciality"],
        experience=row["experience"],
        languages=row["languages"],
        location=row["location"],
        opd_timings=row["opd_timings"],
        expertise=row["expertise"],
        services=row["services"],
        profile_url=row["profile_url"],
        hospital=row["hospital"]
    )

    db.add(doctor)

db.commit()

print("Doctors loaded.")