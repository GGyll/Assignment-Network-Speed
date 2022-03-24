import unittest
from solution import NetworkStation, Device, input_network_stations, initialize




class NetworkSpeedTestCase(unittest.TestCase):
    
    @classmethod
    def setUp(cls):     
        cls.stations = input_network_stations()

    # Individual function tests
    def test_network_device_distance(self):
        n = NetworkStation(x_pos=2,y_pos=5, reach=5)
        distance = round(n.network_device_distance(3, 9), 2)
        self.assertEqual(distance, 4.12)
        
    def test_network_speed(self):
        n = NetworkStation(x_pos=2,y_pos=5, reach=5)
        speed = round(n.network_speed(5, 4), 2)
        self.assertEqual(speed, 3.38)

    def test_network_speed_out_of_reach(self):
        n = NetworkStation(x_pos=2,y_pos=5, reach=5)
        speed = round(n.network_speed(100, 100), 2)
        self.assertEqual(speed, 0)

    # Tests obtaining best_network_station
    def test_initialize(self):
        device=[{'x' : 0, 'y' : 0}]
        best_network_station = initialize(self.stations, device)[0][1]
        self.assertEqual(best_network_station.id, 1)

    def test_initialize_2(self):
        device=[{'x' : 4, 'y' : 10}]
        best_network_station = initialize(self.stations, device)[0][1]
        self.assertEqual(best_network_station.id, 4)

    def test_initialize_no_station_found(self):
        device=[{'x' : 120, 'y' : 64}]
        initialize(self.stations, device)
        self.assertRaises(AttributeError)

