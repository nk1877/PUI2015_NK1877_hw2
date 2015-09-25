import datetime
import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    B52Assignment = json.load(request)
    sum=0;
    #Longitude= B52Assignment['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][1]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']#['VehicleLocation']
    #Latitude=B52Assignment['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][1]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    #print "Bus i is at lattitude {} and longitude {} " .format(Latitude,Longitude)

    k= B52Assignment['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    for rs in k:
        longi= rs['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        lat= rs['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        print "Bus {0} is at lattitude {1} and longitude {2} " .format(sum,lat,longi)
        sum+=1
    print "Number of active buses: {}" .format(sum)
