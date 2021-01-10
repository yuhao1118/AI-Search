# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:07:58 2021

@author: Yuhao
"""

from multiprocessing import Pool
import os
import time

name_tag = "AISearchfile%s.txt"
cities = ["042","048","058","175","180", "535"]

def run(i, algo_name, file_name):
    time.sleep(i*1.2)
    os.system("python "+algo_name+" "+file_name)
    

if __name__ == "__main__":
    algo_name = "AlgAenhanced.py"
    for i in cities:
        file_name = name_tag % i
        pool = Pool(processes=5)
        for j in range(5):
            pool.apply_async(run, (j, algo_name, file_name,))
            
        pool.close()
        pool.join()