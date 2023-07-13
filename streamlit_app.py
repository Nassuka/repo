
import streamlit as st
import numpy as np
import pandas as pd

#from fonctions import calcul_conso_gpl,rendement, calcul_energy_hfo, price_hfo, price_gpl, euro_to_dollar, dollar_to_CFA, dollar_to_ZAR, dollar_to_din_tun, dollar_to_mur, space_in_numbers, courbe
#from gen_pdf import gen_pdf
#from bokeh.plotting import figure
import jinja2
import pdfkit
from datetime import datetime

#Icône et nom de l'onglet
st.set_page_config(page_title='Comparaison HFO vs GPL',page_icon='/Users/nass/Documents/Streamlit-app/Logo_TotalEnergies.png', initial_sidebar_state="expanded", layout = "wide")

#Titre de l'application
st.header('Application de comparaison des coûts de fonctionnement entre le HFO et le GPL')


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


def courbe(base,n,p):
    l=np.zeros((p,n))
    for j in range (p):
        for i in range(n):
            #c = np.random.randint(0,2)
            #if c == 0 : 
                #l[j][i] = base - base*np.random.rand()
                #base = l[j][i]
               # print(i,j)
           
           # else : 
                l[j][i] = base + 0.01*base*np.random.rand()
                base = l[j][i]
                #print(i,j)
        
    return l

def rendement(a):
    l=[]
    for i in range(a+1):
        if i < 8:
            l+= [1 - i*0.018]
        else :
            l += [0.8 + 0.2*(1/(1+ i**0.5))]
        
    return l

#chart_data = pd.DataFrame(courbe(1000,2,20), columns=["a","b"])




def gen_pdf():
    my_name = "Franck AndradeEDFDZHEVC"
    item1 = "TV"
    item2="Couch"
    item3 = "Washing Machine"
    today_date = datetime.today().strftime("%d %b, %Y")
    
    context = {'my_name' : my_name, 'item1': item1, 'item2': item2, 'item3': item3, 'today_date' : today_date}
    
    template_loader = jinja2.FileSystemLoader('/Users/nass/Documents/Streamlit-app/')
    template_env = jinja2.Environment(loader = template_loader)
    
    
    template = template_env.get_template("basic_template.html")
    output_text = template.render(context)
    
    config = pdfkit.configuration(wkhtmltopdf = "/usr/local/bin/wkhtmltopdf")
    pdf = pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration = config)


