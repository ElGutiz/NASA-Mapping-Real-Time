from sgp4.api import Satrec

s = '1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991'
t = '2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482'
satellite = Satrec.twoline2rv(s, t)
#print(satellite)
jd, fr = 2458827, 0.362605
e, r, v = satellite.sgp4(jd, fr) 
#print(e)

print(r)# True Equator Mean Equinox position (km)
print(v)# True Equator Mean Equinox velocity (km/s)



import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://celestrak.com/NORAD/elements/2019-006.txt')
data = r.data.decode('utf-8')
p = data.split('\n')
p.remove(p[len(p)-1])
#print(p[0])
#print(p[1])
#print(p[2])

s = p[1]
t = p[2]
satellite = Satrec.twoline2rv(s, t)
#print(satellite)
jd, fr = 2458827, 0.362605
e, r, v = satellite.sgp4(jd, fr) 
#print(e)
#print(p[0])
#print(r)# True Equator Mean Equinox position (km)
#print(v)# True Equator Mean Equinox velocity (km/s)
from sgp4.api import SGP4_ERRORS

from sgp4.api import jday
#jd, fr = jday(2021, 9, 28, 12, 52, 0)
#print(jd, fr)

