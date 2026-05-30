from scraper.buscar_vagas import buscar_vagas
from services.servico_vaga import Config_db_vagas
def salvar():
    titulo,link,requisitos = buscar_vagas()
    Config_db_vagas.salvar_vagas(titulo,link,requisitos)

