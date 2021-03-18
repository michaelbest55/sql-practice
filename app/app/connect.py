import os
import random
import time

from faker import Faker
from loguru import logger
from sqlalchemy import create_engine


def add_new_row(db, table, profile):
    # Insert a new number into the 'numbers' table.
    values_string = ", ".join([f"'{str(value)}'" for value in profile.values()])
    columns_string = ", ".join([str(key) for key in profile.keys()])

    db.execute(f"INSERT INTO {table} ({columns_string}) VALUES ( {values_string} );")


def get_last_row(db):
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT number " + \
            "FROM user " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM user)" + \
            "LIMIT 1"

    result_set = db.execute(query)
    for (r) in result_set:
        return r[0]


if __name__ == '__main__':
    logger.debug('Application started')
    db_name = os.getenv("POSTGRES_DB")
    db_user = os.getenv("POSTGRES_USER")
    db_pass = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")

    # Connect to to the database
    db_string = f"postgres+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    db = create_engine(db_string)

    faker = Faker()

    for i in range(10):
        profile = faker.profile()
        profile.pop("current_location", None)
        profile['website'] = str(profile['website'][0])
        profile['email'] = profile.pop("mail")
        add_new_row(db, "profile", profile)

    logger.debug("Finished program")
    # while True:
    #     add_new_row()
    #     print('The last value inserted is: {}'.format(get_last_row()))
    #     time.sleep(5)
