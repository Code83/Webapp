import psycopg2

conexion = psycopg2.connect(database="postgres",user="postgres",password="admin")
cursor1 = conexion.cursor()

#Instruccion para insertar
sql_insert="insert into usuarios (nombre, apellidopat, apellidomat, rut, email) values (%s,%s,%s,%s,%s)"
#instruccion para validar usuarios
sql_crea_reserva="insert into ocupados values (%s, %s)"
#insetruccion para borrar por rut
sql_del_reserva = "delete from ocupados where patente = '%s';"
#instruccion para crear los vehiculos
sql_creaAuto="insert into autos (marca,modelo,disponible, patente) values (%s,%s,%s,%s)"
#actualizamos datos de autos
sql4="update autos set kms = %s where patente =%s"
#Obtiene reservas
sql_ver_reserva="select * from ocupados;"
#Elimina usuarios
sql_del_user="delete from usuarios where rut = %s"
#Ver usuarios creados
sql_ver_user="select * from usuarios"

#Definimos funcion para insertar datos en BD
#Se reciben los datos a insertar en la variable datos

def elimina_users(rut):
    cursor1.execute(sql_del_user,(rut,))
    print("Usuario eliminado ")
    conexion.commit()
    conexion.close()

def inserta(datos):
    if rut == '':
        print("rut obligatorio, no se inserta registro")
    else:
        
        cursor1.execute(sql_insert,datos)

        conexion.commit()
        conexion.close()
        print("Ingreso de datos OK")

def consulta_reservas():
    cursor1.execute(sql_ver_reserva)
    for fila in cursor1:
        print(fila)
    conexion.close()

def crea_reserva(v_crea):

    cursor1.execute(sql_crea_reserva,v_crea)
    print("Reserva creada!")
    conexion.commit()
    conexion.close()

def del_reserva(v_del):
    cursor1.execute(sql_del_reserva,v_del)
    print("Reserva eliminada!")
    conexion.commit()
    conexion.close()    

def consulta_usuarios():
    cursor1.execute(sql_ver_user)
    for fila in cursor1:
        print(fila)
    conexion.close()


def creaauto(datosauto):
    cursor1.execute(sql_creaAuto,datosauto)   
    print("Ingreso OK")
    conexion.commit()
    conexion.close()

menu = int(input("""***** Ingresa una opcion *****
                    1.-Ingresar usuario NUEVO
                    2.-Ingresar Vehiculo NUEVO
                    3.-Crea reserva
                    4.-Elimina reserva
                    5.-Ver reservas
                    6.-Eliminar usuarios registrados
                    7.-Ver usuarios creados
                    0.-Salir : """))
#while True:
if menu == 1:
    nombre = input("Ingresa tu nombre: ")
    apepat = input("Ingresa tu apellido paterno: ")
    apemat = input("ingresa tu apellido materno: ")
    rut = input("Ingresa tu rut: ")
    email = input("Ingresa email: ")

    datos = (nombre,apepat,apemat,rut,email)
    inserta(datos)

elif menu == 2:
    marca = input("Ingresa la marca del vehiculo: ")
    patente = input("Ingresa patente: ")
    #kms = int(input("KMS recorridos: "))
    #anofab = int(input("Año de fabricacion: "))
    disponible = input("Disponible? SI/NO: ")
    modelo = input("Modelo: ")
    
    datosauto = (marca,modelo,disponible,patente) 
    creaauto(datosauto)

elif menu==3:
    patente = input("ingresa patente a reservar: ")
    rut = input("ingresa el rut que reserva: ")
    v_crea = (patente, rut)

    crea_reserva(v_crea)


elif menu==4:
    patente = input("Ingresa patente a eliminar: ")
    v_del = patente

    del_reserva(patente)

elif menu==5:
    consulta_reservas()

elif menu==6:
    rut = str(input("Ingresa el RUT del usuario a eliminar: "))
    print ("Se eliminara el usuario rut {0}.".format(rut))
    elimina_users(rut)

elif menu==7:
    consulta_usuarios()

else:
    print("ADIOS")
    #break