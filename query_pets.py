import sqlite3 as lite


def prog():
    while True:
        choice_str = []
        choice = input('Please select person ID number: ')
        choice_str = choice_str + ["SELECT first_name, last_name, age FROM person WHERE id = {}".format(choice)]
        choice_str = choice_str + ["SELECT pet.name, pet.breed, pet.age, pet.dead FROM ((pet \
                                   INNER JOIN person ON person_pet.person_id = person.id)\
                                   INNER JOIN pet ON person_pet.pet_id = pet.id)\
                                   WHERE person_id = {}".format(choice)]
        if choice == "-1":
            exit()
        else:
            db_query(choice_str)


"""SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID)
WHERE Orders.OrderID =  10248;
"""


def db_query(query_str):
    conn = lite.connect('pet.db')
    c = conn.cursor()
    for l in query_str:
        c.execute(l)
        print(c.fetchall())
        conn.commit()
    conn.close()


if __name__ == '__main__':
    prog()
