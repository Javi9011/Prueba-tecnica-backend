from Repositorios.RepositorioLider import RepositorioLider
from Repositorios.RepositorioCapitan import RepositorioCapitan
from Modelos.Lider import Lider
from Modelos.Capitan import Capitan

class ControladorLider():
    def __init__(self):
        print("Creando controlador lider")
        self.repositorioLider=RepositorioLider()
        self.repositorioCapitan=RepositorioCapitan()

    def crearLider(self,bodyRequest):
        print("Creando lider..")
        elLider = Lider(bodyRequest)
        print("Lider a crear en la base de datos: ",elLider.__dict__)
        self.repositorioLider.save(elLider)
        return True

    def buscarTodosLosLideres(self):
        print("Buscando todos los lideres en la base de datos...")
        return self.repositorioLider.findAll()

    def buscarUnLider(self,idObjet):
        print("Lider con id:", idObjet)
        lider = Lider(self.repositorioLider.findById(idObjet))
        return lider.__dict__

    def actualizarLider(self,id,elLider):
        liderActual = Lider(self.repositorioLider.findById(id))
        liderActual.nombre = elLider["nombre"]
        liderActual.apellido = elLider["apellido"]
        liderActual.celular = elLider["celular"]
        return self.repositorioLider.save(liderActual)

    def deleteLider(self,id):
        return self.repositorioLider(id)

    def asignarCapitan(self, idLider, idCapitan):
        capitanActual=Capitan(self.repositorioCapitan.findById(idCapitan))
        liderActual=Lider(self.repositorioLider.findById(idLider))
        print("Capitan encontrado: ",capitanActual.__dict__)
        print("Lider encontrado: ",liderActual.__dict__)
        liderActual.capitan = capitanActual
        print("Lider actualizado: ",liderActual.__dict__)
        return self.repositorioLider.save(liderActual)