# Cadastro de Alunos

Este é um projeto simples de cadastro de alunos feito com Python, utilizando a biblioteca `ttkbootstrap` para a criação de uma interface gráfica. O projeto permite cadastrar alunos, registrar notas e visualizar o boletim e notas de um aluno.

## Funcionalidades

1. **Cadastrar aluno**: O sistema permite cadastrar um aluno, incluindo seu nome e duas notas.
2. **Ver boletim**: O usuário pode visualizar a média final de um aluno.
3. **Ver notas**: O sistema exibe as notas de um aluno.
4. **Ver lista de alunos**: O usuário poderá ver a lista de todos os alunos que foram cadastrados, com suas respectivas notas e média.
5. **Limpar lista de alunos**: O usuário pode limpar a lista de alunos cadastrados quando desejar.

## Interface Gráfica
![Interface_Gráfica](https://github.com/user-attachments/assets/0db42b2f-bfff-439b-a4a8-85aff79234f6)

## Tecnologias Utilizadas

- Python
- ttkbootstrap (interface gráfica)
- json (armazenamento de dados dos alunos)
  
## Como Rodar o Projeto

### 1. Clonar o repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/GuiDev-01/Cadastro_Alunos.git
```
### 2. Criar um ambiente virtual
É recomendado criar um ambiente virtual para gerenciar as dependências do projeto. No terminal, dentro da pasta do projeto, execute os seguintes comandos:
```bash
python -m venv venv
```
### 3. Ativar o ambiente virtual 
- No windows:
  ```bash
  .\venv\Scripts\activate
  ```
- No macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
### 4. Instalar as dependências 
Instale as dependências necessárias (no caso, o ttkbootstrap) usando o pip:
```bash
pip install ttkbootstrap
```
### 5. Executar o projeto
Agora você pode rodar o programa
```bash
python main.py
```
O programa abrirá uma interface gráfica onde você poderá interagir com o cadastro de alunos.

### Como Funciona o Código
Cadastro de Alunos: Ao clicar no botão de cadastro, o nome do aluno e suas notas são capturados e salvos na lista alunos. A média das notas também é calculada e armazenada.

Ver Boletim: Você pode visualizar a média final de um aluno ao inserir o nome dele na entrada apropriada.

Ver Notas: Ao inserir o nome de um aluno, o sistema mostrará as duas notas cadastradas para esse aluno.

### Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções. Caso queira adicionar algo novo ou corrigir algo, basta fazer um fork do projeto e enviar um pull request.

### Licença
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
