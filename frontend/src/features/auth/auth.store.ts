import { defineStore } from "pinia";
import { IUserRole } from "./auth.types";
import type { IUserSignUp, IUserSignIn} from "./auth.types";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    signUpUser: {
      role: IUserRole.CLIENT
    } as IUserSignUp,
    signInUser: {} as IUserSignIn
  }),

  actions: {
    async signUp() {
      console.log(this.signUpUser)
    },
    async signIn() {
      console.log(this.signInUser)
    }
  }
});