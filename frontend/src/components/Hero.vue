
&lt;template&gt;
  &lt;section class="hero"&gt;
    &lt;div class="hero-content"&gt;
      &lt;div class="hero-badge"&gt;✨ 实时数据更新&lt;/div&gt;
      &lt;h1 class="hero-title"&gt;
        &lt;span class="line"&gt;发现理想&lt;/span&gt;
        &lt;span class="line highlight"&gt;居所&lt;/span&gt;
      &lt;/h1&gt;
      &lt;p class="hero-subtitle"&gt;聚合多平台房源数据，智能筛选，精准匹配，让安家更简单&lt;/p&gt;
    &lt;/div&gt;
    &lt;div class="stats-grid"&gt;
      &lt;StatCard
        v-for="(stat, index) in stats"
        :key="stat.label"
        :stat="stat"
        :index="index"
      /&gt;
    &lt;/div&gt;
  &lt;/section&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import { ref } from 'vue'
import StatCard from './StatCard.vue'
import type { StatItem } from '@/types/property'
import { statsData } from '@/data/mockData'

const stats = ref&lt;StatItem[]&gt;(statsData)
&lt;/script&gt;

&lt;style scoped&gt;
.hero {
  margin-bottom: var(--spacing-xl);
}

.hero-content {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.5rem 1rem;
  background: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: var(--radius-xl);
  color: var(--color-primary-light);
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: var(--spacing-md);
  animation: fadeIn 0.6s ease 0.1s forwards;
  opacity: 0;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3rem, 8vw, 5rem);
  font-weight: 900;
  line-height: 1;
  margin-bottom: var(--spacing-md);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.hero-title .line {
  display: block;
  opacity: 0;
  animation: fadeUp 0.6s ease forwards;
}

.hero-title .line:nth-child(1) { animation-delay: 0.2s; }
.hero-title .line:nth-child(2) { animation-delay: 0.3s; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-title .highlight {
  background: linear-gradient(135deg, var(--color-primary) 0%, #f4d03f 50%, var(--color-primary) 100%);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s ease infinite;
}

@keyframes shimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.hero-subtitle {
  font-size: 1.15rem;
  color: var(--color-text-muted);
  max-width: 600px;
  margin: 0 auto;
  animation: fadeIn 0.6s ease 0.4s forwards;
  opacity: 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-md);
  margin-top: var(--spacing-xl);
}

@media (max-width: 1024px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .stats-grid { grid-template-columns: 1fr; }
}
&lt;/style&gt;
