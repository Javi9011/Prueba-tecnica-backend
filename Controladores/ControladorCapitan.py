from Modelos.Capitan import Capitan
from Repositorios.RepositorioCapitan import RepositorioCapitan


class ControladorCapitan():

    def __init__(self):
        print("Creando controlador capitan...")
        self.repositorioCapitan=RepositorioCapitan()

    def crearCapitan(self, bodyRequest):
        print("Creando capitan...")
        elCapitan = Capitan(bodyRequest)
        print("Capitan a crear en base de datos: ",elCapitan.__dict__)
        self.repositorioCapitan.save(elCapitan)
        return True

    def buscarTodosCapitanes(self):
        print("Buscando todos los capitanes...")
        return self.repositorioCapitan.findAll()

    def buscarCapitan(self,idOject):
        print("Buscando capitan con id ",idOject)
        capitan=Capitan(self.repositorioCapitan.findById(idOject))
        return capitan.__dict__

    def actualizarCapitan(self,id,elCapitan):
        capitanActual=Capitan(self.repositorioCapitan.findById(id))
        capitanActual.nombres = elCapitan["nombres"]
        capitanActual.apellidos = elCapitan["apellidos"]
        capitanActual.celular = elCapitan["celular"]
        return self.repositorioCapitan.save(capitanActual)

    def borrarCapitan(self, id):
        return self.repositorioCapitan.delete(id)






