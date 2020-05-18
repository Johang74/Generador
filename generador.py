#Johan David Gomez Gil
# Lenguajes 2 
#2020

import random
import pymysql

nombre = ['MARIA','MARIA CARMEN','JOSEFA','ISABEL','MARIA DOLORES','CARMEN',
'FRANCISCA','MARIA PILAR','DOLORES','MARIA JOSE','ANTONIA','ANA','MARIA ISABEL',
'MARIA ANGELES','PILAR','ANA MARIA','LUCIA','CRISTINA','LAURA','ENCARNACION','JUANA','MARIA TERESA','ROSARIO','ELENA','MARTA',
'MANUELA','ROSA MARIA','MARIA LLANOS','MARIA JOSEFA','RAQUEL','ANGELES','CONCEPCION','MERCEDES','IRENE','TERESA','BEATRIZ',
'PAULA','ANGELA','JULIA','ANA BELEN','ROCIO','AMPARO','ALICIA','CONSUELO','ROSA','ASCENSION','ANDREA',
'MARIA ROSARIO','MARIA JESUS','MARIA LUISA','ANTONIO','JOSE','FRANCISCO','JUAN','MANUEL','PEDRO','JESUS','ANGEL','MIGUEL','JAVIER','JOSE ANTONIO','DAVID',
'CARLOS','JOSE LUIS','ALEJANDRO','MIGUEL ANGEL','FRANCISCO JAVIER','RAFAEL','DANIEL',
'JUAN JOSE','LUIS','PABLO','JUAN ANTONIO','JOAQUIN','SERGIO','FERNANDO', 
'JUAN CARLOS','ANDRES','JOSE MANUEL','JOSE MARIA','RAMON','RAUL','ALBERTO','ENRIQUE','ALVARO','VICENTE',
'EMILIO','FRANCISCO JOSE','DIEGO','JULIAN','JORGE','ALFONSO','ADRIAN', 
'RUBEN','SANTIAGO','IVAN','JUAN MANUEL','PASCUAL','JOSE MIGUEL','MARIO']

apellido = ['MARTINEZ','LOPEZ','SANCHEZ','GONZALEZ','GOMEZ',
'FERNANDEZ','MORENO','JIMENEZ','PEREZ','RODRIGUEZ',
'NAVARRO','RUIZ','DIAZ','SERRANO','HERNANDEZ','MUÑOZ','SAEZ','ROMERO',
'RUBIO','ALFARO','MOLINA','LOZANO','CASTILLO','PICAZO','ORTEGA','MORCILLO',
'CANO','MARIN','CUENCA','GARRIDO','TORRES','CORCOLES','GIL',
'ORTIZ','CALERO','VALERO','CEBRIAN','RODENAS','ALARCON','BLAZQUEZ','NUÑEZ',
'PARDO','MOYA','TEBAR','REQUENA','ARENAS','BALLESTEROS','COLLADO','RAMIREZ',
'VALENCIA']

ciudad = ['Medellín','Abejorral','Abriaquí','Alejandría','Amalfi','Andes','Angelópolis','Angostura',
'Carolina','Caucasia','Chigorodó','Bello','Sabaneta','Barbosa','Copacabana','Dabeiba','Dabeiba','El Bagre',
'Gomez Plata','Girardota','Guadalupe','Guarne',
'Guatape', 'Itagui','Ituango','Jericó','La Unión','La Estrella','La Ceja','Rionegro','Sabanalarga',
'Sabaneta','Santo Domingo', 'Segovia','Taraza','Valdivia','Yarumal','Barranquilla','Sabanalarga']

profesion = ['Actor','Medico','Abogado','Administrador','Antropólogo','Archivero','Arqueólogo','Arquitecto',
'Astrónomo','Atleta','Bacteriólogo','Barrendero','Bibliotecario','Biofísico','Bombero','Botánico',
'Camarero','Cancerólogo','Cardiólogo','Carnicero','Carpintero','Cocinero','Decorador','Odontologo',
'Dermatólogo','Dibujante','Economista','Electricista','Enfermero','Epidemiólogo','Estadista','Farmacéutico',
'Farmacólogo','Fiscal','Físico','Fisioterapeuta','Comerciante','Forense','Fotógrafo','Genetista','Geógrafo',
'Geriatra','Hepatólogo','Ingeniero','Inmunólogo','Juez','Matemático','Mecánico','Microcirujano','Modelo',
'Neumólogo','Neuroanatomista','Neurobiólogo','Neurólogo','Odontólogo','Oftalmólogo','Oncólogo','Panadero',
'Pediatra','Periodista','Piloto de avión','Programador','Psicólogo','Psiquiatra','Recepcionista','Soldado',
'Taxista','Terapeuta','Vendedor','Veterinario','Virólogo','Zoólogo','Zootécnico']

