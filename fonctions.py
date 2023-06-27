#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:00:25 2023

@author: nass
"""


def calcul_energy_hfo(conso):
    return conso*11774

def calcul_conso_gpl(energy):
    return energy/13800

def price_hfo(conso):
    return conso*408.9

def price_gpl(conso) : 
    return conso*602

def euro_to_dollar(eur):
    return eur * 1.09

def dollar_to_CFA(dollar):
    return dollar * 600.72

def dollar_to_ZAR(dollar): 
    return dollar * 18.34

def dollar_to_mur(dollar):
    return dollar * 45.5

def dollar_to_din_tun(dollar):
    return dollar * 3.09

def space_in_numbers(x):
    n= ""
    
    for i in range(1,len(x) + 1):
        if i%3 == 0 and i != len(x):
            n = " " + x[-i] + n
        else :
            n = x[-i] + n
    
    return n