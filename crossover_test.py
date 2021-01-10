# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:43:53 2021

@author: Yuhao
"""

X1 = [3, 4, 8, 2, 7, 1, 6, 5]
Y1 = [4, 2, 5, 1, 6, 8, 3, 7]

X3 = [1, 2, 3, 4, 5, 6, 7, 8]
Y3 = [2, 7, 5, 8, 4, 1, 6, 3]

X4 = [1, 2, 3, 4, 5, 6, 7, 8]
Y4 = [6, 8, 4, 3, 1, 2, 5, 7]

num_cities = 12

import random

def CX(P1, P2):
    O1 = P2[:]
    O2 = P1[:]
    
    O1[0] = P1[0]
    O2[0] = P2[0]
    
    val_1 = P2[0]
    val_2 = P1[0]
    
    while True:
        loc_1 = P1.index(val_1)
        loc_2 = P2.index(val_2)
        
        O1[loc_1] = val_1
        O2[loc_2] = val_2
        
        val_1 = P2[loc_1]
        val_2 = P1[loc_2]
        
        if val_1 == O1[0] or val_2 == O2[0]:
            break
    
    return O1, O2

def ICX(P1, P2):
    P1 = P1[:]
    P2 = P2[:]
    O1 = [P2[0]]
    O2 = [P1[0]]
    def gen(P1, P2, num):
        return P2[P1.index(num)]
    while len(O1) < num_cities and len(O2) < num_cities:
        next_city_1 = gen(P1, P2, O1[-1])
        next_city_2 = gen(P2, P1, O2[-1])
        if next_city_1 == P2[0] or next_city_2 == P1[0]:
            break
        O1.append(next_city_1)
        O2.append(next_city_2)  
        
    
    if len(O2) < len(P1):
        for i in O1:
            P1.remove(i)
            P2.remove(i)
            
        _O1, _O2 = ICX(P1, P2)
        O1 += _O1
        O2 += _O2    
        
    return O1, O2

def OX(X, Y):
    num_cities = len(X)
    
    loc_1 = random.randint(1, num_cities - 1) # 1 ~ num_cities - 2
    loc_2 = random.randint(loc_1 + 1, num_cities) # 2 ~ num_cities - 1
    
    reserve_O1 = X[loc_1:loc_2]
    reserve_O2 = Y[loc_1:loc_2]
    
    tmp_X = X[loc_2:] + X[:loc_2]
    tmp_Y = Y[loc_2:] + Y[:loc_2]
    
    for i in range(0, loc_2 - loc_1):
        tmp_X.remove(reserve_O2[i])
        tmp_Y.remove(reserve_O1[i])
    
    rest_len = num_cities - loc_2
    
    O1 = tmp_Y[rest_len:] + reserve_O1 + tmp_Y[:rest_len]
    O2 = tmp_X[rest_len:] + reserve_O2 + tmp_X[:rest_len]
        
    return O1, O2

def PMX(X, Y):
    chr_len = len(X)
    insert = random.randrange(chr_len)
    mid = chr_len // 2
    C1 = X[:]
    C2 = Y[:]
    insert_range = range(insert) if insert <= mid else range(insert, chr_len)
    for i in insert_range:
        dup_index = C1.index(Y[i])
        C1[i], C1[dup_index] = C1[dup_index], C1[i]
    
        dup_index = C2.index(X[i])
        C2[i], C2[dup_index] = C2[dup_index], C2[i]
    
    return C1, C2



# 性能比较：越大越好
# PMX > CX > OX > ICX

# 速度比较：
# OX ~= CX > ICX > PMX