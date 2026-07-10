#%% Dependencias

import os
import pandas as pd # Requiere instalación
import numpy as np

#%% Directorios

ruta  = ["/home/deb_scha/Documentos/Proyectos/SB11_ICFES_2025",
         "/home/fed_scha/Documentos/Proyectos/SB11_ICFES_2025",
         "/home/cach_scha/Documentos/Proyectos/SB11_ICFES_2025"]

for i in ruta:
    ruta_verif = os.path.isdir(i)
    print(ruta_verif)
    if ruta_verif == True:
        os.chdir(i)
        break

del(i,ruta,ruta_verif)
    
#%% Datos
# Saber 11
# Enlace: https://www.icfes.gov.co/investigaciones/data-icfes/
sb11_2025 = pd.read_csv("Datos/SB11_20212.txt",sep = ";")

# Variables
vars = pd.read_csv("Datos/vars.csv",sep = ",")

#%% Procesameinto de datos

# Pasar nombres de variables a minúsculas
sb11_2025.rename(columns=str.lower,inplace = True)

# Filtrar variables de interés
sb11_2025_f = sb11_2025.filter(items = vars["Dimensión"])

# Valores faltantes
nna_sb11 = sb11_2025_f.isna().sum().sort_values().to_frame(name = "NA")
nna_sb11["NA (%)"] = (nna_sb11["NA"] / nna_sb11["NA"].sum())*100

# ---- Genero del estudiante
# (98 observaciones) - Creación de categoría
sb11_2025_f["estu_genero"] = sb11_2025_f["estu_genero"].fillna("NA")

# ---- Caracterización geográfica
#  (227 observaciones) - Eliminación 
sb11_2025_fna = sb11_2025_f[sb11_2025_f["estu_depto_reside"].isna()]
sb11_2025_fna["cole_codigo_icfes"].value_counts().reset_index()
sb11_2025_f2 = sb11_2025_f.dropna(subset = ["estu_depto_reside"])

# ---- Tipo de examinando
#  (64482 observaciones) - Eliminación
sb11_2025_fna2 = sb11_2025_f2[sb11_2025_f2["cole_codigo_icfes"].isna()]
sb11_2025_fna2["estu_estudiante"].value_counts()
## Análisis por segmento
sb11_2025_festu = sb11_2025_f2[sb11_2025_f2["estu_estudiante"] == "ESTUDIANTE"]
na_festu = (sb11_2025_festu.isna().sum().sort_values().to_frame(name = "%NA")/sb11_2025_festu.shape[0])*100

### Grupo: ESTUDIANTE
nunna_festu = 0
for i in range(len(na_festu)):
    if float(na_festu.iloc[i]) == 0:
        nunna_festu += 1
##-## Proporción de valores faltantes
(nunna_festu/len(na_festu))*100 # Porcentaje de variables completas
np.mean(na_festu["%NA"]) # Porcentaje promedio de valores faltantes
np.var(na_festu["%NA"]) # Varianza porcentaje de valores faltantes
np.std(na_festu) # Desv. Estandaer porcentaje de valores faltantes

### Grupo: INDIVIDUAL
sb11_2025_find = sb11_2025_f2[sb11_2025_f2["estu_estudiante"] != "ESTUDIANTE"]
na_find = (sb11_2025_find.isna().sum().sort_values().to_frame(name = "%NA")/sb11_2025_find.shape[0])*100
nunna_find = 0
for i in range(len(na_find)):
    if float(na_find.iloc[i]) == 0:
        nunna_find += 1
##-## Proporción de valores faltantes
(nunna_find/len(na_find))*100 # Porcentaje de variables completas
np.mean(na_find["%NA"]) # Porcentaje promedio de valores faltantes
np.var(na_find["%NA"]) # Varianza porcentaje de valores faltantes
np.std(na_find) # Desv. Estandaer porcentaje de valores faltantes

## Eliminación de datos INDIVIDUAL
sb11_2025_f3 = sb11_2025_f2[sb11_2025_f2["estu_estudiante"] == "ESTUDIANTE"]

# ---- Educación de los padres
sb11_2025_f3["fami_educacionmadre"].value_counts().reset_index()
sb11_2025_f3["fami_educacionmadre"] = sb11_2025_f3["fami_educacionmadre"].fillna("No sabe")
sb11_2025_f3["fami_educacionpadre"].value_counts().reset_index()
sb11_2025_f3["fami_educacionpadre"] = sb11_2025_f3["fami_educacionpadre"].fillna("No sabe")

# ---- Estrato socieconómico

