#Ervis Alain [8-938-73]
#Daniella Ramos [8-938-1528]
#Harold Torres [8-943-2153]

import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import Qt
from layoutqt import Ui_MainWindow
import ply.lex as lex
import ply.yacc as yacc

i = 0
j = 0
doorStat = 0

class RpgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.okbtn.clicked.connect(self.rpg)
        self.show()
        
    def rpg(self):
        tokens = ['PUERTA', 'JUGADOR', 'LLAVE', 'NAME']

        #Reglas para las regex
        t_ignore = ' \t' #espacios y TABS
        
        #Funcion para la puerta
        def t_PUERTA(t):
           r'abrir|cerrar|conLlave'
           t.type = 'PUERTA'
           return t
       
        def t_JUGADOR(t):
           r'up|down|right|left'
           t.type = 'JUGADOR'
           return t
       
        def t_LLAVE(t):
           r'guardar|tirar'
           t.type = 'LLAVE'
           return t
        
        def t_NAME(t):
           r'[a-zA-Z_][a-zA-Z_0-9]*'
           t.type = 'NAME'
           return t
       
        def t_error(t):
           print("Carácter Ilegal '%s'" % t.value)
           t.lexer.skip(1)
           
        #Construir el lexer
        lex.lex()
        
        def p_rpg(p):
           #Creación de reglas
           """ 
           todo : expression
               | empty
          """
           s=(str(run(p[1])))
           self.ui.outputtxt.setText(s)
         
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
           
        #Construyendo el parser
        #---------------------------------------------------------------------------------
        parser = yacc.yacc(debug=True)
           
        #Funcion principal
        def run(p):
            global aux
    
            #array de la ubicacion de la llave
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
                if i == 3:
                    i = 0
                aux = pm[i][j]
                if aux == 1:
                    return("Has encontrado la llave! Intenta abrir la puerta") 
                    #return
                else:
                    return("La llave no esta aqui, intenta moverte en otra direccion.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")

            if p == 'right':
                j += 1
                if j == 3:
                    j = 0
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
            if aux == 0:
                if p == 'abrir' or p == 'cerrar' or p == 'conLlave' or p == 'tirar' or p == 'guardar':
                    return("Aun no tienes la llave! Intenta moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).")
    
            #Tirar o guardar las llaves
            if aux == 1:
                if p == 'tirar':
                    aux = 0
                    return('Has tirado la llave. si quieres encontrarla de nuevo, tienes que moverte.\nPuedes moverte hacia arriba (up), abajo (down), derecha (right) o izquierda (left).')
                    #return
                if p == 'guardar':
                    return('Has guardado la llave en tu bolsillo. Puedes abrir, cerrar y cerrar con llave la puerta.')
                    #return
        
        
        s = self.ui.inputtxt.toPlainText()
        if (s.upper() == 'TERMINAR'):
            self.ui.outputtxt.setText("Programa terminado. Gracias por jugar!")
            return
            #parser.parse(s)  
        else:
            parser.parse(s) 
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RpgApp()
    ventana.show()
    sys.exit(app.exec_())