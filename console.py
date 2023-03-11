#!/usr/bin/python3
"""Class for the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """The Command Class"""
    prompt = '(hbnb)'
    __classes = {
        "BaseModel"
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
        arg1 = arg.split()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg1[0], arg1[1])])

    def do_destroy(self, arg):
        """
          Deletes an instance based on the class name and id,
          (save the change into the JSON file).
        """
        objdict = models.storage.all()
        arg1 = arg.split()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg1[0], arg1[1])]
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
