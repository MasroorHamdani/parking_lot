from functools import partial

from constant import COMMANDS

class CommandExecute():
    """
    This class will handle all the commands to be executed
    """
    def __init__(self, maxParking = 6): #default kept at 10
        # parking slot number --> registration plate and color 
        self.by_parkslot = {}
        #color --> registration number
        self.by_color_regisNum = {}
        # color -->  parking slot
        self.by_color_parkslot ={}    
        # registration plate number --> parking slot number        
        self.by_regisNum_parkslot = {}
        # parking slot capacity : default at 10
        self.parkslot_capacity = 0

        # empty slot numbers : All are empty at the start
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
            self.execute_command(command_array)

    def execute_command(self, cmd):
        """
        This function will validate if the passed command is part of our defines funcation so not,
        in case undefined command is passed, it will return the error message and continue.
        For valid command those will be sent to switch to be redirfected to relavant function
        """
        if cmd[0] not in COMMANDS:
            output = 'Invalid Command Passed'
            print(output)
            return output
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
        if len(cmd) < 2:
            output = 'Please Enter valid Max limit' 
            print(output)
            
        else:
            self.maxParking = maxParking
            self.empty_parkslot = list(range(1, int(maxParking)+1))
            output = "Created a parking lot with {} slots".format(maxParking) 
            print(output)
            
        return output

    def park(self, cmd):
        """
        Check for the parking slot availbility
        If space is avaible the park the car, saving its details
        """
        vehicle_details = {}
        vehicle_details['regisNum'] = cmd[1] if len(cmd) >=2 else ''
        vehicle_details['color'] = cmd[2] if len(cmd) >=3 else ''
        if vehicle_details.get('regisNum') and vehicle_details.get('color'):
            # check if available space in parking lot 
            if len(self.empty_parkslot) == 0: # if no parking space available
                # return status :  Sorry, parking lot is full
                output = 'Sorry, parking lot is full'
                print(output)
            else:
                # sort the empty parking list : ascending order
                self.empty_parkslot.sort()
                # parking slot number for incoming vehicle
                # allocate the slot with minimum value : as suggested
                slot = self.empty_parkslot.pop(0)

                # registration number 
                regisNum = vehicle_details['regisNum']
                # incoming vehicle color
                color = vehicle_details['color']
                # insert all the details against search keys on parking slot num
                self.by_parkslot[slot]  = {'regisNum': regisNum, 'color':color}

                # tertiary storage: insert to other mapped fast query storage
                self.by_color_parkslot.setdefault(color,[]).append(slot)
                self.by_color_regisNum.setdefault(color,[]).append(regisNum)
                self.by_regisNum_parkslot[regisNum] = slot

                #return success status : Allocated slot number 3 (ex)
                output = 'Allocated slot number: {}'.format(slot)
                print(output)
                
        else:
            output = 'Please Enter Valid Command'
            print(output)
        return output

    def leave(self, cmd):
        slot = cmd[1] if len(cmd) >=2 else ''
        regisNum = self.by_parkslot[int(slot)].get('regisNum')
        color = self.by_parkslot[int(slot)].get('color')
        # delete the teriary dependency  data 
        del self.by_regisNum_parkslot[regisNum]  # deletes regist->parkinglot map
        # remove the slot against color  if exits 
        try:
            self.by_color_parkslot[color].remove(int(slot))
        except Exception as ex:
            # shouldnt arise unless spurious entry vs exit mechanism
            print("Error - there{}".format(ex))
            return
        try:
            self.by_color_regisNum[color].remove(regisNum)
        except Exception as ex:
            print("Error - here {}".format(ex))
            return
        # delete the primary data resource entry
        del self.by_parkslot[int(slot)]
        # insert new empty parling slot
        self.empty_parkslot.append(int(slot))
        output = 'Slot number {} is free'.format(slot)
        print(output)
        return output

    def status(self, cmd):
        print('Slot No, \t Registration No \t Colour')
        for key, value in self.by_parkslot.items():
            print('{}, \t\t {} \t\t {}'.format(key, value.get('regisNum'), value.get('color')))
        return

    def registration_numbers_for_cars_with_colour(self, cmd):
        color = cmd[1] if len(cmd) >=2 else ''
        slot_list = self.by_color_regisNum.get(color)
        if color:
            if slot_list:
                print(slot_list)
                output = slot_list
            else:
                output = "Not Found"
                print(output)
        else:
            output = "Please pass Valid Color"
            print(output)
        return

    def slot_numbers_for_cars_with_colour(self, cmd):
        color = cmd[1] if len(cmd) >=2 else ''
        slot_list = self.by_color_parkslot.get(color)
        if color:
            if slot_list:
                print(slot_list)
                output = slot_list
            else:
                output = 'Not Found'
                print(output)
        else:
            output = "Please pass Valid Color"
            print(output)
        return output

    def slot_number_for_registration_number(self, cmd):
        regis = cmd[1] if len(cmd) >=2 else ''
        park_lot = self.by_regisNum_parkslot.get(regis)
        if regis:
            if park_lot:
                print(park_lot)
            else:
                print('Not Found')
        else:
            print("Please pass Valid Registarion number")
        return
