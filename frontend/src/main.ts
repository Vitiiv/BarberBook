import { createPinia } from "pinia";
import { createApp } from "vue";
import PrimeVue from "primevue/config";
import MyTheme from '@/assets/theme';
import ToastService from 'primevue/toastservice'
import ConfirmationService from 'primevue/confirmationservice'
import App from "./App.vue";
import router from "./router";
import 'primeicons/primeicons.css';
import "./assets/styles/style.css";

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(PrimeVue, {
  theme: {
    preset: MyTheme
  }
});
app.use(ToastService)
app.use(ConfirmationService)
app.mount("#app");
