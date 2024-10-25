from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
import sys
import conexion


#funciones para la accion de los botones
def agregar():
    nombres=ventana.lineEdit_2.text()
    correo=ventana.lineEdit_3.text()
    print(nombres,correo)
    objContactos=conexion.contactos()
    contactos=objContactos.crearContacto((nombres,correo))
    consultar()


def consultar():#mostrar la db en la tabla
    ventana.tblContactos.setRowCount(0)
    indiceControl=0
    objContactos=conexion.contactos()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        indiceControl+=1 

def eliminar():
    print("Hola soy la acción de eliminar")
    id=ventana.lineEdit.text()
    objContactos=conexion.contactos() 
    contactos=objContactos.borrarContacto(id)
    consultar()

def modificar():
    if validarCampos():
        return False
    print("Hola soy la acción de modificar")
    id= ventana.lineEdit.text()
    nombres= ventana.lineEdit_2.text() 
    correo= ventana.lineEdit_3.text()

    objContactos=conexion.contactos() 
    contactos=objContactos.modificarContacto((nombres,correo,id)) 
    consultar()      

    
def Cancelar():
    print("Accion Cancelar")
 
def validarCampos():
    nombre = ventana.lineEdit_2.text()
    correo = ventana.lineEdit_3.text()
    if not nombre or not correo:
        QMessageBox.warning(ventana, "Advertencia", "Por favor, complete todos los campos.")
        return True
    return False

#termina funcion de los botones

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()
consultar()

#Poner encabezado a la tabla 
ventana.tblContactos.setHorizontalHeaderLabels(['ID', 'NOMBRE', 'CORREO'])

#accion en los botones
ventana.btnadd.clicked.connect(agregar)
ventana.btnmodific.clicked.connect(modificar)
ventana.btndelete.clicked.connect(eliminar)
ventana.btncancel.clicked.connect(Cancelar)


sys.exit(aplicacion.exec())
