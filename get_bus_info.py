import datetime
import json
import sys
import urllib2
import csv

if __name__=='__main__':
    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    B52Assignment = json.load(request)
    k=B52Assignment['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    print "lattitude,  Longitude,  Stop Name,  StopStatus"
    with open('%s' %(sys.argv[3]), 'wb') as fp:
        data = [["lattitude","Longitude","Stop Name","StopStatus"]]
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)
        for num in k:
            lat = num['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            lon = num['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            sn= num['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
            status=num['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
            if(lat == " " or lon == " " or sn == " " or status == " "):
                data = [["N/A"]]
            else:
                data = [[lat, lon,sn,status]]
                a.writerows(data)
                print "{}   {}  {}  {}" .format(lat,lon,sn,status)
