class Person:
    def __init__(self, name, age, gender):
        """Initialize the attributes for the Person class."""
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """Print a message introducing the person."""
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")


person = Person("Magakwe Molebane", 26, "Male")


person.introduce()
