from playwright.sync_api import sync_playwright, expect
import time

#pip install playwright

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
#abrir o navegador
    pagina = navegador.new_page()

#navegar para uma página
    #pagina.goto("http://iess.paineldoprofessor.com.br")
    #pagina.goto("https://suap.pit.pi.gov.br")   #acessar um link específico
    pagina.goto("https://suap.pit.pi.gov.br")

#Pegar informações da página

    print(pagina.title())

#Como selecionar um elemento na tela

    #1° forma:  xpath = não recomenda, porque se alterar um caminho pode quebrar tudo
    #pagina.locator('expath:/html/body/div[1]/main/div[2]/form/div[5]/input')

    #2° forma: get_by (através do gerador de código)
    #pagina.locator("div").filter(has_text="Quero aprender").nth(1).click()
    #pagina.get_by_role("link", name="Fale Conosco").click()

#Preencher um formulário
    pagina.get_by_role("textbox", name="Usuário:").fill("coloque o usuário aqui")
    pagina.get_by_role("textbox", name="Senha:").fill("coloque a senha aqui")
    pagina.get_by_role("button", name="Acessar").click()
    pagina.get_by_role("link", name="Meus Dados").click()
    pagina.get_by_role("link", name="Documentos ").click()
    
    
  #esperar um elemento na tela 
    novo_botao = pagina.get_by_role("link", name="Declaração de Matrícula")
    expect(novo_botao).to_be_visible()
    novo_botao.click()




    time.sleep(60)
    navegador.close()