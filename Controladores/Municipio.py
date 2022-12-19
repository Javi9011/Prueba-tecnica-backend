from Repositorios.RepositorioMunicipio import RepositorioMunicipio
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Municipio import Municipio
from Modelos.Departamento import Departamento

class ControladorMunicipio():
    def __init__(self):
        print("Creando controlador municipio")
        self.repositorioMunicipio=RepositorioMunicipio()
        self.repositorioDepartamento=RepositorioDepartamento()

    def crearMunicipio(self, bodyRequest):
        print("Creando municipio..")
        elMunicipio = Municipio(bodyRequest)
        print("Municipio a crear en la base de datos: ",elMunicipio.__dict__)
        self.repositorioMunicipio.save(elMunicipio)
        return True

    def buscarMunicipio(self):
        print("Buscando todos los municipios..")
        return self.repositorioMunicipio.findAll()

    def buscarUnMunicipio(self,idObject):
        print("Buscando municipio ",idObject)
        municipio = Municipio(self.repositorioMunicipio.findById(idObject))
        return municipio.__dict__

    def actualizarMunicipio(self,id,elMunicipio):
        municipioActual = Municipio(self.repositorioMunicipio.findById(id))
        municipioActual = nombre = elMunicipio["nombre"]
        return self.repositorioMunicipio.save(municipioActual)

    def deleteMunicipio(self,id):
        return self.repositorioMunicipio.delete(id)

    def asignarDepartamento(self,idMunicipio, idDepartamento):
        municipioActual = Municipio(self.repositorioMunicipio.findById(idMunicipio))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(idDepartamento))
        print("Municipio encontrado: ",municipioActual.__dict__)
        print("Departamento encontrado: ",departamentoActual.__dict__)
        municipioActual.departamento = departamentoActual
        print("Municipio actualizado: ",municipioActual.__dict__)
        return self.repositorioMunicipio.save(municipioActual)