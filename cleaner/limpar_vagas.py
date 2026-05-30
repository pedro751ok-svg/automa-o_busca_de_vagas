class Limpador:
    def __init__(self,texto):
        self.texto = texto
    def limpar_texto(self):
        return self.texto.replace("… mais","").strip()