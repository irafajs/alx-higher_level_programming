#!/usr/bin/python3
"""
Shebang to create a python script
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherite rectangle properties"""
    def __init__(self, size, x=0, y=0, id=None):
        """function to initiate the attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """print out the formatted output"""
        return "[square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """method to set width"""
        return self.width

    @size.setter
    def size(self, value):
        """method size as a setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """method update to update and assign attribute"""
        arg_names = ("id", "size", "x", "y")
        if args:
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
