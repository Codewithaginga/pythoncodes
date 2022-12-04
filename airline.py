
#tracking booking to avoid overbooked

class Flight():

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):

        if not self.open_seats():
            return False
        self.passengers.append(name)

        return True

    def open_seats(self):

        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["aginga", "george", "sammy", "eunita"]

for person in people:
    
    if flight.add_passenger(person):
        print(f"added {person} to flight successfull")

    else:
        print(f"No availble seat for {person}")
