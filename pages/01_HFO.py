#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:27:00 2023

@author: nass
"""
import streamlit as st
from Importation_des_informations import test

#Icône et nom de l'onglet
st.set_page_config(page_title='Comparaison HFO vs GPL',page_icon='/Users/nass/Documents/Streamlit-app/Logo_TotalEnergies.png', initial_sidebar_state="expanded", layout = "wide")

st.header("Voici les différents coûts inhérent à l'exploitation du HFO")

st.write(test)