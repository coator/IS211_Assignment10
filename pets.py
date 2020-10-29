import sqlite3 as lite


def db_setup(query_str=str()):
    conn = lite.connect('pet.db')
    c = conn.cursor()
    for line in query_str:
        c.execute(line)
        conn.commit()
    conn.close()


def split_query(query_str):
    query_return = [line+');' for line in query_str.split(');')]
    query_return.pop()
    return query_return



def main():
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

    q = split_query(query)
    db_setup(q)

if __name__ == '__main__':
    main()