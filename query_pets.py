import sqlite3 as lite


def main():
    while True:
        choice_str = []
        choice = input('Please select person ID number: ')
        choice_str = choice_str + ["SELECT first_name, last_name, age FROM person WHERE id = {}".format(choice)]
        choice_str = choice_str + ["""SELECT p.name, p.breed, p.age, p.dead 
                                    FROM pet p
                                    INNER JOIN person_pet pp
                                    ON pp.pet_id = p.id
                                    INNER JOIN person pe
                                    ON pp.person_id =  pe.id
                                    WHERE pe.id = {}""".format(choice)]
        if choice == "-1":
            exit()
        else:
            db_query(choice_str)


def db_query(query_str):
    conn = lite.connect('pet.db')
    c = conn.cursor()
    for l in query_str:
        c.execute(l)
        a = c.fetchall()
        conn.commit()
        if len(a) == 0:
            print('No object found')
        else:
            print(a)
    conn.close()


if __name__ == '__main__':
    main()
