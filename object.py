import math
from PID import PID
class rotate(object):
    def __init__(self,r,w,ux=5,uy=5,dt=0.05):
        self.r=r
        self.w=w
        self.t=(float)2*3.14/w
        self.ux=ux
        self.uy=uy
        self.x=0
        self.y=0
        self.dt=dt

    def get_reward(self):
        t=0
        error=0
        while(t<=self.t):
            self.ux=self.x*t
            self.uy=self.y*t
            ux_t=self.r*self.w*math.cos(self.w*t)
            uy_t=self.r*self.w*math.sin(self.w*t)
            error+=(math.sqrt((self.ux-ux_t)*2+(self.uy-uy_t)*2))/self.dt
            t+=self.dt

        return 1/(1+error) 






