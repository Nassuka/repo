#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:32:03 2023

@author: nass
"""
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#from fonctions import calcul_conso_gpl, calcul_energy_hfo, price_hfo, price_gpl, euro_to_dollar, dollar_to_CFA, dollar_to_ZAR, dollar_to_din_tun, dollar_to_mur, space_in_numbers
#from gen_pdf import gen_pdf

#img = Image.open('Logo_TotalEnergies.png')
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

#Icône et nom de l'onglet
st.set_page_config(page_title='Comparaison HFO vs GPL', page_icon = 'Logo_TotalEnergies.png', initial_sidebar_state="expanded", layout = "wide")

#Titre de l'application
st.header('Application de comparaison des coûts de fonctionnement entre le HFO et le GPL')




#Sidebar
with st.sidebar : 
    st.header('Menu')
    scol1, scol2 = st.columns([1.5,3])
    

    #scol2.image("https://github.com/Nassuka/repo/blob/main/drap_fr.png",width = 30)
    scol2.write("")
    #scol2.image("/Users/nass/Documents/Streamlit-app/drap_en.webp",width = 30)
    

    
    if 'en' not in st.session_state : 
        st.session_state.en = False

    if 'fr' not in st.session_state : 
        st.session_state.fr = True
        
    if 'money' not in st.session_state : 
        st.session_state['money'] = ' $'
        
    if 'conso' not in st.session_state :
        st.session_state['conso'] = 0
        
    def change_fr_to_en() : 
        if st.session_state.fr : 
            st.session_state.en = False
            
        elif st.session_state.fr == False : 
            st.session_state.en = True 
            
        elif st.session_state.fr == False and st.session_state.en == False :
            st.session_state.fr == True

    def change_en_to_fr() : 
        if st.session_state.en : 
            st.session_state.fr = False
            
        elif st.session_state.en == False : 
            st.session_state.fr = True
            
        elif st.session_state.fr == False and st.session_state.en == False :
            st.session_state.fr == True

    
    fr  = scol1.checkbox("Français" , key = "fr", on_change = change_fr_to_en)
    scol1.write("")
    scol1.write("")
    en = scol1.checkbox("English", key = "en", on_change = change_en_to_fr)

         
    
    lang = st.selectbox( "Langues",("Français", "English"))
    
    choose = st.selectbox("Estimations", ("Page d'accueil","HFO", "GPL","Comparaison"))
    
    
    
    st.write("**Veuillez saisir les informations suivantes :** ")
    
    country = st.selectbox("**Pays**",("-- Selectionné --","Afrique du Sud", "Côte d'Ivoire", "France","Ile Maurice", "Sénégal", "Tunisie","Autres"), )
    franc_cfa = ["Côte d'Ivoire", "Sénégal"]
    euro = ["France"]
    dollar = ["Autres"]
    ZAR = ["Afrique du Sud"]
    dina_tun = ["Tunisie"]
    roupie_mauricienne =["Ile Maurice"]
    
    if country in franc_cfa :
        st.session_state.money = " F"
   
    elif country in euro :
        st.session_state.money = " €"
    
    elif country in dollar : 
        st.session_state = " $"
    
    elif country in ZAR :
        st.session_state.money = " R"
    
    elif country in dina_tun :
        st.session_state.money = " DT"
        
    elif country in roupie_mauricienne :
        st.session_state.money = " MUR"
    
    
    power = st.text_input("**Puissance utilisée (en kW) :**")
    consommation = st.number_input("**Consommation mensuelle de Fioul (en tonnes):**")
    nb_employee = st.slider("**Nombre d'employés dans l'usine :**")
    

#French language
if fr :
    if choose == "Page d'accueil":
        with st.form("my_form"):
            st.write("Veuillez entrer les informations ci-dessous :")
            fcol1, fcol2 = st.columns(2)
            st.session_state.conso = fcol1.number_input("**Consommation mensuelle de Fioul (en tonnes):**")
            country = st.selectbox("**Pays**",("-- Selectionné --","Afrique du Sud", "Côte d'Ivoire", "France","Ile Maurice", "Sénégal", "Tunisie","Autres"), )
            
            submitted = st.form_submit_button("Soumettre")
        
        st.write(st.session_state.conso)
            
            
           
        st.write(st.session_state)
        #val = st.button("Générer la facture", on_click=gen_pdf())
        #if val == True : 
            #gen_pdf()
           # with open("/Users/nass/Documents/Streamlit-app/pdf_generated.pdf","rb") as file : 
                
                #data = "/Users/nass/Documents/Streamlit-app/generated_pdf.pdf"
                #st.download_button("Télécharger la facture", data  = file, file_name='facture.pdf', mime = 'document/pdf')
    
    
    if choose == "HFO" : 
        st.write(st.session_state)
        st.write(st.session_state.conso)
        if st.session_state.conso != 0:
            en_hfo = round(calcul_energy_hfo(st.session_state.conso))
            
            
            if st.session_state.money == " €":
                cost_hfo = round(price_hfo(st.session_state.conso))
                
            else :
                #On convertit les euros en dollars
                cost_hfo = round(price_hfo(st.session_state.conso))
                cost_hfo = round(euro_to_dollar(cost_hfo))
                
                if st.session_state.money == " F":
                    cost_hfo = round(dollar_to_CFA(cost_hfo),2)
                
                elif st.session_state.money == " R":
                    cost_hfo = round(dollar_to_ZAR(cost_hfo),2)
                    
                elif st.session_state.money == " DT":
                    cost_hfo = round(dollar_to_din_tun(cost_hfo),2)
                    
                elif st.session_state.money == " MUR":
                    cost_hfo = round(dollar_to_mur(cost_hfo),2)
               
            st.write("Voici l'énergie produit par le HFO :")
        
            st.write (space_in_numbers(str(en_hfo))+"kWh")
            st.write("Voici le coût de la molécule HFO :")
            st.write(str(cost_hfo) + st.session_state.money)
            
        else :
            st.write("Veuillez renseigner votre consommation ")
        
        
    if choose == "GPL" : 
        if consommation != 0 :
            quantity_gpl = round(calcul_conso_gpl(calcul_energy_hfo(consommation)), 2)
            st.write("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.write(str(quantity_gpl)+" tonnes")
            cost_gpl = price_gpl(quantity_gpl)
            st.write("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.write(str(cost_gpl) + st.session_state.money)
        else :
            st.write("Veuillez renseigner votre consommation ")
            
    if choose == "Comparaison" : 
        st.write("Ici sera afficher des grahiques comme l'amortissement sur 10 ans entre le HFO et le GPL, compoaraison de la quatité de CO2 économiser")
    







        
#English language
if en :       
    #val = st.button("Generate the invoive", on_click = gen_pdf())
    #if val == True : 
      #  with open("/Users/nass/Documents/Streamlit-app/pdf_generated.pdf","rb") as file : 
            
            #data = "/Users/nass/Documents/Streamlit-app/generated_pdf.pdf"
           # st.download_button("Download the invoice", data  = file, file_name='facture.pdf', mime = 'document/pdf')
    
    
    if choose == "HFO" : 
        if consommation != 0:
            en_hfo = round(consommation *11774,2)
            cost_hfo = price_hfo(consommation)
            st.write("This is the energy produce by the HFO :")
            st.write (str(en_hfo)+"kWh")
            st.write("The cost of molecule HFO :")
            st.write(str(cost_hfo) + "€")
        else :
            st.write("Veuillez renseigner votre consommation ")
        
        
    if choose == "GPL" : 
        if consommation != 0 :
            quantity_gpl = round(calcul_conso_gpl(calcul_energy_hfo(consommation)), 2)
            st.write("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.write(str(quantity_gpl)+" tonnes")
            cost_gpl = price_gpl(quantity_gpl)
            st.write("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.write(str(cost_gpl) + "€")
        else :
            st.write("Veuillez renseigner votre consommation ")
            
    if choose == "Comparaison" : 
        st.write("Ici sera afficher des grahiques comme l'amortissement sur 10 ans entre le HFO et le GPL, compoaraison de la quatité de CO2 économiser")
  
        
