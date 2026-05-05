
&lt;template&gt;
  &lt;div class="noise-overlay"&gt;&lt;/div&gt;
  &lt;div class="gradient-bg"&gt;&lt;/div&gt;

  &lt;div class="container"&gt;
    &lt;Header
      :current-source="currentSource"
      @source-change="handleSourceChange"
    /&gt;

    &lt;Hero /&gt;

    &lt;Filters
      @type-change="handleTypeChange"
      @search="handleSearch"
      @quick-filter-change="handleQuickFilterChange"
    /&gt;

    &lt;section class="properties-section"&gt;
      &lt;div class="section-header"&gt;
        &lt;div class="section-title-wrapper"&gt;
          &lt;h2 class="section-title"&gt;精选房源&lt;/h2&gt;
          &lt;span class="section-count"&gt;找到 &lt;strong&gt;{{ filteredProperties.length }}&lt;/strong&gt; 套房源&lt;/span&gt;
        &lt;/div&gt;
        &lt;div class="view-toggle"&gt;
          &lt;button
            class="view-btn"
            :class="{ active: viewMode === 'grid' }"
            @click="viewMode = 'grid'"
            title="网格视图"
          &gt;
            &lt;svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"&gt;
              &lt;rect x="3" y="3" width="7" height="7"&gt;&lt;/rect&gt;
              &lt;rect x="14" y="3" width="7" height="7"&gt;&lt;/rect&gt;
              &lt;rect x="14" y="14" width="7" height="7"&gt;&lt;/rect&gt;
              &lt;rect x="3" y="14" width="7" height="7"&gt;&lt;/rect&gt;
            &lt;/svg&gt;
          &lt;/button&gt;
          &lt;button
            class="view-btn"
            :class="{ active: viewMode === 'list' }"
            @click="viewMode = 'list'"
            title="列表视图"
          &gt;
            &lt;svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"&gt;
              &lt;line x1="8" y1="6" x2="21" y2="6"&gt;&lt;/line&gt;
              &lt;line x1="8" y1="12" x2="21" y2="12"&gt;&lt;/line&gt;
              &lt;line x1="8" y1="18" x2="21" y2="18"&gt;&lt;/line&gt;
              &lt;line x1="3" y1="6" x2="3.01" y2="6"&gt;&lt;/line&gt;
              &lt;line x1="3" y1="12" x2="3.01" y2="12"&gt;&lt;/line&gt;
              &lt;line x1="3" y1="18" x2="3.01" y2="18"&gt;&lt;/line&gt;
            &lt;/svg&gt;
          &lt;/button&gt;
        &lt;/div&gt;
      &lt;/div&gt;
      &lt;div
        class="properties-grid"
        :class="{ 'list-view': viewMode === 'list' }"
      &gt;
        &lt;PropertyCard
          v-for="(property, index) in filteredProperties"
          :key="property.id"
          :property="property"
          :index="index"
          :favorites="favorites"
          @click="handlePropertyClick"
          @toggle-favorite="handleToggleFavorite"
        /&gt;
      &lt;/div&gt;
      &lt;div class="load-more"&gt;
        &lt;button
          class="btn-primary"
          :disabled="loading"
          @click="handleLoadMore"
        &gt;
          &lt;span v-if="!loading" class="btn-text"&gt;加载更多&lt;/span&gt;
          &lt;span v-else class="btn-loader"&gt;
            &lt;span class="loader-spinner"&gt;&lt;/span&gt;
          &lt;/span&gt;
        &lt;/button&gt;
      &lt;/div&gt;
    &lt;/section&gt;
  &lt;/div&gt;

  &lt;Footer /&gt;
  &lt;BackToTop /&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import { ref, computed } from 'vue'
import Header from './components/Header.vue'
import Hero from './components/Hero.vue'
import Filters from './components/Filters.vue'
import PropertyCard from './components/PropertyCard.vue'
import Footer from './components/Footer.vue'
import BackToTop from './components/BackToTop.vue'
import { mockProperties } from './data/mockData'
import type { Property, PropertySource, PropertyType, QuickFilter } from './types/property'

