#!/usr/bin/python3
"""Class for the entry point of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel


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
            print(eval(arg)().id)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
