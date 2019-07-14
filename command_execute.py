from functools import partial

from constant import COMMANDS

class CommandExecute():
    """
    This class will handle all the commands to be executed
    """
    def __init__(self, maxParking = 10): #default kept at 10
        # parking slot number --> registration plate and color 
        self.by_parkslot = {}
        # color --> registration plate number, parking slot
        self.by_color_regis_parkslot ={}
        # empty slot numbers : All are empty at the start
        # registration plate number --> parking slot number        
        self.by_regisNum_parkslot = {}
        self.maxParking = maxParking
        self.empty_parkslot = list(range(1, maxParking+1))

    def execute_file(self, cmd_list):
        """
        This function will take all the commands
        from the file passed as argument
        Split the command line by line and pass to executable function
        """
        for line in cmd_list:
            command_array = line.split()
            print(self.execute_command(command_array))

    def execute_command(self, cmd):
        """
        This function will validate if the passed command is part of our defines funcation so not,
        in case undefined command is passed, it will return the error message and continue.
        For valid command those will be sent to switch to be redirfected to relavant function
        """
        if cmd[0] not in COMMANDS:
            print('Invalid Command Passed')
            return
        return self.switch(cmd)

    def switch(self, cmd):
        """
        This is a switch case defined.
        The function names and command are matching
        """
        default = "Incorrect Command Passed"
        return getattr(self, cmd[0], lambda: default)(cmd)

    def create_parking_lot(self, cmd):
        """
        Create the space for parking lot, depeing on the number passed
        """
        maxParking = cmd[1] if len(cmd) >=2 else ''
        self.maxParking = maxParking
        return "Created a parking lot with {} slots".format(maxParking)

    def park(self, cmd):
        """
        Check for the parking slot availbility
        If space is avaible the park the car, saving its details
        """
        vehicle_details = {}
        vehicle_details['regisNum'] = cmd[1] if len(cmd) >=2 else ''
        vehicle_details['color'] = cmd[2] if len(cmd) >=3 else ''

        # check if available space in parking lot 
        if len(self.empty_parkslot) == []: # if no parking space available
            # return status :  Sorry, parking lot is full
            return 'Sorry, parking lot is full' 
        else:
            # sort the empty parking list : ascending order
            self.empty_parkslot.sort()
            # parking slot number for incoming vehicle
            # allocate the slot with minimum value : as suggested
            print(self.empty_parkslot)
            slot = self.empty_parkslot.pop(0)
            print(slot)
            # registration number 
            regisNum = vehicle_details['regisNum']
            # incoming vehicle color
            color = vehicle_details['color']
            # insert all the details against search keys on parking slot num
            self.by_parkslot[slot]  = {'regisNum': regisNum, 'color':color}
            #
            # tertiary storage: insert to other mapped fast query storage
            #self.by_color_regis_parkslot[color] = {'regisNum':regisNum, 'slot':slot}
            self.by_color_regis_parkslot.setdefault(color,[]).append(slot)
            self.by_regisNum_parkslot[regisNum] = slot


            #return success status : Allocated slot number 3 (ex)
            return 'Allocated slot number: {}'.format(slot)

    def leave(self, cmd):
        print(cmd)
        slot = cmd[1] if len(cmd) >=2 else ''
        print(slot)
        regisNum = self.by_parkslot[slot]['regisNum']
        color = self.by_parkslot[slot]['color']
        # delete the teriary dependency  data 
        del self.by_regisNum_parkslot[regisNum]  # deletes regist->parkinglot map
        # remove the slot against color  if exits 
        try:
            self.by_color_regis_parkslot[color].remove(slot)
        except:
            # shouldnt arise unless spurious entry vs exit mechanism
            pass

        # delete the primary data resource entry
        del self.by_parkslot[slot]
        # insert new empty parling slot
        self.empty_parkslot.append(slot)

    def status(self, cmd):
        return self.by_parkslot

    def registration_numbers_for_cars_with_colour(self, cmd):
        print(cmd)

    def slot_numbers_for_cars_with_colour(self, cmd):
        print(cmd)

    def slot_number_for_registration_number(self, cmd):
        print(cmd)
    # def invalid_cmd(self, cmd):
    #     print('Invalid Command Passed')
