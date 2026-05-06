
<template>
  <div
    class="property-card"
    :style="{ animationDelay: `${delay}s` }"
    @click="handleClick"
  >
    <div class="card-shine"></div>
    
    <div class="property-image-container">
      <img :src="property.image" :alt="property.title" class="property-image" loading="lazy" />
      <div class="image-overlay"></div>
      
      <span class="property-badge">{{ property.badge }}</span>
      <span class="property-source">{{ property.sourceName }}</span>
      
      <button
        class="property-favorite"
        :class="{ active: isFavorite }"
        @click.stop="handleFavorite"
      >
        <span class="favorite-icon">{{ isFavorite ? '❤️' : '🤍' }}</span>
        <span class="favorite-ring"></span>
      </button>

      <div class="image-actions">
        <button class="image-action-btn" title="快速查看">
          <span>👁️</span>
        </button>
        <button class="image-action-btn" title="分享">
          <span>📤</span>
        </button>
      </div>
    </div>

    <div class="property-content">
      <h3 class="property-title">{{ property.title }}</h3>
      
      <div class="property-address">
        <span class="address-icon">📍</span>
        <span class="address-text">{{ property.address }}</span>
        <span class="address-distance" v-if="property.distance">距地铁 {{ property.distance }}m</span>
      </div>

      <div class="property-features">
        <div class="feature-item">
          <span class="feature-icon">🏠</span>
          <span class="feature-text">{{ property.rooms }}</span>
        </div>
        <div class="feature-divider"></div>
        <div class="feature-item">
          <span class="feature-icon">📐</span>
          <span class="feature-text">{{ property.area }}</span>
        </div>
        <div class="feature-divider"></div>
        <div class="feature-item">
          <span class="feature-icon">🏢</span>
          <span class="feature-text">{{ property.floor }}</span>
        </div>
      </div>

      <div class="property-tags">
        <span class="tag" v-for="tag in property.tags" :key="tag">{{ tag }}</span>
      </div>

      <div class="property-footer">
        <div class="property-price-wrapper">
          <span class="property-price">{{ property.price }}</span>
          <span class="property-unit">{{ property.priceUnit }}</span>
        </div>
        <div class="property-meta">
          <span class="property-time">{{ property.time }}</span>
          <button class="meta-action-btn" title="更多操作">
            <span>⋮</span>
          </button>
        </div>
      </div>
    </div>

    <div class="card-glow-effect"></div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { Property } from '@/types/property'

interface Props {
  property: Property
  index: number
  favorites: Set<number>
}

const props = defineProps<Props>()

const emit = defineEmits<{
  click: [property: Property]
  toggleFavorite: [id: number]
}>()

const delay = props.index * 0.1
const isFavorite = computed(() => props.favorites.has(props.property.id))

const handleClick = () => {
  emit('click', props.property)
}

const handleFavorite = () => {
  emit('toggleFavorite', props.property.id)
}
</script>

<style scoped>
.property-card {
  background: var(--color-surface);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  opacity: 0;
  animation: cardFadeIn 0.6s ease forwards;
  position: relative;
}

@keyframes cardFadeIn {
  from {
    opacity: 0;
    transform: translateY(40px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.card-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.05),
    transparent
  );
  transition: left 0.6s ease;
  pointer-events: none;
  z-index: 10;
}

.property-card:hover .card-shine {
  left: 100%;
}

.card-glow-effect {
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at 50% 0%,
    rgba(212, 175, 55, 0.15),
    transparent 50%
  );
  opacity: 0;
  transition: opacity 0.4s ease;
  pointer-events: none;
}

.property-card:hover {
  transform: translateY(-12px) scale(1.02);
  box-shadow: 
    var(--shadow-lg),
    0 20px 60px rgba(212, 175, 55, 0.15),
    0 0 40px rgba(212, 175, 55, 0.1);
  border-color: var(--color-primary);
}

.property-card:hover .card-glow-effect {
  opacity: 1;
}

.property-image-container {
  position: relative;
  overflow: hidden;
  height: 260px;
}

.property-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.property-card:hover .property-image {
  transform: scale(1.15);
  filter: brightness(1.1) saturate(1.1);
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    transparent 0%,
    transparent 50%,
    rgba(0, 0, 0, 0.6) 100%
  );
  opacity: 0.6;
  transition: opacity 0.4s ease;
}

.property-card:hover .image-overlay {
  opacity: 0.8;
}

.property-badge {
  position: absolute;
  top: var(--spacing-md);
  left: var(--spacing-md);
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  color: var(--color-secondary);
  border-radius: var(--radius-md);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  z-index: 3;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
  animation: badgeFloat 3s ease-in-out infinite;
}

@keyframes badgeFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-3px); }
}

