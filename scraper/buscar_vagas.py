from playwright.sync_api import sync_playwright
from cleaner.limpar_vagas import Limpador


def buscar_vagas():
    lista_titulos = []
    lista_link = []
    lista_requisitos = []
    with sync_playwright() as pay:
        navegador = pay.chromium.launch(headless = False)
        contexto = navegador.new_context(storage_state="session.json")
        pagina = contexto.new_page()
        pagina2 = contexto.new_page()
        pagina.goto("https://www.linkedin.com/jobs/search-results/?currentJobId=4420212436&keywords=%28est%C3%A1gio%20OR%20junior%20OR%20trainee%29%20AND%20%28backend%20OR%20devops%20OR%20devsecops%20OR%20%22cloud%20engineer%22%29&origin=JOBS_HOME_SEARCH_BUTTON")
        pagina.wait_for_timeout(9000)
        titulo = pagina.query_selector_all("span[aria-hidden='true']")
        cards = pagina.query_selector_all("[componentkey^='job-card-component-ref-'][role='button']")

        for i in titulo:

            texto = i.inner_text().split("\n")[0]
           
            if not texto.strip().startswith("há") and texto.strip() and texto != "Mensagens":
                lista_titulos.append(texto)
            
        for card in cards:
            chave = card.get_attribute('componentkey')
            id_vaga = chave.split('-')[-1]
            lista_link.append("https://www.linkedin.com/jobs/view/" + id_vaga)
        
        for link in lista_link:
            try:
                pagina2.goto(link)
                pagina2.wait_for_timeout(4000)
 
  
                requisitos = pagina2.query_selector('[data-testid="expandable-text-box"]')

                requisito = requisitos.inner_text()
                requisito1 = Limpador(requisito).limpar_texto()
            
                lista_requisitos.append(requisito1)
            except:
                lista_requisitos.append("nao encontrado")
          



        for t ,l,r in zip(lista_titulos,lista_link,lista_requisitos):
            print(t,l,r)
    return lista_titulos,lista_link,lista_requisitos

