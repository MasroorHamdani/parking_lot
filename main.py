#!/usr/bin/env python3
import sys, os

from command_execute import CommandExecute

command_execute_obj = CommandExecute(12)

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
                f = open(file_path, 'r')
                lines = f.readlines()
                f.close()
                # for line in lines:
                #     cmd_list = line.split()
                command_execute_obj.execute_file(lines)
                # cmd_list = cmd_list.split()
                # command_execute_obj.execute_file(cmd_list)
        else:
            while True:
                cmd_input = input("Press Enter the command..\n")
                cmd_list = cmd_input.split()
                if cmd_list[0] == 'exit':
                    break
                command_execute_obj.execute_command(cmd_list)
    except Exception as e:
        print("Error Occured {}".format(e))

if __name__ == "__main__":
    """
    Entry point for our script
    """
    main()
