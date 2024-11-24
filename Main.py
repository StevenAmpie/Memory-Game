from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from random import shuffle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfazGatos.ui", self)  # Carga el diseño creado en Qt Designer

        self.gatos = ['kitty1.png',
                'kitty10.png',
                'kitty11.png',
                'kitty12.png',
                'kitty13.png',
                'kitty14.png',
                'kitty15.png',
                'kitty16.png',
                'kitty17.png',
                'kitty18.png',
                'kitty2.png',
                'kitty3.png',
                'kitty4.png',
                'kitty5.png',
                'kitty6.png',
                'kitty7.png',
                'kitty8.png',
                'kitty9.png',
                'kitty1.png',
                'kitty10.png',
                'kitty11.png',
                'kitty12.png',
                'kitty13.png',
                'kitty14.png',
                'kitty15.png',
                'kitty16.png',
                'kitty17.png',
                'kitty18.png',
                'kitty2.png',
                'kitty3.png',
                'kitty4.png',
                'kitty5.png',
                'kitty6.png',
                'kitty7.png',
                'kitty8.png',
                'kitty9.png',]  

        # Asegurar que el ícono se ajuste al tamaño del botón dinámicamente
        self.botones = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20, self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24, self.pushButton_25, self.pushButton_26, self.pushButton_27, self.pushButton_28, self.pushButton_29, self.pushButton_30, self.pushButton_31, self.pushButton_32, self.pushButton_33, self.pushButton_34, self.pushButton_35, self.pushButton_36
                   ]
        
        for i in self.botones:
                i.setDisabled(True)

        
        #obtener el evento de los botones

        for i in self.botones:
            i.clicked.connect(self.botonPresionado)


        
        self.pushButton_37.clicked.connect(self.reiniciar)
        self.pushButton_38.clicked.connect(self.jugar)


    def reiniciar(self):

        for i in self.botones:
                i.setDisabled(True)


        cont = 0
        self.pushButton_37.setDisabled(True)
        shuffle(self.gatos)
        for i in self.botones:
            i.setStyleSheet(f"border-image: url({self.gatos[cont]});")
            cont+=1
        self.pushButton_38.setDisabled(False)
        QTimer.singleShot(200, lambda: self.pushButton_37.setDisabled(False))
        

        self.contImages = []
        self.botonesPresionados = []
        self.totalParejas = 0
        self.contenedor = []


    def activarBotonesEnAnalizarCant(self):

        for i in self.botones:
                    i.setDisabled(False)

    def ocultarImagenesAlEquivocarse(self):
            
            self.contenedor[0].setStyleSheet(f"")
            self.contenedor[1].setStyleSheet(f"")
            self.contenedor = []



    def vaciarListas(self):
        self.contImages = []
        self.botonesPresionados = []

    def deshabilitarBotones(self):
         
        for i in self.botones:
                i.setDisabled(True)
        QTimer.singleShot(500, self.reiniciar)
         

    def analizarCant(self):

        if len(self.contImages) == 2:

            for i in self.botones:
                i.setDisabled(True)

            if(self.contImages[0] == self.contImages[1]):

                QTimer.singleShot(500, self.activarBotonesEnAnalizarCant)

                self.botonesPresionados[0].setDisabled(True)
                self.botonesPresionados[1].setDisabled(True)
                
                QTimer.singleShot(200, self.vaciarListas)
                self.totalParejas+=1
                self.contenedor = []

                
                if(self.totalParejas == 1):
                    QTimer.singleShot(500, self.deshabilitarBotones)

            
            elif(self.contImages[0] != self.contImages[1]):

                QTimer.singleShot(500, self.activarBotonesEnAnalizarCant)
                QTimer.singleShot(200, self.ocultarImagenesAlEquivocarse)
                QTimer.singleShot(200, self.vaciarListas)
                


    def botonPresionado(self):

        button = self.sender()  
        
        button.setStyleSheet(f"border-image: url({self.gatos[self.botones.index(button)]});")
        button.setDisabled(True)

        
        self.contenedor += [button]
        self.contImages+=[button.styleSheet()]
        self.botonesPresionados += [button]


        QTimer.singleShot(500, self.analizarCant)

    

    def jugar(self):

        self.pushButton_38.setDisabled(True)

        for i in self.botones:
                i.setDisabled(False)
        
        for i in self.botones:
            i.setStyleSheet(f"")



if __name__ == "__main__":
    
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QIcon("Gato.ico"))
    window.reiniciar()
    window.show()
    app.exec_()