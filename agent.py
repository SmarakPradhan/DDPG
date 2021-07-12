import math
import PID
class rotate(object):
    def __init__(self,r=4,w=3.14,ux=5,uy=5,dt=0.05):
        self.r=r
        self.w=w
        self.t=(float)2*3.14/w
        self.ux=ux
        self.uy=uy
        self.x=0
        self.y=0
        self.dt=dt

    def get_reward(self,kp=1.0,ki=0.5,kd=0.5):
        t=0
        error=0
        px=PID(kp,ki,kd)
        py=PID(kp,ki,kd)
        while(t<=self.t):
            self.x+=self.ux*self.dt
            self.y+=self.uy*self.dt
            ux_t=self.r*self.w*math.cos(self.w*t)
            uy_t=self.r*self.w*math.sin(self.w*t)
            error+=(math.sqrt((self.x-ux_t)*2+(self.y-uy_t)*2))/self.dt
            self.ux=px.update(self.ux-ux_t)
            self.uy=py.update(self.uy-uy_t)
            t+=self.dt

        return 1/(1+error) 






