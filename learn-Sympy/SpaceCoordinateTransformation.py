from sympy import symbols, Matrix,sin,cos

def func_matrix_T_v(para_xv,para_yv,para_zv):
	return Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-para_xv,-para_yv,-para_zv,1]])

def func_matrix_T_rx(para_phi):
	return Matrix([[1,0,0,0],[0,cos(para_phi),-sin(para_phi),0],[0,sin(para_phi),cos(para_phi),0],[0,0,0,1]])

def func_matrix_T_ry(para_phi):
	return Matrix([[cos(para_phi),0,sin(para_phi),0],[0,1,0,0],[-sin(para_phi),0,cos(para_phi),0],[0,0,0,1]])

def func_matrix_T_rz(para_phi):
	return Matrix([[cos(para_phi),-sin(para_phi),0,0],[sin(para_phi),cos(para_phi),0,0],[0,0,1,0],[0,0,0,1]])

# 以下函数为坐标点变换矩阵，旋转矩阵为单位正交阵（矩阵转置为矩阵的逆），平移矩阵不然
def func_coor_transform_matrix():
	theta = symbols('theta')
	alpha, beta, gamma = symbols('alpha, beta, gamma')
	R,r = symbols('R, r')
	vx,vy,vz = symbols('vx,vy,vz')

	Trx = Matrix([[1,0,0,0],[0,cos(theta),-sin(theta),0],[0,sin(theta),cos(theta),0],[0,0,0,1]])
	Try = Matrix([[cos(theta),0,sin(theta),0],[0,1,0,0],[-sin(theta),0,cos(theta),0],[0,0,0,1]])
	Trz = Matrix([[cos(theta),-sin(theta),0,0],[sin(theta),cos(theta),0,0],[0,0,1,0],[0,0,0,1]])
	Ttv = Matrix([[1,0,0,vx],[0,1,0,vy],[0,0,1,vz],[0,0,0,1]])
	Mxyz = Matrix([0,0,R+r,1])
	(Ttv.subs([(vx,0),(vy,0),(vz,-R)]))*Mxyz

R_1, r_j = symbols('R_1, r_j')
phi, alpha, beta, gamma, theta = symbols('phi, alpha, beta, gamma, theta')
x_v,y_v,z_v = symbols('x_v,y_v,z_v')
T_v,T_rx,T_ry,T_rz = symbols('T_v,T_rx,T_ry,T_rz')

S = Matrix([0,R_1,0,1])
T_4 = func_matrix_T_rx(gamma)
T_3 = func_matrix_T_v(0,-R_1,0).T
T_2 = func_matrix_T_rz(theta)
T_1 = func_matrix_T_v(0,R_1,0).T

T = T_4 * T_3 * T_2 * T_1
xyz1 = T * Matrix([r_j, R_1, 0, 1])
print(xyz1)
