from Repositorios.RepositorioPuestovotacion import RepositorioPuestovotacion
from Repositorios.RepositorioMunicipio import RepositorioMunicipio
from Modelos.Puestovotacion import Puestovotacion
from Modelos.Municipio import Municipio

class ControladorPuestoVotacion():

    def __init__(self):
        print("Creando puesto de votacion")
        self.repositorioPuestovotacion = RepositorioPuestovotacion()
        self.repositorioMunicipio = RepositorioMunicipio()

    def crearPuestovotacion(self, bodyrequest):
        print("creando puesto votacion...")
        elPuestovotacion = Puestovotacion(bodyrequest)
        print("Puesto de votacion a crear en la BD: ",elPuestovotacion.__dict__)
        self.repositorioPuestovotacion.save(elPuestovotacion)

    def buscarTodosLosPuestos(self):
        print("Buscando todos los puestos de votacion...")
        return self.repositorioPuestovotacion.findAll()

    def buscarUnPuesto(self,idObject):
        print("Buscando puesto votacion:",idObject)
        puesto = Puestovotacion(self.repositorioPuestovotacion.findById(idObject))
        return puesto.__dict__

    def actualizarPuesto(self,id,elPuestovotacion):
        puestoActual = Puestovotacion(self.repositorioPuestovotacion.findById(id))
        puestoActual.nombre = elPuestovotacion["nombre"]
        puestoActual.direccion = elPuestovotacion["direccion"]
        return self.repositorioPuestovotacion.save(puestoActual)

    def borrarPuestoVotacion(self,id):
        return self.repositorioPuestovotacion.delete(id)
        print("Puesto de votacion eliminado de la BD..")

    def asignarMunicipio(self, idPuestovotacion, idMunicipio):
        puestoActual = Puestovotacion(self.repositorioPuestovotacion.findById(idPuestovotacion))
        municipioActual = Municipio(self.repositorioMunicipio.findById(idMunicipio))
        print("Puesto de votacion encontrado: ",puestoActual.__dict__)
        print("Municipio encontrado: ",municipioActual.__dict__)
        puestoActual.municipio = municipioActual
        print("Puesto votacion actualizado", puestoActual.__dict__)
        return self.repositorioPuestovotacion.save(puestoActual)