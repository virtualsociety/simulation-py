'''
Script for data analysis

By Dr. Raymond Hoogendoorn
Copyright 2021
'''

import pandas as pd

df_gender = pd.read_csv('./Input/Bevolking__kerncijfers_07122020_100024.csv', delimiter = ';')
df_age = pd.read_csv('./Input/Bevolking__kerncijfers_07122020_112736.csv', delimiter = ';')
df_lifeexpectancy = pd.read_csv('./Input/Levensverwachting__geslacht__leeftijd__per_jaar_en_periode_van_vijf_jaren__06012021_105805.csv', delimiter = ';')
df_maritalstatus = pd.read_csv('./Input/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_08122020_110015.csv', delimiter = ';')
df_marriageduration = pd.read_csv('./Input/Bestaande_huwelijken_en_partnerschappen__relatieduur__1_januari_08122020_121148.csv', delimiter = ';')
df_employmentstatus = pd.read_csv('./Input/Arbeidsdeelname__kerncijfers__08122020_130106.csv', delimiter = ';')
df_income = pd.read_csv('./Input/Inkomen_van_personen__inkomensklassen__persoonskenmerken_09122020_094158.csv', delimiter = ';')
df_marriage = pd.read_csv('./Input/Huwen_en_huwelijksontbinding__geslacht__leeftijd__31_december___regio_11122020_100116.csv', delimiter = ';')
df_marriage2 = pd.read_csv('./Input/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_11122020_105220.csv', delimiter = ';')
df_withchildren =  pd.read_csv('./Input/Particuliere_huishoudens_naar_samenstelling_en_grootte__1_januari_14122020_114929.csv', delimiter = ';')
df_nrchildren = pd.read_csv('./Input/Huishoudens__kindertal__leeftijdsklasse_kind__regio__1_januari_14122020_114332.csv', delimiter = ';')
df_birthage =  pd.read_csv('./Input/Levend_geboren_kinderen__migratieachtergrond_moeder_en_leeftijd_moeder_14122020_112329.csv', delimiter = ';')
df_capital = pd.read_csv('./Input/vermogensklassen.csv', delimiter = ';')

df_simulated = pd.read_csv('./simulatedpopulation.csv', delimiter = ',')

print(df_simulated.head())