#Sidebar
with st.sidebar : 
    st.header('Menu')
    scol1, scol2 = st.columns([1.8,3])
    

    scol2 .image("/Users/nass/Documents/Streamlit-app/drap_fr.png",width = 30)
    scol2.write("")
    scol2 .image("/Users/nass/Documents/Streamlit-app/drap_en.webp",width = 30)
    

    
    if 'en' not in st.session_state : 
        st.session_state['en'] = False

    if 'fr' not in st.session_state : 
        st.session_state['fr'] = True
        
    if 'ram' not in st.session_state : 
         st.session_state['ram'] = False
          
    if 'filter' not in st.session_state : 
         st.session_state.filter = False
         
    if 'nb_ram' not in st.session_state :
        st.session_state['nb_ram'] = 0
    
    if 'ram_cost' not in st.session_state :
        st.session_state['ram_cost'] = 0
    
    if 'nb_fil' not in st.session_state :
        st.session_state['nb_fil'] = 0
        
    if 'money' not in st.session_state : 
        st.session_state['money'] = ' $'
        
    if 'conso' not in st.session_state :
        st.session_state['conso'] = 0
    
    if 'price_hfo' not in st.session_state :
        st.session_state['price_hfo'] = 0
        
    if 'nb_employee' not in st.session_state :
        st.session_state['nb_employee'] = 0
        
    if 'salary' not in st.session_state :
        st.session_state['salary'] = 0
        
    if 'pci_hfo' not in st.session_state :
        st.session_state['pci_hfo'] = 0
        
    if 'pui' not in st.session_state :
        st.session_state['pui'] = 0
        
    if 'nb_h_per_day' not in st.session_state :
        st.session_state['nb_h_per_day'] = 0
        
    if 'nb_day_per_week' not in st.session_state :
        st.session_state['nb_day_per_week'] = 0
        
    if 'price_kWh' not in st.session_state :
        st.session_state['price_kWh'] = 0
        
    if 'country' not in st.session_state :
        st.session_state['country'] = 'Autres'
        
    if 'meth' not in st.session_state :
        st.session_state['meth'] = 'Personnel interne'
        
    if 'choose' not in st.session_state :
        st.session_state['choose'] = "Page d'accueil"
        
    if 'presta' not in st.session_state :
        st.session_state['presta'] = 0
    
    if 'presta_unknow' not in st.session_state :
        st.session_state['presta_unknow'] = False
        
    if 'other_unknow' not in st.session_state :
        st.session_state['other_unknow'] = False
        
    if 'meth_other' not in st.session_state :
        st.session_state['meth_other'] = ''
    
    if 'price_other_meth' not in st.session_state :
        st.session_state['price_other_meth'] = 0
        
    if 'pieces' not in st.session_state :
        st.session_state['pieces'] = False
    
    if 'change_pcs' not in st.session_state :
        st.session_state['change_pcs'] = ''
    
    if 'but_pcs' not in st.session_state :
        st.session_state['but_pcs'] = ''
        
    if 'c' not in st.session_state :
        st.session_state['c'] = []
        
    if 'cl' not in st.session_state :
        st.session_state['cl'] = []
    
    if 'sum_pcs' not in st.session_state :
        st.session_state['sum_pcs'] = 0
    
    if 'eau' not in st.session_state :
        st.session_state['eau'] = 0
        
    if 'eau_l' not in st.session_state :
        st.session_state['eau_l'] = 0
    
    if 'eau_nb' not in st.session_state :
        st.session_state['eau_nb'] = 0
        
    if 'nett' not in st.session_state :
        st.session_state['nett'] = False
        
    if 'nett_meth' not in st.session_state :
        st.session_state['nett_meth'] = 'Opérateurs interne'
        
    if 'same_empl' not in st.session_state :
        st.session_state['same_empl'] = False
        
    if 'n' not in st.session_state :
        st.session_state['n'] = []
    
    if 'ne' not in st.session_state :
        st.session_state['ne'] = []
        
    if 'but_nett' not in st.session_state :
        st.session_state['but_nett'] = ''
    
    if 'nett_eq' not in st.session_state :
        st.session_state['nett_eq'] = ''
        
    if 'sum_nett' not in st.session_state :
        st.session_state['sum_nett'] = 0
        
    if 'nb_empl2' not in st.session_state :
        st.session_state['nb_empl2'] = 0
    
    if 'nett_presta' not in st.session_state :
        st.session_state['nett_presta'] = 0
    
    if 'nett_cost' not in st.session_state :
        st.session_state['nett_cost'] = 0
    
    if 'additif' not in st.session_state :
        st.session_state['additif'] = False
        
    if 'cost_add' not in st.session_state :
        st.session_state['cost_add'] = 0
        
    if 'name_add' not in st.session_state :
        st.session_state['name_add'] = ''
        
    if 'cons_add' not in st.session_state :
        st.session_state['cons_add'] = 0
    
    if 'add' not in st.session_state :
        st.session_state['add'] = []
        
    if 'but_add' not in st.session_state :
        st.session_state['but_add'] = ''
        
    if 'sum_add' not in st.session_state :
        st.session_state['sum_add'] = 0
        
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
    
    st.session_state.choose = st.selectbox("Estimations", ("Page d'accueil","HFO", "GPL","Comparaison", "Proposition d'optimisation"))
    
    st.divider()
    
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
    if st.session_state.choose == "Page d'accueil":
        #st.write(st.session_state.c)
        with st.form("my_form"):
            st.write("Veuillez entrer les informations ci-dessous :")
            fcol1, fcol2 = st.columns(2)
            st.session_state.conso = fcol1.number_input("**Consommation annuelle de Fioul (en tonnes) :**")
            st.session_state.price_hfo = fcol2.number_input("**Prix de la tonne de Fioul Lourd (monnaie locale) :**")
            country = st.selectbox("**Pays**",("-- Selectionné --","Afrique du Sud", "Côte d'Ivoire", "France","Ile Maurice", "Sénégal", "Tunisie","Autres"), )
           
            col1, col2 = st.columns(2)
            
            st.session_state.pui = col1.number_input("**Puissance de l'installation (en KW) :**")
            st.session_state.price_kWh = col2.number_input("**Coût d'un Kwh :**")
            st.session_state.nb_h_per_day = col1.number_input("**Nombre d'heures de fonctionnement de l'installation par jour :**", min_value=0, max_value=24)
            st.session_state.nb_day_per_week = col2.number_input("**Nombre de jours de fonctionnement de l'installation par semaine :**", min_value=0, max_value=7, step= 1)
            #st.session_state.salary = col2.number_input("**Salaire des employés (monnaie locale) :**")
            
            #st.session_state.nb_fil = st.number_input("**Nombre de filtres :**", step = 1)
           
            #st.session_state.nb_ram = st.number_input("**Nombre de ramonages par an :**", step = 1)
            
            st.session_state.pci_hfo = st.number_input("PCI du Fioul lourd :")
            st.session_state.eau = st.number_input("Combien de m3 d'eau traités pour la maintenance de la chaudière :", step = 1)
            col11, col22 = st.columns(2)
            st.session_state.eau_l = col11.number_input("Coût d'un m3 d'eau traité :")
            st.session_state.eau_nb = col22.number_input("Combien de fois par an l'achat de cet eau est effectuée :")
            
            st.session_state.country = country
            
            if country in franc_cfa :
                st.session_state.salary = 75000
           
            elif country in euro :
                st.session_state.salary = 1539.42
            
            elif country in dollar : 
                st.session_state.salary = 1400
            
            elif country in ZAR :
                st.session_state.salary = 4058.2
            
            elif country in dina_tun :
                st.session_state.salary = 323
                
            elif country in roupie_mauricienne :
                st.session_state.salary = 22404
           
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
                st.session_state.money = " $"
            
            elif country in ZAR :
                st.session_state.money = " R"
            
            elif country in dina_tun :
                st.session_state.money = " DT"
                
            elif country in roupie_mauricienne :
                st.session_state.money = " MUR"
                
            submitted = st.form_submit_button("Soumettre")
        
        #st.write(st.session_state.conso)
        
        st.session_state.meth = st.radio("Par quel méthode effectuez-vous votre maintenance ?", ('Personnel interne', 'Prestataire', 'Autres'))
        if st.session_state.meth == 'Personnel interne' : 
            st.session_state.nb_employee = st.number_input("**Nombre d'employés à cet usage :** ", step = 1)
            st.write("")
            st.write("")
            st.write("")
       
        elif st.session_state.meth == 'Prestataire' :
            st.session_state.presta = st.number_input("**Coût prestataire annuel :** ", step = 1)
            if st.session_state.presta == 0 :
                st.session_state.presta_unknow = st.checkbox("**Je ne connais pas les coûts de mes prestataires**")
                st.write("")
                st.write("")
                st.write("")
                
        elif st.session_state.meth == 'Autres' : 
            st.session_state.meth_other = st.text_input("Veuillez entrer votre méthode de maintenance : ")
            st.session_state.price_other_meth = st.number_input("**Coût annuel de cette méthode :**")
            if st.session_state.price_other_meth ==0 :
                st.session_state.other_unknow = st.checkbox("**Je ne connais pas les coûts de ma méthode**")
                st.write("")
                st.write("")
                st.write("")
        
        
        st.session_state.ram = st.checkbox("Faites-vous des ramonages ?")
        if st.session_state.ram : 
            st.session_state.nb_ram = st.number_input("**Nombre de ramonages par an :**")
            st.session_state.ram_cost= st.number_input("**Coût d'un ramonage :**")
            st.write("")
            st.write("")
            st.write("")
            
        st.session_state.filter = st.checkbox("Avez-vous des filtres ?")
        if st.session_state.filter : 
             st.session_state.nb_fil = st.number_input("**Nombre de filtres :**", step = 1)  
             if st.session_state.nb_fil != 0 :
                 
                 df = pd.DataFrame(data = np.zeros((1,st.session_state.nb_fil)), columns = ('Filtre %d' % i for i in range(1,1 + st.session_state.nb_fil)), index = ["Taille (μm)"])
                 udf = st.data_editor(df)
                 st.write("")
                 st.write("")
                 st.write("")
                 
        st.session_state.pieces = st.checkbox("Avez-vous changé des pièces durant les 10 dernières années ?")
        if st.session_state.pieces :
            st.session_state.change_pcs = st.text_input("Nom de l'équipement changé :")
            #st.write(st.session_state.change_pcs)
            st.session_state.but_pcs = st.button("Ajouter dans le tableau")
            if st.session_state.but_pcs :
                st.session_state.c += [np.transpose(np.array([st.session_state.change_pcs,0,0,0,0,'Non'])).tolist()]
                #st.session_state.c += [st.session_state.change_pcs,0,0]
                
                #st.write(st.session_state.c[0])
                #k = st.session_state.c[0].values()
                #st.write(k)
                #st.session_state.cl = list(st.session_state.c[0].values())
                #st.write(st.session_state.cl)
                
            if len(st.session_state.c) != 0 : 
                df1 = pd.DataFrame(data = st.session_state.c, index = ('Pièces %d' % i for i in range(1,1 + len(st.session_state.c))), columns = ["Nom de la pièce", "Prix de la pièce", "Combien de changement durant les 10 dernières années ?", "Durée de l'intervention (en heures)", "Intervallle de temps entre les interventions (en mois)", "Cela empiète-t-il sur la production ?(Oui ou Non)"])
                udf1 = st.data_editor(df1)
                npdf1 = udf1.to_numpy()
                for i in range(len(st.session_state.c)):
                    st.session_state.c[i][1] = npdf1[i,1]
                    st.session_state.c[i][2] = npdf1[i,2]
                    st.session_state.c[i][3] = npdf1[i,3]
                    st.session_state.c[i][4] = npdf1[i,4]
                    st.session_state.c[i][5] = npdf1[i,5]
                    #st.write(st.session_state.c)
                    #st.write(st.session_state.c[i][1])
                    #st.write(st.session_state.c[i][2])
                if float(st.session_state.c[-1][2]) != 0 and float(st.session_state.c[-1][1]) != 0:
                    st.session_state.sum_pcs += ((float(st.session_state.c[-1][2]) * float(st.session_state.c[-1][1]))/10)
            st.write("")
            st.write("")
            st.write("")
        
      
        
        st.session_state.nett = st.checkbox("Faites-vous du nettoyage (Filtres, tuyauteries, brûleurs)?")
        if st.session_state.nett :
            st.session_state.nett_meth = st.radio("Par quelle moyen nettoyez-vous votre installation ?", ('Opérateurs interne', 'Prestataire'))
            if st.session_state.nett_meth == 'Opérateurs interne':
                st.session_state.same_empl = st.checkbox("Ces opérateurs sont-ils différents de ceux s'occupant de la maintenance ?")
                if st.session_state.same_empl :
                    st.session_state.nb_empl2 = st.number_input("Combien d'employées sont dédiés à cette tâche ?", step = 0.1)
                    st.session_state.nett_co_emp = st.session_state.nb_empl2 * st.session_state.salary
                    st.session_state.nett_cost = st.session_state.nett_co_emp
                    
                st.session_state.nett_eq = st.text_input("Nom de l'équipement nettoyé :")
                
                st.session_state.but_nett = st.button("Ajouter dans le tableau ")
                
                if st.session_state.but_nett :
                    st.session_state.ne += [np.transpose(np.array([st.session_state.nett_eq,0,0,"Non"]))]
                    
                if len(st.session_state.ne) != 0 : 
                    df2 = pd.DataFrame(data = st.session_state.ne, index = ('Pièces %d' % i for i in range(1,1 + len(st.session_state.ne))), columns = ["Nom de l'équipement","Coût de la pièce", "Nombre de changement durant les 10 dernières années", "Durée de l'intervention (en heures)", "Intervallle de temps entre les interventions (en mois)", "Cela empiète-t-il sur la production ?(Oui/Non)"])
                    udf2 = st.data_editor(df2)
                    npdf2 = udf2.to_numpy()
                    for i in range(len(st.session_state.ne)):
                        st.session_state.ne[i][1] = npdf2[i,1]
                        st.session_state.ne[i][2] = npdf2[i,2]
                        st.session_state.ne[i][3] = npdf2[i,3]
                        #st.write(st.session_state.ne[i][0])
                        #st.write(st.session_state.ne[i][1])
                        #st.write(st.session_state.ne[i][2])
                    if (float(st.session_state.ne[-1][2]) != 0) and (float(st.session_state.ne[-1][1]) != 0) and (st.session_state.ne[-1][3] == 'Oui'):
                        st.session_state.sum_nett += (float(st.session_state.ne[-1][1]) * (12/ float(st.session_state.ne[-1][2])))
                        #st.write(st.session_state.sum_nett)
            st.write("")
            st.write("")
            st.write("")
            
        
        if st.session_state.nett_meth == 'Prestataire' :
            st.session_state.nett_presta = st.number_input("Coût annuel du prestataire lié au nettoyage des équipements :")
            st.session_state.nett_cost = st.session_state.nett_presta
            
            st.session_state.nett_eq = st.text_input("Nom de l'équipement nettoyé :")
            
            st.session_state.but_nett = st.button("Ajouter dans le tableau ")
            
            if st.session_state.but_nett :
                st.session_state.ne += [np.transpose(np.array([st.session_state.nett_eq,0,0,"Non"]))]
                
            if len(st.session_state.ne) != 0 : 
                df2 = pd.DataFrame(data = st.session_state.ne, index = ('Pièces %d' % i for i in range(1,1 + len(st.session_state.ne))), columns = ["Nom de l'équipement", "Durée de l'intervention (en heures)", "Intervallle de temps entre les interventions (en mois)", "Cela empiète-t-il sur la production ?(Oui/Non)"])
                udf2 = st.data_editor(df2)
                npdf2 = udf2.to_numpy()
                for i in range(len(st.session_state.ne)):
                    st.session_state.ne[i][1] = npdf2[i,1]
                    st.session_state.ne[i][2] = npdf2[i,2]
                    st.session_state.ne[i][3] = npdf2[i,3]
                    #st.write(st.session_state.ne[i][0])
                    #st.write(st.session_state.ne[i][1])
                    #st.write(st.session_state.ne[i][2])
                if (float(st.session_state.ne[-1][2]) != 0) and (float(st.session_state.ne[-1][1]) != 0) and (st.session_state.ne[-1][3] == 'Oui'):
                    st.session_state.sum_nett += (float(st.session_state.ne[-1][1]) * (12/ float(st.session_state.ne[-1][2])))
                    #st.write(st.session_state.sum_nett)
            st.write("")
            st.write("")
            st.write("")
        
        st.session_state.additif = st.checkbox("Utilisez-vous des additifs ?")
        if st.session_state.additif:
            st.session_state.name_add = st.text_input("Nom de l'additif :")
            st.session_state.cost_add = st.number_input("Coût d'un litre d'additif :")
            st.session_state.cons_add = st.number_input("Consommation annuelle de cet additif :")
            st.session_state.but_add = st.button("Ajouter dans le tableau  ")
            
            if st.session_state.but_add :
                st.session_state.add += [np.transpose(np.array([st.session_state.name_add,st.session_state.cost_add,st.session_state.cons_add]))]
           
            if len(st.session_state.add) != 0 : 
                df_add = pd.DataFrame(data = st.session_state.add, index = ('Additif %d' % i for i in range(1,1 + len(st.session_state.add))), columns = ["Nom de l'additif", "Coût d'un litre d'additif", "Consommation annuelle de cet additif"])
                udf_add = st.data_editor(df_add)
                npdf_add = udf_add.to_numpy()
                for i in range(len(st.session_state.add)):
                    st.session_state.add[i][1] = npdf_add[i,1]
                    st.session_state.add[i][2] = npdf_add[i,2]
                    #st.session_state.add[i][3] = npdf2[i,3]
                    #st.write(st.session_state.ne[i][0])
                    #st.write(st.session_state.ne[i][1])
                    #st.write(st.session_state.ne[i][2])
                if (float(st.session_state.add[-1][2]) != 0) and (float(st.session_state.add[-1][1]) != 0) :
                    st.session_state.sum_add += (float(st.session_state.add[-1][1]) * (float(st.session_state.add[-1][2])))
                    #st.write(st.session_state.sum_nett)
            st.write("")
            st.write("")
            st.write("")
            #df_add = pd.DataFrame(data = np.array([[0,0],[0,0]]), columns = ["Combien de litres d'additif pour" , "combien de litres de HFO"])
            #udf_add = st.data_editor(df_add)
        
                    #st.write(st.session_state.sum_nett)  

                        
                #if st.session_state.ne[-1][2] != 0 and st.session_state.ne[-1][1] != 0:
                    #st.session_state.sum_pcs += float(st.session_state.ne[-1][2]) * float(st.session_state.c[-1][1]/10)
        
        #if st.session_state.nett :
            #st.session_state.nett_meth = st.radio("Par quelle moyen nettoyez-vous votre installation ?", ('Opérateurs interne', 'Prestataire'))
            #if st.session_state.nett_meth == 'Opérateurs interne':
               # st.session_state.same_empl = st.checkbox("Ces opérateurs sont-ils différents de ceux s'occupant de la maintenance ?")
                #if st.session_state.same_empl : 
                    #st.session_state.nett_choice = st.multiselect("Que nettoyez-vous ?",["Filtres", "Tuyauteries", "Brûleurs", "Autres"])
                    #if len(st.session_state.nett_choice) != 0:
                        #for i in range(len(st.session_state.nett_choice)) :
                            #st.session_state.n += [st.session_state.nett_choice[-1]]
                            
                    #for i in range(len(st.session_state.n)):
                       # st.session_state.ne += [st.session_state.n[i]]
                        
                    #st.write(st.session_state.n)
                    #st.write(len(st.session_state.ne))
                    #st.write(st.session_state.ne)
        
        
        
        
        #st.write(st.session_state.c)
        #st.write(st.session_state.sum_pcs)
        
        
        #st.write(udf1)
        #st.write(udf)
        #st.write(st.session_state)
        
        
        
        if submitted :
                val = st.button("Générer la facture", on_click = gen_pdf())
                if val == True : 
           # gen_pdf()
           # with open("/Users/nass/Documents/Streamlit-app/pdf_generated.pdf","rb") as file : 
                
                        data = "/Users/nass/Documents/generated_pdf.pdf"
                        st.download_button("Télécharger la facture", data  = data, file_name='facture.pdf', mime = 'document/pdf')
    
    
    if st.session_state.choose == "HFO" : 
        st.write(st.session_state)
        st.write(st.session_state.conso)
        if st.session_state.conso != 0:
            
            en_hfo = round(st.session_state.conso * st.session_state.pci_hfo)
            
            
            #if st.session_state.money == " €":
            cost_hfo = round(st.session_state.conso * st.session_state.price_hfo)
            cost_en = round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
            if st.session_state.meth == 'Prestataire' and st.session_state.presta != 0:
                cost_mtn = round(st.session_state.presta)  
            elif st.session_state.meth == 'Personnel interne':
                cost_mtn = round(st.session_state.nb_employee * st.session_state.salary)
            elif st.session_state.meth == 'Autres' and st.session_state.price_other_meth != 0:
                cost_mtn = round(st.session_state.price_other_meth)
            elif ((st.session_state.meth == 'Autres' and st.session_state.other_unknow == True and st.session_state.price_other_meth == 0)or (st.session_state.meth == 'Prestataire' and st.session_state.presta_unknow == True and st.session_state.presta == 0)):
                if st.session_state.money == " €":
                    cost_mtn = round(2.19 * st.session_state.conso)
                elif st.session_state.money == " $":
                    cost_mtn = round(euro_to_dollar(2.19) * st.session_state.conso)
                elif st.session_state.money == " F":
                    cost_mtn = round(dollar_to_CFA(euro_to_dollar(2.19)) * st.session_state.conso)
                elif st.session_state.money == " R":
                    cost_mtn = round(dollar_to_ZAR(euro_to_dollar(2.19)) * st.session_state.conso)
                elif st.session_state.money == " DT":
                    cost_mtn = round(dollar_to_din_tun(euro_to_dollar(2.19)) * st.session_state.conso)
                elif st.session_state.money == " MUR":
                    cost_mtn = round(dollar_to_mur(euro_to_dollar(2.19)) * st.session_state.conso)
                    
            
            #else :
                #On convertit les euros en dollars
                #cost_hfo = round(st.session_state.conso * st.session_state.price_hfo)
                #cost_hfo = round(euro_to_dollar(cost_hfo))
                
                #if st.session_state.money == " F":
                    #cost_hfo = round(dollar_to_CFA(cost_hfo),2)
                
                #elif st.session_state.money == " R":
                    #cost_hfo = round(dollar_to_ZAR(cost_hfo),2)
                    
                #elif st.session_state.money == " DT":
                    #cost_hfo = round(dollar_to_din_tun(cost_hfo),2)
                    
                #elif st.session_state.money == " MUR":
                    #cost_hfo = round(dollar_to_mur(cost_hfo),2)"""
               
            #st.write("Voici l'énergie produit par le HFO :")
            #st.write (space_in_numbers(str(en_hfo))+"kWh")
            
            #st.write(cost_hfo)
            #st.write(cost_en)
            #st.write(cost_mtn)
            st.write(st.session_state.sum_nett)
            c1, c2, c3 = st.columns(3)
            c1.metric("Voici le coût de la molécule HFO :", str(cost_hfo) + st.session_state.money)
            c2.metric("Voici le coût énergétique lié au HFO :", str(cost_en) + st.session_state.money)
            c3.metric("Coût annuel moyen lié à la maintenance du site :", str(cost_mtn) + st.session_state.money)
            
           #st.write("Voici le coût de la molécule HFO :")
            #st.write(str(cost_hfo) + st.session_state.money)
            #st.write("Voici le coût énergétique lié au HFO :")
            #st.write(str(cost_en) + st.session_state.money)
           # st.write("Coût annuel moyen lié à la maintenance du site :")
            #st.write(str(cost_mtn) + st.session_state.money)
            
            if st.session_state.eau !=0:
                c2.metric("Coût annuel global de l'eau traitée :", str(round(st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb)) + st.session_state.money)
            
            if st.session_state.ram :
                c1.metric("Coût annuel lié aux ramonages :", str(round(st.session_state.ram_cost * st.session_state.nb_ram)) + st.session_state.money)
            
            if len(st.session_state.c) != 0:
                c3.metric("Coût total lié au changement de pièce :", str(round(st.session_state.sum_pcs)) + st.session_state.money)
            
            if st.session_state.nett :
                c1.metric("Coût total lié au nettoyage du site", str(st.session_state.nett_cost) + st.session_state.money)
                
                if st.session_state.sum_nett != 0:
                    c2.metric("Temps de production perdu :", str(st.session_state.sum_nett)+" heures")
            
            if st.session_state.sum_add != 0 :
                c3.metric("Coût total des additifs", str(st.session_state.sum_add) + st.session_state.money)

                    
            
            
            
            
            st.divider()
            col1, col2 = st.columns([2,1.5])
            st.subheader("Coût annuel total de fonctionnement de votre installation HFO : ")
            st.title(str(round(cost_hfo + cost_en + cost_mtn + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))) + st.session_state.money)
            
            st.divider()
            st.write("")
            st.write("")
            st.write("")
            cost_list = np.array([cost_hfo,cost_en,cost_mtn, st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb, st.session_state.ram_cost * st.session_state.nb_ram, st.session_state.sum_pcs, st.session_state.nett_cost, st.session_state.sum_add])
            data_chart=[]
            for i in range(8):
                data_chart +=  [cost_list* (1.003**i) ]
            
            chart_data_hfo = pd.DataFrame(data= data_chart, columns =["Coût de la molécule", "Coût énergétique", "Coût maintenance du site", "Coût de l'eau","Coût ramonages", "Coût pièces", "Coût nettoyages", "Coût additifs"])
            st.bar_chart(chart_data_hfo)
            
        else :
            def go_base():
                st.session_state.choose = "Page d'accueil"
                return st.session_state.choose 
            st.write("Veuillez renseigner les informations de la page d'accueil ")
            #st.button("Aller à la page d'accueil", on_click = go_base())
        
        
    if st.session_state.choose == "GPL" : 
        if consommation != 0 :
            rend_rand = np.random.rand(3,6)
            coeff_rand = (100-rend_rand)/100
            quantity_gpl = round(coeff_rand * calcul_conso_gpl(calcul_energy_hfo(st.session_state)))
            st.write("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.write(str(quantity_gpl)+" tonnes")
            cost_gpl = price_gpl(quantity_gpl)
            st.write("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.write(str(cost_gpl) + st.session_state.money)
        else :
            st.write("Veuillez renseigner votre consommation ")
            
            
            
    if st.session_state.choose == "Comparaison" : 
        col1, col2 = st.columns(2)
        #st.write("Ici sera afficher des grahiques comme l'amortissement sur 10 ans entre le HFO et le GPL, compoaraison de la quatité de CO2 économiser")
        chart_data = pd.DataFrame(courbe(1,2,20), columns=["a","b"])
        st.bar_chart(chart_data)
        p = figure(title = 'Le rendement en fonction des mois', x_axis_label = 'Mois', y_axis_label = 'Rendement')
        x = [i for i in range(60)]
        p.line(x ,rendement(60), legend_label = 'Rendement', line_width = 4)
        st.bokeh_chart(p, use_container_width = True)
        k= np.zeros((2,60))
        
        for i in range(60):
            k[0][i]= rendement(60)[i]
            k[1][i] = 1
        
        k=k.T
        
        ind = [i for i in range(60)]
        #k = np.array([rendement(60), 1 for i in range(60)]).T
        dfp = pd.DataFrame(k,index = ind, columns = ['rendement HFO', 'rendement GPL'])
        st.subheader("Rendement en fonction du temps (mois) :")
        st.line_chart(dfp)
        st.area_chart(dfp)
        st.bar_chart(dfp)
            
        
        CO2_HFO = round((st.session_state.conso * 25440) / 8000)
        CO2_GPL = round((st.session_state.conso * 19614) / 8000)
        st.write(CO2_HFO)    
        st.metric(label = "Emission de CO2 eq", value = str(CO2_GPL) + " tons eq CO2", delta = str((CO2_HFO-CO2_GPL)*100/CO2_GPL) + " % de tons eq CO2 gagnée")
    
    if st.session_state.choose == "Proposition d'optimisation" :
        co1, co2 = st.columns(2)
        co1.title("Economiseur HFO")
        co2.title("Economiseur GPL")
        
        
        





        
#English language
if en :       
    val = st.button("Generate the invoive", on_click = gen_pdf())
    if val == True : 
        with open("/Users/nass/Documents/Streamlit-app/pdf_generated.pdf","rb") as file : 
            
            #data = "/Users/nass/Documents/Streamlit-app/generated_pdf.pdf"
            st.download_button("Download the invoice", data  = file, file_name='facture.pdf', mime = 'document/pdf')
    
    
    if st.session_state.choose == "HFO" : 
        if consommation != 0:
            en_hfo = round(consommation *11774,2)
            cost_hfo = price_hfo(consommation)
            st.write("This is the energy produce by the HFO :")
            st.write (str(en_hfo)+"kWh")
            st.write("The cost of molecule HFO :")
            st.write(str(cost_hfo) + "€")
        else :
            st.write("Veuillez renseigner votre consommation ")
        
        
    if st.session_state.choose == "GPL" : 
        if consommation != 0 :
            quantity_gpl = round(calcul_conso_gpl(calcul_energy_hfo(consommation)), 2)
            st.write("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.write(str(quantity_gpl)+" tonnes")
            cost_gpl = price_gpl(quantity_gpl)
            st.write("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.write(str(cost_gpl) + "€")
        else :
            st.write("Veuillez renseigner votre consommation ")
            
    if st.session_state.choose == "Comparaison" : 
        st.write("Ici sera afficher des grahiques comme l'amortissement sur 10 ans entre le HFO et le GPL, compoaraison de la quatité de CO2 économiser")
  
        
