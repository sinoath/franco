import csv

class Patient:
    all = []
    def __init__(self, name:str, surname:str, age:int, ID):
        assert age > 0, f"Negative value: age is {age}, must be a positive integer"

        self.__name = name
        self.__surname = surname
        self.age = age
        self.ID = ID
        Patient.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def prognosis(self):
        pass

    @property
    def diagnosis(self):
        pass

    @classmethod
    def instantiate_from_csv(cls, location:str):
        with open(location, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Patient(
                        name = row['name'],
                        surname = row['surname'],
                        age = int(row['age']),
                        ID = int(row['ID'])
                        )

    def __repr__(self):
        return f"Paziente  ID:{self.ID}, {self.__name} {self.__surname}, anni {self.age}"
