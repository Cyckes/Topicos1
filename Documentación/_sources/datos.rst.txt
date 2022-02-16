INTEGRANTES
***********
Universidad Tecnológica de Panamá.

Licenciatura en Ingeniería de Sistemas y Computación.

Proyecto Final de Tópicos Especiales I y Lenguajes Formales, Autómatas y Compiladores.

ERVIS ALAIN
=====================
Cédula: 8-938-73

Correo: ervis.alain@utp.ac.pa

DANIELLA RAMOS
==========================
Cédula: 8-938-1528

correo: daniella.ramos@utp.ac.pa

HAROLD TORRES
=========================
Cédula: 8-943-2153

correo: harold.torres@utp.ac.pa


MEDIDOR DE TEMPERATURA AUTOMÁTICO CON REGLAS LÉXICAS Y SINTÁCTICAS EN PLY
*************************************************************************

Este termometro permite medir la temperatura de las personas en un rango
de 5-10 cm, donde no se necesita una persona que manipule el termometro.
Posee una pantalla que muestra la temperatura y emite una alarma si se
detecta un nivel alto de temperatura.
Se considera temperatura elevada por encima de los 37°C.

A continuación se presenta el listado de tokens que se tomaron en cuenta
para armar las reglas léxicas.


Listado de TOKENS
=================

1. DISTANCIA: referencia a el comando "distancia número" que se introduce para saber la distancia entre la persona y el termometro.
2. ENTERO: referencia a un número de tipo int como entrada.
3. FLOTANTE: referencia a un número de tipo float como entrada.

Listado de Reglas Léxicas
=========================

Ignora carácteres de espacios
-----------------------------
.. code-block:: python

   t_ignore = ' \t'

Returna el Token DISTANCIA
--------------------------
.. code-block:: python

   def t_DISTANCIA(t):
       r'distancia'
       t.value = "DISTANCIA"
       return t

Returna el número convertido en tipo flotante
---------------------------------------------
.. code-block:: python

   def t_FLOTANTE(t):
       r'\d+\.\d+'
       t.value = float(t.value)
       return t

Returna el número convertido en tipo entero
-------------------------------------------
.. code-block:: python

   def t_ENTERO(t):
       r'\d+'
       t.value = int(t.value)
       return t

Verifica los saltos de línea
----------------------------
.. code-block:: python

   def t_newline(t):
       r'\n+'
       t.lexer.lineno += len(t.value)

Verifica los carácteres no permitidos
-------------------------------------
.. code-block:: python

   def t_error(t):
       print("Carácter Ilegal '%s'" % t.value[0])
       t.lexer.skip(1)


Listado de Reglas Sintácticas
=============================

Ejecuta el primer comando para posteriormente derivarlas en una expresión o vacío
---------------------------------------------------------------------------------
.. code-block:: python

   def p_comandos(p):
       #Creando las reglas
       """
       comandos : expresion
                | empty
       """
       self.ui.txtSalida.setText(str(run(p[1])))

Deriva la expresión en base al token DISTANCIA con un número
------------------------------------------------------------
.. code-block:: python

   def p_expresion(p):
       """
       expresion : DISTANCIA numero      
       """
       p[0] = (p[1], p[2])  
              

Deriva los números en tipo entero y flotante
--------------------------------------------
.. code-block:: python

   def p_expresion_int_float(p):
       """
       numero : ENTERO
              | FLOTANTE
       """
       p[0] = p[1]


Evalua errores de escritura
---------------------------
.. code-block:: python

   def p_error(p):
       self.ui.txtSalida.setText("Error de sintaxis!")

Corresponde a los comandos vacíos
---------------------------------
.. code-block:: python

   def p_empty(p):
       """
       empty :
       """
       p[0] = None


Código
======
Código creado para el programa:

Imports utilizados
------------------
Módulos empleados:

.. code-block:: python

   import sys
   from PyQt5.QtWidgets import QApplication, QMainWindow
   from PyQt5.QtGui import QPixmap
   import random

Dentro de GUI se encuentra el diseño de la gui utilizada.

.. code-block:: python

   from GUI import MainWindow

Se utilizó PLY para la creación del lexer y el parser.

.. code-block:: python

   import ply.lex as lex
   import ply.yacc as yacc

