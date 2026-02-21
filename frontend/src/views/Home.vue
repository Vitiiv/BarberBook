<template>
  <div class="max-w-7xl mx-auto">
    <!-- Hero Section -->
    <section class="mb-20 text-center">
      <div class="relative inline-block mb-6">
        <h1 class="text-7xl font-black tracking-tight">
          <span class="text-text">ESTILO É</span>
          <span class="text-secondary block mt-2">ATITUDE</span>
        </h1>
        <div class="absolute -bottom-2 left-0 w-full h-1 bg-gradient-to-r from-transparent via-secondary to-transparent" />
      </div>
      
      <p class="text-xl text-text-secondary max-w-2xl mx-auto mb-8">
        Mais que um corte, uma experiência premium
      </p>

      <button class="group relative px-8 py-4 bg-secondary text-primary-950 rounded-full font-semibold text-lg overflow-hidden transition-all duration-300 hover:shadow-2xl hover:shadow-secondary/30 hover:scale-105">
        <span class="relative z-10">Agendar Horário</span>
        <div class="absolute inset-0 bg-gradient-to-r from-secondary-400 to-secondary-600 translate-y-full group-hover:translate-y-0 transition-transform duration-300" />
      </button>
    </section>

    <!-- Serviços -->
    <section class="mb-20">
      <h2 class="text-4xl font-bold text-center mb-12">
        Nossos <span class="text-secondary">Serviços</span>
      </h2>

      <div class="grid md:grid-cols-3 gap-6">
        <div 
          v-for="servico in servicos" 
          :key="servico.nome"
          class="group relative bg-surface border border-border rounded-2xl p-6 hover:border-secondary transition-all duration-300 overflow-hidden"
        >
          <!-- Gradient hover effect -->
          <div class="absolute inset-0 bg-gradient-to-br from-secondary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
          
          <div class="relative z-10">
            <!-- Ícone -->
            <div class="w-14 h-14 bg-secondary/10 rounded-xl flex items-center justify-center mb-4 group-hover:bg-secondary/20 transition-colors">
              <i :class="servico.icone" class="text-2xl text-secondary" />
            </div>

            <!-- Conteúdo -->
            <h3 class="text-xl font-bold mb-2 text-text group-hover:text-secondary transition-colors">
              {{ servico.nome }}
            </h3>
            <p class="text-text-secondary text-sm mb-4">
              {{ servico.descricao }}
            </p>

            <!-- Footer -->
            <div class="flex items-center justify-between">
              <span class="text-3xl font-bold text-secondary">
                R$ {{ servico.preco }}
              </span>
              <span class="text-sm text-text-muted bg-surface-light px-3 py-1 rounded-full">
                {{ servico.duracao }}
              </span>
            </div>
          </div>

          <!-- Borda animada -->
          <div class="absolute inset-0 rounded-2xl border-2 border-secondary opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none" />
        </div>
      </div>
    </section>

    <!-- Time de Barbeiros -->
    <section class="mb-20">
      <h2 class="text-4xl font-bold text-center mb-12">
        Nosso <span class="text-secondary">Time</span>
      </h2>

      <div class="grid md:grid-cols-4 gap-6">
        <div 
          v-for="barbeiro in barbeiros" 
          :key="barbeiro.nome"
          class="group relative bg-surface border border-border rounded-2xl overflow-hidden hover:border-secondary transition-all duration-300"
        >
          <!-- Imagem -->
          <div class="aspect-square bg-surface-light relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-transparent" />
            <div class="absolute bottom-4 left-4 right-4">
              <div class="flex items-center gap-1 mb-1">
                <i v-for="n in 5" :key="n" class="pi pi-star-fill text-secondary text-xs" />
              </div>
            </div>
          </div>

          <!-- Info -->
          <div class="p-4">
            <h3 class="text-lg font-bold text-text mb-1">{{ barbeiro.nome }}</h3>
            <p class="text-sm text-text-secondary mb-3">{{ barbeiro.especialidade }}</p>
            
            <button class="w-full py-2 bg-surface-light text-text rounded-lg text-sm font-medium hover:bg-secondary hover:text-primary-950 transition-all duration-300">
              Ver Agenda
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Final -->
    <section class="relative bg-gradient-to-br from-surface via-surface-light to-surface rounded-3xl p-12 text-center overflow-hidden border border-border">
      <!-- Efeito de brilho -->
      <div class="absolute inset-0 opacity-20">
        <div class="absolute top-0 left-1/4 w-96 h-96 bg-secondary rounded-full blur-3xl" />
        <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-accent rounded-full blur-3xl" />
      </div>

      <div class="relative z-10">
        <h2 class="text-4xl font-bold mb-4">
          Pronto para mudar seu <span class="text-secondary">visual?</span>
        </h2>
        <p class="text-text-secondary mb-8 max-w-2xl mx-auto">
          Agende seu horário agora e garanta o melhor atendimento
        </p>
        
        <div class="flex gap-4 justify-center">
          <button class="px-8 py-4 bg-secondary text-primary-950 rounded-full font-semibold hover:shadow-2xl hover:shadow-secondary/30 transition-all duration-300 hover:scale-105">
            Agendar Agora
          </button>
          <button class="px-8 py-4 bg-transparent border-2 border-secondary text-secondary rounded-full font-semibold hover:bg-secondary hover:text-primary-950 transition-all duration-300">
            Ver Preços
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const servicos = [
  {
    nome: 'Corte Tradicional',
    descricao: 'Corte clássico com acabamento perfeito e lavagem',
    preco: '45',
    duracao: '30 min',
    icone: 'pi pi-scissors'
  },
  {
    nome: 'Barba Completa',
    descricao: 'Barba feita com navalha e toalha quente',
    preco: '35',
    duracao: '25 min',
    icone: 'pi pi-user'
  },
  {
    nome: 'Corte + Barba',
    descricao: 'Combo completo para um visual impecável',
    preco: '70',
    duracao: '50 min',
    icone: 'pi pi-star'
  },
]

const barbeiros = [
  { nome: 'Carlos Silva', especialidade: 'Cortes Modernos' },
  { nome: 'João Pedro', especialidade: 'Barbas & Cortes' },
  { nome: 'Rafael Costa', especialidade: 'Degradê Expert' },
  { nome: 'Lucas Mendes', especialidade: 'Estilo Clássico' },
]
</script>