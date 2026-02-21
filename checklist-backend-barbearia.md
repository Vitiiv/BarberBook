# 📋 Checklist Backend - Sistema de Barbearia

## 🎯 Stack Recomendada
- [ ] Python 3.11+
- [ ] FastAPI (framework web)
- [ ] SQLAlchemy (ORM)
- [ ] PostgreSQL (banco de dados)
- [ ] Alembic (migrations)
- [ ] Pydantic (validação)
- [ ] python-jose[cryptography] (JWT)
- [ ] passlib[bcrypt] (hash de senhas)
- [ ] python-multipart (upload de arquivos)

---

## 🔧 Configuração Inicial

### Setup do Projeto
- [ ] Criar estrutura de pastas
- [ ] Configurar ambiente virtual (venv)
- [ ] Criar requirements.txt
- [ ] Configurar variáveis de ambiente (.env)
- [ ] Configurar CORS
- [ ] Documentação automática (Swagger/OpenAPI)

### Estrutura de Pastas Sugerida
```
backend/
├── app/
│   ├── main.py              # Entry point
│   ├── config.py            # Configurações
│   ├── database.py          # Conexão DB
│   │
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   ├── barbeiro.py
│   │   ├── servico.py
│   │   ├── agendamento.py
│   │   └── avalacao.py
│   │
│   ├── schemas/             # Pydantic schemas
│   │   ├── user.py
│   │   ├── barbeiro.py
│   │   ├── servico.py
│   │   └── agendamento.py
│   │
│   ├── routers/             # Endpoints
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── barbeiros.py
│   │   ├── servicos.py
│   │   └── agendamentos.py
│   │
│   ├── services/            # Lógica de negócio
│   │   ├── auth_service.py
│   │   ├── agendamento_service.py
│   │   └── notificacao_service.py
│   │
│   └── utils/               # Utilitários
│       ├── security.py      # JWT, hash
│       ├── dependencies.py  # Injeção de dependências
│       └── validators.py
│
├── alembic/                 # Migrations
├── tests/                   # Testes
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🗄️ Banco de Dados & Modelos

### Tabelas/Modelos a Criar

#### 1. Usuários (users)
- [ ] id (UUID/int)
- [ ] nome (string)
- [ ] email (string, unique)
- [ ] telefone (string)
- [ ] senha_hash (string)
- [ ] tipo (enum: 'cliente', 'barbeiro', 'admin')
- [ ] ativo (boolean)
- [ ] foto_perfil (string/url, nullable)
- [ ] created_at (datetime)
- [ ] updated_at (datetime)

#### 2. Barbeiros (barbeiros)
- [ ] id (UUID/int)
- [ ] user_id (FK para users)
- [ ] especialidades (string/json)
- [ ] biografia (text, nullable)
- [ ] avaliacao_media (float)
- [ ] total_atendimentos (int)
- [ ] horario_inicio (time)
- [ ] horario_fim (time)
- [ ] dias_trabalho (json: ['seg', 'ter', 'qua', ...])
- [ ] intervalo_atendimento (int, em minutos)

#### 3. Serviços (servicos)
- [ ] id (UUID/int)
- [ ] nome (string)
- [ ] descricao (text)
- [ ] duracao (int, em minutos)
- [ ] preco (decimal)
- [ ] ativo (boolean)
- [ ] categoria (string, nullable)
- [ ] imagem (string/url, nullable)

#### 4. Agendamentos (agendamentos)
- [ ] id (UUID/int)
- [ ] cliente_id (FK para users)
- [ ] barbeiro_id (FK para barbeiros)
- [ ] servico_id (FK para servicos)
- [ ] data (date)
- [ ] horario_inicio (time)
- [ ] horario_fim (time)
- [ ] status (enum: 'pendente', 'confirmado', 'em_atendimento', 'concluido', 'cancelado')
- [ ] observacoes (text, nullable)
- [ ] preco_cobrado (decimal)
- [ ] created_at (datetime)
- [ ] updated_at (datetime)
- [ ] cancelado_por (FK para users, nullable)
- [ ] motivo_cancelamento (text, nullable)

#### 5. Avaliações (avaliacoes)
- [ ] id (UUID/int)
- [ ] agendamento_id (FK para agendamentos)
- [ ] cliente_id (FK para users)
- [ ] barbeiro_id (FK para barbeiros)
- [ ] nota (int, 1-5)
- [ ] comentario (text, nullable)
- [ ] created_at (datetime)

#### 6. Horários Bloqueados (horarios_bloqueados)
- [ ] id (UUID/int)
- [ ] barbeiro_id (FK para barbeiros)
- [ ] data (date)
- [ ] horario_inicio (time)
- [ ] horario_fim (time)
- [ ] motivo (string)

#### 7. Configurações da Barbearia (configuracoes)
- [ ] id (int)
- [ ] nome_barbearia (string)
- [ ] telefone (string)
- [ ] endereco (text)
- [ ] horario_funcionamento (json)
- [ ] intervalo_minimo_cancelamento (int, em horas)
- [ ] antecedencia_maxima_agendamento (int, em dias)

### Migrations
- [ ] Configurar Alembic
- [ ] Criar migration inicial
- [ ] Script para popular dados de exemplo

---

## 🔐 Autenticação & Autorização

### Funcionalidades de Auth
- [ ] Registro de usuário (cliente)
- [ ] Login (email + senha)
- [ ] Logout
- [ ] Geração de token JWT
- [ ] Validação de token JWT
- [ ] Refresh token
- [ ] Recuperação de senha (enviar email)
- [ ] Redefinição de senha
- [ ] Verificação de email (opcional)

### Endpoints de Auth
```
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/logout
POST   /api/auth/refresh
POST   /api/auth/forgot-password
POST   /api/auth/reset-password
GET    /api/auth/me (usuário logado)
```

### Middleware/Dependencies
- [ ] Dependência para verificar token
- [ ] Dependência para verificar role (admin, barbeiro, cliente)
- [ ] Dependência para pegar usuário logado

---

## 👤 Gestão de Usuários

### Endpoints de Usuários
```
GET    /api/users              # Listar (admin)
GET    /api/users/{id}         # Ver perfil
PUT    /api/users/{id}         # Atualizar perfil
DELETE /api/users/{id}         # Deletar (admin)
POST   /api/users/{id}/upload-foto  # Upload foto perfil
```

### Funcionalidades
- [ ] Listar usuários (admin)
- [ ] Ver perfil próprio
- [ ] Atualizar perfil próprio
- [ ] Upload de foto de perfil
- [ ] Alterar senha
- [ ] Desativar conta

---

## 💇 Gestão de Barbeiros

### Endpoints de Barbeiros
```
GET    /api/barbeiros           # Listar ativos
GET    /api/barbeiros/{id}      # Ver detalhes
POST   /api/barbeiros           # Criar (admin)
PUT    /api/barbeiros/{id}      # Atualizar
DELETE /api/barbeiros/{id}      # Deletar (admin)
GET    /api/barbeiros/{id}/horarios-disponiveis  # Horários livres
GET    /api/barbeiros/{id}/avaliacoes            # Avaliações
```

### Funcionalidades
- [ ] Listar barbeiros ativos
- [ ] Filtrar barbeiros por especialidade
- [ ] Ver detalhes do barbeiro (bio, avaliação, especialidades)
- [ ] Ver horários disponíveis do barbeiro em uma data
- [ ] Criar/editar barbeiro (admin)
- [ ] Definir horários de trabalho
- [ ] Bloquear horários específicos
- [ ] Ver agenda do barbeiro (próprio)
- [ ] Ver histórico de atendimentos

---

## ✂️ Gestão de Serviços

### Endpoints de Serviços
```
GET    /api/servicos            # Listar ativos
GET    /api/servicos/{id}       # Ver detalhes
POST   /api/servicos            # Criar (admin)
PUT    /api/servicos/{id}       # Atualizar (admin)
DELETE /api/servicos/{id}       # Deletar (admin)
```

### Funcionalidades
- [ ] Listar serviços ativos
- [ ] Filtrar por categoria
- [ ] Criar serviço
- [ ] Editar serviço (nome, preço, duração)
- [ ] Desativar/ativar serviço
- [ ] Upload de imagem do serviço

---

## 📅 Sistema de Agendamentos (CORE)

### Endpoints de Agendamentos
```
GET    /api/agendamentos                    # Listar (filtros)
GET    /api/agendamentos/{id}               # Ver detalhes
POST   /api/agendamentos                    # Criar
PUT    /api/agendamentos/{id}               # Reagendar
DELETE /api/agendamentos/{id}               # Cancelar
PATCH  /api/agendamentos/{id}/confirmar     # Confirmar
PATCH  /api/agendamentos/{id}/iniciar       # Iniciar atendimento
PATCH  /api/agendamentos/{id}/finalizar     # Finalizar
GET    /api/agendamentos/meus               # Meus agendamentos (cliente)
GET    /api/agendamentos/barbeiro/{id}      # Agenda do barbeiro
```

### Funcionalidades

#### Criar Agendamento
- [ ] Validar se horário está disponível
- [ ] Validar conflito com outros agendamentos
- [ ] Validar se está dentro do horário de funcionamento
- [ ] Validar antecedência mínima
- [ ] Validar antecedência máxima
- [ ] Calcular horário de término (início + duração do serviço)
- [ ] Criar registro no banco
- [ ] Enviar notificação (email/SMS) ao cliente
- [ ] Enviar notificação ao barbeiro

#### Listar Agendamentos
- [ ] Filtrar por data
- [ ] Filtrar por barbeiro
- [ ] Filtrar por cliente
- [ ] Filtrar por status
- [ ] Ordenar por data/hora
- [ ] Paginação

#### Reagendar
- [ ] Validar novo horário disponível
- [ ] Validar prazo de reagendamento
- [ ] Atualizar registro
- [ ] Notificar cliente e barbeiro

#### Cancelar
- [ ] Validar prazo mínimo para cancelamento
- [ ] Marcar como cancelado
- [ ] Registrar motivo e quem cancelou
- [ ] Liberar horário
- [ ] Notificar cliente e barbeiro

#### Confirmar/Iniciar/Finalizar
- [ ] Barbeiro confirma agendamento
- [ ] Barbeiro marca início do atendimento
- [ ] Barbeiro finaliza atendimento
- [ ] Atualizar status
- [ ] Permitir avaliação após finalizar

#### Horários Disponíveis
- [ ] Calcular slots disponíveis para um barbeiro em uma data
- [ ] Considerar horário de trabalho do barbeiro
- [ ] Considerar agendamentos existentes
- [ ] Considerar horários bloqueados
- [ ] Retornar lista de horários livres

---

## ⭐ Sistema de Avaliações

### Endpoints de Avaliações
```
POST   /api/avaliacoes                # Criar avaliação
GET    /api/avaliacoes/barbeiro/{id}  # Avaliações de um barbeiro
GET    /api/avaliacoes/minhas         # Minhas avaliações
```

### Funcionalidades
- [ ] Cliente avaliar barbeiro (nota 1-5 + comentário)
- [ ] Validar que agendamento foi finalizado
- [ ] Validar que cliente ainda não avaliou esse agendamento
- [ ] Atualizar avaliação média do barbeiro
- [ ] Listar avaliações de um barbeiro
- [ ] Impedir edição/exclusão de avaliação (ou permitir apenas 1x)

---

## 📊 Relatórios & Dashboard (Admin)

### Endpoints de Relatórios
```
GET    /api/relatorios/faturamento        # Faturamento
GET    /api/relatorios/agendamentos       # Estatísticas
GET    /api/relatorios/barbeiros          # Performance
GET    /api/relatorios/servicos           # Mais vendidos
```

### Funcionalidades
- [ ] Faturamento por período
- [ ] Total de agendamentos por status
- [ ] Taxa de cancelamento
- [ ] Horários de pico
- [ ] Serviços mais procurados
- [ ] Ranking de barbeiros (por atendimentos, avaliação)
- [ ] Receita por barbeiro
- [ ] Receita por serviço
- [ ] Novos clientes por período
- [ ] Taxa de retorno de clientes

---

## 🔔 Sistema de Notificações

### Funcionalidades
- [ ] Email de confirmação de cadastro
- [ ] Email de confirmação de agendamento
- [ ] Email de lembrete (24h antes)
- [ ] Email de lembrete (1h antes)
- [ ] Email de cancelamento
- [ ] Email de reagendamento
- [ ] Notificação ao barbeiro de novo agendamento
- [ ] Notificação ao barbeiro de cancelamento

### Implementação
- [ ] Configurar SMTP (Gmail, SendGrid, etc)
- [ ] Templates de email HTML
- [ ] Fila de emails (Celery + Redis, opcional)
- [ ] SMS (Twilio, opcional)

---

## 🛡️ Segurança & Validações

### Segurança
- [ ] Hash de senhas com bcrypt
- [ ] Tokens JWT com expiração
- [ ] Validação de tipos com Pydantic
- [ ] Sanitização de inputs
- [ ] Rate limiting (proteção contra spam)
- [ ] CORS configurado corretamente
- [ ] HTTPS em produção
- [ ] Logs de auditoria (quem fez o quê)

### Validações Importantes
- [ ] Email válido
- [ ] Telefone válido
- [ ] CPF válido (opcional)
- [ ] Horários de agendamento válidos
- [ ] Datas não podem ser no passado
- [ ] Agendamentos não podem sobrepor
- [ ] Barbeiro não pode estar em dois lugares ao mesmo tempo

---

## 🧪 Testes

### Testes Unitários
- [ ] Testes de modelos
- [ ] Testes de schemas
- [ ] Testes de validações
- [ ] Testes de utils/helpers

### Testes de Integração
- [ ] Testes de endpoints de auth
- [ ] Testes de endpoints de agendamentos
- [ ] Testes de regras de negócio
- [ ] Testes de permissões

### Ferramentas
- [ ] pytest
- [ ] pytest-cov (cobertura)
- [ ] Factory Boy (fixtures)

---

## 📦 Deploy & DevOps

### Preparação para Deploy
- [ ] Dockerfile
- [ ] docker-compose.yml
- [ ] Variáveis de ambiente para produção
- [ ] Gunicorn/Uvicorn workers
- [ ] Nginx (reverse proxy)
- [ ] SSL/TLS (Let's Encrypt)

### CI/CD
- [ ] GitHub Actions (build, test, deploy)
- [ ] Testes automáticos em PR
- [ ] Deploy automático em merge

### Monitoring
- [ ] Logs estruturados
- [ ] Health check endpoint
- [ ] Sentry (error tracking, opcional)

---

## 🚀 Funcionalidades Extras (Futuro)

### Nice to Have
- [ ] Chat em tempo real (WebSocket)
- [ ] Histórico de preferências do cliente
- [ ] Sistema de fidelidade/pontos
- [ ] Pacotes de serviços (combo)
- [ ] Lista de espera (se cancelar, próximo da lista)
- [ ] Integração com Google Calendar
- [ ] Pagamento online (Stripe, Mercado Pago)
- [ ] QR Code para check-in
- [ ] Dashboard mobile para barbeiro
- [ ] Multi-tenancy (várias barbearias)

---

## 📚 Documentação

### O que documentar
- [ ] README.md completo
- [ ] Como rodar localmente
- [ ] Como rodar testes
- [ ] Variáveis de ambiente
- [ ] Endpoints da API (Swagger já gera)
- [ ] Fluxo de agendamento
- [ ] Regras de negócio
- [ ] Diagrama ER do banco

---

## 🎯 Priorização (MVP - Mínimo Viável)

### Fase 1 - Essencial (2-3 semanas)
1. ✅ Setup do projeto
2. ✅ Autenticação (registro, login, JWT)
3. ✅ CRUD de usuários
4. ✅ CRUD de barbeiros
5. ✅ CRUD de serviços
6. ✅ Sistema de agendamentos (criar, listar, cancelar)
7. ✅ Horários disponíveis

### Fase 2 - Importante (1-2 semanas)
1. Sistema de avaliações
2. Notificações por email
3. Reagendamento
4. Confirmação de agendamento
5. Dashboard básico (admin)

### Fase 3 - Complementar (1-2 semanas)
1. Relatórios avançados
2. Upload de imagens
3. Horários bloqueados
4. Testes automatizados
5. Deploy

### Fase 4 - Extras (quando tiver tempo)
1. SMS
2. Pagamento online
3. Chat
4. Sistema de fidelidade

---

## 💡 Dicas para seu amigo

### Boas Práticas
- Sempre validar dados de entrada
- Usar migrations para mudanças no banco
- Commitar frequentemente
- Escrever código limpo e comentado
- Testar endpoints no Postman/Insomnia
- Documentar decisões importantes

### Recursos de Estudo
- Documentação oficial do FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy tutorial: https://docs.sqlalchemy.org/
- JWT em Python: https://pyjwt.readthedocs.io/
- Curso FastAPI (YouTube)

### Ferramentas Úteis
- **Postman/Insomnia**: testar API
- **DBeaver/pgAdmin**: visualizar banco
- **Docker Desktop**: rodar PostgreSQL local
- **Alembic**: gerenciar migrations

---

## 📌 Comandos Úteis

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
uvicorn app.main:app --reload

# Criar migration
alembic revision --autogenerate -m "descrição"

# Rodar migration
alembic upgrade head

# Rodar testes
pytest

# Rodar com coverage
pytest --cov=app tests/
```

---

**Boa sorte com o desenvolvimento! 🚀**
