from database import database
from app import create_app

app = create_app()
app.app_context().push()


def drop_tables():
    sql = "DROP TABLE IF EXISTS kayttajat, vinkit, kirjat, users, tips, book_tips"
    database.session.execute(sql)
    database.session.commit()


def create_tables():
    with open("schema.sql", "r", encoding="utf8") as schema_file:
        schema = schema_file.readlines()

    database.session.execute(''.join(schema))
    database.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()
