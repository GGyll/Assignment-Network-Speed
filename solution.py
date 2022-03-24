from math import dist

class NetworkStation:
    _stations = []

    def __init__(self, x_pos, y_pos, reach):
        self.id = len(NetworkStation._stations) + 1
        # Assign coordinates & reach
        self.x_pos, self.y_pos = x_pos, y_pos
        self.reach = reach
        # Append to object manager list to keep track
        NetworkStation._stations.append(self)

    # Get distance between Device and Network Station
    def network_device_distance(self, device_x_pos, device_y_pos):
        distance = dist( 
                        (device_x_pos, device_y_pos), 
                        (self.x_pos, self.y_pos)
                    )
        return distance

    # Get speed from distance
    def network_speed(self, device_x_pos, device_y_pos):  
        distance = self.network_device_distance(device_x_pos, device_y_pos)
        # print(f'DISTANCE: {distance}')
        if distance > self.reach:
            speed = 0
            # print(f'Discarding distance: {distance} for {self}')
        else:
            speed = (self.reach - distance) ** 2   
        return speed

    def __repr__(self):
        return ': '.join(['STATION', str(self.id)])

class Device:
    _devices = []
    
    def __init__(self, x_pos, y_pos):
        self.id = len(Device._devices) + 1
        # Assign coordinates
        self.x_pos, self.y_pos = x_pos, y_pos
        # Append to object manager list to keep track
        Device._devices.append(self)
    
    # Main function to determine the best station for each device
    def best_network_station(self):
        best_speed, best_station = 0, None

        for station in NetworkStation._stations: 
            speed = station.network_speed(self.x_pos, self.y_pos)
            # print(f'{station}, SPEED: {speed}')
            if speed > best_speed:
                best_speed = speed
                best_station = station 
        # print(f' BEST SPEED: {best_speed}')
        
        if best_station == None:
            print(f'No network station within reach for {self} at point {self.x_pos},{self.y_pos}')
            return
        else:
            print(f'Best network station for {self} at point {self.x_pos},{self.y_pos} is {best_station} located at {best_station.x_pos},{best_station.y_pos} with speed {round(best_speed, 2)}')
            return best_station

    def __repr__(self):
        return ': '.join(['DEVICE', str(self.id)])

# DATA INPUTS

# Network Stations
def input_network_stations():
    station_1 = {'x' : 0, 'y' : 0, 'reach': 9}
    station_2 = {'x' : 20, 'y' : 20, 'reach': 6}
    station_3 = {'x' : 10, 'y' : 0, 'reach': 12}
    station_4 = {'x' : 5, 'y' : 5, 'reach': 13}
    station_5 = {'x' : 99, 'y' : 25, 'reach': 2}
    stations = [station_1, station_2, station_3, station_4, station_5]
    return stations

# Devices
def input_devices():
    device_1 = {'x' : 0, 'y' : 0}
    device_2 = {'x' : 100,'y' : 100}
    device_3 = {'x' : 15, 'y' : 10}
    device_4 = {'x' : 18, 'y' : 18}
    device_5 = {'x' : 13, 'y' : 13}
    device_6 = {'x' : 25, 'y' : 99}
    devices = [device_1, device_2, device_3, device_4, device_5, device_6]
    return devices

# Initialize the objects and start the program
def initialize(stations, devices):
    # Create the NetworkStation objects
    for station in stations:
        NetworkStation(station['x'], station['y'], station['reach']) 
    
    # Create the Device objects and start the program
    best_network_stations = []
    for device in devices:
        d = Device(device['x'], device['y'])    
        # Append list of the device and it's best_network_station to the list
        best_network_stations.append([d, d.best_network_station()])
    return best_network_stations

# This only runs the solution if it is executed directly, so that we can unit test separately
if __name__ == "__main__":
    stations = input_network_stations()
    devices = input_devices()
    print(initialize(stations, devices))
