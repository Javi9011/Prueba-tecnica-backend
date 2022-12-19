from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Departamento import Departamento

class ControladorDepartamento():
    def __init__(self):
        print("Creando controlador departamento...")
        self.repositorioDepartamento=RepositorioDepartamento()

    def crearDepartamento(self,bodyRequest):
        print("Creando departamento")
        elDepartamento=Departamento(bodyRequest)
        print("Departamento a crear en la base de datos",elDepartamento.__dict__)
        self.repositorioDepartamento.save(elDepartamento)
        return True

    def buscarTodosLosDepartamentos(self):
        print("Buscando todos los departamentos en la base de datos...")
        return self.repositorioDepartamento.findAll()

    def buscarDepartamento(self,idObject):
        print("Buscar departamento",idObject)
        departamento=Departamento(self.repositorioDepartamento.findById(idObject))
        return departamento.__dict__

    def actualizarDepartamento(self, id,elDepartamento):
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
        departamentoActual.nombre = elDepartamento["nombre"]
        return self.repositorioDepartamento.save(departamentoActual)

    def deleteDepartamento(self,id):
        return self.repositorioDepartamento.delete(id)