#everything about rotation matrices
from .external.math import *

def ROT1(a): #All rots from Vallado, p.162, (3-15). Matrices from russian Wikipedia is for other coordinate system
    return matrix([[1,0,0],[0,cos(a),sin(a)],[0,-sin(a),cos(a)]])

def ROT2(a):
    return matrix([[cos(a),0,-sin(a)],[0,1,0],[sin(a),0,cos(a)]])

def ROT3(a):
    return matrix([[cos(a),sin(a),0],[-sin(a),cos(a),0],[0,0,1]])

def angle(vector_a,vector_b):
    return degrees(acos(dot(vector_a,vector_b)/(magnitude(vector_a)*magnitude(vector_b))))

def signedAngle(vector_a,vector_b,vector_axis):
    return degrees(atan2(dot(cross(vector_a,vector_b),vector_axis),dot(vector_a,vector_b)))
