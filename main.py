from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCapitan import ControladorCapitan
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.Municipio import ControladorMunicipio
from Controladores.ControladorPuestoVotacion import ControladorPuestoVotacion
from Controladores.ControladorLider import ControladorLider
from Controladores.ControladorCapitanComuna import ControladorCapitancomuna
from Controladores.ControladorVotante import ControladorVotante

controladorCapitan = ControladorCapitan()
controladorDepartamento = ControladorDepartamento()
controladorMunicipio = ControladorMunicipio()
controladorPuestovotacion = ControladorPuestoVotacion()
controladorLider = ControladorLider()
controladorCapitancomuna = ControladorCapitancomuna()
controladorVotante = ControladorVotante()

app=Flask(__name__)
cors=CORS(app)
#Prueba tecnica desarrollada por Nelson Javier Amaya Guerrero
#Metodos para crear, buscar, actualizar y eliminar un capitan de la Base de Datos MongoDB/ Se exponen rutas
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ....."
    return jsonify(json)

@app.route("/capitan", methods=['POST'])
def crearCapitan():
    data=request.get_json()
    json=controladorCapitan.crearCapitan(data)
    return jsonify(json)

@app.route("/capitan", methods=['GET'])
def buscarTodos():
    result=controladorCapitan.buscarTodosCapitanes()
    if not result:
        return {"resultado": "No se encuentran capitanes"}
    else:
        return jsonify(result)

@app.route("/capitan/<string:id>", methods=['GET'])
def buscarCapitan(id):
    result=controladorCapitan.buscarCapitan(id)
    if result is None:
        return {"resultado": "No se encuentra capitan en la base de datos"}
    else:
        return jsonify(result)

@app.route("/capitan/<string:id>", methods=['PUT'])
def actualizaCandidato(id):
    data=request.get_json()
    json=controladorCapitan.actualizarCapitan(id,data)
    return jsonify(json)

@app.route("/capitan/<string:id>", methods=['DELETE'])
def eliminarCapitan(id):
    result=controladorCapitan.borrarCapitan(id)
    if result is None:
        return {"resutado": "No se elimino el capitan de la base de datos"}
    else:
        return jsonify(result)

#Metodos para crear, buscar, actualizar y eliminar un Departamento de Colombia de la Base de Datos MongoDB/ Se exponen rutas

@app.route("/departamento", methods=['POST'])
def creandoDepartamento():
    data = request.get_json()
    json = controladorDepartamento.crearDepartamento(data)
    return jsonify(json)

@app.route("/departamento", methods=['GET'])
def buscarTodosDeptos():
    result = controladorDepartamento.buscarTodosLosDepartamentos()
    if result is None:
        return {"resultado":"No se encuentra departamento en la base de datos"}
    else:
        return jsonify(result)

@app.route("/departamento/<string:id>", methods=['GET'])
def buscarDepartamento(id):
    result = controladorDepartamento.buscarDepartamento(id)
    if result is None:
        return {"resultado":"No se encuentra departamento en la base de datos"}
    else:
        return jsonify(result)

@app.route("/departamento/<string:id>", methods=['PUT'])
def actualizandoDepartamento(id):
    data = request.get_json()
    json = controladorDepartamento.actualizarDepartamento(id,data)
    return jsonify(json)