const currentSource = ref&lt;PropertySource&gt;('all')
const currentType = ref&lt;PropertyType&gt;('all')
const currentQuickFilter = ref&lt;QuickFilter&gt;('all')
const searchQuery = ref('')
const viewMode = ref&lt;'grid' | 'list'&gt;('grid')
const favorites = ref(new Set&lt;number&gt;())
const loading = ref(false)

const filteredProperties = computed(() =&gt; {
  return mockProperties.filter(property =&gt; {
    const sourceMatch = currentSource.value === 'all' || property.source === currentSource.value
    const typeMatch = currentType.value === 'all' || property.type === currentType.value
    const searchMatch = !searchQuery.value ||
      property.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      property.address.toLowerCase().includes(searchQuery.value.toLowerCase())

    let quickFilterMatch = true
    if (currentQuickFilter.value === 'new') {
      quickFilterMatch = property.badge.includes('新上')
    } else if (currentQuickFilter.value === 'hot') {
      quickFilterMatch = property.badge.includes('热门')
    } else if (currentQuickFilter.value === 'low') {
      quickFilterMatch = property.type === 'rent' ? property.price &lt; 4000 : property.price &lt; 300
    }

    return sourceMatch &amp;&amp; typeMatch &amp;&amp; searchMatch &amp;&amp; quickFilterMatch
  })
})

const handleSourceChange = (source: PropertySource) =&gt; {
  currentSource.value = source
}

const handleTypeChange = (type: PropertyType) =&gt; {
  currentType.value = type
}

const handleSearch = (query: string) =&gt; {
  searchQuery.value = query
}

const handleQuickFilterChange = (filter: QuickFilter) =&gt; {
  currentQuickFilter.value = filter
}

const handlePropertyClick = (property: Property) =&gt; {
  console.log('Property clicked:', property.title)
}

const handleToggleFavorite = (id: number) =&gt; {
  if (favorites.value.has(id)) {
    favorites.value.delete(id)
  } else {
    favorites.value.add(id)
  }
}

const handleLoadMore = () =&gt; {
  loading.value = true
  setTimeout(() =&gt; {
    loading.value = false
  }, 1500)
}
&lt;/script&gt;

&lt;style scoped&gt;
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: var(--spacing-lg);
  position: relative;
  z-index: 1;
}

.properties-section {
  margin-bottom: var(--spacing-xl);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-lg);
}

.section-title-wrapper {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-md);
}

.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  font-weight: 700;
}

.section-count {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.section-count strong {
  color: var(--color-primary);
  font-weight: 600;
}

.view-toggle {
  display: flex;
  gap: 0.25rem;
  background: var(--color-surface);
  padding: 0.375rem;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
}

.view-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 0.75rem;
  border: none;
  background: transparent;
  color: var(--color-text-muted);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.view-btn:hover {
  color: var(--color-text);
}

.view-btn.active {
  background: var(--color-surface-light);
  color: var(--color-primary);
}

.properties-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: var(--spacing-lg);
}

.properties-grid.list-view {
  grid-template-columns: 1fr;
}

.list-view .property-card {
  display: flex;
}

.list-view .property-card .property-image-container {
  width: 320px;
  flex-shrink: 0;
  height: 240px;
}

.list-view .property-card .property-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.load-more {
  text-align: center;
  margin-top: var(--spacing-xl);
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 2.25rem;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  border: none;
  border-radius: var(--radius-xl);
  color: var(--color-secondary);
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition-normal);
  box-shadow: var(--shadow-gold);
  position: relative;
  overflow: hidden;
}

.btn-primary::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), transparent);
  transform: translateX(-100%);
  transition: transform var(--transition-slow);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(212, 175, 55, 0.4);
}

.btn-primary:hover:not(:disabled)::before {
  transform: translateX(100%);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.loader-spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid transparent;
  border-top-color: var(--color-secondary);
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 768px) {
  .section-header {
    flex-direction: column;
    gap: var(--spacing-md);
    align-items: flex-start;
  }

  .properties-grid {
    grid-template-columns: 1fr;
  }

  .list-view .property-card {
    flex-direction: column;
  }

  .list-view .property-card .property-image-container {
    width: 100%;
    height: 200px;
  }
}
&lt;/style&gt;
