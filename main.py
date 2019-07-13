#!/usr/bin/env python3
import sys, os

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) >= 2 else ''
    if file_path:
        cmd_list = []
        if os.path.isfile(file_path):
            f = open(file_path, 'r')
            for line in f:
                cmd_list.append(line)
    else:
        while True:
            command = input("Press Enter the command..\n")
            if command == 'exit':
                break
