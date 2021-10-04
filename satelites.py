from matplotlib.pyplot import step
from numpy.linalg import norm
from sgp4.api import Satrec
from sgp4.api import jday
from datetime import datetime
from scipy.integrate import ode
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

# gravitational constant
G_meters = 6.67430e-11       # m**3 / kg / s**2
G        = G_meters * 10**-9 # km**3/ kg / s**2
#CONSTS
EARTH_EQUATORIAL_RADIUS = 6378.135  # equatorial radius
EARTH_FLATTENING_CONSTANT = 1 / 298.26
GEO_SYNC_RADIUS = 42164.57
EARTH_MU=5.972e24 * G

plt.style.use('dark_background')
fig = plt.figure()
fig.set_facecolor('black')
ax = p3.Axes3D(fig)
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False

anim = []
trayectory = []

def animate(i):
    d.propagar()
    pos = d.get_trayectory()
    pos = pos[-1:]
    
    last_pos = pos[-1]
    trayectory.append(last_pos.tolist())
    trayectory_f = np.asarray(trayectory)
    
    ax.clear()
    ax.plot([0], [0], [0], 'bo', markersize=9, label="Earth")
    ax.plot(pos[::, 0], pos[::, 1], pos[::, 2], 'ro')
    ax.plot(trayectory_f[::, 0], trayectory_f[::, 1], trayectory_f[::, 2], 'w--')    

class Derbis(object):
    def __init__(self,s,t):
        self.t=t
        self.s=s
        self.satellite = Satrec.twoline2rv(s, t)
        self.propagar
        self.get_trayectory
    
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
    def two_body(self,t,y,mu=EARTH_MU):
        rx,ry,rz,vx,vy,vz=y
        r=np.array([rx,ry,rz])
        #calc norm of r
        norm_r=np.linalg.norm(r)

        #two body aceleration
        ax,ay,az= r*mu/norm_r**3
        return [vx,vy,vz,ax,ay,az]
    
    def get_trayectory(self,tspan=100.0*60.0,dt=100.0,mu=EARTH_MU):
        #r0,v0=d.propagar()
        r0=[*self.position]
        v0=[*self.velocity]
        
        #number of steps
        n_steps=int(np.ceil(tspan/dt))
        ys=np.zeros((n_steps,6))
        ts=np.zeros((n_steps,1))

        #initial conditions
        y0=r0+v0
        ys[0]=np.array(y0)
        step=1

        #solver
        solver=ode(d.two_body)
        solver.set_integrator('lsoda')
        solver.set_initial_value(y0,0)
        solver.set_f_params(mu)

        while step<n_steps:
            solver.integrate(solver.t+dt)
            #print(solver.t,solver.y)
            ts[step]=solver.t
            ys[step]=solver.y
            step+=1

        self.rs=ys[:,:3]

        return self.rs

d = Derbis('1 24946U 97051C   21274.45158536  .00000109  00000-0  32175-4 0  9992','2 24946  86.3924 350.7298 0008414 161.7940 198.3558 14.33750944258574')
print(*d.propagar())

anim = animation.FuncAnimation(fig, animate, interval=1000) 

plt.show()

