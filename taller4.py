import pandas as pd
import pandas as pd

# lectura de archivos en la nuve 

# ID del archivo en Google Drive
file_id = '17dJ5NaxghaGWrDCEtbFtRjfb7gqDXe-H'
# Construir la URL de descarga directa
url = f'https://drive.google.com/uc?id={file_id}'

# Lee el archivo CSV 
df = pd.read_csv(url, sep=";")

# lectura archivo local 

df_employees = pd.read_csv("employees.csv", sep=";")


#ejercicios de la unidad 4 
# punto 1

print("Trabajadores pertenecientes al departamento 50 y con un salario mayor o igual a 4000")
print(df[(df.SALARY >= 4000) & (df.DEPARTMENT_ID == 50)][['FIRST_NAME','LAST_NAME','SALARY', 'DEPARTMENT_ID']])

#punto 2 
print("Cargo de los trabajadores con nombr4e Alexander")
print(df[(df.FIRST_NAME == "Alexander") ][['FIRST_NAME','LAST_NAME','JOB_ID']])

#punto 6 
print("trabajadores con el salario minimo ")
print(df[(df.SALARY == df['SALARY'].min()) ][['FIRST_NAME','LAST_NAME','SALARY']])

# punto 7 
print(" empleados con el salario mayor al salario promedio de la compañia ")

print(df[(df.SALARY >= df['SALARY'].mean())][['FIRST_NAME','LAST_NAME','SALARY']])

#punto 8
print("trabajadores con el salario maximo ")
print(df[(df.SALARY == df['SALARY'].max()) ][['FIRST_NAME','LAST_NAME','SALARY']])

#punto 13 
print("punto 13")
print(df[df.LAST_NAME.str.contains('[k h]', regex=True)])

# punto 14 
print("punto 14")
print(df[df.LAST_NAME.str.contains('h.{2}o', regex=True)])

#punto 15 
print("punto 15")
print(df[df.LAST_NAME.str.contains('[g$]', regex=True)])

#punto 16 
print("punto 16")
print(df[df['SALARY'] == df['SALARY'].max()][['FIRST_NAME', 'LAST_NAME']])

#punto 17 
print("punto 17")
print(df.sort_values(by='SALARY', ascending=False))

#punto 18 
print("punto 18")
print(df[(df['SALARY'] >= 13500) & (df['SALARY'] <= 17000)][['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'SALARY']])

#punto 19 
print("punto 19")
print(df[df['DEPARTMENT_ID'].isin([10, 20, 40, 70])][['DEPARTMENT_ID', 'FIRST_NAME']])

#punto 20 
print("punto 20")
print(df[~df['DEPARTMENT_ID'].isin([10, 20, 40, 70])][['DEPARTMENT_ID', 'FIRST_NAME']])