@app.route("/departamento/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
    result = controladorDepartamento.deleteDepartamento(id)
    if result is None:
        return {"resultado":"No se elimino el departamento de la base de datos"}
    else:
        return jsonify(result)

#Metodos para crear, buscar, actualizar y eliminar un Municipio de Colombia de la Base de Datos MongoDB/ Se exponen rutas

@app.route("/municipio", methods=['POST'])
def creandoMunicipio():
    data = request.get_json()
    json = controladorMunicipio.crearMunicipio(data)
    return jsonify(json)

@app.route("/municipio", methods=['GET'])
def buscarTodosLosMunicipios():
    result = controladorMunicipio.buscarMunicipio()
    if not result:
        return {"resultado":"No se encuentran municipios"}
    else:
        return jsonify(result)

@app.route("/municipio/<string:id>", methods=['GET'])
def buscarUnMunicipio(id):
    result = controladorMunicipio.buscarUnMunicipio(id)
    if result is None:
        return {"resultado":"No se encuentran datos"}
    else:
        return jsonify(result)

@app.route("/municipio/<string:id>", methods=['PUT'])
def actualizandoMunicipio(id):
    data = request.get_json()
    json = controladorMunicipio.actualizarMunicipio(id,data)
    return jsonify(json)

@app.route("/municipio/<string:id>", methods=['DELETE'])
def eliminarMunicipio(id):
    result = controladorMunicipio.deleteMunicipio(id)
    if result is None:
        return {"resultado": "No se elimina el municipio en base de datos!"}
    else:
        return jsonify(result)

@app.route("/municipio/<string:idMunicipio>/departamento/<string:idDepartamento>", methods=['PUT'])
def asignarDepartamentoAMunicipio(idMunicipio,idDepartamento):
    result = controladorMunicipio.asignarDepartamento(idMunicipio,idDepartamento)
    return jsonify(result)

#Metodos para crear, buscar, actualizar y eliminar puestos de votacion de Colombia de la Base de Datos MongoDB/ Se exponen rutas

@app.route("/puestovotacion", methods=['POST'])
def crearPuesto():
    data = request.get_json()
    json = controladorPuestovotacion.crearPuestovotacion(data)
    return jsonify(json)

@app.route("/puestovotacion",methods=['GET'])
def buscarTodosPuestos():
    result = controladorPuestovotacion.buscarTodosLosPuestos()
    if not result:
        return {"resultado":"No se encuentran puestos"}
    else:
        return jsonify(result)

@app.route("/puestovotacion/<string:id>", methods=['GET'])
def buscarPuesto(id):
    result = controladorPuestovotacion.buscarUnPuesto(id)
    if result is None:
        return {"result":"No se encuentran puesto de votacion"}
    else:
        return jsonify(result)

@app.route("/puestovotacion/<string:id>", methods=['PUT'])
def actualizandoPuesto(id):
    data = request.get_json()
    json = controladorPuestovotacion.actualizarPuesto(id,data)
    return jsonify(json)

@app.route("/puestovotacion/<string:id>", methods=['DELETE'])
def eliminandoPuesto(id):
    result = controladorPuestovotacion.borrarPuestoVotacion(id)
    if result is None:
        return {"resultado": "No se elimina puesto"}
    else:
        return jsonify(result)

@app.route("/puestovotacion/<string:idPuestovotacion>/municipio/<string:idMunicipio>", methods=['PUT'])
def asignarMunicipioAPuesto(idPuestovotacion,idMunicipio):
    result=controladorPuestovotacion.asignarMunicipio(idPuestovotacion,idMunicipio)
    return jsonify(result)

#Metodos para crear, buscar, actualizar y eliminar lideres de la Base de Datos MongoDB/ Se exponen rutas

@app.route("/lider", methods=['POST'])
def creandoLider():
    data = request.get_json()
    json = controladorLider.crearLider(data)
    return jsonify(json)

@app.route("/lider", methods=['GET'])
def buscarTodosLider():
    result = controladorLider.buscarTodosLosLideres()
    if not result:
        return {"resultado": "No se encuentran lideres"}
    else:
        return jsonify(result)

@app.route("/lider/<string:id>", methods=['GET'])
def buscarUno(id):
    result = controladorLider.buscarUnLider(id)
    if result is None:
        return {"resultado":"No se encuentra lider"}
    else:
        return jsonify(result)

@app.route("/lider/<string:id>", methods=['PUT'])
def actualizandoLider(id):
    data = request.get_json()
    json = controladorLider.actualizarLider(id,data)
    return jsonify(json)

@app.route("/lider/<string:id>", methods=['DELETE'])
def eliminarLider(id):
    result = controladorLider.deleteLider(id)
    if result is None:
        return {"resultado":"No se elimino lider"}
    else:
        return jsonify(result)

@app.route("/lider/<string:idLider>/capitan/<string:idCapitan>",methods=['PUT'])
def asignarCapiALider(idLider,idCapitan):
    result = controladorLider.asignarCapitan(idLider,idCapitan)
    return jsonify(result)

#Metodos para crear, buscar, actualizar y eliminar Capitanes comuna de la Base de Datos MongoDB/ Se exponen rutas

@app.route("/capitancomuna/municipio/<string:idMunicipio>/capitan/<string:idCapitan>", methods=['POST'])
def crearCapComuna(idMunicipio, idCapitan):
    data = request.get_json()
    json=controladorCapitancomuna.crearCapitanComuna(data,idMunicipio,idCapitan)
    return jsonify(json)

@app.route("/capitancomuna", methods=['GET'])
def buscarTodosLoscapcom():
    json=controladorCapitancomuna.buscarTodosCapcom()
    return jsonify(json)

@app.route("/capitancomuna/<string:id>",methods=['GET'])
def buscarPorUnID(id):
    json=controladorCapitancomuna.buscarUnCapcom(id)
    return jsonify(json)

@app.route("/capitancomuna/<string:id>",methods=['DELETE'])
def eliminarCapcom(id):
    json=controladorCapitancomuna.deleteCapcom(id)
    return jsonify(json)

#Metodos para crear, buscar, actualizar y eliminar votante de la Base de Datos MongoDB/ Se exponen rutas

@app.route("/votante", methods=['POST'])
def creandoVotante():
    data = request.get_json()
    json = controladorVotante.crearVotante(data)
    return jsonify(json)

@app.route("/votante", methods=['GET'])
def buscarTodosLosVotantes():
    result = controladorVotante.buscarTodosLosVotantes()
    if not result:
        return {"resultado":"No se encuentran candidatos"}
    else:
        return jsonify(result)

@app.route("/votante/<string:id>", methods=['GET'])
def buscarUnVotante(id):
    result = controladorVotante.buscarUnVotante(id)
    if result is None:
        return {"resultado":"No se encuentran el votante con ese ID"}
    else:
        return jsonify(result)

@app.route("/votante/<string:id>", methods=['PUT'])
def actualizandoUnVotante(id):
    data = request.get_json()
    json = controladorVotante.actualizarVotante(id,data)
    return jsonify(json)

@app.route("/votante/<string:id>", methods=['DELETE'])
def eliminarVotante(id):
    result = controladorVotante.deleteVotante(id)
    if result is None:
        return {"resultado":"No se elimino el votante de la base de datos"}
    else:
        return jsonify(result)

#Metodos para asignarle al votante el lider, municipio, puesto de votacion

@app.route("/votante/<string:idVotante>/lider/<string:idLider>",methods=['PUT'])
def asignacionLiderAVotante(idVotante,idLider):
    result=controladorVotante.asignarLiderAVotante(idVotante,idLider)
    return jsonify(result)

@app.route("/votante/<string:idVotante>/municipio/<string:idMunicipio>",methods=['PUT'])
def asignacionMunicipioAVotante(idVotante,idMunicipio):
    result=controladorVotante.asignarMunicipioAVotante(idVotante,idMunicipio)
    return jsonify(result)

@app.route("/votante/<string:idVotante>/puesto/<string:idPuesto>",methods=['PUT'])
def asignacionPuestodeVotacion(idVotante,idPuesto):
    result=controladorVotante.asignarPuestoDeVotacionAVotante(idVotante,idPuesto)
    return jsonify(result)

#configuracion de la url expuesta para el servicio obteniendo datos llave/valor o JSON


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
