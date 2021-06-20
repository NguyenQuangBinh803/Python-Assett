from scipy.integrate import odeint

import numpy as np

import matplotlib.pyplot as plt


def model(v,t,u,load):
    '''
    v: velocity
    t: time
    u: control signal
    load: mass
    '''
    
    Cd = 0.24
    rho = 1.225
    A = 5.0
    Fp = 30
    m = 500
    dv_dt = (1/(m+load))*(Fp*u - 0.5*rho*A*Cd*v*v)
    return dv_dt
final_time = 60 # sec
nsteps = 61
delta_t = final_time/(nsteps-1)
ts = np.linspace(0, final_time, nsteps)
control_signal = np.zeros(nsteps)
control_signal[11:] = 50.0

load  = 200
v0 = 0
vs = np.zeros(nsteps)

for i in range(nsteps-1):
    current_control_signal = control_signal[i]

    if current_control_signal > 100:
        current_control_signal = 100
    elif current_control_signal < -50:
        current_control_signal = -50
    v = odeint(model, v0, [0, delta_t], args=(current_control_signal, load))
    v0 = v[-1]
    vs[i+1] = v0

plt.figure()
plt.subplot(2,1,1)
plt.plot(ts, vs, 'b-', linewidth=2)
plt.plot([0,final_time], [25,25], 'k--', linewidth=2)
plt.ylabel('Velocity')
plt.legend(['123'], ['123'], loc=2)
plt.subplot(2,1,2)
plt.plot(ts, control_signal, 'b-', linewidth=2)
plt.ylabel('Signal')
plt.legend(['123'], ['123'], loc=2)

plt.show()

    
