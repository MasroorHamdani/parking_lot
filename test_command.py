import unittest

# import CommandExecute from command_execute

from command_execute import CommandExecute
command_execute_obj = CommandExecute()

class TestCommand(unittest.TestCase):
    """
    Test cases for commands validation
    """
    def test_invalid_command(self):
        cmd = 'some unknow command'
        result = command_execute_obj.execute_command(cmd)
        expected_result = "Invalid Command Passed"
        self.assertEqual(expected_result, result)

    def test_create_parking(self):
        cmd = 'create_parking_lot 6'
        cmd_list = cmd.split()
        result = command_execute_obj.create_parking_lot(cmd_list)
        expected_result = "Created a parking lot with 6 slots"
        self.assertEqual(expected_result, result)

    def test_create_with_invalid_agu(self):
        cmd = 'create_parking_lot'
        cmd_list = cmd.split()
        result = command_execute_obj.create_parking_lot(cmd_list)
        expected_result = "Please Enter valid Max limit"
        self.assertEqual(expected_result, result)

    def test_park(self):
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        result = command_execute_obj.park(cmd_list)
        expected_result = "Allocated slot number: 1"
        self.assertEqual(expected_result, result)

    def test_park_full(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # try adding 2nd parking
        cmd = 'park KA-01-HH-9999 White'
        cmd_list = cmd.split()
        result = command_execute_obj.park(cmd_list)
        expected_result = "Sorry, parking lot is full"
        self.assertEqual(expected_result, result)

    def test_park_invalid_cmd(self):
        cmd = 'park KA-01-HH-1234'
        cmd_list = cmd.split()
        result = command_execute_obj.park(cmd_list)
        expected_result = "Please Enter Valid Command"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()