#!/usr/bin/python3


import cmd


class HBnBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None

    def do_quit(self, arg):
        'Exit the interactive console'
        return True

    def do_EOF(self, arg):
        'Exit the interactive console'
        return True


if __name__ == '__main__':
    HBnBCommand().cmdloop()
