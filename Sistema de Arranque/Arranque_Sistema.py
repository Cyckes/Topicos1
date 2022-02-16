# -*- coding: utf-8 -*-
#Ervis Alain [8-938-73]
#Daniella Ramos [8-938-1528]
#Harold Torres [8-943-2153]


import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Interfaz import MainWindow
import ply.lex as lex
import ply.yacc as yacc
import random

disponibilidad=False
class Arranque_Sistema(QMainWindow):
    global disponibilidad, ver
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.ui.ejecutar.clicked.connect(self.calcular)
        self.ui.txtestado.setText("** Apagado ** " )
        self.show()
        
    
    def calcular(self):
        global disponibilidad,ver

        #variable auxiliar para las funciones
        tokens = ['ESTADO', 'SOLICITUD', 'REINICIOS', 'NAME']
        
        #Reglas para las regex
        t_ignore = ' \t' #espacios y TABS
        
        #Para el estado del encendido
        def t_ESTADO(t):
            r'PasoConfirmado|PasoRechazado'
            t.type = 'ESTADO'
            return t
        
        #Para la solicitud
        def t_SOLICITUD(t):
            r'Encender|Apagar'
            t.type = 'SOLICITUD'
            return t
        #Para la cantidad de reinicios
        def t_REINICIOS(t):
            r'[0-9]'
            t.type = 'REINICIOS'
            return t
        #Para el nombre del usuario
        def t_NAME(t):
            r'[a-zA-Z_][a-zA-Z_0-9]*'
            t.type = 'NAME'
            return t
        
        
        def t_error(t):
            self.ui.txtsalida.setText("Carácter Ilegal '%s'" % t.value)
            t.lexer.skip(1)
            
            
        #Construir el lexer
        lex.lex()
        
        def p_Iniciar(p):
            #Creación de reglas
            """ 
            todo : expression
                 | empty
            """
            run(p[1])
        
        #Para líneas vacías
        def p_empty(p):
            """
            empty :
            """
            p[0] = None
            
        
        #Solicitud del usuario
        def p_solicitud(p):
            'expression : SOLICITUD'
            p[0] = p[1]
            
        #Para la cantidad de Reinicio
        def p_Reiniciar(p):
            'expression : REINICIOS'
            p[0] = p[1]
                    
        #Para el estado del encendido
        def p_estado(p):
            'expression : ESTADO'
            p[0] = p[1]
            
        #Nombre del Usuario
        def p_expname(p):
            '''expression : NAME
            '''
            try:
                p[0] = p[1]
            except LookupError:
                print(f"Undefined name {p[1]!r}")
                p[0] = 0
                
                
        def p_error(p):
            print(f"Syntax error at {p.value!r}")        
                
        #Construcción del parse
        parser = yacc.yacc()
        
        
        def run(p):
            global disponibilidad,ver
            
            encendido=False #Asignación por defecto
            resultado="" # Contiene el resultado de la ejecución
            
            try:
                encendido=disponibilidad # Asignar si esta encendida
            except NameError:
                pass
                
            
            #Primera validación
            if p=='Encender':
                
                pasos=['Prueba de Auto-Encendido', 
                       'Encuentra un Dispositivo de Arranque', 
                       'Cargando Sistema Operativo',
                       'Control de transferencia al SO']
                #Iniciar la cantidad de reinicios
                cant_reiniciar=0
                verificar=False
                
                # Validad si el sistema no esta encendido 
                # Si no esta encendido realiza el proceso de encendido
                if (encendido==False):
                    #Verificar hasta que el pc encienda
                    while (encendido!=True):
                        #variable que control el arreglo de los pasos
                        i=0
                        if(verificar==True):
                            cant_reiniciar+=1
                            resultado=resultado+ 'Error Reiniciando... \n'
                        verificar=True
                        #Si se obtiene un valor mayor a 3 el paso es valido
                        while (random.randint(1,20)>3 and i<=len(pasos)-1):
                                resultado= resultado +'Paso '+ str(i+1) + ' * ' + pasos[i] + ' *  exitoso \n'
                                i+=1
                        #Si todos los paso estan completado 
                        if(i==len(pasos)):
                            resultado= resultado + ' Cantidad de reinicios: ' + str(cant_reiniciar) + ' \n'
                            resultado= resultado + ' Encendido del dispositivo completado satisfactoriamente\n'
                            encendido=True
                            disponibilidad=True
                        #Error encontrado en el arranque del dispositivo
                        elif(i<=len(pasos)):
                                resultado=resultado +'Paso '+ str(i+1) + ' * ' + pasos[i] + ' *  fallido \n'
                    self.ui.txtsalida.setText(resultado)
                    
                    #Por si el sistema esta encendido
                else:
                    self.ui.txtsalida.setText("El equipo se encuentra encendido")

                if (disponibilidad==True):
                    ver="Encendido.png"
                    self.mostrar()
                    self.ui.txtestado.setText("** Encendido **")
                        
                elif(disponibilidad==False): 
                    ver="Apagado.png"
                    self.mostrar()  
                    self.ui.txtestado.setText("** Apagado **")
                    
            # Segunda Validación
            elif p == 'Apagar':
                #Verificar si el equipo esta encendido para apagarlo
                if encendido==True:
                    disponibilidad=False
                    self.ui.txtsalida.setText("El equipo se ha detenido * Aceptado *")
               
                #Si el equipo se encuentra Apagado   
                else:
                    self.ui.txtsalida.setText("El equipo ya esta apagado * Denegado *")

                if (disponibilidad==True):
                    ver="Encendido.png"
                    self.mostrar()
                    self.ui.txtestado.setText("** Encendido **")
                    
                elif(disponibilidad==False): 
                    ver="Apagado.png"
                    self.mostrar()
                    self.ui.txtestado.setText("** Apagado **")
            else:
                self.ui.txtsalida.setText("Entrada no aceptada intente con: \n - Encender \n - Apagar")
        
        s = self.ui.txtentrada.toPlainText()
        parser.parse(s)
        
        
        
    def mostrar(self):
        global ver
        pixmap = QtGui.QPixmap(ver) # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.ui.imagen.width(), self.ui.imagen.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.ui.imagen.setPixmap(pixmap) # Set the pixmap onto the label
        self.ui.imagen.setAlignment(QtCore.Qt.AlignCenter) # Align the label to cente
        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Arranque_Sistema()
    ventana.show()
    sys.exit(app.exec_())