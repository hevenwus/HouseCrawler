
&lt;template&gt;
  &lt;button
    v-show="isVisible"
    class="back-to-top"
    @click="scrollToTop"
  &gt;
    &lt;span&gt;↑&lt;/span&gt;
  &lt;/button&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import { ref, onMounted, onUnmounted } from 'vue'

const isVisible = ref(false)

const handleScroll = () =&gt; {
  isVisible.value = window.scrollY &gt; 500
}

const scrollToTop = () =&gt; {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() =&gt; {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() =&gt; {
  window.removeEventListener('scroll', handleScroll)
})
&lt;/script&gt;

&lt;style scoped&gt;
.back-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  border: none;
  border-radius: 50%;
  color: var(--color-secondary);
  font-size: 1.25rem;
  cursor: pointer;
  box-shadow: var(--shadow-gold);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition-normal);
  z-index: 1000;
}

.back-to-top:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(212, 175, 55, 0.4);
}
&lt;/style&gt;
