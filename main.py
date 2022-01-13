import sys
import os
import json

from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar
from PyQt5.uic import loadUi

class client:
    def __init__(self, name = None, path = None):
        self.Name = name
        self.Id = id
        self.path_folder = path
        self.order = None
        self.type = None
        
    def __del__(self):
        self.Name = None
        self.Id = None
        self.path_folder = None
        self.order = None
        self.type = None

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('./Interface gráfica/interface.ui',self )
        self.folder_path = 'D:/Users/micae/Documents/Colorfilme/Testes/'
        self.statusBar().showMessage(str("Pronto."))

        self.pushButton.clicked.connect(self.openFolder)
        self.pushButton_3.clicked.connect(self.revelar)
        self.pushButton_4.clicked.connect(self.createFolder)

    def createFolder(self):
        data = self.readJson()
        print(data)
        global Client
        Client = client(name = self.lineEdit.text() , path = self.folder_path + self.lineEdit.text() )
        Client.Id = 1

        try:
            os.mkdir(Client.path_folder)
            os.system(f'start {os.path.realpath(Client.path_folder)}')
            self.statusBar().showMessage(str("Em seleção de Fotos"))
        except:
            print("Não foi possível criar pasta.")
            self.statusBar().showMessage(str("Aconteceu algum problema."))

    def openFolder(self):
        id = self.lineEdit_2.text() 
        if id is None:
            self.statusBar().showMessage(str("Informe o Nº de serviço."))
        else:   
            try:
                Client
            except NameError:
                var_exists = False
            else :
                var_exists = True

            if var_exists:
                os.system(f'start {os.path.realpath(Client.path_folder)}')
            else:
                data = self.readJson()
                if id in data:
                    os.system(f'start {os.path.realpath(data[str(id)]["Path"])}')
                else:
                    self.statusBar().showMessage(str("Número de Serviço não encontrado."),3000)

            
    def cancel_op(self):
        path = self.folder_path +'/' + name
        os.rmdir(path)

    def revelar(self):
        try:
            Client
        except NameError:
            self.statusBar().showMessage(str("Nenhum pedido no sistema."))
        else :
            print(Client.Name)
            dataJson = { Client.Id: {
            "Name": Client.Name, 
            "Path": Client.path_folder,
            "Order":{"10x15":5, "20x30":7}, 
            "Type":"Amador"}}
            
            self.writeJson(dataJson)
            self.cleanObj()
            data = self.readJson()
            print(data)

    def cleanObj(self):
        Client.__del__() 

    def readJson(self):
        try:
            with open('./backlog.json','r') as f:
                data = json.load(f)
            f.close()
        except IOError:
            data = None
        return data

    def writeJson(self,dados):
        try:
            with open('./backlog.json','a+') as f:
                json.dump(dados, f, indent=4)
            f.close()
        except:
            "Algo deu errado..."







app = QApplication(sys.argv)
window = MyApp()
window.show()
# TODO: see if usein exit() method from sys and not from QWidget make sense. It's make exceptions easier to hendle
sys.exit(app.exec_())