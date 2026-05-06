
<template>
  <header class="header">
    <div class="header-background"></div>
    
    <div class="logo" @click="handleLogoClick">
      <div class="logo-icon-wrapper">
        <span class="logo-icon">🏠</span>
        <div class="logo-glow"></div>
        <div class="logo-ring"></div>
      </div>
      <div class="logo-text-wrapper">
        <span class="logo-text">HouseCrawler</span>
        <span class="logo-tagline">
          <span class="tagline-dot"></span>
          智能房产数据平台
        </span>
      </div>
    </div>

    <nav class="nav glass-effect">
      <div class="nav-indicator" :style="indicatorStyle"></div>
      <button
        v-for="item in navItems"
        :key="item.source"
        :class="['nav-btn', { active: currentSource === item.source }]"
        @click="handleSourceChange(item.source)"
        @mouseenter="handleMouseEnter(item.source)"
        @mouseleave="handleMouseLeave"
      >
        <span class="nav-btn-icon">{{ item.icon }}</span>
        <span class="nav-btn-label">{{ item.label }}</span>
        <span class="nav-btn-count" v-if="getSourceCount(item.source) > 0">
          {{ getSourceCount(item.source) }}
        </span>
      </button>
    </nav>

    <div class="header-actions">
      <button class="action-btn glass-effect-light" @click="toggleTheme" :title="isDark ? '切换主题' : '切换主题'">
        <span v-if="isDark">🌙</span>
        <span v-else>☀️</span>
      </button>
      <button class="action-btn glass-effect-light" title="通知">
        <span>🔔</span>
        <span class="notification-badge">3</span>
      </button>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import type { PropertySource } from '@/types/property'
import { mockProperties } from '@/data/mockData'

interface NavItem {
  source: PropertySource
  label: string
  icon: string
}

const props = defineProps<{
  currentSource: PropertySource
}>()

const emit = defineEmits<{
  sourceChange: [source: PropertySource]
}>()

const isDark = ref(true)
const hoveredSource = ref<PropertySource | null>(null)

const navItems: NavItem[] = [
  { source: 'all', label: '全部', icon: '📊' },
  { source: 'beike', label: '贝壳', icon: '🏘️' },
  { source: 'douban', label: '豆瓣', icon: '💬' },
  { source: 'baletu', label: '巴乐兔', icon: '🐰' }
]

const indicatorStyle = computed(() => {
  const activeIndex = navItems.findIndex(item => 
    hoveredSource.value ? item.source === hoveredSource.value : item.source === props.currentSource
  )
  return {
    transform: `translateX(${activeIndex * 100}%)`,
    width: `${100 / navItems.length}%`
  }
})

const getSourceCount = (source: PropertySource) => {
  if (source === 'all') return mockProperties.length
  return mockProperties.filter(p => p.source === source).length
}

const handleSourceChange = (source: PropertySource) => {
  emit('sourceChange', source)
}

const handleMouseEnter = (source: PropertySource) => {
  hoveredSource.value = source
}

const handleMouseLeave = () => {
  hoveredSource.value = null
}

const handleLogoClick = () => {
  emit('sourceChange', 'all')
}

const toggleTheme = () => {
  isDark.value = !isDark.value
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-md) 0 var(--spacing-lg);
  position: relative;
  animation: headerSlideIn 0.6s ease;
}

@keyframes headerSlideIn {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.header-background {
  position: absolute;
  top: 0;
  left: -50%;
  right: -50%;
  height: 100%;
  background: radial-gradient(ellipse at center top, rgba(212, 175, 55, 0.08), transparent 70%);
  pointer-events: none;
  z-index: -1;
}

.logo {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  cursor: pointer;
  transition: transform var(--transition-spring);
}

.logo:hover {
  transform: scale(1.02);
}

.logo-icon-wrapper {
  position: relative;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-icon {
  font-size: 2.2rem;
  position: relative;
  z-index: 2;
  filter: drop-shadow(0 0 8px rgba(212, 175, 55, 0.5));
  transition: transform var(--transition-spring);
}

.logo:hover .logo-icon {
  transform: scale(1.1) rotate(5deg);
}

.logo-glow {
  position: absolute;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(212, 175, 55, 0.5) 0%, transparent 70%);
  animation: pulseGlow 3s ease-in-out infinite;
  z-index: 1;
}

@keyframes pulseGlow {
  0%, 100% { 
    opacity: 0.5; 
    transform: scale(1); 
  }
  50% { 
    opacity: 1; 
    transform: scale(1.15); 
  }
}

.logo-ring {
  position: absolute;
  width: 100%;
  height: 100%;
  border: 2px solid var(--color-primary);
  border-radius: var(--radius-full);
  animation: ringPulse 2s ease-in-out infinite;
  opacity: 0.3;
}

@keyframes ringPulse {
  0%, 100% { transform: scale(1); opacity: 0.3; }
  50% { transform: scale(1.1); opacity: 0.1; }
}

.logo-text-wrapper {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.logo-text {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
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
  letter-spacing: 0.08em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tagline-dot {
  width: 6px;
  height: 6px;
  background: var(--color-success);
  border-radius: var(--radius-full);
  animation: dotPulse 2s ease-in-out infinite;
}

@keyframes dotPulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

.nav {
  display: flex;
  gap: 0.5rem;
  padding: 0.5rem;
  position: relative;
  overflow: hidden;
}

.nav-indicator {
  position: absolute;
  top: 0.5rem;
  left: 0.5rem;
  height: calc(100% - 1rem);
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  border-radius: var(--radius-lg);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: var(--shadow-gold);
  z-index: 0;
}

.nav-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  background: transparent;
  color: var(--color-text-muted);
  border-radius: var(--radius-lg);
  cursor: pointer;
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 0.95rem;
  font-weight: 500;
  transition: all var(--transition-normal);
  position: relative;
  z-index: 1;
}

.nav-btn-icon {
  font-size: 1.25rem;
  transition: transform var(--transition-spring);
}

.nav-btn:hover .nav-btn-icon {
  transform: scale(1.2) rotate(-5deg);
}

.nav-btn-label {
  position: relative;
}

.nav-btn-count {
  position: absolute;
  top: -8px;
  right: -12px;
  min-width: 18px;
  height: 18px;
  background: var(--color-accent);
  color: white;
  font-size: 0.7rem;
  font-weight: 600;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 0.3rem;
  animation: countPop 0.3s ease;
}

@keyframes countPop {
  0% { transform: scale(0); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

.nav-btn.active {
  color: var(--color-secondary);
}

.nav-btn:hover:not(.active) {
  color: var(--color-text);
}

.header-actions {
  display: flex;
  gap: var(--spacing-sm);
}

.action-btn {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  cursor: pointer;
  transition: all var(--transition-normal);
  position: relative;
}

.action-btn:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: var(--shadow-gold);
}

.action-btn:active {
  transform: translateY(-1px) scale(1);
}

.notification-badge {
  position: absolute;
  top: 6px;
  right: 6px;
  min-width: 16px;
  height: 16px;
  background: var(--color-accent);
  color: white;
  font-size: 0.65rem;
  font-weight: 700;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
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

  .nav-btn-label {
    display: none;
  }

  .nav-btn {
    padding: 0.75rem 1rem;
  }

  .header-actions {
    position: absolute;
    top: var(--spacing-md);
    right: 0;
  }
}
</style>
