#%% Dependencias %%#
import os
import pandas as pd # Requiere instalación

#%% Directorios %%#
ruta  = ["/home/deb_scha/Documentos/Proyectos/SB11_ICFES_2025",
         "/home/fed_scha/Documentos/Proyectos/SB11_ICFES_2025",
         "/home/cach_scha/Documentos/Proyectos/SB11_ICFES_2025"]

for i in ruta:
    ruta_verif = os.path.isdir(i)
    print(ruta_verif)
    if ruta_verif == True:
        os.chdir(i)
        break
    
#%% Datos %%#
# Enlace: https://www.icfes.gov.co/investigaciones/data-icfes/
sb11_2025 = pd.read_csv("Datos/SB11_20212.txt",sep = ";")
