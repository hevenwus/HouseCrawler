
<template>
  <section class="hero">
    <div class="hero-background">
      <div class="hero-orb hero-orb-1"></div>
      <div class="hero-orb hero-orb-2"></div>
      <div class="hero-orb hero-orb-3"></div>
      <div class="hero-grid"></div>
    </div>

    <div class="hero-content">
      <div class="hero-badge">
        <span class="badge-icon">✨</span>
        <span>实时数据更新</span>
        <span class="badge-pulse"></span>
      </div>

      <h1 class="hero-title">
        <span class="line">发现理想</span>
        <span class="line highlight">居所</span>
      </h1>

      <p class="hero-subtitle">
        <span class="subtitle-text">聚合多平台房源数据</span>
        <span class="subtitle-separator">•</span>
        <span class="subtitle-text">智能筛选</span>
        <span class="subtitle-separator">•</span>
        <span class="subtitle-text">精准匹配</span>
        <br>
        <span class="subtitle-highlight">让安家更简单</span>
      </p>

      <div class="hero-actions">
        <button class="btn-luxury">
          <span>🚀</span>
          <span>开始探索</span>
        </button>
        <button class="btn-ghost">
          <span>📖</span>
          <span>了解更多</span>
        </button>
      </div>
    </div>

    <div class="stats-grid">
      <StatCard
        v-for="(stat, index) in stats"
        :key="stat.label"
        :stat="stat"
        :index="index"
      />
    </div>

    <div class="hero-scroll-indicator">
      <span class="scroll-text">向下滚动</span>
      <div class="scroll-mouse">
        <div class="scroll-wheel"></div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import StatCard from './StatCard.vue'
import type { StatItem } from '@/types/property'
import { statsData } from '@/data/mockData'

const stats = ref<StatItem[]>(statsData)
</script>

<style scoped>
.hero {
  margin-bottom: var(--spacing-2xl);
  position: relative;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: -1;
  overflow: hidden;
}

.hero-orb {
  position: absolute;
  border-radius: var(--radius-full);
  filter: blur(100px);
  opacity: 0.4;
  animation: orbFloat 20s ease-in-out infinite;
}

.hero-orb-1 {
  width: 600px;
  height: 600px;
  background: linear-gradient(135deg, var(--color-primary), transparent);
  top: -200px;
  left: -100px;
  animation-delay: 0s;
}

.hero-orb-2 {
  width: 500px;
  height: 500px;
  background: linear-gradient(135deg, var(--color-accent), transparent);
  top: -100px;
  right: -150px;
  animation-delay: -7s;
}

.hero-orb-3 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, var(--color-success), transparent);
  bottom: -100px;
  left: 50%;
  transform: translateX(-50%);
  animation-delay: -14s;
}

@keyframes orbFloat {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  25% {
    transform: translate(30px, -30px) scale(1.1);
  }
  50% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  75% {
    transform: translate(20px, 10px) scale(1.05);
  }
}

.hero-grid {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(212, 175, 55, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(212, 175, 55, 0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
  animation: gridPulse 4s ease-in-out infinite;
}

@keyframes gridPulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

.hero-content {
  text-align: center;
  margin-bottom: var(--spacing-2xl);
  position: relative;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  background: rgba(212, 175, 55, 0.12);
  border: 1px solid rgba(212, 175, 55, 0.4);
  border-radius: var(--radius-xl);
  color: var(--color-primary-light);
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: var(--spacing-lg);
  animation: fadeInUp 0.6s ease 0.1s forwards;
  opacity: 0;
  position: relative;
  overflow: hidden;
}

.badge-icon {
  font-size: 1.1rem;
  animation: iconBounce 2s ease-in-out infinite;
}

@keyframes iconBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-3px); }
}

.badge-pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  background: rgba(212, 175, 55, 0.2);
  border-radius: inherit;
  transform: translate(-50%, -50%) scale(0);
  animation: badgePulse 2s ease-out infinite;
}

@keyframes badgePulse {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(2);
    opacity: 0;
  }
}

.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3.5rem, 10vw, 6rem);
  font-weight: 900;
  line-height: 1;
  margin-bottom: var(--spacing-lg);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.hero-title .line {
  display: block;
  opacity: 0;
  animation: fadeInUp 0.6s ease forwards;
}

.hero-title .line:nth-child(1) { animation-delay: 0.2s; }
.hero-title .line:nth-child(2) { animation-delay: 0.3s; }

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-title .highlight {
  background: linear-gradient(135deg, var(--color-primary) 0%, #f4d03f 50%, var(--color-primary) 100%);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s ease infinite;
  position: relative;
}

.hero-title .highlight::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 3px;
  background: linear-gradient(90deg, transparent, var(--color-primary), transparent);
  animation: underlineGlow 2s ease-in-out infinite;
}

@keyframes underlineGlow {
  0%, 100% { opacity: 0.5; width: 60%; }
  50% { opacity: 1; width: 80%; }
}

@keyframes shimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.hero-subtitle {
  font-size: 1.2rem;
  color: var(--color-text-muted);
  max-width: 700px;
  margin: 0 auto var(--spacing-xl);
  line-height: 1.8;
  animation: fadeInUp 0.6s ease 0.4s forwards;
  opacity: 0;
}

.subtitle-text {
  display: inline-block;
  transition: all var(--transition-normal);
}

.subtitle-separator {
  display: inline-block;
  margin: 0 0.75rem;
  color: var(--color-primary);
  animation: separatorPulse 2s ease-in-out infinite;
}

@keyframes separatorPulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

.subtitle-highlight {
  display: inline-block;
  color: var(--color-primary);
  font-weight: 600;
  margin-top: 0.5rem;
  animation: highlightPop 0.6s ease 0.5s forwards;
  opacity: 0;
}

@keyframes highlightPop {
  0% {
    opacity: 0;
    transform: scale(0.8);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

.hero-actions {
  display: flex;
  gap: var(--spacing-md);
  justify-content: center;
  animation: fadeInUp 0.6s ease 0.5s forwards;
  opacity: 0;
}

.hero-scroll-indicator {
  position: absolute;
  bottom: -80px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  animation: fadeIn 0.6s ease 1s forwards, bounce 2s ease-in-out infinite 1.5s;
  opacity: 0;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes bounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(-10px); }
}

.scroll-text {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.15em;
}

.scroll-mouse {
  width: 24px;
  height: 38px;
  border: 2px solid var(--color-primary);
  border-radius: 12px;
  position: relative;
  opacity: 0.6;
}

.scroll-wheel {
  width: 4px;
  height: 8px;
  background: var(--color-primary);
  border-radius: 2px;
  position: absolute;
  top: 6px;
  left: 50%;
  transform: translateX(-50%);
  animation: scrollWheel 1.5s ease-in-out infinite;
}

@keyframes scrollWheel {
  0% {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateX(-50%) translateY(12px);
    opacity: 0;
  }
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-md);
  margin-top: var(--spacing-2xl);
  position: relative;
}

@media (max-width: 1024px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .stats-grid { grid-template-columns: 1fr; }
  
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .hero-scroll-indicator {
    display: none;
  }
}
</style>
