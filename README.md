<<<<<<< HEAD
Este é um arquivo README personalizado para o seu projeto **TechWeek**, estruturado para refletir a implementação técnica que desenvolvemos, focando na integração entre o backend em Flask e o frontend moderno.

---

# 🚀 TechWeek - UniCesumar Londrina

O **TechWeek** é uma plataforma web desenvolvida para gerenciar e apresentar um evento de tecnologia e inteligência artificial na UniCesumar, Londrina. Este projeto combina um backend robusto em Python com uma interface de usuário dinâmica e responsiva.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python com o framework Flask para gerenciamento de rotas e lógica de servidor.
* **Frontend:** HTML5, CSS3 (com foco em design responsivo e efeitos visuais avançados) e JavaScript.
* **Banco de Dados:** Integração com Supabase para o gerenciamento de registros e dados de usuários.
* **Deployment:** Configurado para hospedagem na plataforma Render.

## 📋 Funcionalidades Implementadas

* **Rotas Dinâmicas:** Sistema de rotas Flask para navegação fluida entre as páginas de palestrantes, cronograma e inscrições.
* **Interface Responsiva:** Barra de navegação adaptável e layouts que funcionam em diferentes tamanhos de tela.
* **Design Avançado:**
* Cards de palestrantes com efeitos de transição *hover* personalizados.
* Uso de efeitos de desfoque (*blur*) e fontes customizadas para uma estética moderna e tecnológica.
=======
# 🖥️ TechWeek 1ª Edição — UniCesumar

Site oficial do evento **TechWeek**, organizado pela UniCesumar.

---

## 🛠️ Tecnologias

- **HTML5**
- **CSS3**
- **JavaScript**
- **Python** (back-end com `app.py`)
- **Node.js** (dependências via `package.json`)

---

## 📁 Estrutura do Projeto
>>>>>>> 4de7ac4240996dcadd2b34908c9e30449d350955

```
Techweek/
├── techweek-frontend/
│   ├── static/
│   │   ├── img/                    # Imagens do projeto
│   │   ├── ajuda.css
│   │   ├── ajuda.js
│   │   ├── devs.css
│   │   ├── inscricao.css
│   │   ├── palestrantes.css
│   │   ├── perfil.css
│   │   ├── style.css               # Estilos globais
│   │   ├── fundo-inscricao.mp4     # Vídeo de fundo (inscrição)
│   │   └── fundo-principal.mp4     # Vídeo de fundo (principal)
│   └── templates/
│       ├── index.html              # Landing page
│       ├── ajuda.html              # FAQ
│       ├── dashboard.html          # Dashboard
│       ├── devs.html               # Time de desenvolvimento
│       ├── inscricao.html          # Página de inscrição
│       ├── login.html              # Login
│       ├── palestrantes.html       # Palestrantes
│       ├── perfil.html             # Perfil do usuário
│       └── sucesso.html            # Confirmação de inscrição
├── app.py                          # Back-end Python
├── requirements.txt                # Dependências Python
├── package.json                    # Dependências Node
└── README.md
```

<<<<<<< HEAD
* **Sistema de Inscrição:** Integração funcional com o backend Supabase para capturar e armazenar dados de participantes com segurança.

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/Jslus12/Techweek.git

```
=======
---

## 📄 Páginas
>>>>>>> 4de7ac4240996dcadd2b34908c9e30449d350955

| Arquivo | Descrição |
|---------|-----------|
| `index.html` | Landing page com hero, agenda e localização |
| `devs.html` | Time de desenvolvimento |
| `ajuda.html` | Perguntas frequentes (FAQ) |
| `palestrantes.html` | Palestrantes do evento |
| `inscricao.html` | Formulário de inscrição |
| `login.html` | Autenticação |
| `perfil.html` | Perfil do participante |
| `dashboard.html` | Painel interno |
| `sucesso.html` | Confirmação de inscrição |

<<<<<<< HEAD
2. **Configure o ambiente virtual:**

```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Variáveis de Ambiente:** Certifique-se de configurar as variáveis de ambiente necessárias para a conexão com o Supabase e as chaves do Flask no seu ambiente local ou no painel do Render.

5.  **Inicie o servidor:**
    ```bash
    python app.py
    ```

## 🌐 Deployment

O projeto está configurado para ser implantado no **Render**. Durante o processo de deploy, focamos na correção de erros de caminho de arquivos e na configuração correta do Python para garantir que as rotas (como o erro 404 anteriormente discutido) funcionem perfeitamente em produção.

---

*Projeto desenvolvido como parte das iniciativas de tecnologia da UniCesumar Londrina.*

```
=======
---

## 🚀 Como rodar

### Front-end
Abra `templates/index.html` diretamente no navegador.

### Back-end (Python)
1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o servidor:
```bash
python app.py
```

---

## 📅 Evento

**Quando:** Junho de 2026
**Onde:** Auditório Principal — UniCesumar, Londrina/PR
**Horário:** 19h00 às 22h00

### Programação
| Dia | Data | Descrição |
|-----|------|-----------|
| 01 | SEG | Abertura Oficial |
| 02 | TER | TechWeek |
| 03 | QUA | TechWeek |

---

## 👨‍💻 Time de Desenvolvimento

| Nome | Função |
|------|--------|
| Rafael Piasentin | Desenvolvedor Front-End / QA |
| Felipe Piva | Desenvolvedor Fullstack |
| Rafael Koti | Desenvolvedor Fullstack |
| Nicollas Azalim | Desenvolvedor |
| Heitor Henrique | Desenvolvedor |
| João Lucas Delbianco | Desenvolvedor Front-End |
| Roberto Muller | Desenvolvedor |
| Bruno Stainski | Desenvolvedor |

---

## 📝 Licença

Projeto acadêmico — UniCesumar © 2026
>>>>>>> 4de7ac4240996dcadd2b34908c9e30449d350955
