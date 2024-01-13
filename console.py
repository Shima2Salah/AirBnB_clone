#!/usr/bin/python3
"""Program console"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class that displays the console"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Command to exit the program"""
        return True

    def do_EOF(self, args):
        """Command on console (CTRL + D)"""
        return True

    def do_create(self, args):
        """Command to create an instance of a class."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State",
                             "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            new = eval(args[0])()
            new.save()
            print(new.id)

    def do_all(self, args):
        """Command to print the string representation of all instances."""
        args = shlex.split(args)
        if args == []:
            models.storage.reload()
            ans_list = []
            for ins, obj in models.storage.all().items():
                ans_list.append(obj.__str__())
            print(ans_list)
        elif args[0] not in ["BaseModel", "User", "Place", "State",
                             "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            ans_list = []
            for ins, obj in models.storage.all().items():
                if obj.__class__.__name__ == args[0]:
                    ans_list.append(obj.__str__())
            print(ans_list)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State",
                             "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            for ins, obj in models.storage.all().items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    print(obj.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State",
                             "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            curr_objs = models.storage.all()
            for ins, obj in curr_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    del(curr_objs[ins])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State",
                             "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            curr_objs = models.storage.all()
            for ins, obj in curr_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(args) == 3:
                        print("** value missing **")
                        return
                    else:
                        new_arg = args[3]
                        if hasattr(obj, str(args[2])):
                            new_arg = (type(getattr(obj, args[2])))(args[3])
                        obj.__dict__[args[2]] = new_arg
                        models.storage.save()
                        return
            print("** no instance found **")

    def emptyline(self):
        """An empty line doesn't execute anything"""
        pass

    def default(self, args):
        """Handling of default command."""
        try:
            self.onecmd(eval(args))
        except:
            print("*** Unknown syntax: " + args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
