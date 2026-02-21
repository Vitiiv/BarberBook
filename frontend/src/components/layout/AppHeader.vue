<template>
  <div class="w-full bg-surface/80 backdrop-blur-xl border border-border h-16 rounded-full shadow-2xl">
    <section class="w-full h-full flex justify-around items-center px-2">
      <div
        v-for="item in items"
        :key="item"
        @click="activeTab = item"
        class="relative flex items-center gap-2 px-6 py-2.5 rounded-full cursor-pointer transition-all duration-300 ease-out group"
        :class="activeTab === item 
          ? 'bg-secondary text-primary-950 shadow-lg shadow-secondary/20' 
          : 'hover:bg-surface-light text-text-secondary hover:text-text'"
      >
        <!-- Bullet animado -->
        <span
          v-if="activeTab === item"
          class="w-2 h-2 rounded-full bg-primary-950 animate-pulse"
        />
        
        <!-- Texto -->
        <h2 class="text-sm font-medium tracking-wide transition-all duration-300"
            :class="activeTab === item ? 'font-semibold' : ''">
          {{ item }}
        </h2>

        <!-- Underline hover effect -->
        <div 
          v-if="activeTab !== item"
          class="absolute bottom-1 left-1/2 -translate-x-1/2 w-0 h-0.5 bg-secondary transition-all duration-300 group-hover:w-3/4"
        />
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref('Home')
const items = ['Home', 'Sobre', 'Pacotes', 'Time']
</script>