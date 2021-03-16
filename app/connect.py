import os
import random
import time

from faker import Faker
from loguru import logger
from sqlalchemy import create_engine


db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")

# Connect to to the database
db_string = f"postgres+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
db = create_engine(db_string)

faker=Faker()
faker.profile()

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) " +
               "VALUES (" +
               str(n) + "," +
               str(int(round(time.time() * 1000))) + ");")


# def get_last_row():
#     # Retrieve the last number inserted inside the 'numbers'
#     query = "" + \
#             "SELECT number " + \
#             "FROM numbers " + \
#             "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" + \
#             "LIMIT 1"
#
#     result_set = db.execute(query)
#     for (r) in result_set:
#         return r[0]



if __name__ == '__main__':
    logger.debug('Application started')

    while True:
        add_new_row(random.randint(1, 100000))
        print('The last value inserted is: {}'.format(get_last_row()))
        time.sleep(5)
