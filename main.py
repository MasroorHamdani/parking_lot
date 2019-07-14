#!/usr/bin/env python3
import sys, os

from command_execute import CommandExecute

command_execute_obj = CommandExecute()


def main():
    """
    This function will handle the interaction part
    Differentiates if the commands are passed
    as a file or manually
    """
    try:
        file_path = sys.argv[1] if len(sys.argv) >= 2 else ''
        if file_path:
            cmd_list = []
            if os.path.isfile(file_path):
                cmd_list = open(file_path, 'r')
                command_execute_obj.execute_file(cmd_list)
        else:
            while True:
                cmd = input("Press Enter the command..\n")
                if cmd == 'exit':
                    break
                command_execute_obj.execute_command(cmd)
    except Exception as e:
        print("Error Occured {}".format(e))

if __name__ == "__main__":
    """
    Entry point for our script
    """
    main()
