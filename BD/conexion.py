import mysql.connector
from mysql.connector import Error

#class
class DAO():
    #Constructor
    def __init__(self):
        
        try:
            self.conexion= mysql.connector.connect(
                host= 'localhost',
                port= '3306',
                user= 'root',
                password = '',
                db= 'universidad'
            )
        except Error as ex:
            print("Error al intentar conexion: {0}".format(ex))
#fin de la class
    def listarCursos(self):
        if self.conexion.cursor():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY Nombre ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar conectar: {0}".format(ex))

    def registrarCursos(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', '{2}')"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("Curso registrado \n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    def actualizarCurso(self,curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET Nombre = '{0}',Creditos = '{1}' WHERE Codigo = '{2}'"
                cursor.execute(sql.format(curso[1],curso[2], curso[0]))
                self.conexion.commit()
                print("Curso Actualizado \n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))


    def eliminarCurso(self, codigoCursoEmiminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEmiminar))
                self.conexion.commit()
                print("Curso eliminado \n")

            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))













