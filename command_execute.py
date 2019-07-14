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
        func = self.find_function(cmd)
        return func(cmd)

    def find_function(self, cmd):
        function_switcher = {
            'create_parking_lot': 'create_parking_lot',
            'park': 'park',
            'leave': 'leave',
            'status': 'status'
        }
        return function_switcher.get(cmd, lambda: 'Invalid Command')

    def create_parking_lot(self, cmd):
        print(cmd, "****")

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
