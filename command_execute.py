from functools import partial

class CommandExecute():
    """
    This class will handle all the commands to be executed
    """
    def execute_file(self, cmd_list):
        """
        This function will take all the commands
        from the file passed as argument
        Pass commands to relavant functions one by one
        """
        for line in cmd_list:
            self.execute_command(line)

    def execute_command(self, cmd):
        return self.switch(cmd)

    def switch(self, cmd):
        default = "Incorrect Command Passed"
        return getattr(self, cmd, lambda: default)(cmd)

    def create_parking_lot(self, cmd):
        print(cmd, "****")
        return

    def park(self, cmd):
        print(cmd)

    def leave(self, cmd):
        print(cmd)

    def status(self, cmd):
        print(cmd)

    def registration_numbers_for_cars_with_colour(self, cmd):
        print(cmd)

    def slot_numbers_for_cars_with_colour(self, cmd):
        print(cmd)

    # def invalid_cmd(self, cmd):
    #     print('Invalid Command Passed')
