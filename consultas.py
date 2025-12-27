# 1. Import libraries
import csv
from datetime import datetime, timedelta
import json
try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print('')

# 2. History search

# 2.1 History search by course

def history_course(regist):
    print('---------------------------\n♦ Historial por curso ♦ \n---------------------------')
    l=[]
    printe= []
    for i in regist:
        if i['Curso_ID'] not in l:
            l.append(i['Curso_ID'])   
    
    for i in l:
        user= ''
        a=[]
        for j in regist:
            if i == j['Curso_ID']:
                user=j['Nombre del curso']
                a.append(j)
        print(f"Historial de incripciones curso: {user}")
        print(a)

# 2.2 History search by user
def history_user(regist):
    print('---------------------------\n♦ Historial por usuario ♦ \n---------------------------')
    l=[]
    printe= []
    for i in regist:
        if i['Nombre del usuario'] not in l:
            l.append(i['Nombre del usuario'])   
    
    for i in l:
        user= ''
        a=[]
        for j in regist:
            if i == j['Nombre del usuario']:
                user=j['Nombre del usuario']
                a.append(j)
        print(f"Historial de incripciones usuario: {user}")
        print(a)

# 3. Export report data

def report(users,courses,regist):
    month_year =''
    while True:
        report= input('¿Desea ver el reporte por Mes o Año:').lower()
        if report =='mes' or report =='año':
            month_year= report
            break
        else:
            print('El valor no es valido, vuelve a intentarlo')
    
    months=[]
    years=[]
    for i in regist:
        if datetime.strptime(i['Fecha de inscripción'],"%Y-%m-%d").month not in months:
            months.append(datetime.strptime(i['Fecha de inscripción'],"%Y-%m-%d").month)
        if datetime.strptime(i['Fecha de inscripción'],"%Y-%m-%d").year not in years:
            years.append(datetime.strptime(i['Fecha de inscripción'],"%Y-%m-%d").year)
    
    if month_year=='mes':
        for i in months:
            user= ''
            a=[]
            for j in regist:
                if i == datetime.strptime(j['Fecha de inscripción'],"%Y-%m-%d").month:
                    user=datetime.strptime(j['Fecha de inscripción'],"%Y-%m-%d").month
                    a.append(j)
            print(f"Historial de incripciones mes: {user}")
            print(a)
    elif month_year=='año':
        for i in years:
            user= ''
            a=[]
            for j in regist:
                if i == datetime.strptime(j['Fecha de inscripción'],"%Y-%m-%d").year:
                    user=datetime.strptime(j['Fecha de inscripción'],"%Y-%m-%d").year
                    a.append(j)
            print(f"Historial de incripciones año: {user}")
            print(a)

