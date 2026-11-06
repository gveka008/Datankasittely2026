import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuration import DATABASE_URL
from Database.models import User
from API.fetch_data import fetch_and_store_users
from Data_analysis.analysis import analyze_data
from Data_protection.anonymize import anonymize
from Data_protection.masking import mask

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def main():
    print("Pipeline starts")
    print("Fetching and storing users")
    fetch_and_store_users()

    print("Data from db and anonymizing & masking")
    session=SessionLocal()
    db_users=session.query(User).all()
    session.close()
    users_list = [
        {
            "id": u.id,
            "name": u.name,
            "username": u.username,
            "email": u.email,
            "city": u.city,
            "phone": u.phone,
            "website": u.website,
            "company_name": u.company_name
        } for u in db_users
    ]
    anonymized_users = anonymize(users_list)
    fully_processed_users = mask(anonymized_users)
    print("Pandas analyze")
    analyze_data(fully_processed_users)
    print("Pipeline done")

if __name__ == "__main__":
    main()