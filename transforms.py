#Python code for some of the most commonly used transforms 
#Angles are considered to be in rad. Convert to deg before use

import numpy as np
import math

#Rotation matrices 

def d_t_r(deg):
    """ Converts degree to radians """

    return deg*math.pi/180

def R_x(theta):
    """Returns the rotation matrix about x-axis"""

    rx = np.array([[1,0,0],
                   [0,np.cos(theta),-np.sin(theta)],
                   [0,np.sin(theta),np.cos(theta)]])
    return rx

def R_z(theta):
    """Returns the rotation matrix about z-axis"""

    rz = np.array([[np.cos(theta),-np.sin(theta),0],
                   [np.sin(theta),np.cos(theta),0],
                   [0,0,1]])
    return rz   

def R_y(theta):
    """Returns the rotation matrix about z-axis"""

    ry = np.array([[np.cos(theta),0,np.sin(theta)],
                   [0,1,0],
                   [-np.sin(theta),0,np.cos(theta)]])
    return ry
    
def euler_zyx(alpha,beta,gamma):
    """ Returns the rotation matrix given 3 euler angles, in zyx format """
    
    return R_z(alpha) @ R_y(beta) @ R_x(gamma)

def fixed_xyz(alpha,beta,gamma):
    """ Returns the rotation matrix given 3 fixed angles (Roll-Pitch-Yaw) """

    return R_z(alpha) @ R_y(beta) @ R_x(gamma)



#Homegenous transform matrix 

def gen_transf(rot_mat,p_org):
    """ Generates and returns the homegenous transform matrix, given a rotation matrix and origin offset """

    ht = np.zeros((4,4))
    ht[3,3] = 1
    ht[0:3,0:3] = rot_mat
    ht[0:3,3] = p_org
    return ht

def inv_transf(transf_mat):
    """ Inverts a transform matrix """

    inv_ht = np.zeros((4,4))

    inv_ht[3,3] = 1
    inv_ht[0:3,0:3] = transf_mat[0:3,0:3].T
    inv_ht[0:3,3] = -inv_ht[0:3,0:3] @ transf_mat[0:3,3]

    return inv_ht




