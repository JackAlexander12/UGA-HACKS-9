#user model code here
from MySQL import create_engine, Column, Integer, String
from MySQL.ext.declarative import declarative_base
from MySQL.orm import sessionmaker
CREATE DATABASE IF NOT EXISTS marketplace_

CREATE TABLE IF NOT EXISTS buyers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(25) UNIQUE,
    email VARCHAR(16) UNIQUE,
    password VARCHAR(20)

    );

INSERT INTO buyers (username, email, password) VALUES

# When the database is up and running REPLACE THIS LINK THANKYOU!
engine = create_engine('mysql+pymysql://username:password@localhost/database_name', echo=True)


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
    




if __name__ == "__main__":
    # Create a new buyer
    new_buyer = Buyer()
    session.add(new_buyer)
    session.commit()


if ___name___ == "__main___":
    new_Seller = Seller()
    session.add(new_Seller)
    session.commit()