Clase GUIApplication
--------------------
Se creó la clase GUIApplication para enlazar con la interfaz creada

.. code-block:: python

   class GUIApplication(QMainWindow):

Función __init__
-----------------
En esta función se inicia y conecta con el botón "ejecutar" para ejecutar el
comando. También se carga la imagen de estado "encendido".

.. code-block:: python

   def __init__(self):
       super().__init__()
       self.ui = MainWindow()
       self.ui.setupUi(self)
       self.ui.botonEjecutar.clicked.connect(self.ejecutar)
       pixmap = QPixmap("on.png")
       self.ui.labelEstado.setPixmap(QPixmap(pixmap))
       self.show()

Función run
-----------
Comprueba el comando "distancia" de entrada y verifica la distancia y temperatura
medida.

.. code-block:: python

   def run(p):
       cadena = ""
       if (type(p) == tuple):
           if (p[0] == "DISTANCIA"):
               if (p[1] > 10):
                   return("ACÉRQUESE MÁS PARA PODER TOMAR LA TEMPERATURA")
               else:
                   cadena+=("DISTANCIA ADECUADA")
                   cerca = True
                   if (cerca):
                       temp = round(random.uniform(29,40),2)
                       if (temp > 37):
                           return(cadena+"\nTOMANDO TEMPERATURA"+"\nTEMPERATURA MEDIDA = "+str(temp)+
                                       "\nALARMA ACTIVADA, TEMPERATURA ALTA DETECTADA")
                       elif (temp < 37):
                             return(cadena+"\nTOMANDO TEMPERATURA"+"\nTEMPERATURA MEDIDA = "+str(temp)+
                                       "\nTEMPERATURA NORMAL")
       else:
           return p
    
Entrada de comandos
-------------------
Se ingresa el comando "distancia número" o "apagar". Para medir la temperatura
y apagar el termometro respectivamente

.. code-block:: python

   s = self.ui.txtEntrada.toPlainText()
   self.ui.txtEntrada.setText("")
   if(s.upper()=="APAGAR"):
      self.ui.txtSalida.setText("MEDIDOR DE TEMPERATURA APAGADO")
      pixmap = QPixmap("off.png")
      self.ui.labelEstado.setPixmap(QPixmap(pixmap))
    else:
        pixmap = QPixmap("on.png")
        self.ui.labelEstado.setPixmap(QPixmap(pixmap))
        parser.parse(s)

Lexer
------
El lexer escanea la entrada y produce los tokens correspondientes. 

Construcción del lexer:
.. code-block:: python

   lexer = lex.lex()

Parser
--------
El parser analiza los tokens y produce el resultado del análisis (Reglas sintácticas).

A continuación, se presentará la construcción del parser:
.. code-block:: python

   parser = yacc.yacc(debug=True)

Código de la interfaz gráfica
-----------------------------

