"""Registro de ocorrências de pragas do AgroMonitor (RF02 e RF03)."""

from datetime import date

ocorrencias = []
NIVEIS = ("baixo", "médio", "alto")


def registrar_ocorrencia(id_talhao, praga, nivel, data=None):
    """Registra uma ocorrência de praga em um talhão."""
    if nivel not in NIVEIS:
        raise ValueError(f"Nível inválido. Use: {', '.join(NIVEIS)}.")
    ocorrencia = {"id_talhao": id_talhao, "praga": praga, "nivel": nivel, "data": data or date.today()}
    ocorrencias.append(ocorrencia)
    return ocorrencia


def historico_talhao(id_talhao):
    """Devolve as ocorrências de um talhão, da mais recente para a mais antiga."""
    return sorted((o for o in ocorrencias if o["id_talhao"] == id_talhao), key=lambda o: o["data"], reverse=True)
