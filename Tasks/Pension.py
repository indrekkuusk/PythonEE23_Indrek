class Person:
    def __init__(self, name, surname, gender, age, personal_id):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.personal_id = personal_id

    def is_retired(self):
        """Check whether the person has reached the retirement age."""
        if self.gender == 'male':
            return self.age >= 65
        elif self.gender == 'female':
            return self.age >= 60
        else:
            return False  # Assuming non-binary individuals have no specific retirement age

    def age_difference(self, other_person):
        """Return the age difference between this person and another person."""
        return abs(self.age - other_person.age)

# Example usage
person1 = Person("John", "Doe", "male", 70, "123456789")
person2 = Person("Jane", "Doe", "female", 65, "987654321")

print(f"{person1.name} {person1.surname} is retired:", person1.is_retired())
print(f"{person2.name} {person2.surname} is retired:", person2.is_retired())

age_diff = person1.age_difference(person2)
print(f"Age difference between {person1.name} and {person2.name} is {age_diff} years.")

# In this solution:
#
# We define a Person class with fields name, surname, gender, age, and personal_id in the constructor (__init__ method).
# The is_retired method checks whether the person has reached the retirement age based on their gender.
# The age_difference method calculates the absolute difference in age between the current person and another person.
# We demonstrate the usage of these methods with example instances of the Person class (person1 and person2).




