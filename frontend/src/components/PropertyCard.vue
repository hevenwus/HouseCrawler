
&lt;template&gt;
  &lt;div
    class="property-card"
    :style="{ animationDelay: `${delay}s` }"
    @click="handleClick"
  &gt;
    &lt;div class="property-image-container"&gt;
      &lt;img :src="property.image" :alt="property.title" class="property-image" loading="lazy" /&gt;
      &lt;span class="property-badge"&gt;{{ property.badge }}&lt;/span&gt;
      &lt;span class="property-source"&gt;{{ property.sourceName }}&lt;/span&gt;
      &lt;button
        class="property-favorite"
        :class="{ active: isFavorite }"
        @click.stop="handleFavorite"
      &gt;
        {{ isFavorite ? '❤️' : '🤍' }}
      &lt;/button&gt;
    &lt;/div&gt;
    &lt;div class="property-content"&gt;
      &lt;h3 class="property-title"&gt;{{ property.title }}&lt;/h3&gt;
      &lt;div class="property-address"&gt;
        &lt;span&gt;📍&lt;/span&gt;
        &lt;span&gt;{{ property.address }}&lt;/span&gt;
      &lt;/div&gt;
      &lt;div class="property-info"&gt;
        &lt;span class="info-item"&gt;{{ property.rooms }}&lt;/span&gt;
        &lt;span class="info-item"&gt;📐 {{ property.area }}&lt;/span&gt;
        &lt;span class="info-item"&gt;{{ property.floor }}&lt;/span&gt;
      &lt;/div&gt;
      &lt;div class="property-footer"&gt;
        &lt;div class="property-price"&gt;
          {{ property.price }}&lt;span class="unit"&gt;{{ property.priceUnit }}&lt;/span&gt;
        &lt;/div&gt;
        &lt;div class="property-time"&gt;{{ property.time }}&lt;/div&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import { computed } from 'vue'
import type { Property } from '@/types/property'

interface Props {
  property: Property
  index: number
  favorites: Set&lt;number&gt;
}

const props = defineProps&lt;Props&gt;()

const emit = defineEmits&lt;{
  click: [property: Property]
  toggleFavorite: [id: number]
}&gt;()

const delay = props.index * 0.1
const isFavorite = computed(() =&gt; props.favorites.has(props.property.id))

const handleClick = () =&gt; {
  emit('click', props.property)
}

const handleFavorite = () =&gt; {
  emit('toggleFavorite', props.property.id)
}
&lt;/script&gt;

&lt;style scoped&gt;
.property-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all var(--transition-normal);
  cursor: pointer;
  opacity: 0;
  animation: cardFadeIn 0.5s ease forwards;
  position: relative;
}

@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.property-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 0%, rgba(212, 175, 55, 0.1), transparent 60%);
  opacity: 0;
  transition: opacity var(--transition-normal);
  pointer-events: none;
  z-index: 1;
}

.property-card:hover {
  transform: translateY(-12px) scale(1.02);
  box-shadow: var(--shadow-lg), var(--shadow-gold);
  border-color: var(--color-primary);
}

.property-card:hover::before {
  opacity: 1;
}

.property-image-container {
  position: relative;
  overflow: hidden;
  height: 240px;
}

.property-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-slow), filter var(--transition-slow);
}

.property-card:hover .property-image {
  transform: scale(1.1);
  filter: brightness(1.1);
}

.property-badge {
  position: absolute;
  top: var(--spacing-md);
  left: var(--spacing-md);
  padding: 0.375rem 0.75rem;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  color: var(--color-secondary);
  border-radius: var(--radius-md);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  z-index: 2;
  box-shadow: var(--shadow-sm);
}

.property-source {
  position: absolute;
  top: var(--spacing-md);
  right: var(--spacing-md);
  padding: 0.375rem 0.75rem;
  background: rgba(10, 10, 20, 0.9);
  color: var(--color-text);
  border-radius: var(--radius-md);
  font-size: 0.75rem;
  font-weight: 600;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 2;
}

.property-favorite {
  position: absolute;
  bottom: var(--spacing-md);
  right: var(--spacing-md);
  width: 40px;
  height: 40px;
  background: rgba(10, 10, 20, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  cursor: pointer;
  backdrop-filter: blur(10px);
  z-index: 2;
  transition: all var(--transition-fast);
}

.property-favorite:hover {
  background: rgba(212, 175, 55, 0.2);
  border-color: var(--color-primary);
  transform: scale(1.1);
}

.property-favorite.active {
  background: rgba(233, 69, 96, 0.2);
  border-color: var(--color-accent);
}

.property-content {
  padding: var(--spacing-lg);
  position: relative;
  z-index: 1;
}

.property-title {
  font-size: 1.15rem;
  font-weight: 600;
  margin-bottom: var(--spacing-sm);
  color: var(--color-text);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.4;
}

.property-address {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  margin-bottom: var(--spacing-md);
}

.property-info {
  display: flex;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  padding-bottom: var(--spacing-md);
  border-bottom: 1px solid var(--color-border);
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  color: var(--color-text-muted);
  font-size: 0.85rem;
}

.property-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.property-price {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.property-price .unit {
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 0.85rem;
  font-weight: 400;
  color: var(--color-text-muted);
  -webkit-text-fill-color: var(--color-text-muted);
}

.property-time {
  color: var(--color-text-muted);
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.375rem;
}
&lt;/style&gt;
