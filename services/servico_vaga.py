from scraper.buscar_vagas import buscar_vagas
from database.db import Vagas,session
from notifier.notificação_telegram import start
class Config_db_vagas:

    @staticmethod
    def salvar_vagas(titulo,link,requisitos):
        for titulo,link,requisitos in zip(titulo,link,requisitos):
            with session() as sessao:
                vaga =Vagas(
                    titulo = titulo,
                    link = link,
                    requisitos = requisitos
                    )
                sessao.add(vaga)
                sessao.commit()
            start(f"Título: {titulo[:100]} \nLink: {link} \nRequisitos: {requisitos[:500]}")
    @staticmethod
    def mostar_table_vagas(text,link):
        with session() as sessao:
            vaga = sessao.query(Vagas).filter_by(link=link).first()
            if not vaga:
                return "vaga nao encotrada"
            return vaga
