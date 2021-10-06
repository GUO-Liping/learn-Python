from sympy import symbols,exp,Integral,integrate,Derivative,diff
from sympy import conjugate,I,oo,pi,sqrt,fourier_transform

x, y = symbols('x y', real=True)
a, f = symbols('a f', positive=True)
t = symbols('t')

# 高斯函数前三阶导数
g0t = exp(-t**2)
g1t = Derivative(g0t, (t, 1), evaluate=True)
g2t = Derivative(g0t, (t, 2), evaluate=True)
g3t = Derivative(g0t, (t, 3), evaluate=True)

# 高斯函数前三阶导数的复共轭
g0t_con = conjugate(g0t)
g1t_con = conjugate(g1t)
g2t_con = conjugate(g2t)
g3t_con = conjugate(g3t)

# 高斯函数前三阶导数的能量归一化因子
C0 = sqrt(1/integrate(g0t*g0t_con,(t,-oo,+oo)))
C1 = sqrt(1/integrate(g1t*g1t_con,(t,-oo,+oo)))
C2 = sqrt(1/integrate(g2t*g2t_con,(t,-oo,+oo)))
C3 = sqrt(1/integrate(g3t*g3t_con,(t,-oo,+oo)))

# 能量归一化后的高斯小波
gauss0 = C0*g0t
gauss1 = (-1)**2*C1*g1t
gauss2 = (-1)**3*C2*g2t
gauss3 = (-1)**4*C3*g3t

# 能量归一化后的高斯小波的傅里叶变换
ftg0 = fourier_transform(gauss0, t, f)
ftg1 = fourier_transform(gauss1, t, f)
ftg2 = fourier_transform(gauss2, t, f)
ftg3 = fourier_transform(gauss3, t, f)

# 能量归一化后的高斯小波的中心频率
fc0 = integrate(f*ftg0*conjugate(ftg0),(f,0,+oo))/integrate(ftg0*conjugate(ftg0),(f,0,+oo))
fc1 = integrate(f*ftg1*conjugate(ftg1),(f,0,+oo))/integrate(ftg1*conjugate(ftg1),(f,0,+oo))
fc2 = integrate(f*ftg2*conjugate(ftg2),(f,0,+oo))/integrate(ftg2*conjugate(ftg2),(f,0,+oo))
fc3 = integrate(f*ftg3*conjugate(ftg3),(f,0,+oo))/integrate(ftg3*conjugate(ftg3),(f,0,+oo))
