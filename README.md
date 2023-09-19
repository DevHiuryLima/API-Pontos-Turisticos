# API Pontos Turisticos

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/DevHiuryLima/API-Pontos-Turisticos?color=A30000">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/DevHiuryLima/API-Pontos-Turisticos?color=A30000">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/DevHiuryLima/API-Pontos-Turisticos?color=A30000">

  <img alt="Github issues" src="https://img.shields.io/github/issues/DevHiuryLima/API-Pontos-Turisticos?color=A30000" />

  <img alt="Github forks" src="https://img.shields.io/github/forks/DevHiuryLima/API-Pontos-Turisticos?color=A30000" />

  <img alt="Github stars" src="https://img.shields.io/github/stars/DevHiuryLima/API-Pontos-Turisticos?color=A30000" />
</p>

&#xa0;

## 📖 Sobre

<p align="justify">
Esta API é um projeto durante um curso da 
<a href="https://www.udemy.com/" target="_blank">Udemy</a> 
chamado <a href="https://www.udemy.com/course/apis-restful-com-django-rest-framework/" target="_blank">Criando poderosas 
API's RESTful com Django Rest Framework</a>. Neste aprendi dominar o Django Rest Framework, uma poderosa ferramenta que 
torna o desenvolvimento de APIs mais produtivo e eficiente.  Compreendi todos os conceitos essenciais das APIs RESTful, 
incluindo viewsets, serializers, respostas, permissões, autenticação por token, consumo de APIs e muito mais.</p>

<p align="justify">A API de Pontos Turísticos desenvolvida possui as seguintes características:</p>

- RESTful Web API para exposição de pontos turísticos de uma região;
- Propor um novo ponto turístico;
- Moderação dos pontos turísticos cadastrados;
- Listagem básica dos pontos turísticos ( Lista resumida );
- Listagem completa dos pontos turísticos;
- Detalhe de um ponto turístico;
- Atualização de um ponto turístico por usuários autorizados;
- Deleção de um ponto turístico por usuários autorizados.

⚠️ Aviso: A API foi hospedada no Heroku apenas durante o curso, com o propósito de aprendizado.

&#xa0;

## :computer: Tecnologias

#### **Web** 
  - **[Python 3][python]**
  - **[Django][django]**
  - **[Django Rest Framework][django_rest_framework]**
 
  \* Consulte o arquivo <kbd>[requirements-dev.txt](lhttps://github.com/DevHiuryLima/API-Pontos-Turisticos/blob/main/requirements-dev.txt)</kbd> para obter as dependências específicas do projeto.
  
#### **Banco de Dados** 
  
  - **[SQLite][sqlite3]**
  
#### **Ferramentas e Utilitários**

  - IDE: **[PyCharm][pycharm]**
  - SGBD: **[Beekeeper][beekeeper]**
  - Teste de API: **[Insomnia][insomnia]**
  - Ícones: **[Markdown Emoji][markdown_emoji]**

&#xa0;

## 🎨 Layout

Essas são apenas algumas telas de documentação da API do Django Rest Framework.
<div align="center">  
    <a href="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/8ec04471-1858-4344-a3b5-1f92a6590a4b" target="_blank" >
      <img src="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/8ec04471-1858-4344-a3b5-1f92a6590a4b" title="Tela inicial que mostra uma visão geral dos principais endpoints da API." alt="Tela inicial que mostra uma visão geral dos principais endpoints da API.">
    </a>
</div>

<div align="center">
  <a href="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/8ec04471-1858-4344-a3b5-1f92a6590a4b" target="_blank" >
    <img src="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/d39136e6-7e50-41bb-b81b-662001e42041" title="Tela de 'Detail View' de um Ponto Turístico. Uma tela que exibe os detalhes de um ponto." alt="Tela de 'Detail View' de um Ponto Turístico. Uma tela que exibe os detalhes de um ponto.">
  </a>
</div>

<div align="center">
  <a href="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/8dd41731-df88-4794-8206-8c2b448c7ebd" target="_blank" >
    <img src="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/8dd41731-df88-4794-8206-8c2b448c7ebd" title="Tela de 'List View' de Atração. Uma tela que exibe todas as atrações." alt="Tela de 'List View' de Atração. Uma tela que exibe todas as atrações.">
  </a>
</div>

<div align="center">
  <a href="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/7ae0ce70-5a6e-449a-ac00-46e14fc0b7e8" target="_blank" >
    <img src="https://github.com/DevHiuryLima/API-Pontos-Turisticos/assets/69491885/7ae0ce70-5a6e-449a-ac00-46e14fc0b7e8" title="Tela de 'List View' de Endereço. Uma tela que exibe todos os endereços." alt="Tela de 'List View' de Endereço. Uma tela que exibe todos os endereços.">
  </a>
</div>

&#xa0;

## 🚀 Como executar o projeto

#### Pré-requisitos
  - É **essencial** possuir o **[Python 3][python]** instalado na máquina.
  - É **nescessário** ter o `pipenv` instalado.

&#xa0;

1. Faça um clone :

```sh
  $ git clone https://github.com/DevHiuryLima/Curso-de-Django.git
```

&#xa0;

2. Instale as dependências:

  - **No Linux:**
```
  $ python -m venv venv
```

```
  $ source venv/Scripts/activate
``` 

```
  $ ./activate
```

  Volte para a pasta raiz e execute o comando:
```
  $ pip install -r requirements.txt
```

&#xa0;

  - **No windows**
```
  $ python -m venv venv
```

```
  $ cd venv\Scripts
```

```
  $ ./activate
```

  Volte para a pasta raiz e execute o comando:
```
  $ pip install -r requirements.txt
```

&#xa0;

⚠️ Aviso: Somente se faltar o Django no arquivo `requirements-dev.txt`, (dentro da pasta raiz) execute o comando:
```
  $ pip install Django
```

&#xa0;

3. Crie as migrations e execute-as:

```
  $ python manage.py makemigrations
```

```
  $ python manage.py migrate
```

&#xa0;

4. Crie um super user:

```
  $ python manage.py createsuperuser
```

&#xa0;

5. Execute a aplicação 

 Pelo terminal na pasta raiz do projeto execute o comando.
```
  $ python manage.py runserver
```

&#xa0;

## :octocat: Como contribuir

1. Faça um **fork** do projeto.
1. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
1. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
1. Envie as suas alterações: `git push origin my-feature`
> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](https://github.com/firstcontributions/first-contributions)

&#xa0;

[Voltar para o topo](https://github.com/DevHiuryLima/API-Pontos-Turisticos#top)



<!-- Techs Web -->

[python]: https://www.python.org/
[django]: https://www.djangoproject.com/
[django_rest_framework]: https://www.django-rest-framework.org/



<!-- Techs Server -->

[sqlite3]: https://github.com/mapbox/node-sqlite3



<!-- Techs Utilitárias -->

[pycharm]: https://www.jetbrains.com/pt-br/pycharm/
[beekeeper]: https://www.beekeeperstudio.io/
[insomnia]: https://insomnia.rest/
[markdown_emoji]: https://github.com/ikatyang/emoji-cheat-sheet
