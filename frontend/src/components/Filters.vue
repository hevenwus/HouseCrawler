
&lt;template&gt;
  &lt;section class="filter-section"&gt;
    &lt;div class="filter-controls"&gt;
      &lt;div class="filter-group"&gt;
        &lt;label class="filter-label"&gt;房源类型&lt;/label&gt;
        &lt;select class="filter-select" v-model="selectedType" @change="handleTypeChange"&gt;
          &lt;option value="all"&gt;全部类型&lt;/option&gt;
          &lt;option value="rent"&gt;🏠 租房&lt;/option&gt;
          &lt;option value="sell"&gt;🏘️ 二手房&lt;/option&gt;
          &lt;option value="deal"&gt;📋 成交记录&lt;/option&gt;
        &lt;/select&gt;
      &lt;/div&gt;
      &lt;div class="filter-group"&gt;
        &lt;label class="filter-label"&gt;区域&lt;/label&gt;
        &lt;select class="filter-select"&gt;
          &lt;option value="all"&gt;全部区域&lt;/option&gt;
          &lt;option value="xuhui"&gt;📍 徐汇&lt;/option&gt;
          &lt;option value="feixi"&gt;📍 肥西&lt;/option&gt;
          &lt;option value="sh"&gt;📍 上海&lt;/option&gt;
        &lt;/select&gt;
      &lt;/div&gt;
      &lt;div class="filter-group search-group"&gt;
        &lt;label class="filter-label"&gt;搜索&lt;/label&gt;
        &lt;div class="search-wrapper"&gt;
          &lt;input
            ref="searchInputRef"
            type="text"
            class="search-input"
            placeholder="搜索房源、地址、关键词..."
            v-model="searchQuery"
            @input="handleSearch"
          /&gt;
          &lt;span class="search-icon"&gt;🔍&lt;/span&gt;
        &lt;/div&gt;
      &lt;/div&gt;
    &lt;/div&gt;
    &lt;div class="quick-filters"&gt;
      &lt;button
        v-for="filter in quickFilters"
        :key="filter.value"
        class="quick-filter-btn"
        :class="{ active: selectedQuickFilter === filter.value }"
        @click="handleQuickFilter(filter.value)"
      &gt;
        {{ filter.icon }} {{ filter.label }}
      &lt;/button&gt;
    &lt;/div&gt;
  &lt;/section&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import { ref, onMounted } from 'vue'
import type { PropertyType, QuickFilter } from '@/types/property'

const emit = defineEmits&lt;{
  typeChange: [type: PropertyType]
  search: [query: string]
  quickFilterChange: [filter: QuickFilter]
}&gt;()

const selectedType = ref&lt;PropertyType&gt;('all')
const selectedQuickFilter = ref&lt;QuickFilter&gt;('all')
const searchQuery = ref('')
const searchInputRef = ref&lt;HTMLInputElement | null&gt;(null)

const quickFilters = [
  { value: 'all' as QuickFilter, label: '不限价格', icon: '' },
  { value: 'low' as QuickFilter, label: '性价比高', icon: '💰' },
  { value: 'new' as QuickFilter, label: '新上房源', icon: '🆕' },
  { value: 'hot' as QuickFilter, label: '热门推荐', icon: '🔥' }
]

const handleTypeChange = () =&gt; {
  emit('typeChange', selectedType.value)
}

const handleSearch = () =&gt; {
  emit('search', searchQuery.value)
}

const handleQuickFilter = (filter: QuickFilter) =&gt; {
  selectedQuickFilter.value = filter
  emit('quickFilterChange', filter)
}

onMounted(() =&gt; {
  const handleKeyDown = (e: KeyboardEvent) =&gt; {
    if (e.key === '/' &amp;&amp; document.activeElement !== searchInputRef.value) {
      e.preventDefault()
      searchInputRef.value?.focus()
    }
    if (e.key === 'Escape') {
      searchInputRef.value?.blur()
    }
  }

  document.addEventListener('keydown', handleKeyDown)
})
&lt;/script&gt;

&lt;style scoped&gt;
.filter-section {
  margin-bottom: var(--spacing-xl);
}

.filter-controls {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-md);
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-label {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.filter-select,
.search-input {
  width: 100%;
  padding: 0.875rem 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  color: var(--color-text);
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 0.95rem;
  transition: all var(--transition-fast);
}

.search-group {
  grid-column: span 1;
}

.search-wrapper {
  position: relative;
}

.search-icon {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.125rem;
  pointer-events: none;
}

.filter-select:focus,
.search-input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
}

.quick-filters {
  display: flex;
  gap: var(--spacing-sm);
  flex-wrap: wrap;
}

.quick-filter-btn {
  padding: 0.5rem 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  color: var(--color-text-muted);
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-normal);
}

.quick-filter-btn:hover {
  border-color: var(--color-primary);
  color: var(--color-text);
  background: var(--color-surface-light);
}

.quick-filter-btn.active {
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  border-color: transparent;
  color: var(--color-secondary);
}

@media (max-width: 1024px) {
  .filter-controls { grid-template-columns: 1fr; }
}
&lt;/style&gt;
