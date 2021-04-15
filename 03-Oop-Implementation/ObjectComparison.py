
 class PersonCompetence:
    def __init__(self, name, senior, age):
        self.name = name
        self.senior = senior
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    list_or_person = []
    list_or_person.append(PersonCompetence("Edward", 12, 50))
    list_or_person.append(PersonCompetence("Edward2", 12, 10))
    list_or_person.append(PersonCompetence("Edward3", 12, 20))

    print(list_or_person)
    print(sorted(list_or_person))