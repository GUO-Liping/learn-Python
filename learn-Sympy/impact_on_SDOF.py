from sympy import symbols, exp, Integral, integrate, Derivative, diff, lambdify
from sympy import conjugate, I, oo, pi, sin, cos, sqrt, fourier_transform
import numpy as np

u0, v0 = symbols('u0 v0', real=True)
t = symbols('t', real=True)
t_val = np.arange(0.001,0.5,0.002)

p_0, t_1 =  symbols('p_0 t_1', real=True)
m, c, k = symbols('m c k', real=True)

omega = sqrt(k/m)
omega_bar = pi/t_1
ksi = c/(2*m*omega)
omega_D = omega*sqrt(1-ksi**2)
beta = omega_bar/omega

G_1 = (p_0/k)*(-2*ksi*beta)/((1-beta**2)**2+(2*ksi*beta)**2)
G_2 = (p_0/k)*(1-beta**2)/((1-beta**2)**2+(2*ksi*beta)**2)

C1 = (u0-G_1)*cos(omega_D*t) + (v0+(u0-G_1)*ksi*omega-G_2*omega_bar)/omega_D*sin(omega_D*t)
C2 = exp(-ksi*omega*t)
C3 = G_1*cos(omega_bar*t) + G_2*sin(omega_bar*t)

ut = C1*C2+C3
vt = diff(ut,t)
at = diff(ut,t,t)

#ut_val = ut.subs([(u0, 0), (v0, 0), (m, 100), (c, 0.5), (k, 100), (p_0, 10), (t_1, 0.1), (t,0)])
#vt_val = vt.subs([(u0, 0), (v0, 0), (m, 100), (c, 0.5), (k, 100), (p_0, 10), (t_1, 0.1), (t,0)])
#at_val = at.subs([(u0, 0), (v0, 0), (m, 100), (c, 0.5), (k, 100), (p_0, 10), (t_1, 0.1), (t,0)])

ut_numpy = lambdify(t, ut, "numpy")
vt_numpy = lambdify(t, vt, "numpy")
at_numpy = lambdify(t, at, "numpy")

ut_numpy(t_val)
vt_numpy(t_val)
at_numpy(t_val)
