# Serviço de gateway

O serviço de gateway faz a conexão entre os serviços disponíveis e o front end. Com a existência do gateway, o front end precisa conehcer apenas um serviço. Caso algum dos serviços seja alterado, é possível manter a mesma interface com o front-end realizando a adaptação no gateway. Por enquanto, o gateway apenas redireciona as chamadas para as devidas rotas.
O gateway também unifica toda a documentação dos serviços em uma única URL.

> NOTA: Para utilizar o gateway, todos os outros serviços precisam estar em execução.

## Instalação local

A utilização local do serviço requer que sejam criadas variáveis de ambiente com a URL de cada serviço. Para isso, execute os seguintes comandos no PowerShell:

```bash
$env:PSITEST_AUTH="http://localhost:8002"
$env:PSITEST_CADASTRO="http://localhost:8003"
$env:PSITEST_QUESTIONARIOS="http://localhost:8004"
$env:PSITEST_RESPOSTAS="http://localhost:8005"
```

> NOTA: Caso os serviços estejam executando em outro endereço, subistua pelo endereço correto.

Para utilizar o serviço localmente, é recomendado a criação de um ambiente virtual.

```bash
python -m venv .venv
.venv/scripts/activate
```

Após a criação do ambiente virtual, instale as dependências do projeto.

```bash
pip install -r requirements.txt
```

### Execução

Para executar o servidor, utilize o comando:

```bash
fastapi run app --port 8000
```

O servidor estará disponível em `http://localhost:8000`.

## Utilizando via Docker

Para executar via Docker, é necessário ter o Docker instalado e em execução. Também é necessário que exista uma rede chamada `psitest`. A rede deve ser criada uma única vez com o seguinte comando:

```bash
docker network create psitest
```

Após a criação da rede, execute o seguinte comando para criar a imagem do serviço:

```bash
docker compose up
```

O serviço estará disponível em `http://localhost:8000`.