materia = ['Español','Ingles','Sociales','Matematicas','Tecnologia', 'Ed fisica', 'Filosofia',
'Ciencias politicas', 'Etica','Frances','Geografia','Historia','Politica','Dibujo tecnico',
'Artistica','Economia','Emprendimiento','Fisica','Quimica','Ecologia','Electronica','Estadistica',
'Programacion','Biologia','Italiano','Educacion musical','Agricultura basica',
'Ciencias naturales']

identificador = ['A','B','C','D','F','G','H','I','J','K']

#---------------------Datos del paciente-----------------------------------------------------------

def generarNombre():
    nombre =""
    nom = random.choice(apellido)
    nom2 = random.choice(apellido)
    nombre = nom + " " + nom2 
    return str(nombre)

def generarApellidos():
    ape = ""
    nom = random.choice(apellido)
    nom2 = random.choice(apellido)
    ape = nom + " " + nom2 
    return str(ape)



def generarNumDocumento():
    return int(random.randint(100, 999999))

def generarDireccion():
    city = random.choice(ciudad)
    carrera = random.randint(5, 90)
    calle = random.randint(5, 90)
    casa = random.randint(5, 90)
    barrio = ""
    
    barrio = city + " " +"Cra " + str(carrera) + " # " + str(calle) + "-" + str(casa)
    return str(barrio)

def generarGrado():
    return random.randint(0,11)

def generarNombreActividad():
    return str(random.choice(profesion))

def generarDescripcionActividad():
    ac = random.randint(167100,999999)
    desc = ""
    desc = "Hacer los siguiente: " + str(ac)
    return str(desc)

def generarMateria():
    return str(random.choice(materia))

def generarIdentificador():
    return str(random.choice(identificador))



#--------------------------------------LLENAR LA BD-------------------------------------------   



def llenarBD(cantidad):
    i = 0
    while i < cantidad :
        try:
            db = pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                db = 'colegio'
            )

            cursor = db.cursor()

            documentoEs = generarNumDocumento()

            estudiante =[documentoEs, generarNombre(),generarApellidos(),generarDireccion()]
            cursor.execute("INSERT INTO estudiante VALUES (%s,%s,%s,%s)",estudiante)

            documentoAcu = generarNumDocumento()
            acudiente = [documentoAcu, generarNombre(),generarApellidos(),generarDireccion()]
            cursor.execute("INSERT INTO acudiente VALUES (%s,%s,%s,%s)",acudiente)

            documentoDoc = generarNumDocumento()
            docente = [documentoDoc,generarNombre(),generarApellidos(),generarDireccion()]
            cursor.execute("INSERT INTO docente VALUES (%s,%s,%s,%s)",docente)

            actividad = [generarNombreActividad(),generarDescripcionActividad()]
            cursor.execute("INSERT INTO actividad VALUES (NULL,%s,%s)",actividad)

            materia = generarMateria()
            cursor.execute("INSERT INTO materia VALUES (NULL,%s)",materia)

            grupo = [generarGrado(),generarIdentificador()]
            cursor.execute("INSERT INTO grupo VALUES (NULL,%s,%s)",grupo)

            estudianteAcudiente = [documentoEs,documentoAcu]
            cursor.execute("INSERT INTO estudianteacudiente VALUES (%s,%s)",estudianteAcudiente)

            cursor.execute("SELECT id FROM materia WHERE nombre = %s",materia)
            idmateria = cursor.fetchone()

            cursor.execute("INSERT INTO docentemateria VALUES(%s,%s)",(documentoDoc, idmateria[0]))

            #db.commit() 

            cursor.execute("SELECT COUNT(id) FROM grupo")
            cantGrupos = cursor.fetchone()

            cursor.execute("SELECT COUNT(id) FROM actividad")
            cantActividades = cursor.fetchone()
            
            cursor.execute("SELECT COUNT(id) FROM materia")
            cantMaterias = cursor.fetchone()


            idGrupo = random.randint(1,cantGrupos[0])
            idActividad = random.randint(1,cantActividades[0])
            idMat = random.randint(1,cantMaterias[0])
            nota = random.randint(0,10)
            
            cursor.execute("INSERT INTO grupoactividad VALUES(%s,%s)",(idGrupo,idActividad))
            cursor.execute("INSERT INTO estudianteactividadnota VALUES(%s,%s,%s)",(documentoEs,idActividad,nota))
            cursor.execute("INSERT INTO actividadmateria VALUES(%s,%s)",(idActividad,idMat))


            db.commit() 
            print ("Operacion realizada")
            cursor.execute("SELECT COUNT(id) FROM estudiante")
            cant =cursor.fetchone()
            print (cant[0])
            i = i+1

        except pymysql.OperationalError as errorSQL:
            print("Error ejecutando comando: ",errorSQL)
        finally:
            db.close()
