#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """This is the BASE which shows the base for other classes in project 0x0C.

    Private Class Attributes:
        __nb_object (int): this is the number of bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """this sets new base Base.

        Args:
            id (int): this identify the new base set.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): this is a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """encode JSON serialization list of objects to a file.

        Args:
            list_objs (list): this is a list of inherited Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """shows deserialization of a JSON string.

        Args:
            json_string (str): A JSON string rep of a list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """this return class of instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """encodes CSV serialization objects to a file.

        Args:
            list_objs (list): collection of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """shows CSV of classes instantiated from afile.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Outputs Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        pturt = turtle.Turtle()
        pturt.screen.bgcolor("#b7312c")
        pturt.pensize(3)
        pturt.shape("turtle")

        pturt.color("#ffffff")
        for rect in list_rectangles:
            pturt.showturtle()
            pturt.up()
            pturt.goto(rect.x, rect.y)
            pturt.down()
            for i in range(2):
                pturt.forward(rect.width)
                pturt.left(90)
                pturt.forward(rect.height)
                pturt.left(90)
            pturt.hideturtle()

        pturt.color("#b5e3d8")
        for sq in list_squares:
            pturt.showturtle()
            pturt.up()
            pturt.goto(sq.x, sq.y)
            pturt.down()
            for i in range(2):
                pturt.forward(sq.width)
                pturt.left(90)
                pturt.forward(sq.height)
                pturt.left(90)
            pturt.hideturtle()

        pturtle.exitonclick()
