import os


def carregar_recorde(caminho):
    """Carrega o recorde do arquivo indicado. Retorna 0 se não existir ou em erro."""
    try:
        if not os.path.exists(caminho):
            # garante diretório
            pasta = os.path.dirname(caminho)
            if pasta and not os.path.exists(pasta):
                os.makedirs(pasta, exist_ok=True)
            with open(caminho, "w", encoding="utf-8") as f:
                f.write("0")
            return 0

        with open(caminho, "r", encoding="utf-8") as f:
            texto = f.read().strip()
            return int(texto) if texto.isdigit() else 0
    except Exception:
        return 0


def salvar_recorde(caminho, valor):
    """Salva o recorde (int) no arquivo indicado."""
    try:
        pasta = os.path.dirname(caminho)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(str(int(valor)))
    except Exception:
        # falhar silenciosamente é aceitável aqui; o jogo continua
        pass
