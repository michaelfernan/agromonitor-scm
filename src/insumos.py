"""Controle de aplicação de insumos do AgroMonitor (RF04).

Nova funcionalidade solicitada pelo time de operações da cooperativa.
"""

from datetime import date

from talhoes import talhoes

aplicacoes = []


def registrar_aplicacao(id_talhao, produto, dose_por_ha, data=None):
    """Registra a aplicação de um insumo em um talhão e calcula a quantidade total usada."""
    talhao = next((t for t in talhoes if t["id"] == id_talhao), None)
    if talhao is None:
        raise ValueError(f"Talhão {id_talhao} não encontrado.")
    if dose_por_ha <= 0:
        raise ValueError("A dose por hectare deve ser maior que zero.")
    aplicacao = {
        "id_talhao": id_talhao,
        "produto": produto,
        "dose_por_ha": dose_por_ha,
        "quantidade_total": round(dose_por_ha * talhao["area_ha"], 2),
        "data": data or date.today(),
    }
    aplicacoes.append(aplicacao)
    return aplicacao


def aplicacoes_do_talhao(id_talhao):
    """Lista as aplicações de insumos de um talhão."""
    return [a for a in aplicacoes if a["id_talhao"] == id_talhao]


if __name__ == "__main__":
    from talhoes import cadastrar_talhao

    t = cadastrar_talhao("Fazenda Boa Vista", "Talhão 1", 12.5)
    print(registrar_aplicacao(t["id"], "Fertilizante NPK 10-10-10", 2.0))
