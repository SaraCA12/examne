# 1. Import libraries

import csv
from datetime import datetime, timedelta
import json
try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print('')
try:
    import gestion_cursos as gc
except ModuleNotFoundError:
    print('')
try:
    import gestion_inscripciones as gi
except ModuleNotFoundError:
    print('')
try:
    import consultas as cs
except ModuleNotFoundError:
    print('')

# 2. Open files

# 2.1 Open 'usuarios.csv' file

users= []   # create a list to store dictionaries with the data of the file

#Use try/except to validate the existence of the file 'usuarios.csv' or create a new file with that name and the headers
try:
    with open('usuarios.csv', "r", encoding="utf-8") as archivo:
        next(archivo)
        for i in archivo:
            i= i.strip("\n")
            colum = i.split(',')
            users.append({'Usuario': colum[0], 
                            'Contrasena':colum[1],
                            'Rol': colum[2],'Cursos': colum[3]})
except FileNotFoundError:
    with open("usuarios.csv", "w",newline="") as archivo: 
        escri = csv.writer(archivo)
        escri.writerow(['Usuario','Contrasena','Rol'])

# 2.2 Open 'cursos.csv' file

courses= []   # create a list to store dictionaries with the data of the file

#Use try/except to validate the existence of the file 'usuarios.csv' or create a new file with that name and the headers
try:
    with open('cursos.csv', "r", encoding="utf-8") as archivo1:
        next(archivo1) #Skip headers
        for i in archivo1:
            i= i.strip("\n")
            colum1 = i.split(',')
            courses.append({'Curso_ID': colum1[0], 
                            'Nombre del curso':colum1[1],
                            'Departamento': colum1[2],
                            'Cupos ocupados': colum1[3],
                            'Cupos disponibles': colum1[4],
                            'Cupo maximo':colum1[5],
                            'Estado':colum1[6],
                            'Fecha de cierre':colum1[7]})
except FileNotFoundError:
    with open("cursos.csv", "w",newline="") as archivo1:
        escri = csv.writer(archivo1)
        escri.writerow(['Course_ID','Course_Name','Department','Occupied_Places','Available_Places','Max_Places','Status','Close_Date'])

# 2.3 Open 'inscripciones.csv' file

regist= []   # create a list to store dictionaries with the data of the file

#Use try/except to validate the existence of the file 'usuarios.csv' or create a new file with that name and the headers
try:
    with open('inscripciones.csv', "r", encoding="utf-8") as archivo2:
        next(archivo2) #Skip headers
        for i in archivo2:
            i= i.strip("\n")
            colum2 = i.split(',')
            regist.append({'Inscripción_ID': colum2[0], 
                            'Nombre del usuario':colum2[1],
                            'Curso_ID': colum2[2],
                            'Nombre del curso': colum2[3],
                            'Fecha de inscripción': colum2[4],
                            'Cantidad de cursos del usuario':colum2[5]})
except FileNotFoundError:
    with open("inscripciones.csv", "w",newline="") as archivo2: 
        escri = csv.writer(archivo2)
        escri.writerow(['Regist_ID','User_Name','Course_ID','Course_Name','Regist_Date','No_Courses'])

# 2.4 Open 'config.json' file
config= []
try:
    with open("config.json", "r", encoding="utf-8") as f1:
        config = json.load(f1)
except FileNotFoundError:
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump([], f, indent=1)

# 3. Login system

def login():

    #Create a list that contains lists with every user and password of the file
    user_pass =[]
    for i in users:
        user_pass.append([i['Usuario'],i['Contrasena']])

    acceso='no'
    cont=0
    
    # This loop asks the user name and password, and verifies if they are correct both, if not you have 3 opportunities to enter the correct answer
    while True:
        user_name=input('Introduce el usuario: ').lower()
        password=input('Introduce la contraseña: ')
        cont= cont+1  #sum 1 every repeated loop
        valide= 'no'

        for i in user_pass:
            if i[0]==user_name and i[1]==password: 
                valide='si'
                acceso='si'
                break
        if valide=='no':
            print('\nContraseña o Usuario Incorrecto, Intentalo de nuevo\n')
        elif valide=='si':
            print('Has accedido al sistema')
            break
        
        #Verifies if the loop has been done 3 times, if yes log out the user
        if cont>=3:
            print('\nAlcanzaste el Máximo de Intentos Permitidos\nAhorra se cerrará el programa, Regresa Pronto!')
            break
    return acceso, user_name

# 4. Main Menu

