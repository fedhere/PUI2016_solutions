from __future__ import print_function
__author__ = 'fb55'

import sys
import urllib2
import json

DEBUG = False  # change to True for debugging statements

if __name__ == '__main__':
    '''Displays the location of all MTA busses currently running for a given bus line.

    Arguments: 
        MTA key
        Bus line

    Output:
        print to screen
    '''

    if not len(sys.argv) == 3:
        print('''USAGE:
        $python show_bus_locations.py <MTA_KEY> <BUS_LINE>''')
        sys.exit()
    key, bus_line = sys.argv[1:]
    print('BUS LINE:', bus_line)

    bus_url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + key + \
               '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line

    if DEBUG:
        print("the url is:", bus_url)

    # queries the url for json format bus data
    response = urllib2.urlopen(bus_url)
    busdata = json.load(response)

    # counting the number of active busses
    nbusses = len(busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]\
                  ['VehicleActivity'])

    print('Number of Active Buses : %d' % nbusses)

    # extracting and printing info for each bus
    for i in range(nbusses):
        busi = busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]\
               ['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']

        print('Bus %d is at latitude %f and longitude %f' % (i,
                                                              busi['Latitude'],
                                                              busi['Longitude']))
