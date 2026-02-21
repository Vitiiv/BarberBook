<template>
  <div class="min-h-screen bg-background flex items-center justify-center px-4">
    <div class="w-full max-w-lg">
      <!-- Header -->
      <header class="text-center mb-10 space-y-2">
        <h1 class="text-4xl font-bold tracking-wide">
          Criar Conta
        </h1>
        <p class="text-text-secondary text-sm">
          Cadastre-se para começar
        </p>
      </header>
      <!-- Card -->
      <Card class="shadow-2xl rounded-2xl">
        <template #content>
          <form
            class="space-y-6"
            @submit.prevent="authStore.signUp()"
          >
            <!-- Name -->
            <div class="space-y-2">
              <label class="block text-sm font-medium">
                Nome completo
              </label>
              <InputText
                required
                class="w-full"
                type="text"
                placeholder="Seu nome completo"
                v-model="authStore.signUpUser.name"
              />
            </div>
            <!-- Email -->
            <div class="space-y-2">
              <label class="block text-sm font-medium">
                Email
              </label>
              <InputText
                required
                type="email"
                class="w-full"
                placeholder="Seu email"
                v-model="authStore.signUpUser.email"
              />
            </div>
            <!-- Telephone -->
            <div class="space-y-2">
              <label class="block text-sm font-medium">
                Telefone
              </label>
              <InputMask
                required
                mask="(99) 99999-9999" roles
                class="w-full",
                v-model="authStore.signUpUser.telephone"
              />
            </div>
            <!-- Password -->
            <div class="space-y-2">
              <label class="block text-sm font-medium">
                Senha
              </label>
              <Password
                required
                toggleMask 
                fluid
                :feedback="false"
                v-model="authStore.signUpUser.password"
              />
            </div>
            <!-- Submit -->
            <Button
              type="submit"
              label="Cadastrar"
              icon="pi pi-user-plus"
              class="w-full"
            />
          </form>
          <!-- Divider -->
          <div class="relative my-6">
            <Divider class="border-border" />
            <span
              class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2  bg-surface px-4 text-sm text-text-secondary"
            >
              ou
            </span>
          </div>
          <!-- Login -->
          <div class="text-center">
            <p class="text-sm text-text-secondary">
              Já possui conta?
              <router-link
                to="/sign-in"
                class="text-secondary hover:text-secondary-400 transition-colors font-semibold ml-1"
              >
                Entrar
              </router-link>
            </p>
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../auth.store';
import Button from 'primevue/button';
import Card from 'primevue/card';
import Divider from 'primevue/divider';
import InputMask from 'primevue/inputmask';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';

const authStore = useAuthStore();
</script>