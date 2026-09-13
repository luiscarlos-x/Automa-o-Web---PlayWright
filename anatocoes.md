    pagina.goto()  #acessar um link específico

    pagina.go_back #voltar para uma página anterior

    pagina.go_forward 
    #avançar para uma página que deu go_back e ele retorona

# teste 01 - SUAP
    from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    #abrir o navegador
    pagina = navegador.new_page()

    #navegar para uma página
    #pagina.goto("http://iess.paineldoprofessor.com.br")
    pagina.goto("https://suap.pit.pi.gov.br")   #acessar um link específico
    
    # Esperar a página carregar completamente
    pagina.wait_for_load_state("networkidle")
    time.sleep(2)
    
    # Tentar preencher usando locator por ID
    pagina.locator("#id_username").fill("20261BIA0006")
    pagina.locator("#id_password").fill("luis22almeida")
    
    # Clicar no botão Acessar
    pagina.locator("input[type='submit'][value='Acessar']").click()

    time.sleep(4)
    navegador.close()