.property-source {
  position: absolute;
  top: var(--spacing-md);
  right: var(--spacing-md);
  padding: 0.5rem 0.875rem;
  background: rgba(10, 10, 20, 0.85);
  color: var(--color-text);
  border-radius: var(--radius-md);
  font-size: 0.8rem;
  font-weight: 600;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 3;
}

.property-favorite {
  position: absolute;
  bottom: var(--spacing-md);
  right: var(--spacing-md);
  width: 48px;
  height: 48px;
  background: rgba(10, 10, 20, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  backdrop-filter: blur(10px);
  z-index: 3;
  transition: all 0.3s ease;
}

.favorite-icon {
  font-size: 1.4rem;
  transition: all 0.3s ease;
  position: relative;
  z-index: 2;
}

.favorite-ring {
  position: absolute;
  width: 100%;
  height: 100%;
  border: 2px solid transparent;
  border-radius: var(--radius-full);
  transition: all 0.3s ease;
}

.property-favorite:hover {
  transform: scale(1.15);
  background: rgba(212, 175, 55, 0.2);
  border-color: var(--color-primary);
}

.property-favorite:hover .favorite-ring {
  border-color: var(--color-primary);
  animation: ringExpand 0.6s ease forwards;
}

@keyframes ringExpand {
  0% { transform: scale(1); opacity: 1; }
  100% { transform: scale(1.5); opacity: 0; }
}

.property-favorite.active {
  background: rgba(233, 69, 96, 0.2);
  border-color: var(--color-accent);
  animation: favoritePop 0.4s ease;
}

@keyframes favoritePop {
  0% { transform: scale(1); }
  50% { transform: scale(1.3); }
  100% { transform: scale(1); }
}

.image-actions {
  position: absolute;
  bottom: var(--spacing-md);
  left: var(--spacing-md);
  display: flex;
  gap: 0.5rem;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.4s ease;
  z-index: 3;
}

.property-card:hover .image-actions {
  opacity: 1;
  transform: translateY(0);
}

.image-action-btn {
  width: 40px;
  height: 40px;
  background: rgba(10, 10, 20, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  backdrop-filter: blur(10px);
  font-size: 1.1rem;
  transition: all 0.3s ease;
}

.image-action-btn:hover {
  background: rgba(212, 175, 55, 0.2);
  border-color: var(--color-primary);
  transform: translateY(-3px);
}

.property-content {
  padding: var(--spacing-lg);
  position: relative;
  z-index: 2;
}

.property-title {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: var(--spacing-sm);
  color: var(--color-text);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.5;
  transition: color 0.3s ease;
}

.property-card:hover .property-title {
  color: var(--color-primary);
}

.property-address {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  margin-bottom: var(--spacing-md);
  padding-bottom: var(--spacing-md);
  border-bottom: 1px solid var(--color-border);
}

.address-icon {
  font-size: 1rem;
  flex-shrink: 0;
}

.address-text {
  flex: 1;
}

.address-distance {
  font-size: 0.8rem;
  color: var(--color-success);
  background: rgba(74, 222, 128, 0.1);
  padding: 0.25rem 0.625rem;
  border-radius: var(--radius-sm);
  flex-shrink: 0;
}

.property-features {
  display: flex;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  align-items: center;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.feature-icon {
  font-size: 1rem;
}

.feature-divider {
  width: 1px;
  height: 20px;
  background: var(--color-border);
}

.property-tags {
  display: flex;
  gap: 0.5rem;
  margin-bottom: var(--spacing-md);
  flex-wrap: wrap;
}

.tag {
  padding: 0.375rem 0.75rem;
  background: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: var(--radius-md);
  font-size: 0.75rem;
  color: var(--color-primary-light);
  transition: all 0.3s ease;
}

.property-card:hover .tag {
  background: rgba(212, 175, 55, 0.2);
  border-color: var(--color-primary);
}

.property-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--spacing-md);
  border-top: 1px solid var(--color-border);
}

.property-price-wrapper {
  display: flex;
  align-items: baseline;
  gap: 0.375rem;
}

.property-price {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  transition: all 0.3s ease;
}

.property-card:hover .property-price {
  transform: scale(1.05);
}

.property-unit {
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 0.9rem;
  font-weight: 400;
  color: var(--color-text-muted);
}

.property-meta {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.property-time {
  color: var(--color-text-muted);
  font-size: 0.85rem;
}

.meta-action-btn {
  width: 32px;
  height: 32px;
  background: transparent;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--color-text-muted);
  font-size: 1.2rem;
  transition: all 0.3s ease;
}

.meta-action-btn:hover {
  background: rgba(212, 175, 55, 0.1);
  border-color: var(--color-primary);
  color: var(--color-primary);
}
</style>
