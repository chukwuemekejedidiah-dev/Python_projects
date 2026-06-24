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



#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass


# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.__class__.__name__} makes the sound 'woof'")
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.__class__.__name__} makes the sound 'meow'")
#
#
# class Goat(Animal):
#     def make_sound(self):
#         print(f"a {self.__class__.__name__} makes the sound 'bleat'")
#
#
# class Human(Animal):
#     def make_sound(self):
#         print(f" a {self.__class__.__name__} makes the sound 'Hello'")
#
#
# if __name__ == "__main__":
#     animals = [Dog(), Cat(), Goat(), Human()]
#     for animal in animals:
#         animal.make_sound()
