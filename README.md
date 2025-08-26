
---

# Test Automation Practice Page

## Descrição

Este projeto contém uma suíte de testes automatizados para a página **Automation Practice**, utilizando **Selenium WebDriver** e **pytest**.
O objetivo é validar funcionalidades como login, campos de entrada, seleção de opções, upload de arquivos, modais e iframes.

---

## Estrutura do Projeto

```
TEST AUTOMATION PRACTICE PAGE/
│
├─ __pycache__/               # Cache do Python
├─ .pytest_cache/             # Cache do pytest
├─ confest.py                 # Configurações e fixtures do pytest
├─ CT001_login_valido_test.py
├─ CT002_login_invalido_test.py
├─ CT003_login_campo_vazio_test.py
├─ CT004_option_selection_test.py
├─ CT005_actions_buttons_test.py
├─ CT006_checkbox_test.py
├─ CT007_data_test.py
├─ CT008_hiperlink_test.py
├─ CT009_hover_test.py
├─ CT010_iframe_test.py
├─ CT011_upload_test.py
├─ CT012_modal_test.py
├─ report.html                # Relatório gerado após execução dos testes
```

---

## Pré-requisitos

* Python 3.13+
* Selenium (`pip install selenium`)
* pytest (`pip install pytest`)
* pytest-html (`pip install pytest-html`)
* Microsoft Edge WebDriver ou outro navegador compatível

---

## Como Executar os Testes

No terminal, execute o seguinte comando na raiz do projeto:

```bash
pytest -v --html=report.html --self-contained-html
```

* `-v`: modo verbose, exibe cada teste e seu resultado.
* `--html=report.html`: gera um relatório HTML detalhado.
* `--self-contained-html`: gera o relatório com todos os recursos embutidos.

---

## Funcionalidades Testadas

1. **Login**

   * Validação de login válido
   * Validação de login inválido
   * Campos vazios

2. **Opções e Interações**

   * Seleção de opções (`<select>` e radio buttons)
   * Botões de ação (alerts, confirm e prompt)
   * Checkbox e múltiplas opções
   * Hover e menus interativos

3. **Campos Especiais**

   * Input de datas
   * Upload de arquivos

4. **Navegação e Estrutura**

   * Links e hiperlinks
   * Iframes e conteúdo aninhado
   * Modais

---

## Boas Práticas Utilizadas

* Organização de testes por funcionalidade
* Uso de **fixtures** no `conftest.py` para setup/teardown
* Espera explícita (`WebDriverWait`) para elementos dinâmicos
* Assert de visibilidade e conteúdo
* Relatórios HTML detalhados com pytest-html

---
## Plano de Testes

| **Seção**                    | **Descrição**                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Id**                       | 002                                                                                                                                                                                                                                              |
| **Objetivo**                 | Acessar a página Test Automation e testar funcionalidades, como login, action buttons, checkbox, modal                                                                                                                                           |
| **Ferramentas**              | Selenium, Pytest                                                                                                                                                                                                                                 |
| **Critérios de Aceite**      | Página *Test Automation* disponível: “Test Automation Practice Page”                                                                                                                                                                             |
| **Escopo**                   | - Validação do login com senha correta e incorreta <br> - Validação da sessão do botão de seleção <br> - Validação dos buttons *Show alert*, mudar cor do fundo <br> - Upload de arquivo, checkbox, date picker, hiperlink, hover, iframe, modal |
| **Fora do Escopo**           | Funcionalidade de *Tabbet Navigation*                                                                                                                                                                                                            |
| **Resultado Geral Esperado** | Todas as funcionalidades funcionando conforme solicitado       

## Casos de Teste
|

| **Id** | **Objetivo**                                          | **Pré-condições**                         | **Passos**                                                          | **Resultado Esperado**                                                                                           | **Prioridade** |
| ------ | ----------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------- | ------------------------------

---------------------------------------------------------------------------------- | -------------- |
| 001    | Validar a funcionalidade de Login com senha válida    | Estar com a Página Test Automation aberta | 1. Digitar Username: `admin`, Senha: `1234` <br> 2. Clicar em Login | Mensagem exibida: *“Login successful!”*                                                                          | Alta           |
| 002    | Validar a funcionalidade de Login com senha inválida  | Estar com a Página Test Automation aberta | 1. Digitar Username: `admin`, Senha: `1111` <br> 2. Clicar em Login | Mensagem exibida: *“Incorrect username or password.”*                                                            | Alta           |
| 003    | Validar a funcionalidade de Login com campo em branco | Estar com a Página Test Automation aberta | 1. Acessar Login Form <br> 2. Clicar em Login                       | Aviso exibido: *“Preencha esse campo”*                                                                           | Médio          |
| 004    | Validar se o dropdown de opções funciona corretamente | Estar com a Página Test Automation aberta | 1. Acessar *Option Selection* <br> 2. Selecionar uma opção          | Ao abrir mostra todas opções; ao selecionar, fecha e mantém opção visível                                        | Média          |
| 005    | Validar se os botões de ação funcionam corretamente   | Estar com a Página Test Automation aberta | 1. Em Action Buttons, clicar em *Show alert* e confirmar            | Alerta exibido: *“This is a test alert!”* <br> Ao clicar em OK, fecha; outros botões funcionam conforme descrito | Média          |
| 006    | Validar se os checkbox funcionam normalmente          | Estar com a Página Test Automation aberta | 1. Clicar em Feature 1 e 2 <br> 2. Clicar novamente para desmarcar  | Ao clicar, checkbox seleciona/deseleciona corretamente                                                           | Média          |
| 007    | Validar se é permitido colocar a data corretamente    | Estar com a Página Test Automation aberta | 1. Digitar data no formato `dd/mm/aaaa`                             | Data fica visível corretamente                                                                                   | Média          |
| 008    | Validar se o link externo abre                        | Estar com a Página Test Automation aberta | 1. Clicar em *Go to Example.com*                                    | Nova aba abre, título exibido: *“Example Domains”*                                                               | Baixa          |
| 009    | Validar se o Hover funciona corretamente              | Estar com a Página Test Automation aberta | 1. Passar o mouse sobre *Hover over this menu*                      | Exibe 3 opções ocultas                                                                                           | Baixa          |
| 010    | Interagir com o iFrame                                | Estar com a Página Test Automation aberta | 1. Acessar iframe e clicar em *More information...*                 | Nova aba abre com mensagem *“Example Domains”*                                                                   | Baixa          |
| 011    | Validar o Upload de arquivo                           | Estar com a Página Test Automation aberta | 1. Clicar no botão de upload <br> 2. Selecionar arquivo             | Exibir mensagem: *“Selected File: \[nome do arquivo]”*                                                           | Baixa          |
| 012    | Validar se o Modal abre e fecha corretamente          | Estar com a Página Test Automation aberta | 1. Clicar em *Open Modal* <br> 2. Fechar com *Close Modal*          | Exibir mensagem: *“This is a modal window.”* e modal fechar após clicar em “x”                                   | Baixa          |

---

## Relatório

* Após execução, o arquivo `report.html` é gerado.
* Exibe:

  * Status de cada teste (pass/fail/skip)
  * Tempo de execução
  * Tracebacks detalhados em caso de falha
  * Informações do ambiente de teste (Python, plataforma, pacotes, plugins)

---

## Observações

* Inputs de arquivo (`<input type="file">`) podem receber caminho absoluto.
* Para modais, valida-se **primeiro o conteúdo**, depois fecha-se o modal e verifica-se que desapareceu.
* Para iframes aninhados, sempre trocar de frame na ordem correta e retornar para o `default_content()` ao final.

---

