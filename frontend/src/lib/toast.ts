import { useToast as usePrimeToast } from 'primevue/usetoast'

function useToast() {
  const toast = usePrimeToast();

  return {
    success(message: string, detail?: string) {
      toast.add({
        severity: 'success',
        summary: message,
        detail,
        life: 3000
      })
    },
    error(message: string, detail?: string) {
      toast.add({
        severity: 'error',
        summary: message,
        detail,
        life: 5000
      })
    },
    info(message: string, detail?: string) {
      toast.add({
        severity: 'info',
        summary: message,
        detail,
        life: 3000
      })
    },
    warning(message: string, detail?: string) {
      toast.add({
        severity: 'warn',
        summary: message,
        detail,
        life: 4000
      })
    }
  }

}

export default useToast