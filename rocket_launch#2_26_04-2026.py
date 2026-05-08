import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation as FA
from scipy.integrate import odeint
m_d=45#kg
m_f1=125#kg
C1=0.5
C2=0.63
ro_0=1.225#kg/m^3
mu=-8#kg/s
Isp=250#s
g=9.81#m/s^2
C_par=1.9
r=0.1#m
H=10000#m
t=np.linspace(0,400,3000)
def dSdt(t,S):
    y,v_y,m=S
    r1=r
    C=C1
    ro=ro_0*pow(np.e,-(y/H))
    dmdt=mu
    if(t>(-m_f1/mu)):
        dmdt=0
    if(v_y<0):
        C=C2
    if(v_y<0 and y<=2000 ):
       C=C_par
       r1=1
    a_y=-g-0.5*ro*np.pi*r1**2*C*np.sqrt(v_y**2)*v_y/m-dmdt*Isp*g/m
    return v_y,a_y,dmdt
y_0=0
m_0=m_d+m_f1
v_y_0=0
S_0=(y_0,v_y_0,m_0)
sol=odeint(dSdt,y0=S_0,t=t,tfirst=True)
y_sol=sol.T[0]
v_y_sol=sol.T[1]
v=np.sqrt(v_y_sol**2)
m_sol=sol.T[2]
fig,ax=plt.subplots()
ax.set_ylim(0,105000)
ax.set_xlim(0,400)
ax.set_ylabel('altitude [m]')
ax.set_xlabel('time [s]')
ax.set_title('y(t)')
line_y,=ax.plot([],[],color='blue',label='y(t)')
y_vals=[]
m_vals=[]
t_vals=[]
v_vals=[]
plt.grid()
plt.legend()
plt.axvline(-m_f1/mu,color='red',linestyle='--')
plt.axhline(2000,color='orange',linestyle='--')
fig2,ax2=plt.subplots()
ax2.set_ylim(0,2000)
ax2.set_xlim(0,400)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('velocity [m/s]')
ax2.set_title('v(t)')
plt.axvline(-m_f1/mu,color='red',linestyle='--')
plt.grid()
fig3,ax3=plt.subplots()
ax3.set_ylim(0,175)
ax3.set_xlim(0,400)
ax3.set_ylabel('mass [kg]')
ax3.set_xlabel('time [s]')
ax3.set_title('m(t)')
plt.grid()
plt.axhline(45,color='blue',linestyle='--')
line_v,=ax2.plot([],[],color='orange',label='v(t)')
line_m,=ax3.plot([],[],color='red',label='m(t)')
plt.axvline(-m_f1/mu,color='orange',linestyle='--')
def update(frame):
    t_vals.append(t[frame])
    y_vals.append(y_sol[frame])
    v_vals.append(v[frame])
    m_vals.append(m_sol[frame])
    line_y.set_data(t_vals,y_vals)
    line_v.set_data(t_vals,v_vals)
    line_m.set_data(t_vals,m_vals)
    return line_y,line_v,line_m
ani=FA(fig,update,frames=len(t),interval=5,blit=True,repeat=False)
y_max=round((max(y_sol)),3)
v_max=round(max(v),3)
print('max altitude:')
print(y_max)
print('max velocity:')
print(v_max)
ax.legend()
ax2.legend()
ax3.legend()
plt.show()
