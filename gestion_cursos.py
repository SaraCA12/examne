# 1. Import Libraries

import csv
from datetime import datetime, timedelta
import json
try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print('')

# 2. Functions for manage 'cursos.csv' file

# 2.1 Add new course

def add_new(courses):
    print('---------------------------\n♦ Adición de cursos♦ \n---------------------------')
    #Introducing the information
    while True:
        # a. Asign a ID number
        id_co= len(courses)+101
        
        # b. Name of the course
        co_name= input('Introduce el nombre del curso:\n►►►')
        
        # c. Department
        deparments= ['gestión','finanzas', 'rh']
        while True:
            depar_cour= input(f"\nIntroduce el departamento del curso:\nLos departamentos disponibles son:{deparments}\n►►►").lower()
            if depar_cour in deparments:
                break
            else:
                print('\nEL departamento no existe, Intentalo de nuevo\n')
        
        # d. Initial status
        in_sta= 0
        
        # e. Max_places
        while True:   
            try:
                max_plac= abs(int(input('\nInserte los cupos maximos del curso:\n►►►')))
                break
            except ValueError:
                print('\n¡ERROR! Porfavor inserte un valor correcto (Número entero)')

        # f. Available_Places
        av_plac= max_plac

        # g. Status
        status= ['abierto','inactivo', 'cerrado']
        while True:
            stat= input(f"\nIntroduce el estado del curso:\nLos estados disponibles son:{status}\n►►►").lower()
            if stat in status:
                break
            else:
                print('\nEL estado no existe, Intentalo de nuevo\n')

        # h. Close date
        while True:
            close_date= input('\nIntroduce la fecha de cierre de inscripciones en formato Año-Mes-Día:\n►►► ')
            try:
                datee= datetime.strptime(close_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')
            except TypeError:
                print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')
            except AttributeError:
                print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')
            except NameError:
                print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')     

        #Create a new dictionary with the information entered
        new_course= {'Curso_ID': id_co, 
                    'Nombre del curso':co_name,
                    'Departamento': depar_cour,
                    'Cupos ocupados': in_sta,
                    'Cupos disponibles': av_plac,
                    'Cupo maximo':max_plac,
                    'Estado':stat,
                    'Fecha de cierre':close_date}
        courses.append(new_course)

        ask= input('¿Deseas ingresar otro curso? (S/N): ' ).lower()
        if ask == 'n' or ask=='no':
            break
    
    # Save the new course in csv file
    try:
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(courses[0].keys())
            for i in courses:
                write.writerow(i.values())
            print('Los cambios se han guardado!')
    except FileNotFoundError:
        print('El archivo no existe, se ha creado un nuevo archivo con las columnas predeterminadas')
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(['Course_ID','Course_Name','Department','Occupied_Places','Available_Places','Max_Places','Status','Close_Date'])

# 2.2 Show all courses 

def show_courses(courses): 
    print('---------------------------\n♦ Despliegue de cursos♦ \n---------------------------')
    show=[]
    headers = [['Course_ID','Course_Name','Department','Occupied_Places','Available_Places','Max_Places','Status','Close_Date']]
    for i in courses:
        show.append([i['Curso_ID'],i['Nombre del curso'], i['Departamento'], i['Cupos ocupados'],i['Cupos disponibles'],i['Cupo maximo'],i['Estado'], i['Fecha de cierre']])
    try:
        table= tabulate(show, headers=headers, tablefmt='fancy_grid')
        print(table)
    except ModuleNotFoundError:
        for i in show:
            print({'Curso_ID': i[0], 'Nombre del curso':i[1],'Departamento': i[2],'Cupos ocupados': i[3],'Cupos disponibles': i[4],'Cupo maximo':i[5],'Estado':i[6],'Fecha de cierre':i[7]})
    except NameError:
        for i in show:
            print({'Curso_ID': i[0], 'Nombre del curso':i[1],'Departamento': i[2],'Cupos ocupados': i[3],'Cupos disponibles': i[4],'Cupo maximo':i[5],'Estado':i[6],'Fecha de cierre':i[7]})

# 2.3 Delete courses

def courses_delete(courses):
    print('---------------------------\n♦ Eliminación de cursos♦ \n---------------------------')
    while True:
        name= ''
        while True: 
            id_cour= input('Ingresa el ID del curso que deseas eliminar: ').lower()
            lista=[]
            for i in courses:
                lista.append(i['Curso_ID'])
                
            if id_cour not in lista: # Informs the user that the course was not found, but offers the option to add it to the file
                preg = input('Curso no encontrado, (si deseas ver la lista de cursos escribe y): ').lower()
                if preg == 'y':
                    show_courses(courses)
                    
            elif id_cour in lista:
                name=id_cour
                break
        
        # Block to delete product information of the product selected
        for i in courses:
            if i['Curso_ID']== name:
                courses.pop(courses.index(i))
                print(f"\nCurso {i['Nombre del curso']} Eliminado Exitosamente! ")
        
        delete_another= input('\n¿Deseas eliminar otro producto? (No): ').lower()
        if delete_another== "no":
            print('\nVuelve pronto!')
            break

    # Save the new course in csv file
    try:
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(courses[0].keys())
            for i in courses:
                write.writerow(i.values())
            print('Los cambios se han guardado!')
    except FileNotFoundError:
        print('El archivo no existe, se ha creado un nuevo archivo con las columnas predeterminadas')
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(['Course_ID','Course_Name','Department','Occupied_Places','Available_Places','Max_Places','Status','Close_Date'])

# 2.4 Update courses

def update_course(courses,regist): 
    print('---------------------------------\n♦ Actualización de cursos♦ \n--------------------------------')
    while True:
        id= ''
        while True: 
            id_cour= input('\nIngresa el ID del curso que deseas actualizarar: ').lower()
            lista=[]
            for i in courses:
                lista.append(i['Curso_ID'])
                
            if id_cour not in lista: # Informs the user that the product was not found, but offers the option to add it to the inventory
                preg = input('Curso no encontrado, (si deseas agregar el curso escribe y): ').lower()
                if preg == 'y':
                    add_new(courses)
            elif id_cour in lista:
                id=id_cour
                break
        
        while True: # Asks the user which information to update; if the user enters a value other than 1, 2, 3, 4 or 5 it prints 'Invalid option' and ask again for a new value.
            update= input('¿Que deseas actualizar?\n1. Nombre del curso\n2. Departamento\n3. Cupo Máximo\n4. Estado\n5. Fecha de cierre\nSelecciona un número: ')
            if update=='1':
                new_name= input('\nInserte el nuevo nombre del curso: ')
                for i in courses:
                    if i['Curso_ID']== id:
                        i['Nombre del curso']= new_name
                        print(i['Nombre del curso'])
                        print(f"\nNombre del curso actualizado exitosamente!\nCurso_ID: {i['Curso_ID']} || Nombre del curso: {i['Nombre del curso']} ")
                for i in regist:
                    if i['Curso_ID']== id:
                        i['Nombre del curso']= new_name
        
            elif update=='2':
                deparments= ['gestión','finanzas', 'rh']
                while True:
                    new_depar= input(f"\nInserte el nuevo departamento del curso:\nLos departamentos disponibles son:{deparments}\n►►►").lower()
                    if new_depar in deparments:
                        break
                    else:
                        print('\nEL departamento no existe, Intentalo de nuevo\n')

                for i in courses:
                    if i['Curso_ID']== id:
                        i['Deparamento']= new_depar
                        print(f"\nNombre del departamento actualizado exitosamente!\nCurso_ID: {i['Curso_ID']} || Nombre del curso: {i['Nombre del curso']}|| Departamento: {i['Departamento']} ")

            elif update=='3':
                while True:  
                    try:
                        new_place = abs(int(input('\nInserte el nuevo cupo maximo del curso: ')))
                        break
                    except ValueError:
                        print('\n¡ERROR! Porfavor inserte un valor correcto (Número entero)')

                for i in courses:
                    if i['Curso_ID']== id:
                        i['Curso_ID']== id
                        print(f"\nCupo maximo actualizado exitosamente!\nCurso_ID: {i['Curso_ID']} || Nombre del curso: {i['Nombre del curso']}|| Cupo maximo: {i['Cupo maximo']} ")
            
            elif update=='4':
                status= ['abierto','inactivo', 'cerrado']
                while True:
                    new_stat= input(f"\nIntroduce el nuevo estado del curso:\nLos estados disponibles son:{status}\n►►►").lower()
                    if new_stat in status:
                        break
                    else:
                        print('\nEL estado no existe, Intentalo de nuevo\n')
                
                for i in courses:
                    if i['Curso_ID']== id:
                       i['Estado']== new_stat
                       print(f"\nEstado Actualizado Exitosamente!\nCurso_ID: {i['Curso_ID']} || Nombre del curso: {i['Nombre del curso']}|| Estado: {i['Estado']} ")
            
            elif update=='5':
                while True:
                    new_close_date= input('\nIntroduce la fecha de cierre de inscripciones en formato Año-Mes-Día:\n►►► ')
                    try:
                        datee= datetime.strptime(new_close_date, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')
                    except TypeError:
                        print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')
                    except AttributeError:
                        print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')
                    except NameError:
                        print('\nEl formato de la fecha no es correcto, Vuelve a intentarlo\n')   
                
                for i in courses:
                    if i['Curso_ID']== id:
                       i['Fecha de cierre']== new_close_date
                       print(f"Estado Actualizado Exitosamente!\nCurso_ID: {i['Curso_ID']} || Nombre del curso: {i['Nombre del curso']}|| Fecha de cierre: {i['Fecha de cierre']} ")
            
            else: 
                print('Opción no disponible, vuelve a intentarlo') 
            
            new_upd= input('\n¿Deseas actualizar otro item del mismo curso? (No): ').lower()
            if new_upd== "no":
                break
        
        new_change= input('\n¿Deseas actualizar otro curso? (No): ').lower()
        if new_change== "no":
            break
    
    # Save the updated course in csv file
    try:
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(courses[0].keys())
            for i in courses:
                write.writerow(i.values())

    except FileNotFoundError:
        print('El archivo no existe, se ha creado un nuevo archivo con las columnas predeterminadas')
        with open("cursos.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(['Course_ID','Course_Name','Department','Occupied_Places','Available_Places','Max_Places','Status','Close_Date'])
    
    # Save the updated inscription list in csv file
    try:
        with open("inscripciones.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(regist[0].keys())
            for i in regist:
                write.writerow(i.values())
    except FileNotFoundError:
        print('El archivo no existe, se ha creado un nuevo archivo con las columnas predeterminadas')
        with open("inscripciones.csv", "w",newline="",encoding= "utf-8") as archivo:
            write = csv.writer(archivo)
            write.writerow(['Regist_ID','User_Name','Course_ID','Course_Name','Regist_Date','No_COurses'])

# autodaved