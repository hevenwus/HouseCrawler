
&lt;template&gt;
  &lt;header class="header"&gt;
    &lt;div class="logo"&gt;
      &lt;div class="logo-icon-wrapper"&gt;
        &lt;span class="logo-icon"&gt;🏠&lt;/span&gt;
        &lt;div class="logo-glow"&gt;&lt;/div&gt;
      &lt;/div&gt;
      &lt;div class="logo-text-wrapper"&gt;
        &lt;span class="logo-text"&gt;HouseCrawler&lt;/span&gt;
        &lt;span class="logo-tagline"&gt;智能房产数据平台&lt;/span&gt;
      &lt;/div&gt;
    &lt;/div&gt;
    &lt;nav class="nav"&gt;
      &lt;button
        v-for="item in navItems"
        :key="item.source"
        :class="['nav-btn', { active: currentSource === item.source }]"
        @click="handleSourceChange(item.source)"
      &gt;
        &lt;span class="nav-btn-icon"&gt;{{ item.icon }}&lt;/span&gt;
        &lt;span&gt;{{ item.label }}&lt;/span&gt;
      &lt;/button&gt;
    &lt;/nav&gt;
  &lt;/header&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import type { PropertySource } from '@/types/property'

interface NavItem {
  source: PropertySource
  label: string
  icon: string
}

const props = defineProps&lt;{
  currentSource: PropertySource
}&gt;()

const emit = defineEmits&lt;{
  sourceChange: [source: PropertySource]
}&gt;()

const navItems: NavItem[] = [
  { source: 'all', label: '全部', icon: '📊' },
  { source: 'beike', label: '贝壳', icon: '🏘️' },
  { source: 'douban', label: '豆瓣', icon: '💬' },
  { source: 'baletu', label: '巴乐兔', icon: '🐰' }
]

const handleSourceChange = (source: PropertySource) =&gt; {
  emit('sourceChange', source)
}
&lt;/script&gt;

&lt;style scoped&gt;
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-md) 0 var(--spacing-lg);
  animation: slideDown 0.6s ease;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.logo {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.logo-icon-wrapper {
  position: relative;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-glow {
  position: absolute;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(212, 175, 55, 0.4) 0%, transparent 70%);
  animation: pulseGlow 3s ease-in-out infinite;
}

@keyframes pulseGlow {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.1); }
}

.logo-icon {
  font-size: 2rem;
  position: relative;
  z-index: 1;
}

.logo-text-wrapper {
  display: flex;
  flex-direction: column;
}

.logo-text {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-light) 50%, var(--color-primary) 100%);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmerGradient 4s ease infinite;
}

@keyframes shimmerGradient {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.logo-tagline {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  letter-spacing: 0.05em;
}

.nav {
  display: flex;
  gap: var(--spacing-sm);
  background: var(--color-surface);
  padding: 0.375rem;
  border-radius: var(--radius-xl);
  border: 1px solid var(--color-border);
}

.nav-btn {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.625rem 1.125rem;
  border: none;
  background: transparent;
  color: var(--color-text-muted);
  border-radius: var(--radius-lg);
  cursor: pointer;
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all var(--transition-normal);
  position: relative;
}

.nav-btn-icon {
  font-size: 1.125rem;
}

.nav-btn:hover {
  color: var(--color-text);
  background: var(--color-surface-light);
}

.nav-btn.active {
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  color: var(--color-secondary);
  box-shadow: var(--shadow-gold);
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    gap: var(--spacing-md);
  }

  .nav {
    width: 100%;
    justify-content: center;
  }
}
&lt;/style&gt;
