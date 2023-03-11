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
        'Create a new instance of Base Model'
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
          Display the string representation of a class instance of a given id.
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
