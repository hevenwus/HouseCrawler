
import { ref, onMounted, watch } from 'vue'

export function useCounterAnimation(targetValue: number, duration = 1500) {
  const displayValue = ref(0)
  const isAnimating = ref(false)

  const animate = () => {
    isAnimating.value = true
    displayValue.value = 0
    const start = 0
    const increment = targetValue / (duration / 16)
    let current = start

    const timer = setInterval(() => {
      current += increment
      if (current >= targetValue) {
        displayValue.value = targetValue
        clearInterval(timer)
        isAnimating.value = false
      } else {
        displayValue.value = current
      }
    }, 16)
  }

  const formatValue = (value: number) => {
    return value % 1 !== 0 ? value.toFixed(1) : Math.floor(value).toString()
  }

  return {
    displayValue,
    isAnimating,
    animate,
    formatValue
  }
}
