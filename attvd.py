# Sistema de Gestão de Frota e Locação de Veículos

class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.__modelo = ""
        self.__placa = ""
        self.__valor_diaria = 0.0

        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    # Getter e Setter do modelo
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        if isinstance(modelo, str) and len(modelo.strip()) >= 3:
            self.__modelo = modelo.strip()
        else:
            print("Erro: o modelo deve ter pelo menos 3 caracteres.")

    # Getter e Setter da placa
    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        if isinstance(placa, str) and len(placa.strip()) >= 7:
            self.__placa = placa.strip().upper()
        else:
            print("Erro: a placa deve ter pelo menos 7 caracteres.")

    # Getter e Setter do valor da diária
    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_valor_diaria(self, valor):
        if (
            isinstance(valor, (int, float))
            and not isinstance(valor, bool)
            and valor > 0
        ):
            self.__valor_diaria = float(valor)
        else:
            print("Erro: o valor da diária deve ser positivo.")

    # Testes de validação
if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Dados válidos
    veiculo_valido = Veiculo("Honda Civic", "ABC1234", 180.00)

    print(
        f"Veículo criado: {veiculo_valido.get_modelo()} - "
        f"Placa: {veiculo_valido.get_placa()} - "
        f"Diária: R$ {veiculo_valido.get_valor_diaria():.2f}"
    )

    # 2. Teste de diária negativa
    print("\n--- Teste 1: Tentativa de diária negativa ---")
    veiculo_invalido = Veiculo("Toyota Corolla", "DEF5678", -150.00)

    print(
        f"Valor mantido com segurança: "
        f"R$ {veiculo_invalido.get_valor_diaria():.2f}"
    )

    # 3. Teste de modelo muito curto
    print("\n--- Teste 2: Tentativa de modelo inválido ---")
    veiculo_valido.set_modelo("AB")

    print("Modelo protegido:", veiculo_valido.get_modelo())
