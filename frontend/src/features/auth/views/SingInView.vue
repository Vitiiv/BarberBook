<template>
  <div class="min-h-screen bg-background flex items-center justify-center p-6">
    <div class="w-full max-w-md">
      <!-- Header -->
      <header class="text-center mb-10 space-y-2">
        <h1 class="text-4xl font-bold text-secondary tracking-wide">
          BARBER SHOP
        </h1>
        <p class="text-text-secondary text-sm">
          Faça login para continuar
        </p>
      </header>
      <!-- Card -->
      <Card
        class="shadow-2xl border border-border bg-surface rounded-2xl p-8"
      >
        <template #content>
          <form
            class="space-y-6"
            @submit.prevent="authStore.signIn()"
          >
            <!-- Email -->
            <div class="space-y-2">
              <label
                for="email"
                class="block text-sm font-medium text-text"
              >
                Email
              </label>

              <InputText
                id="email"
                type="email"
                v-model="authStore.signInUser.email"
                class="w-full bg-surface-light border border-border text-text
                       focus:border-secondary focus:ring-1 focus:ring-secondary
                       rounded-lg px-3 py-2 transition-all duration-200"
                required
              />
            </div>
            <!-- Password -->
            <div class="space-y-2">
              <label
                for="password"
                class="block text-sm font-medium text-text"
              >
                Senha
              </label>

              <InputText
                id="password"
                type="password"
                v-model="authStore.signInUser.password"
                class="w-full bg-surface-light border border-border text-text
                       focus:border-secondary focus:ring-1 focus:ring-secondary
                       rounded-lg px-3 py-2 transition-all duration-200"
                required
              />
            </div>
            <!-- Submit -->
            <Button
              type="submit"
              class="w-full bg-secondary border-none text-primary-950
                     hover:bg-secondary-600
                     active:scale-[0.99]
                     transition-all duration-200
                     font-semibold py-2 rounded-lg flex items-center justify-center gap-2"
            >
              <i class="pi pi-sign-in" />
              Entrar
            </Button>
          </form>
          <!-- Divider -->
          <div class="relative my-6">
            <Divider class="border-border" />
            <span
              class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 
                     bg-surface px-4 text-sm text-text-secondary"
            >
              ou
            </span>
          </div>
          <!-- Register -->
          <div class="text-center">
            <p class="text-sm text-text-secondary">
              Não tem conta?
              <router-link
                to="/sign-up"
                class="text-secondary hover:text-secondary-400 transition-colors font-semibold ml-1"
              >
                Cadastre-se gratuitamente
              </router-link>
            </p>
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import Button from 'primevue/button';
import Card from 'primevue/card';
import Divider from 'primevue/divider';
import InputText from 'primevue/inputtext';
import { useAuthStore } from '../auth.store';

const authStore = useAuthStore();
</script>