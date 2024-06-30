#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# 2024.06.23 Created by T.Ishigaki

LIBRARY = "numpy"

if LIBRARY == 'numpy':
  import numpy as xp
  def norm(vec):
    return xp.linalg.norm(vec)
  def zeros(shape1, shape2=0):
    return xp.zeros((shape1,shape2))
elif LIBRARY == 'sympy':
  import sympy as xp
  def norm(vec):
    return xp.sqrt(sum([elem**2 for elem in vec]))
  def zeros(shape1, shape2=0):
    return xp.zeros(shape1,shape2)
else:
  raise ValueError("Unsupported library. Choose 'numpy' or 'sympy'.")

def jac_X_wrt_scaler(lie, vec, a, dvec):
  rot = lie.mat(vec, a)
  integ_rot = lie.adj_integ_mat(vec, -a)

  return rot @ lie.hat(integ_rot @ dvec)

def jac_Xv_wrt_vector(lie, vec, a, v):
  rot = lie.mat(vec, a)
  integ_rot = lie.adj_integ_mat(vec, -a)

  return rot @ lie.hat_commute(v) @ integ_rot