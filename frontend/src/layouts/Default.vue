<template>
  <div class="min-h-screen bg-background">
    <!-- Header -->
    <header class="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-full max-w-2xl px-4">
      <AppHeader />
    </header>

    <!-- Main Content -->
    <main class="pt-28 pb-16 px-4">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import AppHeader from '@/components/layout/AppHeader.vue'
</script>