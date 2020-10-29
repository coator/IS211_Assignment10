import pets
import query_pets
import load_pets
import os

def main():
    if os.path.exists("pet.db"):
        os.remove("pet.db")
    else:
        pass
    a = open("pet.db", "w")
    a.close()
    pets.main()
    load_pets.main()
    query_pets.main()

main()