from sgp4.api import Satrec
from sgp4.api import jday
from datetime import datetime


#CONSTS
EARTH_EQUATORIAL_RADIUS = 6378.135  # equatorial radius
EARTH_FLATTENING_CONSTANT = 1 / 298.26
GEO_SYNC_RADIUS = 42164.57
class Derbis(object):
    def __init__(self,s,t):
        self.t=t
        self.s=s
        self.satellite = Satrec.twoline2rv(s, t)
    
    def propagar(self):
        #get actual date
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        now = now.split()
        #separar la fecha y la hora
        year,month,day=now[0].split('-')
        hour,minute,seconds=now[1].split(':')
        #get jd and fr from jday funcation
        self.jd, self.fr = jday(int(year),int(month),int(day),int(hour),int(minute),int(seconds))
        
        #get position and velocity based on jd and fr
        e, self.position, self.velocity = self.satellite.sgp4(self.jd, self.fr)
        
        return self.position,self.velocity

d = Derbis('1 24946U 97051C   21274.45158536  .00000109  00000-0  32175-4 0  9992','2 24946  86.3924 350.7298 0008414 161.7940 198.3558 14.33750944258574')
print(*d.propagar())