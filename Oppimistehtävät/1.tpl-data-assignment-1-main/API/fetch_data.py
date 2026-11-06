import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Database.models import User
from configuration import DATABASE_URL, API_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

#Mallia alembic exercise main

def fetch_and_store_users():
    response = requests.get(API_URL)
    users = response.json()

    session = SessionLocal()
    for u in users:
        user = User(
            id=u["id"],
            name=u["name"],
            username=u["username"],
            email=u["email"],
            city=u.get("address", {}).get("city"),
            phone=u["phone"],
            website=u["website"],
            company_name=u.get("company", {}).get("name")
        )
        session.merge(user) 
    session.commit()
    session.close()
    print("Users inserted into database.")
