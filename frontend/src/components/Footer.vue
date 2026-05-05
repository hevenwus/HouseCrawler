
&lt;template&gt;
  &lt;footer class="footer"&gt;
    &lt;div class="footer-content"&gt;
      &lt;div class="footer-logo"&gt;
        &lt;span class="logo-icon"&gt;🏠&lt;/span&gt;
        &lt;span class="logo-text"&gt;HouseCrawler&lt;/span&gt;
      &lt;/div&gt;
      &lt;p class="footer-text"&gt;© 2024 HouseCrawler. 让每一次安家都更安心。&lt;/p&gt;
      &lt;div class="footer-links"&gt;
        &lt;a href="#" class="footer-link"&gt;关于我们&lt;/a&gt;
        &lt;span class="footer-separator"&gt;•&lt;/span&gt;
        &lt;a href="#" class="footer-link"&gt;使用帮助&lt;/a&gt;
        &lt;span class="footer-separator"&gt;•&lt;/span&gt;
        &lt;a href="#" class="footer-link"&gt;免责声明&lt;/a&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/footer&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
&lt;/script&gt;

&lt;style scoped&gt;
.footer {
  text-align: center;
  padding: var(--spacing-xl) 0;
  border-top: 1px solid var(--color-border);
  margin-top: var(--spacing-xl);
}

.footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-md);
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer-logo .logo-icon {
  font-size: 1.5rem;
}

.footer-logo .logo-text {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer-text {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.footer-links {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.footer-link {
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: 0.85rem;
  transition: color var(--transition-fast);
}

.footer-link:hover {
  color: var(--color-primary);
}

.footer-separator {
  color: var(--color-border);
}
&lt;/style&gt;
