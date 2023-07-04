class Atencion:
    codigo = ''
    producto = ''
    valor = 0
    destino = ''
    impuesto = 0


    def __init__(self):
        self.codigo = 'AA-01'
        self.producto = 's/n'
        self.valor = 900000
        self.destino = 's/d'
        self.impuesto = 0.05

    def setCodigo(self, codigo):
        if len(codigo) == 5:
            if codigo[0:2].isalpha() and codigo[3:4].isdigit():
                self.codigo = codigo
                return True
            else:
                print("Error: Codigo debe tener largo de 5 (AA-01)")
                return False


    def setProducto(self, producto):
        if producto == 'limones' or producto == 'peras' or producto == 'manzanas':
            self.producto = producto
            return True
        else:
            print("Error: Tipo de producto no valido (limones, peras o manzanas")
            return False

    def setValor(self, valor):
        if 900000 <= valor <= 4500000:
            self.valor = valor
            return True
        else:
            print("Error: Valor debe estar entre 900.000 y 4.500.000")
            return False

    def setImpuesto(self, valor, impuesto):
        if valor >= 1200000:
            impuestos = 0.1 * valor
            self.impuesto = impuestos
            return True
        else:
            impuestos = 0.05 * valor
            self.impuesto = impuestos
            return False