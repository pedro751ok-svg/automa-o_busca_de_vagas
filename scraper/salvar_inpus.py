from playwright.sync_api import sync_playwright

def buscar_vagas():
    with sync_playwright() as pay:
        navegador = pay.chromium.launch(headless = False)
        contexto = navegador.new_context()
        pagina = contexto.new_page()
        pagina.goto("https://www.linkedin.com/jobs/search-results/?currentJobId=4414051218&keywords=devops&origin=JOBS_HOME_SEARCH_BUTTON")
        pagina.wait_for_timeout(5000)
        input("")

        contexto.storage_state(path="session.json")
        navegador.close()
buscar_vagas()
