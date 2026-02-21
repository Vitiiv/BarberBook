<template>
  <button 
    class="relative px-6 py-3 rounded-full font-semibold transition-all duration-300 overflow-hidden group"
    :class="variantClasses"
  >
    <span class="relative z-10">
      <slot />
    </span>
    <div 
      v-if="variant === 'primary'"
      class="absolute inset-0 bg-gradient-to-r from-secondary-400 to-secondary-600 translate-y-full group-hover:translate-y-0 transition-transform duration-300"
    />
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  variant?: 'primary' | 'secondary' | 'outline'
}>()

const variantClasses = computed(() => {
  switch (props.variant) {
    case 'primary':
      return 'bg-secondary text-primary-950 hover:shadow-2xl hover:shadow-secondary/30 hover:scale-105'
    case 'secondary':
      return 'bg-surface-light text-text hover:bg-surface border border-border'
    case 'outline':
      return 'bg-transparent border-2 border-secondary text-secondary hover:bg-secondary hover:text-primary-950'
    default:
      return 'bg-secondary text-primary-950 hover:shadow-2xl hover:shadow-secondary/30 hover:scale-105'
  }
})
</script>