from Atencion import *
import random as rn
import numpy as np
arreglo = np.array([])


def salir():
    print("Sebastian Hurtado 04/07/2023")


def agregarAtencion(arreglo):
    ate = Atencion()
    c = False
    while not c:
        c = ate.setCodigo(input("Ingrese Codigo:"))
    c = False
    while not c:
        c = ate.setProducto(input("Ingrese tipo de producto (limones, peras, o manzanas:"))
    c = False
    while not c:
        try:
            c = ate.setValor(int(input("Ingrese valor del container:")))
        except BaseException as error:
            print(f"Error: {error}")
    ate.destino = input("Ingrese Destino:")
    return np.append(arreglo, ate)


def buscarAtencion(arreglo):
    codigo_container = input("Ingrese Codigo del container:")
    flag = False
    for Atencion in arreglo:
        if Atencion.codigo == codigo_container:
            print(f"Codigo: {Atencion.codigo}")
            print(f"Producto: {Atencion.producto}")
            print(f"Valor: {Atencion.valor}")
            print(f"Destino: {Atencion.destino}")
            print(f"Impuesto: {Atencion.impuesto}")
            flag = True
    if not flag:
        print("Error: No se encontro el producto")


def imprimirAtencion(arreglo):
    print("1) Certificado de embarque")
    print("2) Certificado de producto original")
    numero_folio = rn.randint(100, 5000)
    try:
        opc = int(input("Ingrese opcion:"))
        match opc:
            case 1:
                codigo_container = input("Ingrese Codigo del container:")
                flag = False
                for item in arreglo:
                    if item.codigo == codigo_container:
                        print("Certificado de Embarque")
                        print(f"Codigo: {item.codigo}")
                        print(f"Producto: {item.producto}")
                        print(f"Valor: {item.valor}")
                        print(f"Destino: {item.destino}")
                        print(f"Impuesto: {item.impuesto}")
                        print(f"Numero de Folio: {numero_folio}")
                        flag = True
                if not flag:
                    print("Error: No se encontro el producto")
            case 2:
                codigo_container = input("Ingrese Codigo del container:")
                flag = False
                for Atencion in arreglo:
                    if Atencion.codigo == codigo_container:
                        print("Certificado de Producto Original")
                        print(f"Codigo: {Atencion.codigo}")
                        print(f"Producto: {Atencion.producto}")
                        print(f"Valor: {Atencion.valor}")
                        print(f"Destino: {Atencion.destino}")
                        print(f"Impuesto: {Atencion.impuesto}")
                        print(f"Numero de Folio: {numero_folio}")
                        flag = True
                if not flag:
                    print("Error: No se encontro el producto")
    except BaseException as error:
        print(f"Error: {error}")


ciclo = True
while ciclo:
    print("Menu Frutas Cholito")
    print("1) Grabar")
    print("2) Buscar")
    print("3) Imprimir Atencion")
    print("4) Salir")
    try:
        opc = int(input("Ingrese una opcion:"))
        match opc:
            case 1:
                print("Grabar")
                arreglo = agregarAtencion(arreglo)
            case 2:
                print("Buscar")
                buscarAtencion(arreglo)
            case 3:
                print("Imprimir Atencion")
                imprimirAtencion(arreglo)
            case 4:
                ciclo = salir()
    except BaseException as error:
        print(f"Error: {error}")
