import axios from "axios";

const api = axios.create({
  baseURL: 'http://26.217.117.21:8000',
  headers: {
    'Content-Type': 'application/json'
  }
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('@token')

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})

export default api