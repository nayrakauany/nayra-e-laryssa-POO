class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def atualizar_telefone(self, telefone):
        if isinstance(telefone, str) and len(telefone.strip()) >= 10:
            self.__telefone = telefone.strip()
        else:
            print("Erro: telefone inválido.")


class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.__modelo = modelo
        self.__placa = placa
        self.__valor_diaria = valor_diaria

    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    def atualizar_valor_diaria(self, valor):
        if isinstance(valor, (int, float)) and not isinstance(valor, bool) and valor > 0:
            self.__valor_diaria = float(valor)
        else:
            print("Erro: valor da diária inválido.")


class Locacao:
    def __init__(self, cliente, veiculo, data_inicio, dias):
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__data_inicio = data_inicio
        self.__dias = dias

    def get_cliente(self):
        return self.__cliente

    def get_veiculo(self):
        return self.__veiculo

    def get_data_inicio(self):
        return self.__data_inicio

    def get_dias(self):
        return self.__dias

    def calcular_total(self):
        return self.__veiculo.get_valor_diaria() * self.__dias

    def confirmar(self):
        return self.__dias > 0


# Teste do sistema
if __name__ == "__main__":
    cliente = Cliente("Nayra Kauany", "12345678900", "19999999999")
    veiculo = Veiculo("Honda Civic", "ABC1234", 180.00)
    locacao = Locacao(cliente, veiculo, "23/10/2026", 3)

    print("=== SISTEMA DE LOCAÇÃO ===")
    print("Cliente:", locacao.get_cliente().get_nome())
    print("Veículo:", locacao.get_veiculo().get_modelo())
    print("Placa:", locacao.get_veiculo().get_placa())
    print("Data:", locacao.get_data_inicio())
    print("Dias:", locacao.get_dias())
    print(f"Valor total: R$ {locacao.calcular_total():.2f}")
    print("Locação confirmada:", locacao.confirmar())
