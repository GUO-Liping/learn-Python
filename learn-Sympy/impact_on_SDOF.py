from sympy import symbols, exp, Integral, integrate, Derivative, diff, lambdify
from sympy import conjugate, I, oo, pi, sin, cos, sqrt, fourier_transform
import numpy as np
import matplotlib.pyplot as plt

t_total = 5
t_impact =0.5
dt = 0.002
t_I_array = np.arange( 0, t_impact, dt)
t_II_array = np.arange(0,t_total-t_impact, dt)
u0_val = 0
v0_val = 0
m_val = 250
c_val = 300
k_val = 18000
p_0_val = -10000

u0, v0, u1, v1 = symbols('u0 v0 u1 v1', real=True)
t = symbols('t', real=True)
p_0, t_1 =  symbols('p_0 t_1', real=True)
m, c, k = symbols('m c k', real=True)
# omega, omega_bar, xi, omega_D, beta, G_1, G_2 = symbols('omega omega_bar xi omega_D beta G_1 G_2', real=True)

omega = sqrt(k/m)
omega_bar = pi/t_1
xi = c/(2*m*omega)
omega_D = omega*sqrt(1-xi**2)
beta = omega_bar/omega

G_1 = (p_0/k)*(-2*xi*beta)/((1-beta**2)**2+(2*xi*beta)**2)
G_2 = (p_0/k)*(1-beta**2)/((1-beta**2)**2+(2*xi*beta)**2)


C1 = (u0-G_1)*cos(omega_D*t) + (v0+(u0-G_1)*xi*omega-G_2*omega_bar)/omega_D*sin(omega_D*t)
C2 = exp(-xi*omega*t)
C3 = G_1*cos(omega_bar*t) + G_2*sin(omega_bar*t)

ut_I = C1*C2+C3
vt_I = diff(ut_I,t)
at_I = diff(ut_I,t,t)
print('ut_I=',ut_I)
print('vt_I=',vt_I)
print('at_I=',at_I)

ut_I_subs = ut_I.subs([(u0, u0_val), (v0, v0_val), (m, m_val), (c, c_val), (k, k_val), (p_0, p_0_val), (t_1, t_impact)])
vt_I_subs = vt_I.subs([(u0, u0_val), (v0, v0_val), (m, m_val), (c, c_val), (k, k_val), (p_0, p_0_val), (t_1, t_impact)])
at_I_subs = at_I.subs([(u0, u0_val), (v0, v0_val), (m, m_val), (c, c_val), (k, k_val), (p_0, p_0_val), (t_1, t_impact)])

ut_I_numpy = lambdify(t, ut_I_subs, "numpy")
vt_I_numpy = lambdify(t, vt_I_subs, "numpy")
at_I_numpy = lambdify(t, at_I_subs, "numpy")

ut_I_array = ut_I_numpy(t_I_array)
vt_I_array = vt_I_numpy(t_I_array)
at_I_array = at_I_numpy(t_I_array)

u1_val = ut_I_subs.subs([(t,t_impact)])
v1_val = vt_I_subs.subs([(t,t_impact)])
a1_val = at_I_subs.subs([(t,t_impact)])

ut_II = (u1*cos(omega_D*t) + ((v1+u1*xi*omega)/omega_D)*sin(omega_D*t)) * exp(-xi*omega*t)
vt_II = diff(ut_II,t)
at_II = diff(ut_II,t,t)
print('ut_II=',ut_II)
print('vt_II=',vt_II)
print('at_II=',at_II)

ut_II_subs = ut_II.subs([(u1, u1_val), (v1, v1_val), (m, m_val), (c, c_val), (k, k_val)])
vt_II_subs = vt_II.subs([(u1, u1_val), (v1, v1_val), (m, m_val), (c, c_val), (k, k_val)])
at_II_subs = at_II.subs([(u1, u1_val), (v1, v1_val), (m, m_val), (c, c_val), (k, k_val)])

ut_II_numpy = lambdify(t, ut_II_subs, "numpy")
vt_II_numpy = lambdify(t, vt_II_subs, "numpy")
at_II_numpy = lambdify(t, at_II_subs, "numpy")

ut_II_array = ut_II_numpy(t_II_array)
vt_II_array = vt_II_numpy(t_II_array)
at_II_array = at_II_numpy(t_II_array)


t_array = np.arange(0, t_total, dt)
ut_array = np.concatenate((ut_I_array,ut_II_array),axis = 0)
vt_array = np.concatenate((vt_I_array,vt_II_array),axis = 0)
at_array = np.concatenate((at_I_array,at_II_array),axis = 0)
'''
plt.subplot(2,3,1)
plt.plot(t_I_array, ut_I_array)
plt.subplot(2,3,2)
plt.plot(t_I_array, vt_I_array)
plt.subplot(2,3,3)
plt.plot(t_I_array, at_I_array)

plt.subplot(2,3,4)
plt.plot(t_II_array, ut_II_array)
plt.subplot(2,3,5)
plt.plot(t_II_array, vt_II_array)
plt.subplot(2,3,6)
plt.plot(t_II_array, at_II_array)
plt.show()
'''
plt.figure(num=None, figsize=(15,4), dpi=None, facecolor=None, edgecolor=None, frameon=True)
plt.subplot(1,3,1)
plt.plot(t_array, ut_array)
plt.subplot(1,3,2)
plt.plot(t_array, vt_array)
plt.subplot(1,3,3)
plt.plot(t_array, at_array)
plt.show()