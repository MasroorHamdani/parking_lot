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

    def test_park_invalid_noreg_cmd(self):
        cmd = 'park    '
        cmd_list = cmd.split()
        result = command_execute_obj.park(cmd_list)
        expected_result = "Please Enter Valid Command"
        self.assertEqual(expected_result, result)

    def test_park_leave(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # Leave slot 1
        cmd = 'leave 1'
        cmd_list = cmd.split()
        result = command_execute_obj.leave(cmd_list)
        expected_result = "Slot number 1 is free"
        self.assertEqual(expected_result, result)

    def test_park_invalid_leave_input(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # Leave without passing slot
        cmd = 'leave'
        cmd_list = cmd.split()
        result = command_execute_obj.leave(cmd_list)
        expected_result = "Please Enter Valid Command"
        self.assertEqual(expected_result, result)

    def test_park_invalid_leave_slot(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # Leave with invalid slot
        cmd = 'leave 7'
        cmd_list = cmd.split()
        result = command_execute_obj.leave(cmd_list)
        expected_result = "Not Found"
        self.assertEqual(expected_result, result)

    def test_park_status(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # status command
        cmd = 'status'
        cmd_list = cmd.split()
        result = command_execute_obj.status(cmd_list)
        expected_result = "1, \t\t KA-01-HH-1234 \t\t White"
        self.assertEqual(expected_result, result)

    def test_park_reg_with_color(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 Red'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # registration_numbers_for_cars_with_colour command execution
        cmd = 'registration_numbers_for_cars_with_colour Red'
        cmd_list = cmd.split()
        result = command_execute_obj.registration_numbers_for_cars_with_colour(cmd_list)
        expected_result = ['KA-01-HH-1234']
        self.assertEqual(expected_result, result)

    def test_park_reg_with_color_insensitive(self):
        """
        Search across is case sensitive
        """
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # registration_numbers_for_cars_with_colour command execution
        cmd = 'registration_numbers_for_cars_with_colour white'
        cmd_list = cmd.split()
        result = command_execute_obj.registration_numbers_for_cars_with_colour(cmd_list)
        expected_result = 'Not Found'
        self.assertEqual(expected_result, result)

    def test_park_reg_with_color_invalid_param(self):
        """
        Search across is case sensitive
        """
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-1234 White'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # registration_numbers_for_cars_with_colour command execution
        cmd = 'registration_numbers_for_cars_with_colour'
        cmd_list = cmd.split()
        result = command_execute_obj.registration_numbers_for_cars_with_colour(cmd_list)
        expected_result = 'Please pass Valid Color'
        self.assertEqual(expected_result, result)

    def test_park_slot_with_color(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-22 Blue'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # slot_numbers_for_cars_with_colour command execution
        cmd = 'slot_numbers_for_cars_with_colour Blue'
        cmd_list = cmd.split()
        result = command_execute_obj.slot_numbers_for_cars_with_colour(cmd_list)
        expected_result = [1]
        self.assertEqual(expected_result, result)

    def test_park_slot_with_color_invalid_param(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-22 Blue'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # slot_numbers_for_cars_with_colour command execution
        cmd = 'slot_numbers_for_cars_with_colour'
        cmd_list = cmd.split()
        result = command_execute_obj.slot_numbers_for_cars_with_colour(cmd_list)
        expected_result = "Please pass Valid Color"
        self.assertEqual(expected_result, result)

    def test_park_slot_with_color_invalid_color(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-22 Blue'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # slot_numbers_for_cars_with_colour command execution
        cmd = 'slot_numbers_for_cars_with_colour Green'
        cmd_list = cmd.split()
        result = command_execute_obj.slot_numbers_for_cars_with_colour(cmd_list)
        expected_result = "Not Found"
        self.assertEqual(expected_result, result)

    def test_park_slot_with_reg(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-22 Blue'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # slot_numbers_for_cars_with_colour command execution
        cmd = 'slot_number_for_registration_number KA-01-HH-22'
        cmd_list = cmd.split()
        result = command_execute_obj.slot_number_for_registration_number(cmd_list)
        expected_result = 1
        self.assertEqual(expected_result, result)

    def test_park_slot_with_reg_invalid_param(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-22 Blue'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # slot_numbers_for_cars_with_colour command execution
        cmd = 'slot_number_for_registration_number'
        cmd_list = cmd.split()
        result = command_execute_obj.slot_number_for_registration_number(cmd_list)
        expected_result = "Please pass Valid Registarion number"
        self.assertEqual(expected_result, result)

    def test_park_slot_with_reg_invalid_regis(self):
        # Allocate Space
        cmd = 'create_parking_lot 1'
        cmd_list = cmd.split()
        command_execute_obj.create_parking_lot(cmd_list)
        # Add one parking
        cmd = 'park KA-01-HH-22 Blue'
        cmd_list = cmd.split()
        command_execute_obj.park(cmd_list)
        # slot_numbers_for_cars_with_colour command execution
        cmd = 'slot_number_for_registration_number KK-01-11-NH'
        cmd_list = cmd.split()
        result = command_execute_obj.slot_number_for_registration_number(cmd_list)
        expected_result = "Not Found"
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()