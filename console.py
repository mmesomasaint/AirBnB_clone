#!/usr/bin/python3
"""Class for the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """The Command Class"""
    prompt = '(hbnb)'
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_quit(self, arg):
        'Exit the interactive console'
        return True

    def do_EOF(self, arg):
        'Exit the interactive console'
        return True

    def do_create(self, arg):
        """
          Creates a new instance of BaseModel,
          saves it (to the JSON file) and prints the id.
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            models.storage.new(obj)
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """
          Prints the string representation of an instance
          based on the class name and id.
        """
        objdict = models.storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
          Deletes an instance based on the class name and id,
          (save the change into the JSON file).
        """
        objdict = models.storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            models.storage.save()

    def do_all(self, arg):
        """
          Prints all string representation of all instances
          based or not on the class name.
        """
        objdict = models.storage.all()
        args = arg.split()
        if len(args) == 0:
            print([obj.__str__() for obj in objdict.values()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            all = []
            for key, obj in objdict.items():
                keys = key.split(".")
                if keys[0] == args[0]:
                    all.append(obj.__str__())
            print(all)

    def do_update(self, arg):
        """
          Updates an instance based on the class name and id
          by adding or updating attribute (save the change into the JSON file).
        """
        objdict = models.storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = objdict["{}.{}".format(args[0], args[1])]
            obj.__dict__[args[2]] = args[3]
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
