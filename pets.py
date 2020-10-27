import sqlite3 as lite


def db_setup(query_str=str()):
    conn = lite.connect('pet.db')
    c = conn.cursor()
    for line in query_str:
        c.execute(line)
        conn.commit()
    conn.close()


def split_query(query_str=str(),split=str()):
    query_split = query_str.split(split)
    query_return = []
    for line in query_split:
        query_return = query_return + [line+split]
    query_return.pop()
    return query_return


query = """CREATE TABLE person(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
CREATE TABLE pet(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);
CREATE TABLE person_pet(
    person_id INTEGER,
    pet_id INTEGER
);"""

query = split_query(query, ');')
db_setup(query)