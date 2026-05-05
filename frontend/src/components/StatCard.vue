
&lt;template&gt;
  &lt;div class="stat-card" :style="{ animationDelay: `${delay}s` }"&gt;
    &lt;div class="stat-icon"&gt;{{ stat.icon }}&lt;/div&gt;
    &lt;div class="stat-value"&gt;{{ formatValue(displayValue) }}&lt;/div&gt;
    &lt;div class="stat-label"&gt;{{ stat.label }}&lt;/div&gt;
    &lt;div v-if="stat.trend" class="stat-trend" :class="stat.trend"&gt;{{ stat.trendValue }}&lt;/div&gt;
  &lt;/div&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import { ref, onMounted } from 'vue'
import type { StatItem } from '@/types/property'
import { useCounterAnimation } from '@/composables/useCounterAnimation'

interface Props {
  stat: StatItem
  index: number
}

const props = defineProps&lt;Props&gt;()

const delay = 0.4 + props.index * 0.1
const { displayValue, animate, formatValue } = useCounterAnimation(props.stat.value)

onMounted(() =&gt; {
  setTimeout(animate, delay * 1000)
})
&lt;/script&gt;

&lt;style scoped&gt;
.stat-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--spacing-lg);
  text-align: center;
  transition: all var(--transition-normal);
  position: relative;
  overflow: hidden;
  animation: fadeUp 0.6s ease forwards;
  opacity: 0;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--color-primary), var(--color-accent));
  transform: scaleX(0);
  transition: transform var(--transition-normal);
}

.stat-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 0%, rgba(212, 175, 55, 0.1), transparent 60%);
  opacity: 0;
  transition: opacity var(--transition-normal);
}

.stat-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg), var(--shadow-gold);
  border-color: var(--color-primary);
}

.stat-card:hover::before {
  transform: scaleX(1);
}

.stat-card:hover::after {
  opacity: 1;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.stat-icon {
  font-size: 2rem;
  margin-bottom: var(--spacing-sm);
  position: relative;
  z-index: 1;
}

.stat-value {
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.25rem;
  position: relative;
  z-index: 1;
}

.stat-label {
  color: var(--color-text-muted);
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: var(--spacing-sm);
  position: relative;
  z-index: 1;
}

.stat-trend {
  font-size: 0.8rem;
  padding: 0.25rem 0.625rem;
  border-radius: var(--radius-sm);
  display: inline-block;
  position: relative;
  z-index: 1;
}

.stat-trend.up {
  background: rgba(74, 222, 128, 0.15);
  color: var(--color-success);
}

.stat-trend.down {
  background: rgba(233, 69, 96, 0.15);
  color: var(--color-accent);
}
&lt;/style&gt;
