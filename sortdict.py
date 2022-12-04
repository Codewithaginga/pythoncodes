people = [

    {"name": "Harry", "House": "azuri"},
    {"name": "George", "House": "hazuri"},
    {"name": "Eunita", "House": "imani"}
]

def f(person):
    return person["House"]


people.sort(key=f)
print(people)