# Automação de Busca de Vagas

Sistema desenvolvido em Python para automatizar a coleta, processamento e distribuição de vagas do LinkedIn.

A aplicação extrai informações relevantes das vagas, aplica filtros personalizados, armazena os resultados em banco de dados e envia notificações através de um bot do Telegram.

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de automatizar o monitoramento de vagas de emprego, reduzindo o trabalho manual de busca e organização das oportunidades encontradas.

As informações coletadas incluem:

* Título da vaga
* Requisitos
* Link da vaga

Após a coleta, os dados são tratados, armazenados e distribuídos automaticamente.

## Funcionalidades

* Coleta automatizada de vagas do LinkedIn
* Persistência de sessão utilizando cookies
* Extração de informações relevantes das vagas
* Filtros personalizados para refinar os resultados
* Limpeza e tratamento dos dados coletados
* Armazenamento em banco de dados utilizando SQLAlchemy
* Envio automático de notificações para o Telegram
* Arquitetura modular e organizada
* Separação de responsabilidades entre os componentes

## Tecnologias Utilizadas

* Python
* Playwright
* SQLAlchemy
* SQLite
* Telegram Bot API
* JSON
* Cookies de Navegação

## Estrutura do Projeto

```text
project/
│
├── controller/
├── service/
├── scraper/
├── cleaner/
├── notifier/
├── database/
│
├── session.json
├── main.py
└── requirements.txt
```

## Arquitetura

```text
LinkedIn
    │
    ▼
Scraper
    │
    ▼
Cleaner
    │
    ▼
Filtros
    │
    ▼
Banco de Dados
    │
    ▼
Telegram
```

## Funcionamento

1. O usuário realiza a autenticação manual no LinkedIn.
2. A sessão é armazenada em `session.json`.
3. O scraper acessa as páginas de vagas.
4. As informações relevantes são extraídas.
5. Os dados passam pelo processo de limpeza e tratamento.
6. Os filtros definidos são aplicados.
7. Os resultados são armazenados no banco de dados.
8. As vagas são enviadas automaticamente para o Telegram.

## Instalação

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio

pip install -r requirements.txt

playwright install
```

## Execução

```bash
python main.py
```

## Demonstração

Adicione capturas de tela ou GIFs demonstrando:

* Execução do scraper
* Registros armazenados no banco de dados
* Mensagens recebidas pelo Telegram

Exemplo:

```md
![Telegram](assets/telegram.png)

![Banco de Dados](assets/database.png)
```

## Desafios Técnicos

Durante o desenvolvimento foram aplicados conceitos como:

* Web Scraping
* Automação de Navegadores
* Persistência de Sessão
* Manipulação de Cookies
* Navegação em páginas dinâmicas
* Tratamento de Dados
* Integração com Banco de Dados
* Integração com APIs
* Arquitetura em Camadas
* Organização de Projetos Python

## Observações

Este projeto não realiza candidaturas automáticas.

Seu objetivo é automatizar a coleta, organização e distribuição de informações sobre vagas de emprego, mantendo a interação final sob responsabilidade do usuário.
