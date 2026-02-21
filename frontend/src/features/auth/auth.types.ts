export interface IUserSignIn {
  email: string
  password: string
}

export interface IUserSignUp {
  name: string
  email: string
  password: string
  telephone: string
  role: IUserRole
}

export enum IUserRole {
  CLIENT = 'cliente',
  BARBER = 'barbeiro',
  ADMIN = 'admin'
}