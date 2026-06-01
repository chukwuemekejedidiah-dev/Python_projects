class Patient:

    def __init__(self, patient_id, name, age, illness):
        self.patient_id = patient_id
        self.name = name
        self._age = age
        self._illness = illness

    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self._age)
        print("Illness:", self._illness)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Invalid age")

    @property
    def illness(self):
        return self._illness

    @illness.setter
    def illness(self, illness):
        self._illness = illness


patient1 = Patient(101, "John Kirk", 25, "Malaria")

patient1.display_info()

print("\nPatient Age:", patient1.age)
print("Patient Illness:", patient1.illness)

patient1.age = 26
patient1.illness = "Typhoid"

print("\nUpdated Patient Information")
patient1.display_info() 