#!/usr/bin/python3
"""Parent class for running in cmd"""
import cmd
from models import storage
from models.base_model import BaseModel


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
        """method doesnot print previous command"""
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
        if key not in storage.all():
            print("** no instance found **")
            return
        inst = storage.all()[key]
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
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """method Prints all str representn of all inst"""
        arguments = arg.split()
        if len(arguments) > 1:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            class_name = arguments[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            req_class = globals()[class_name]
            print([str(inst) for inst in storage.all().values()
                   if isinstance(inst, req_class)])
        else:
            print([str(inst) for inst in storage.all().values()])

    def do_update(self, arg):
        """method for Updates instance based on the class name"""
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
            print("** class doesn't exist **")
            return
        updated_class = globals()[class_name]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        inst = storage.all()[key]
        setattr(inst, attr_name, eval(attr_value))
        inst.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
