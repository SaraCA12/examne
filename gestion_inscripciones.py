# 1. Import libraries
import csv
from datetime import datetime, timedelta, date
import json
try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print('')

# 2. Functions for manage 'cursos.csv' file

# 2.1 Add new course

def add_regist(user_name,users,courses,regist):
    print('---------------------------\n♦ Adición de inscripciones♦ \n---------------------------')
    #Introducing the information
    while True:
        # a. Asign a ID number
        id_co= len(regist)+1001
        
        # b. Name of the user
        co_name= user_name
        
        # c. ID of the course
        id= ''
        while True: 
            id_cour= input('\nIngresa el ID del curso que deseas inscriibir: ').lower()
            lista=[]
            for i in courses:
                lista.append(i['Curso_ID'])
            if id_cour in lista:
                id=id_cour
                break
            else:
                print('Este curso no existe, Intentalo de nuevo')
        
        # d. Name of the course
        name_co= ''
        for i in courses:
            if i['Curso_ID'] == id:
                name_co = i['Nombre del curso']

        # e. Date of inscription
        hoy= date.today().strftime('%Y-%m-%d')
        # f. Available_Places
        cant= ''
        for i in users:
            if i['Usuario']==co_name:
                cant= i['Cursos']


        #Create a new dictionary with the information entered
        new_regist= {'Inscripción_ID': id_co, 
                            'Nombre del usuario':co_name,
                            'Curso_ID': id,
                            'Nombre del curso': name_co,
                            'Fecha de inscripción': hoy,
                            'Cantidad de cursos del usuario':cant}
        regist.append(new_regist)

        ask= input('¿Deseas ingresar otro curso? (S/N): ' ).lower()
        if ask == 'n' or ask=='no':
            break
    
    # Save the new course in csv file
    try:
        with open("inscripciones.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(regist[0].keys())
            for i in regist:
                write.writerow(i.values())
            print('Los cambios se han guardado!')
    except FileNotFoundError:
        print('El archivo no existe, se ha creado un nuevo archivo con las columnas predeterminadas')
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(['Inscripcion_ID','Nombre del usuario','Curso_ID','Nombre del curso','Fecha de inscripción','Cantidad de cursos del usuario'])

# 2.2 Show all courses 

def show_regist(users,courses,regist):
    print('---------------------------\n♦ Despliegue de inscripciones♦ \n---------------------------')
    show=[]
    headers = [['Inscripcion_ID','Nombre del usuario','Curso_ID','Nombre del curso','Fecha de inscripción','Cantidad de cursos del usuario']]
    for i in regist:
        show.append([i['Inscripción_ID'],i['Nombre del usuario'], i['Curso_ID'], i['Nombre del curso'],i['Fecha de inscripción'],i['Cantidad de cursos del usuario']])
    try:
        table= tabulate(show, headers=headers, tablefmt='fancy_grid')
        print(table)
    except ModuleNotFoundError:
        for i in show:
            print({'Inscripcion_ID': i[0], 'Nombre del usuario':i[1],'Curso_ID': i[2],'Nombre del curso': i[3],'Fecha de inscripción': i[4],'Cantidad de cursos del usuario':i[5]})
    except NameError:
        for i in show:
            print({'Inscripcion_ID': i[0], 'Nombre del usuario':i[1],'Curso_ID': i[2],'Nombre del curso': i[3],'Fecha de inscripción': i[4],'Cantidad de cursos del usuario':i[5]})

# 2.3 Delete courses

def regist_delete(users,courses,regist):
    print('---------------------------\n♦ Cancelación de inscripciones♦ \n---------------------------')
    while True:
        name= ''
        while True: 
            id_ins= input('Ingresa el ID de la inscripción a eliminar: ').lower()
            lista=[]
            for i in regist:
                lista.append(i['Inscripción_ID'])
                
            if id_ins not in lista: # Informs the user that the inscription was not found'Inscripción_ID'
                preg = input('Inscripción no encontrada, (si deseas añadir una inscripción escribe y): ').lower()
                if preg == 'y':
                    add_regist(users,courses,regist)
                    
            elif id_ins in lista:
                name=id_ins
                break
        
        # Block to delete inscription information of the inscription selected
        for i in regist:
            if i['Inscripción_ID']== name:
                regist.pop(regist.index(i))
                print(f"\nInscripción {name} Eliminada Exitosamente! ")
        
        delete_another= input('\n¿Deseas eliminar otra inscripción? (No): ').lower()
        if delete_another== "no":
            print('\nVuelve pronto!')
            break

    # Save the new course in csv file
    try:
        with open("inscripciones.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(regist[0].keys())
            for i in regist:
                write.writerow(i.values())
            print('Los cambios se han guardado!')
    except FileNotFoundError:
        print('El archivo no existe, se ha creado un nuevo archivo con las columnas predeterminadas')
        with open("inscripciones.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(['Inscripcion_ID','Nombre del usuario','Curso_ID','Nombre del curso','Fecha de inscripción','Cantidad de cursos del usuario'])