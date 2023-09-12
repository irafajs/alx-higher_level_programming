class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance."""
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student with values from json."""
        for key, value in json.items():
            setattr(self, key, value)
