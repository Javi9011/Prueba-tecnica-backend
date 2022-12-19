from Repositorios.RepositorioCapitancomuna import RepositorioCapitancomuna
from Repositorios.RepositorioMunicipio import RepositorioMunicipio
from Repositorios.RepositorioCapitan import RepositorioCapitan
from Modelos.Capitancomuna import Capitancomuna
from Modelos.Municipio import Municipio
from Modelos.Capitan import Capitan

class ControladorCapitancomuna():
    def __init__(self):
        print("Creando controlador capitan comuna")
        self.repositorioCapitancomuna = RepositorioCapitancomuna()
        self.repositorioMunicipio = RepositorioMunicipio()
        self.repositorioCapitan =RepositorioCapitan()

    def index(self):
        return self.repositorioCapitancomuna.findAll()

    """Asignar capitan y municipio a capitan-comuna"""
    def crearCapitanComuna(self,bodyrequest,idMunicipio,idCapitan):
        nuevoCapcom = Capitancomuna(bodyrequest)
        elMunicipio = Municipio(self.repositorioMunicipio.findById(idMunicipio))
        elCapitan = Capitan(self.repositorioCapitan.findById(idCapitan))
        nuevoCapcom.municipio = elMunicipio
        nuevoCapcom.capitan = elCapitan
        print("CapitanComuna a crear en BD:",nuevoCapcom.__dict__)
        return self.repositorioCapitancomuna.save(nuevoCapcom)

    def buscarTodosCapcom(self):
        print("Buscando todos los Capcom...")
        return self.repositorioCapitancomuna.findAll()

    def buscarUnCapcom(self,id):
        elCapcom =Capitancomuna(self.repositorioCapitancomuna.findById(id))
        return elCapcom.__dict__

    def deleteCapcom(self,id):
        return self.repositorioCapitancomuna.delete(id)


