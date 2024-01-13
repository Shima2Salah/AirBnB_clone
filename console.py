#!/usr/bin/python3
"""Parent class for running in cmd"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Parent Command class"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """method end the file of app"""
        print("")
        return True

    def emptyline(self):
        """method doesnt print previous command"""
        pass

    def do_create(self, arg):
        """method for creating new class"""
        arguments = arg.split()
        if len(arguments) != 1:
            print("** class name missing **")
            return
        new_class = arguments[0]
        if new_class not in globals():
            print("** class doesn't exist **")
            return
        all_classes = globals()[new_class]
        inst = all_classes()
        inst.save()
        print(inst.id)

    def do_show(self, arg):
        """method print string representation of instance"""
        arguments = arg.split()
        if len(arguments) != 2:
            if len(arguments) == 0:
                print("** class name missing **")
            else:
                print("** instance id missing **")
            return
        class_name, instance_id = arguments
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_class = globals()[class_name]
        key = f"{class_name}.{instance_id}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        inst = models.storage.all()[key]
        print(inst)

    def do_destroy(self, arg):
        """method deletes an instance"""
        arguments = arg.split()
        if len(arguments) != 2:
            if len(arguments) == 0:
                print("** class name missing **")
            else:
                print("** instance id missing **")
            return
        class_name, instance_id = arguments
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        destroyed_class = globals()[class_name]
        key = f"{class_name}.{instance_id}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg == "":
            print("** class name missing **")
            return
        if arg == "all":
            all_inst = [str(inst) for inst in models.storage.all().values()
                        if isinstance(inst, eval(arg))]
            if not all_inst:
                print("** class doesn't exist **")
            else:
                print("\n".join(all_inst))

    def do_update(self, arg):
        """Updates an instance based on the class"""
        arguments = arg.split()
        if len(arguments) != 4:
            if len(arguments) < 4:
                if len(arguments) == 0:
                    print("** class name missing **")
                elif len(arguments) == 1:
                    print("** instance id missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = arguments
        if class_name not in globals():
            print("** class name missing **")
            return
        updated_class = globals()[class_name]
        key = f"{class_name}.{instance_id}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        inst = models.storage.all()[key]
        if attr_name == "email" and attr_value.endswith("@example.com"):
            inst.email = attr_value
        elif attr_name == "amenity" and attr_value in ["pool", "jacuzzi"]:
            inst.amenity = eval(attr_value)
        else:
            setattr(inst, attr_name, eval(attr_value))
        inst.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
