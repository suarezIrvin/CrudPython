import sqlite3
from sqlite3.dbapi2 import connect

#conexion de la base de datos
class contactos:
    def iniciarConexion(self):
        conexion=sqlite3.connect('sistema.s3db')
        return conexion
        
    def leerContactos(self):
         conexion=self.iniciarConexion()
         cursor=conexion.cursor()
         sentenciaSQL="SELECT * FROM contactos"
         cursor.execute(sentenciaSQL)
         return cursor.fetchall()
    
    def crearContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentenciaSQL="INSERT INTO contactos(nombres,correo) VALUES(?,?)"
        cursor.execute(sentenciaSQL,datosContacto)
        conexion.commit()
        conexion.close() 
    
    def borrarContacto(self,idContacto):
      conexion=self.iniciarConexion()
      cursor= conexion.cursor()
      sentencialSQL="DELETE FROM contactos WHERE id=(?)" 
      cursor.execute(sentencialSQL,[idContacto]) 
      conexion.commit()
      conexion.close()

    def modificarContacto(self,datosContacto): 
      conexion=self.iniciarConexion()
      cursor= conexion.cursor()
      sentencialSQL="UPDATE contactos SET nombres=? ,correo=? WHERE id=?" 
      cursor.execute(sentencialSQL,datosContacto)
      conexion.commit()
      conexion.close()