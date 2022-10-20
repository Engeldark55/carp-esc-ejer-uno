from email import message
from os import close
from PySide6.QtWidgets import QWidget
from view.Windows_main import Ui_Form_main as Main
from controller.mensaje import Mensaje as msj

class Notas(QWidget, Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.mensaje = msj()
        self.mensaje.btn_ok.clicked.connect(lambda: self.mensaje.close())
        self.btn_save.clicked.connect(lambda:  self.optener_data())
        #self.checkBox_A.stateChanged.connect(lambda: self.check_aprovado())
        #self.checkBox_R.stateChanged.connect(lambda: self.check_reprovado())

    def optener_data(self):
        nombre = self.line_nombre.text()
        cali = int(self.line_cali.text())
        if cali >= 70:
            resolucion_1 = self.checkBox_A = 'aprovado'
         
            self.mensaje.show()
            self.mensaje.label_msj.setText(f'el alumno: {nombre} obtuvo una calificacion de {cali} por lo que esta {resolucion_1}')
            self.btn_save.clicked.connect(lambda: Notas.show())
            #print(f'el alumno: {nombre} obtuvo una calificacion de {cali} por lo que esta {resolucion_1}')
        if cali < 70:
            resolucion_2 = self.checkBox_R = 'reprovado'
        
            self.mensaje.show()
            self.mensaje.label_msj.setText(f'el alumno: {nombre} obtuvo una calificacion de {cali} por lo que esta {resolucion_2}')
            #print(f'el alumno: {nombre} obtuvo una calificacion de {cali} por lo que esta {resolucion_2}')

      
    