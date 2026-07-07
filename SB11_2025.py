#%% Dependencias

import os
import pandas as pd # Requiere instalación

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

# Filtrar solo estudiantes
sb11_2025_f = sb11_2025_f[sb11_2025_f["estu_estudiante"] == "ESTUDIANTE"]

# Valores faltantes
nna_sb11 = sb11_2025_f.isna().sum().sort_values().to_frame(name = "NA")
nna_sb11["NA (%)"] = (nna_sb11["NA"] / nna_sb11["NA"].sum())*100

#%% Distribución de las variables

# Distribución de estudiantes por departamento
## Frecuencia absoluta
tf_dpto = sb11_2025_f["estu_depto_reside"].value_counts().reset_index()
tf_dpto.columns = ["Departamento","Estudiantes"]

## Participación porcentual
tf_dpto["Estudiantes (%)"] = (tf_dpto["Estudiantes"] / tf_dpto["Estudiantes"].sum())*100