def menu(users,courses,regist):
    print('----------------------------------------------------')
    print('♦♦♦ BIENVENIDO AL SISTEMA DE GESTIÓN COURSETRACK ♦♦♦')
    print('----------------------------------------------------')
    acceso, user_name= login()

    if acceso=='no':
        print('No tienes acceso')
    elif acceso=='si':
        type_user= ''
        for i in users:
            if i['Usuario']==user_name:
                type_user= i['Rol']

        if type_user == 'ADMIN':
            print('\n----Bienvenido adminstrador---')
            while True:
                print('\nSelecciona una opción:\n1.Gestión de cursos\n2.Gestión de inscripciones\n3.Consulta Historial\n4.Reportes\n5.Salir\n>>>')
                while True: 
                    try:
                        option= abs(int(input('Seleccione la acción que desea realizar: ')))
                        break
                    except ValueError:
                        print('¡ERROR! Porfavor inserte una opción correcta (1-4)')
                if option==1:
                    print('\nOpción 1: Gestión de cursos')
                    print('\nSelecciona una opción:\n1.Añadir curso\n2.Mostrar cursos\n3.Borrar Cursos\n4.Actualizar cursos\n>>>')
                    while True:    
                        while True: 
                            try:
                                option1= abs(int(input('Seleccione la acción que desea realizar: ')))
                                break
                            except ValueError:
                                print('¡ERROR! Porfavor inserte una opción correcta (1-4)')
                        if option1 == 1:
                            gc.add_new(courses)
                            break
                        if option1 == 2:
                            gc.show_courses(courses)
                            break
                        if option1 == 3:
                            gc.courses_delete(courses)
                            break
                        if option1 == 4:
                            gc.update_course(courses,regist)
                            break
                        else:
                            print('No tenemos esa opción, vuelve a intentarlo')


                elif option==2:
                    print('\nOpción 2: Gestión de inscripciones')
                    print('\nSelecciona una opción:\n1.Añadir inscripción\n2.Mostrar inscripciones\n3.Borrar Inscripción\n>>>')
                    while True:    
                        while True: 
                            try:
                                option2= abs(int(input('Seleccione la acción que desea realizar: ')))
                                break
                            except ValueError:
                                print('¡ERROR! Porfavor inserte una opción correcta (1-3)')
                        if option2 == 1:
                            gi.add_regist(user_name,users,courses,regist)
                            break
                        if option2 == 2:
                            gi.show_regist(users,courses,regist)
                            break
                        if option2 == 3:
                            gi.regist_delete(users,courses,regist)
                            break
                        else:
                            print('No tenemos esa opción, vuelve a intentarlo')              
                elif option==3:
                    print('\nOpción 3: Consulta historial')
                    print('\nSelecciona una opción:\n1.Consulta por curso\n2.Consulta por usuario\n>>>')
                    while True:    
                        while True: 
                            try:
                                option3= abs(int(input('Seleccione la acción que desea realizar: ')))
                                break
                            except ValueError:
                                print('¡ERROR! Porfavor inserte una opción correcta (1-2)')
                        if option3 == 1:
                            cs.history_course(regist)
                            break
                        if option3 == 2:
                            cs.history_user(regist)
                            break
                        else:
                            print('No tenemos esa opción, vuelve a intentarlo')

                elif option==4:
                    print('\nOpción 4: Reportes')
                    cs.report(users,courses,regist)

                elif option==5:
                    print('\nOpción 5: Salir')
                    print('▬▬▬▬▬▬¡Vuelve pronto!▬▬▬▬▬▬')
                    break

                else:
                    print('No tenemos esa opción, vuelve a intentarlo')

        elif type_user =='STUDENT':
            print('\n----Bienvenido estudiante---')
            while True:
                print('\nSelecciona una opción:\n1.Gestión de cursos\n2.Gestión de inscripciones\n3.Salir\n>>>')
                while True: 
                    try:
                        option= abs(int(input('Seleccione la acción que desea realizar: ')))
                        break
                    except ValueError:
                        print('¡ERROR! Porfavor inserte una opción correcta (1-4)')
                if option==1:
                    print('\nOpción 1: Gestión de cursos')
                    print('\nSelecciona una opción:\n1.Mostrar cursos>>>')
                    while True:    
                        while True: 
                            try:
                                option1= abs(int(input('Seleccione la acción que desea realizar: ')))
                                break
                            except ValueError:
                                print('¡ERROR! Porfavor inserte una opción correcta (1)')
                        if option1 == 1:
                            gc.show_courses(courses)
                            break
                        else:
                            print('No tenemos esa opción, vuelve a intentarlo')

                elif option==2:
                    print('\nOpción 2: Gestión de inscripciones')
                    print('\nSelecciona una opción:\n1.Añadir inscripción\n>>>')
                    while True:    
                        while True: 
                            try:
                                option2= abs(int(input('Seleccione la acción que desea realizar: ')))
                                break
                            except ValueError:
                                print('¡ERROR! Porfavor inserte una opción correcta (1)')
                        if option2 == 1:
                            gi.add_regist(user_name,users,courses,regist)
                            break
                        else:
                            print('No tenemos esa opción, vuelve a intentarlo')              
                elif option==3:
                    print('\nOpción 3: Salir')
                    print('▬▬▬▬▬▬¡Vuelve pronto!▬▬▬▬▬▬')
                    break

                else:
                    print('No tenemos esa opción, vuelve a intentarlo')
        else:
            print('Tipo de usuario no identificado, Vuelve a intentarlo desde el inicio')

menu(users,courses,regist)
