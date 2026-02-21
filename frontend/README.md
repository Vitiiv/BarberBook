├── src/
│   ├── assets/
│   │   ├── images/
│   │   ├── icons/
│   │   └── styles/
│   │       └── main.css (Tailwind imports)
│   │
│   ├── components/
│   │   ├── common/          # Componentes reutilizáveis
│   │   │   ├── AppButton.vue
│   │   │   ├── AppInput.vue
│   │   │   └── AppModal.vue
│   │   ├── layout/          # Componentes de layout
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppSidebar.vue
│   │   │   └── AppFooter.vue
│   │   └── features/        # Componentes específicos por feature
│   │       ├── agendamento/
│   │       │   ├── CalendarioAgendamento.vue
│   │       │   └── FormAgendamento.vue
│   │       └── barbeiro/
│   │           └── CardBarbeiro.vue
│   │
│   ├── views/               # Páginas/Rotas
│   │   ├── auth/
│   │   │   ├── LoginView.vue
│   │   │   └── RegisterView.vue
│   │   ├── cliente/
│   │   │   ├── DashboardView.vue
│   │   │   ├── AgendamentoView.vue
│   │   │   └── HistoricoView.vue
│   │   ├── barbeiro/
│   │   │   ├── AgendaView.vue
│   │   │   └── ClientesView.vue
│   │   └── admin/
│   │       ├── DashboardView.vue
│   │       └── RelatoriosView.vue
│   │
│   ├── router/
│   │   ├── index.ts         # Configuração principal
│   │   └── guards.ts        # Guards de autenticação
│   │
│   ├── stores/              # Pinia stores
│   │   ├── auth.ts          # Store de autenticação
│   │   ├── agendamento.ts   # Store de agendamentos
│   │   ├── barbeiro.ts      # Store de barbeiros
│   │   └── user.ts          # Store do usuário logado
│   │
│   ├── services/            # Comunicação com API
│   │   ├── api.ts           # Configuração base do axios
│   │   ├── auth.service.ts
│   │   ├── agendamento.service.ts
│   │   └── barbeiro.service.ts
│   │
│   ├── composables/         # Composition API reusáveis
│   │   ├── useAuth.ts
│   │   ├── useToast.ts
│   │   └── useForm.ts
│   │
│   ├── types/               # TypeScript types/interfaces
│   │   ├── auth.types.ts
│   │   ├── agendamento.types.ts
│   │   ├── barbeiro.types.ts
│   │   └── api.types.ts
│   │
│   ├── utils/               # Funções utilitárias
│   │   ├── date.ts
│   │   ├── format.ts
│   │   └── validation.ts
│   │
│   ├── constants/           # Constantes da aplicação
│   │   └── index.ts
│   │
│   ├── layouts/             # Layouts de páginas
│   │   ├── DefaultLayout.vue
│   │   ├── AuthLayout.vue
│   │   └── AdminLayout.vue
│   │
│   ├── App.vue
│   └── main.ts