.. code-block:: python

   from PyQt5 import QtCore, QtGui, QtWidgets


   class MainWindow(object):
       def setupUi(self, MainWindow):
           MainWindow.setObjectName("MainWindow")
           MainWindow.resize(448, 654)
           icon = QtGui.QIcon()
           icon.addPixmap(QtGui.QPixmap("pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           MainWindow.setWindowIcon(icon)
           MainWindow.setStyleSheet("background-color: rgb(0, 113, 168);")
           MainWindow.setIconSize(QtCore.QSize(40, 40))
           self.centralwidget = QtWidgets.QWidget(MainWindow)
           self.centralwidget.setObjectName("centralwidget")
           self.label = QtWidgets.QLabel(self.centralwidget)
           self.label.setGeometry(QtCore.QRect(190, 40, 81, 41))
           self.label.setObjectName("label")
           self.label_2 = QtWidgets.QLabel(self.centralwidget)
           self.label_2.setGeometry(QtCore.QRect(170, 220, 111, 31))
           self.label_2.setObjectName("label_2")
           self.txtSalida = QtWidgets.QTextEdit(self.centralwidget)
           self.txtSalida.setGeometry(QtCore.QRect(70, 270, 331, 271))
           font = QtGui.QFont()
           font.setPointSize(10)
           font.setBold(True)
           font.setWeight(75)
           self.txtSalida.setFont(font)
           self.txtSalida.setStyleSheet("background-color: rgb(255, 245, 238);")
           self.txtSalida.setFrameShape(QtWidgets.QFrame.StyledPanel)
           self.txtSalida.setReadOnly(True)
           self.txtSalida.setObjectName("txtSalida")
           self.txtEntrada = QtWidgets.QTextEdit(self.centralwidget)
           self.txtEntrada.setGeometry(QtCore.QRect(130, 100, 201, 51))
           font = QtGui.QFont()
           font.setPointSize(10)
           font.setBold(True)
           font.setWeight(75)
           self.txtEntrada.setFont(font)
           self.txtEntrada.setStyleSheet("background-color: rgb(255, 245, 238);")
           self.txtEntrada.setObjectName("txtEntrada")
           self.botonEjecutar = QtWidgets.QPushButton(self.centralwidget)
           self.botonEjecutar.setGeometry(QtCore.QRect(180, 170, 97, 29))
           font = QtGui.QFont()
           font.setBold(False)
           font.setWeight(50)
           self.botonEjecutar.setFont(font)
           self.botonEjecutar.setStyleSheet("background-color: rgb(255, 255, 255);")
           self.botonEjecutar.setObjectName("botonEjecutar")
           self.label_3 = QtWidgets.QLabel(self.centralwidget)
           self.label_3.setGeometry(QtCore.QRect(110, 580, 59, 17))
           self.label_3.setObjectName("label_3")
           self.labelEstado = QtWidgets.QLabel(self.centralwidget)
           self.labelEstado.setGeometry(QtCore.QRect(190, 560, 181, 61))
           self.labelEstado.setFrameShape(QtWidgets.QFrame.Box)
           self.labelEstado.setScaledContents(True)
           self.labelEstado.setObjectName("labelEstado")
           MainWindow.setCentralWidget(self.centralwidget)
           self.statusbar = QtWidgets.QStatusBar(MainWindow)
           self.statusbar.setObjectName("statusbar")
           MainWindow.setStatusBar(self.statusbar)

           self.retranslateUi(MainWindow)
           QtCore.QMetaObject.connectSlotsByName(MainWindow)

       def retranslateUi(self, MainWindow):
           _translate = QtCore.QCoreApplication.translate
           MainWindow.setWindowTitle(_translate("MainWindow", "Medidor de Temperatura Automático"))
           self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#f5973d;\">Entrada</span></p></body></html>"))
           self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#f5973d;\">Salida</span></p></body></html>"))
           self.txtEntrada.setToolTip(_translate("MainWindow", "Comando: \"distancia NÚMERO\""))
           self.botonEjecutar.setText(_translate("MainWindow", "Ejecutar"))
           self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Estado</span></p></body></html>"))
           self.labelEstado.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


   if __name__ == "__main__":
       import sys
       app = QtWidgets.QApplication(sys.argv)
       MainWindow = QtWidgets.QMainWindow()
       ui = MainWindow()
       ui.setupUi(MainWindow)
       MainWindow.show()
       sys.exit(app.exec_())

Juego RPG con Reglas Léxicas y Sintácticas en Ply
**************************************************
Este problema específico trata de un jugador dentro de una habitación con una puerta.
El jugador puede abrir, cerrar y cerrar con llave la puerta, si consigue la llave que se encuentra en la habitación.
Dentro de la habitación hay 2 llaves. El jugador también podrá tirar o guardar la llave, una vez la haya adquirido.

Código
=======
El código utilizado para la resolución de este problema fue el siguiente:

Imports utilizados
-------------------
Para realizar el proyecto, se utilizaron varios módulos.

Los módulos utilizados fueron:

.. code-block:: python

  import sys
  from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
  from PyQt5.QtCore import Qt

Dentro de layoutqt se encuentra el diseño de la gui utilizada, creada con QTPython

.. code-block:: python

  from layoutqt import Ui_MainWindow
  
Se utilizó Ply para la creación del lexer y el parser.
 
.. code-block:: python

  import ply.lex as lex
  import ply.yacc as yacc

Variables globales
-------------------
Para manejar variables que se utilizan en varios procesos, declaramos variables globales que se irán modificando a medida que se ejecuta el código.

.. code-block:: python

  i = 0
  j = 0
  doorStat = 0
  
Clase RpgApp
-------------
Creamos una clase llamada RpgApp, la cual tendrá como parámetro QMainWindow, lo que la enlazará con la interfaz gráfica creada.

.. code-block:: python

  class RpgApp(QMainWindow):
  
Función __init__
------------------
Dentro de esta función se inicia y conecta el botón que se utiliza para que se lea el input,
 como se mostrará a coninuación:
 
.. code-block:: python

  def __init__(self):
	super().__init__()
	self.ui = Ui_MainWindow()
	self.ui.setupUi(self)
	self.ui.okbtn.clicked.connect(self.rpg)
	self.show()
 
Listado de TOKENS
=================
Los tokens utilizados en este programa fueron:

.. code-block:: python

  tokens = ['PUERTA', 'JUGADOR', 'LLAVE', 'NAME']
  
Listado de Reglas Léxicas
=========================
Las reglas que se utilizaron para cada token fueron:

.. code-block:: python

  #Reglas para las regex
        t_ignore = ' \t' #espacios y TABS
        
        #Funcion para la puerta
        def t_PUERTA(t):
           r'abrir|cerrar|conLlave'
           t.type = 'PUERTA'
           return t

		#Funcion para el movimiento del jugador   
        def t_JUGADOR(t):
           r'up|down|right|left'
           t.type = 'JUGADOR'
           return t
       
	    #Funcion para el estado de la llave
        def t_LLAVE(t):
           r'guardar|tirar'
           t.type = 'LLAVE'
           return t
        
		#Nombre del heroe
        def t_NAME(t):
           r'[a-zA-Z_][a-zA-Z_0-9]*'
           t.type = 'NAME'
           return t
       
        def t_error(t):
           print("Carácter Ilegal '%s'" % t.value)
           t.lexer.skip(1)


Las reglas anteriormente definidas nos indican los comandos que se pueden introducir dentro del juego, ya que son parte del lenguaje.

Lexer
------
El lexer escanea la entrada y produce los tokens correspondientes. 

A continuación, se presentará la construcción del lexer:
.. code-block:: python

   lex.lex()

Listado de Reglas Sintácticas
=============================
A continuación se verán las funciones creadas para cada tipo de token.

Funcion de definicion de sintaxis
---------------------------------
.. code-block:: python

   def p_rpg(p):
	#Creación de reglas
	""" 
	todo : expression
		 | empty
	"""
	s=(str(run(p[1])))
	self.ui.outputtxt.setText(s)
	
Dentro de esta función, se define la sintaxis y se imprime en el editText llamado outputtxt la salida de la función run.

Funciones de valores de entrada
-------------------------------
.. code-block:: python

    #Para líneas vacías
	def p_empty(p):
	   """
	   empty :
	  """
	   p[0] = None
	  
	#para nombrar al heroe
	def p_expname(p):
	   '''expression : NAME
	   '''
	   try:
		  p[0] = p[1]
	   except LookupError:
		  print(f"Undefined name {p[1]!r}")
		  p[0] = 0
		  
	#Para el movimiento del heroe
	def p_moveplayer(p):
	  'expression : JUGADOR'
	  p[0] = p[1]

	#Para el estado de la llave
	def p_key(p):
	   'expression : LLAVE'
	   p[0] = p[1]
		
	#Para el estado de la puerta
	def p_doorstatur(p):
	   'expression : PUERTA'
	   p[0] = p[1]
   
	def p_error(p):
	   s=("Error de sintaxis!")
	   self.ui.outputtxt.setText(s)
	
Se puede apreciar que hay una función para cada regla creada anteriormente.

Parser
--------
El parser analiza los tokens y produce el resultado del análisis.

A continuación, se presentará la construcción del parser:
.. code-block:: python

  parser = yacc.yacc(debug=True)
  
Función principal
------------------
Se definirá la función run, encargada de revisar las entradas y realizar las operaciones necesarias en cada caso.

.. code-block:: python

  #Funcion principal
	def run(p):
		global aux

		#array de la ubicacion de la llave, el jugador empieza en pm[0][0]
		pm = [[0,0,1],
			  [1,0,0],
			  [0,0,0]]
		global i
		global j

		#variable auxiliar para saber el estado de la llave
		aux = pm[i][j]

		#Movimiento del heroe
		if p =='up':
			i -= 1
			aux = pm[i][j]
			if aux == 1:
				return("Has encontrado la llave! Intenta abrir la puerta")           
			else:
				return("La llave no esta aqui, intenta moverte en otra direccion.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")

		if p == 'down':
			i += 1
			aux = pm[i][j]
			if aux == 1:
				return("Has encontrado la llave! Intenta abrir la puerta") 
				#return
			else:
				return("La llave no esta aqui, intenta moverte en otra direccion.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")

		if p == 'right':
			j += 1
			aux = pm[i][j]
			if aux == 1:
				return("Has encontrado la llave! Intenta abrir la puerta")
				#return
			else:
				return("La llave no esta aqui, intenta moverte en otra direccion.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")

		if p == 'left':
			j -= 1
			aux = pm[i][j]
			if aux == 1:
				return("Has encontrado la llave! Intenta abrir la puerta")
				#return
			else:
				return("La llave no esta aqui, intenta moverte en otra direccion.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")

		#Estado de la puerta
		global doorStat
		if aux == 1:
			if p == 'abrir':
				if doorStat == 1:
					return("La puerta ya estaba abierta. Intenta cerrarla o ponerle llave.")
				else:
					doorStat = 1
					return("Has abierto la puerta. Ahora pueden entrar mounstros.")
			if p == 'cerrar':
				if doorStat == 1:
					doorStat = 0
					return("Has cerrado la puerta. Ya no pueden entrar mas mounstros.")
				else:
					return("La puerta ya estaba cerrada. Intenta abrirla o ponerle llave.")
			if p == 'conLlave':
				if doorStat != 2:
					doorStat = 2
					return("Has cerrado la puerta con llave. La puerta ahora se encuentra cerrada y con llave")
				else:
					return("La puerta ya estaba cerrada con llave. Intenta abrirla o cerrarla (sin llave).")
		if aux == 0: #Si aux esta en 0, el heroe no tiene la lave, por lo que no podrá realizar ninguna acción que requiera llave
			if p == 'abrir' or p == 'cerrar' or p == 'conLlave' or p == 'tirar' or p == 'guardar':
				return("Aun no tienes la llave! Intenta moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")

		#Tirar o guardar las llaves
		if aux == 1:
			if p == 'tirar':
				aux = 0 #Si decide tirar las llave, la variable aux cambiar'a a 0 para indicar que no tiene la llave
				return('Has tirado la llave. si quieres encontrarla de nuevo, tienes que moverte.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).')
				#return
			if p == 'guardar':
				return('Has guardado la llave en tu bolsillo. Puedes abrir, cerrar y cerrar con llave la puerta.')
				#return

Dentro de esta función se ejecutan todas las órdenes que envie el jugador y, dependiendo de las circunstancias, las consecuencias cambiarán.

Entrada por parte del usuario
------------------------------
El usuario escribirá dentro de un editText llamado inputtxt y, este input, se guardará dentro de una variable s, para ser enviado al parser.

Si el usuario escribe la palabra TERMINAR, saldrá un mensaje de despedida en el outputtxt.

.. code-block:: python

    s = self.ui.inputtxt.toPlainText()
	if (s.upper() == 'TERMINAR'):
		self.ui.outputtxt.setText("Programa terminado. Gracias por jugar!")
		return
		#parser.parse(s)  
	else:
		parser.parse(s)
		
Main
------
Para ejecutar la ventana del GUI, hay que iniciarla.

.. code-block:: python

  if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RpgApp()
    ventana.show()
    sys.exit(app.exec_())
	
Código de la interfaz gráfica
------------------------------
.. code-block:: python

  from PyQt5 import QtCore, QtGui, QtWidgets

  class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 384)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Dani XD/Desktop/gameboy.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
		"background-color: rgb(114, 45, 36);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.okbtn = QtWidgets.QPushButton(self.centralwidget)
        self.okbtn.setGeometry(QtCore.QRect(10, 300, 311, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 122, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.okbtn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.okbtn.setFont(font)
        self.okbtn.setStyleSheet("background-color: rgb(167, 122, 75);")
        self.okbtn.setObjectName("okbtn")
        self.inputtxt = QtWidgets.QTextEdit(self.centralwidget)
        self.inputtxt.setGeometry(QtCore.QRect(10, 210, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputtxt.setFont(font)
        self.inputtxt.setStyleSheet("background-color: rgb(236, 198, 162);")
        self.inputtxt.setObjectName("inputtxt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 116, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 210, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 45, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_2.setPalette(palette)
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.outputtxt = QtWidgets.QTextEdit(self.centralwidget)
        self.outputtxt.setGeometry(QtCore.QRect(350, 70, 311, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outputtxt.setFont(font)
        self.outputtxt.setStyleSheet("background-color: rgb(236, 198, 162);")
        self.outputtxt.setObjectName("outputtxt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 225, 100))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aventura RPG"))
        self.okbtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Haz clic aquí para darle las instrucciones al heroe.</p><p>El resultado de tus instrucciones se verá en el cuadro de texto de la derecha.</p><p>¡Suerte!</p></body></html>"))
        self.okbtn.setText(_translate("MainWindow", "Ok"))
        self.inputtxt.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ingresa aquí las instrucciones que le darás al heroe.</p><p>Puedes moverte en 4 direcciones, utilizando <span style=\" font-weight:600;\">up</span> (arriba), <span style=\" font-weight:600;\">down</span> (abajo),<span style=\" font-weight:600;\"> right</span> (derecha) o <span style=\" font-weight:600;\">left</span> (izquierda).</p><p>Tambien puedes<span style=\" font-weight:600;\"> abrir</span> la puerta,<span style=\" font-weight:600;\"> cerrar</span> la puerta o ponerla <span style=\" font-weight:600;\">conLlave</span>.</p><p>Al adquirir la llave, puedes<span style=\" font-weight:600;\"> guardar</span> la llave o<span style=\" font-weight:600;\"> tirar</span> la llave.</p><p>Para terminar la partida, deberás escribir <span style=\" font-weight:600;\">TERMINAR</span>.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Aventura RPG"))
        self.label_2.setText(_translate("MainWindow", "Resultado de la Aventura"))
        self.outputtxt.setToolTip(_translate("MainWindow", "<html><head/><body><p>Aquí aparecerán la consecuencias de las instrucciones que le des al heroe.</p><p>Suerte y... escoge con cuidado.</p></body></html>"))
        self.label_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\"C:/Users/Dani XD/Desktop/heroes.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"C:/Users/Dani XD/Desktop/heroes.png\"/></p></body></html>"))
  #import rcs2_rc
  #import rsc_rc


  if __name__ == "__main__":
      import sys
      app = QtWidgets.QApplication(sys.argv)
      MainWindow = QtWidgets.QMainWindow()
      ui = Ui_MainWindow()
      ui.setupUi(MainWindow)
      MainWindow.show()
      sys.exit(app.exec_())


Sistema de Arranque de una Computadora
**************************************


Listado de TOKENS
=================

.. code-block:: python

   #variable auxiliar para las funciones
   tokens = ['ESTADO', 'SOLICITUD', 'REINICIOS', 'NAME']

Listado de Reglas Léxicas
=========================

.. code-block:: python

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
        
   #En caso de error de algun carácter ilegal
   def t_error(t):
       self.ui.txtsalida.setText("Carácter Ilegal '%s'" % t.value)
       t.lexer.skip(1)

Listado de Reglas  Sintácticas
==============================

.. code-block:: python

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

Código
======

Módulos importados
------------------

.. code-block:: python

   import sys
   from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
   from PyQt5 import QtCore, QtGui, QtWidgets
   from PyQt5.QtCore import Qt
   from Interfaz import MainWindow
   import ply.lex as lex
   import ply.yacc as yacc
   import random

Clase principal Arranque_Sistema
--------------------------------

.. code-block:: python

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
        
Construyendo Lexer
------------------

.. code-block:: python

   #Construir el lexer
   lex.lex()
        
Construyendo Parser
-------------------

.. code-block:: python
    
   #Construcción del parse
   parser = yacc.yacc()
        
Función run
-----------

.. code-block:: python

   def run(p):
       global disponibilidad,ver 
       #Disponibilidad puede estar encendido o Apagado 
       #ver Permite conocer que imagen se va a visualizar
       encendido=False #Asignación por defecto
       resultado="" # Contiene el resultado de la ejecución
            
       #Validar en caso disponibilidad no tenga valor
       try:
           encendido=disponibilidad # Asignar si esta encendida
       except NameError:
           pass   
            
       #Primera validación
       if p=='Encender':
          #Pasos que se debe cumplir
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
                     i=0 # Inicializar variable en 0
                     if(verificar==True):
                        #Contar la cantidad de reinicios en el encendido
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
          #Conocer que imagen se mostrara
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
            #Conocer que imagen se mostrara
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
       #Captar el dato introducido en textedit
       s = self.ui.txtentrada.toPlainText()
       parser.parse(s)
        
        
   # Funcion para mostrar la imagen
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

Código de la interfaz gráfica
------------------------------

.. code-block:: python

   from PyQt5 import QtCore, QtGui, QtWidgets


   class MainWindow(object):
       def setupUi(self, MainWindow):
           MainWindow.setObjectName("MainWindow")
           MainWindow.resize(409, 674)
           MainWindow.setAutoFillBackground(False)
           icon = QtGui.QIcon()
           icon.addPixmap(QtGui.QPixmap("30537.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           MainWindow.setWindowIcon(icon)
           MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
           self.centralwidget = QtWidgets.QWidget(MainWindow)
           self.centralwidget.setObjectName("centralwidget")
           self.ejecutar = QtWidgets.QPushButton(self.centralwidget)
           self.ejecutar.setGeometry(QtCore.QRect(150, 200, 101, 31))
           self.ejecutar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
           self.ejecutar.setStyleSheet("background-color:rgb(255, 255, 255);\n"
   "font: 75 10pt \"MS Shell Dlg 2\";")
           self.ejecutar.setObjectName("ejecutar")
           self.txtentrada = QtWidgets.QTextEdit(self.centralwidget)
           self.txtentrada.setGeometry(QtCore.QRect(40, 140, 341, 51))
           self.txtentrada.setStyleSheet("background-color:rgb(255, 255, 255)")
           self.txtentrada.setObjectName("txtentrada")
           self.label = QtWidgets.QLabel(self.centralwidget)
           self.label.setGeometry(QtCore.QRect(0, 0, 411, 61))
           self.label.setStyleSheet("background-color: rgb(0, 120, 176);\n"
   "\n"
   "color: rgb(255, 255, 255);\n"
   "")
           self.label.setObjectName("label")
           self.label_2 = QtWidgets.QLabel(self.centralwidget)
           self.label_2.setGeometry(QtCore.QRect(40, 100, 181, 21))
           self.label_2.setStyleSheet("")
           self.label_2.setObjectName("label_2")
           self.imagen = QtWidgets.QLabel(self.centralwidget)
           self.imagen.setGeometry(QtCore.QRect(110, 460, 201, 131))
           self.imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
           self.imagen.setFrameShape(QtWidgets.QFrame.Box)
           self.imagen.setText("")
           self.imagen.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
           self.imagen.setObjectName("imagen")
           self.label_4 = QtWidgets.QLabel(self.centralwidget)
           self.label_4.setGeometry(QtCore.QRect(160, 430, 91, 21))
           self.label_4.setStyleSheet("")
           self.label_4.setObjectName("label_4")
           self.txtestado = QtWidgets.QLabel(self.centralwidget)
           self.txtestado.setGeometry(QtCore.QRect(160, 610, 105, 31))
           self.txtestado.setStyleSheet("background-color:rgb(255, 255, 255);")
           self.txtestado.setFrameShape(QtWidgets.QFrame.Box)
           self.txtestado.setObjectName("txtestado")
           self.txtsalida = QtWidgets.QTextEdit(self.centralwidget)
           self.txtsalida.setGeometry(QtCore.QRect(40, 290, 341, 121))
           self.txtsalida.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
           self.txtsalida.setStyleSheet("background-color:rgb(255, 255, 255);")
           self.txtsalida.setReadOnly(True)
           self.txtsalida.setObjectName("txtsalida")
           self.label_6 = QtWidgets.QLabel(self.centralwidget)
           self.label_6.setGeometry(QtCore.QRect(40, 250, 201, 31))
           self.label_6.setStyleSheet("")
           self.label_6.setObjectName("label_6")
           MainWindow.setCentralWidget(self.centralwidget)
           self.statusbar = QtWidgets.QStatusBar(MainWindow)
           self.statusbar.setObjectName("statusbar")
           MainWindow.setStatusBar(self.statusbar)
           MainWindow.setStatusBar(self.statusbar)
        
           ver="Apagado.png"
           pixmap = QtGui.QPixmap(ver) # Setup pixmap with the provided image
           pixmap = pixmap.scaled(self.imagen.width(), self.imagen.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
           self.imagen.setPixmap(pixmap) # Set the pixmap onto the label
           self.imagen.setAlignment(QtCore.Qt.AlignCenter) # Align the label to cente

           self.retranslateUi(MainWindow)
           QtCore.QMetaObject.connectSlotsByName(MainWindow)

       def retranslateUi(self, MainWindow):
           _translate = QtCore.QCoreApplication.translate
           MainWindow.setWindowTitle(_translate("MainWindow", "Arranque"))
           self.ejecutar.setText(_translate("MainWindow", "Ejecutar"))
           self.txtentrada.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
   "p, li { white-space: pre-wrap; }\n"
   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
           self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Sistema de Arranque de una </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Computadora</span></p></body></html>"))
           self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ingrese su solicitud</span></p></body></html>"))
           self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Estado</span></p></body></html>"))
           self.txtestado.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
           self.txtsalida.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
   "p, li { white-space: pre-wrap; }\n"
   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
           self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Resultado del Proceso</span></p></body></html>"))

   if __name__ == "__main__":
       import sys
       app = QtWidgets.QApplication(sys.argv)
       MainWindow = QtWidgets.QMainWindow()
       ui = MainWindow()
       ui.setupUi(MainWindow)
       MainWindow.show()
       sys.exit(app.exec_())


IMAGENES
********

Interfaz de Termometro Automático
=================================

.. figure:: _static/UI1.png
   :align:  center

.. figure:: _static/UI2.png
   :align:  center

.. figure:: _static/UI3.png
   :align:  center


Interfaz del juego RPG
======================

.. figure:: _static/sc1.png

Tooltips incorporados

.. figure:: _static/sct1.png

.. figure:: _static/sct2.png

.. figure:: _static/sct3.png

Programa Corriendo

.. figure:: _static/game1.png

.. figure:: _static/game2.png

.. figure:: _static/game3.png

.. figure:: _static/game4.png

.. figure:: _static/game5.png


Interfaz de Sistema de Arranque de una Computadora
==================================================

Interfaz Principal
------------------

Al introducir Encender, se valida que el sistema se encuentre Apagado, si es así procede a
realizar varios intentos si en tal caso en el encendido de la computadora en uno de los pasos
marca error, esto se repite hasta que el equipo encienda, al suceder esto cambia el estado del
equipo ha Encendido.
Al introducir Apagar, se valida si el sistema este encendido, de ser así se detiene el sistema y
vuelve a cambiar el esta a Apagado. Es importante mencionar que al ejecutar la aplicación por
primera vez, esta da por defecto muestra que el sistema se encuentra apagado.

.. figure:: _static/Imagen1.png

Ejecución 1
-----------

El sistema por defecto viene apagado, por lo cual al introducir Apagar como primera solicitud el
sistema nos informara que tal acción es rechazada, ya que el sistema se encuentra Apagado.

.. figure:: _static/Imagen2.png

Ejecución 2
-----------
Al introducir Encender, como previamente el dispositivo se encontraba Apagado, se realiza test
internamente tantas veces sea necesario, hasta que equipo encienda satisfactoriamente, por medio
de la interfaz nos mostrara el resultado de la ejecución paso a paso, para observar en que punto
hubo algún fallo por lo cual el sistema tuvo que reiniciar.

.. figure:: _static/Imagen3.png

Ejecución 3
-----------
El equipo al estar Encendido y recibir una nueva solicitud de Encender, este informa al usuario
que el sistema ya se encuentra encendido.

.. figure:: _static/Imagen4.png

Ejecución 4
-----------
Ahora al equipo estar Encendido, puede aceptar la solicitud de Apagar, por lo cual realiza en
cambio de estado.

.. figure:: _static/Imagen4.png

