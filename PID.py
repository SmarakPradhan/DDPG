class PID(object):
    # initialize stored data
    def __init__(self,kp=1.0,Ki=0.05, Kd=0.05):

        self.error=0,self.kp=kp,self.ki=ki,self.kd=kd
        self.e_prev=0
        self.e_cum=0 

    def update(self,error,u):
        self.error=error
        error_kp=self.error
        error_kd=self.error-self.e_prev
        error_ki=self.error+self.e_cum

        total_error=self.kp*error_kp+self.ki*error_ki+self.kd*error_kd
        print("total error: ",total_error)
        u=u-total_error

        self.e_prev=error
        self.e_cum=error_ki

        return u
    