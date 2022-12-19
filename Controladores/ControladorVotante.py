from Repositorios.RepositorioVotante import RepositorioVotante
from Repositorios.RepositorioLider import RepositorioLider
from Repositorios.RepositorioMunicipio import RepositorioMunicipio
from Repositorios.RepositorioPuestovotacion import RepositorioPuestovotacion
from Modelos.Votante import Votante
from Modelos.Lider import Lider
from Modelos.Municipio import Municipio
from Modelos.Puestovotacion import Puestovotacion

class ControladorVotante():
    def __init__(self):
        print("Creando controlador del votante....")
        self.repositorioVotante=RepositorioVotante()
        self.repositorioLider=RepositorioLider()
        self.repositorioMunicipio=RepositorioMunicipio()
        self.repositorioPuestovotacion=RepositorioPuestovotacion()

    def crearVotante(self, bodyrequest):
        print("Creando votante..")
        elVotante = Votante(bodyrequest)
        print("Votante a crear en la base de datos: ",elVotante.__dict__)
        self.repositorioVotante.save(elVotante)
        return True

    def buscarTodosLosVotantes(self):
        print("Buscando todos los votantes...")
        return self.repositorioVotante.findAll()

    def buscarUnVotante(self,idObject):
        print("Buscando votante: ",idObject)
        votante = Votante(self.repositorioVotante.findById(idObject))
        return votante.__dict__

    def actualizarVotante(self,id,elVotante):
        votanteActual=Votante(self.repositorioVotante.findById(id))
        votanteActual.nombres = elVotante["nombres"]
        votanteActual.apellidos = elVotante["apellidos"]
        votanteActual.direccion = elVotante["direccion"]
        votanteActual.telefono = elVotante["telefono"]
        votanteActual.cedula = elVotante["cedula"]
        votanteActual.mesa = elVotante["mesa"]
        return self.repositorioVotante.save(votanteActual)

    def deleteVotante(self,id):
        return self.repositorioVotante.delete(id)

    def asignarLiderAVotante(self,idVotante,idLider):
        liderActual=Lider(self.repositorioLider.findById(idLider))
        votanteActual=Votante(self.repositorioVotante.findById(idVotante))
        votanteActual.lider=liderActual
        print("Votante se le asigna lider", liderActual.__dict__)
        return self.repositorioVotante.save(votanteActual)

    def asignarMunicipioAVotante(self,idVotante,idMunicipio):
        municipioActual=Municipio(self.repositorioMunicipio.findById(idMunicipio))
        votanteActual=Votante(self.repositorioVotante.findById(idVotante))
        votanteActual.municipio=municipioActual
        print("Votante se le asigna municipio", municipioActual.__dict__)
        return self.repositorioVotante.save(votanteActual)

    def asignarPuestoDeVotacionAVotante(self,idVotante,idPuesto):
        puestoActual=Puestovotacion(self.repositorioPuestovotacion.findById(idPuesto))
        votanteActual=Votante(self.repositorioVotante.findById(idVotante))
        votanteActual.puesto=puestoActual
        print("Votante se le asigna puesto de votacion", puestoActual.__dict__)
        return self.repositorioVotante.save(votanteActual)
