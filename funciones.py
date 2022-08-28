
def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} Creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")

def pedirDatosRegistro():
    global creditos, codigo
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("ingrese codigo: ")
        if len(codigo)==6:
            codigoCorrecto=True
        else:
            print("codigo es de 6 digitos")

    nombre=input("ingrese nombre: ")

    creditoCorrecto= False
    while(not creditoCorrecto):
        creditos = input("ingrese creditos: ")
        if creditos.isnumeric():
            if int(creditos)>0:
                creditoCorrecto = True
                creditos = int(creditos)
            else:
                print("El credito debe ser mayor a 0")

        else:
            print("credito es numerico")

    curso= (codigo,nombre,creditos)
    return curso



def pedirDatosActualizacion(cursos):


    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese codigo a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("ingrese nombre a modificar: ")
        creditoCorrecto = False
        while (not creditoCorrecto):
            creditos = input("ingrese creditos a modificar: ")
            if creditos.isnumeric():
                if int(creditos) > 0:
                    creditoCorrecto = True
                    creditos = int(creditos)
                else:
                    print("El credito debe ser mayor a 0")

            else:
                print("credito es numerico")

        curso = (codigoEditar, nombre, creditos)

    else:
        curso = None


    return curso







def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar=input("Ingrese codigo a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo=True
            break
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar










