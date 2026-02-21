/** biome-ignore-all lint/complexity/noStaticOnlyClass: <explanation> */
import api from "@/lib/axios";
import type { IUserSignUp, IUserSignIn } from "./auth.types";

export class AuthService {
  static async signUp(email: string, password: string) {
    return api.post<IUserSignIn>('/auth/sign-in', { email, password })
  }
}