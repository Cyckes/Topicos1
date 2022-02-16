import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import MainWindow
from PyQt5.QtGui import QPixmap
import ply.lex as lex
import ply.yacc as yacc
import random
        
        
class GUIApplication(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.ui.botonEjecutar.clicked.connect(self.ejecutar)
        
        pixmap = QPixmap("on.png")
        self.ui.labelEstado.setPixmap(QPixmap(pixmap))
            
        self.show()
        
        
    def ejecutar(self):
        # NOMBRE DE LOS TOKENS
        tokens = ["DISTANCIA", "ENTERO", "FLOTANTE"]

        # REGLAS DE EXPRESIONES REGULARES
        #t_NOMBRE = r'[a-zA-Z][a-zA-Z]*'
        t_ignore = ' \t' # caracteres ignorados (espacios y TABS)
        
        # Función para la distancia
        def t_DISTANCIA(t):
            r'distancia'
            t.value = "DISTANCIA"
            return t

        # Función para números flotantes
        def t_FLOTANTE(t):
            r'\d+\.\d+'
            t.value = float(t.value)
            return t

        # Función para números enteros
        def t_ENTERO(t):
            r'\d+'# el + significa N caracteres
            t.value = int(t.value)
            return t
        
        # Función para saltos de linea
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)
            
        # Función de posibles errores
        def t_error(t):
            error=("\nCarácter Ilegal '%s'" % t.value[0])
            self.ui.txtSalida.setText(error)
            t.lexer.skip(1)
    
        #Construir el lexer
        lexer = lex.lex()



        #Función para Parser
        def p_comandos(p):
            #Creando las reglas
            """
            comandos : expresion
                     | empty
            """
            self.ui.txtSalida.setText(str(run(p[1])))
    
        #Función para las expresiones
        def p_expresion(p):
            """
            expresion : DISTANCIA numero
                  
            """
            p[0] = (p[1], p[2])  
    
        #Función para las expresiones INT y Float
        def p_expresion_int_float(p):
            """
            numero : ENTERO
                   | FLOTANTE
            """
            p[0] = p[1]

        #Función para errores
        def p_error(p):
            self.ui.txtSalida.setText("Error de sintaxis!")
    
        #Función para líneas vacías
        def p_empty(p):
            """
            empty :
            """
            p[0] = None
    
        #Construyendo el parser
        parser = yacc.yacc()

        #Función final
        #cerca = False
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
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GUIApplication()
    ventana.show()
    sys.exit(app.exec_())