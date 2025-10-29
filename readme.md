🍲 Receitas de Cozinha

Receitas de Cozinha é um projeto web desenvolvido com Django, que permite explorar, cadastrar, editar, excluir e consultar receitas.
Cada receita possui nome, ingredientes, modo de preparo, categoria e imagem ilustrativa.
Além disso, o sistema permite filtrar receitas por categoria, facilitando a busca por pratos variados.

🚀 Funcionalidades

✅ Cadastrar novas receitas
✅ Listar todas as receitas
✅ Visualizar detalhes de uma receita
✅ Editar e excluir receitas existentes
✅ Upload de imagem para cada receita
✅ Filtro de receitas por categoria
✅ Sistema de autenticação (login/logout)

🛠️ Tecnologias utilizadas

Python 3.x

Django 5.x

HTML5 / CSS3

SQLite3 (banco de dados padrão do Django)

⚙️ Instalação e execução
1️⃣ Clone o repositório
git clone https://github.com/seuusuario/receitas-de-cozinha.git
cd receitas-de-cozinha

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

5️⃣ Crie um superusuário (para acessar o painel admin)
python manage.py createsuperuser

6️⃣ Inicie o servidor
python manage.py runserver


Acesse no navegador:
👉 http://127.0.0.1:8000/

🧁 Estrutura do projeto
receitas_de_cozinha/
├── receitas/              # Aplicação principal
│   ├── models.py          # Modelo de Receita
│   ├── views.py           # Lógica das views
│   ├── urls.py            # Rotas da aplicação
│   ├── templates/         # Páginas HTML
├── receitas_de_cozinha/   # Configurações do projeto
├── manage.py
└── requirements.txt


📸 Exemplo de receita

Bolo de Chocolate
Categoria: Doce
Ingredientes: Farinha, ovos, leite, chocolate em pó, fermento...

Modo de preparo: Misture tudo, asse por 40 minutos e aproveite! 🍫

🔒 Autenticação

O sistema requer login para cadastrar, editar ou excluir receitas.
Usuários não autenticados podem apenas visualizar e buscar receitas.

💻 Desenvolvido com Django 💚