"""Cadastro de propriedades e talhões do AgroMonitor (RF01)."""

talhoes = []


def cadastrar_talhao(propriedade, nome, area_ha):
    """Cadastra um talhão e devolve o registro criado."""
    if area_ha <= 0:
        raise ValueError("A área do talhão deve ser maior que zero.")
    talhao = {"id": len(talhoes) + 1, "propriedade": propriedade, "nome": nome, "area_ha": area_ha}
    talhoes.append(talhao)
    return talhao


def listar_talhoes(propriedade):
    """Lista os talhões de uma propriedade."""
    return [t for t in talhoes if t["propriedade"] == propriedade]


if __name__ == "__main__":
    cadastrar_talhao("Fazenda Boa Vista", "Talhão 1", 12.5)
    cadastrar_talhao("Fazenda Boa Vista", "Talhão 2", 8.0)
    for t in listar_talhoes("Fazenda Boa Vista"):
        print(t)
