
# HouseCrawler - 智能房产数据平台

采用 **Vue 3 + TypeScript + Vite** 构建的奢华风格房产数据展示平台，融合了精致的玻璃拟态效果和未来科技感设计。

## ✨ 技术栈

- Vue 3 (Composition API + Script Setup)
- TypeScript (完整类型安全)
- Vite 5 (极速开发体验)
- CSS 变量系统 (现代化样式管理)

## 🎨 设计亮点

### 视觉风格
- **玻璃拟态 (Glassmorphism)**: 半透明磨砂效果，营造层次感
- **动态光效**: 金色渐变、光晕脉动、呼吸灯效果
- **粒子系统**: 背景漂浮粒子，增添活力
- **噪点纹理**: 精致的噪点叠加，增强质感
- **渐变背景**: 多层次径向渐变，深度感十足

### 色彩系统
- 主色：皇家金色 (#d4af37)
- 强调色：活力红 (#e94560)
- 辅助色：成功绿 (#4ade80)
- 深邃背景：#080810
- 半透明表面：rgba 模式

### 动画系统
- **入场动画**: 卡片依次淡入上升
- **交互动画**: 悬停缩放、光效滑动
- **滚动动画**: 平滑滚动、滚动指示器
- **脉冲效果**: Logo 光晕、徽章浮动
- **弹性过渡**: 弹簧物理动画

## 🚀 快速开始

### 安装依赖
```bash
npm install
```

### 开发模式
```bash
npm run dev
```
访问 http://localhost:5173

### 生产构建
```bash
npm run build
```

## 📁 项目结构

```
frontend/
├── src/
│   ├── components/              # Vue 组件库
│   │   ├── Header.vue           # 智能导航头
│   │   ├── Hero.vue             # 动态主视觉
│   │   ├── StatCard.vue        # 统计卡片
│   │   ├── Filters.vue          # 高级筛选器
│   │   ├── PropertyCard.vue     # 房源卡片
│   │   ├── Footer.vue           # 页脚
│   │   └── BackToTop.vue        # 返回顶部
│   ├── types/                   # TypeScript 类型
│   │   └── property.ts
│   ├── data/                    # 模拟数据
│   │   └── mockData.ts
│   ├── composables/             # 组合式函数
│   │   └── useCounterAnimation.ts
│   ├── App.vue                  # 根组件
│   ├── main.ts                  # 入口文件
│   └── style.css                # 全局样式系统
├── index.html
├── vite.config.ts
├── tsconfig.json
├── package.json
└── README.md
```

## 🎯 核心功能

### 1. 智能导航
- ✅ 数据源筛选（全部/贝壳/豆瓣/巴乐兔）
- ✅ 动态数量统计显示
- ✅ 平滑指示器动画
- ✅ Logo 脉冲光效

### 2. 主视觉区域
- ✅ 动态渐变光球漂浮动画
- ✅ 网格背景脉动效果
- ✅ 滚动鼠标指示器
- ✅ 渐变标题文字动画

### 3. 数据统计
- ✅ 数字滚动动画
- ✅ 趋势指示器（上升/下降）
- ✅ 悬停光效增强
- ✅ 延迟入场动画

### 4. 高级筛选
- ✅ 类型筛选（租房/二手房/成交记录）
- ✅ 区域筛选
- ✅ 智能搜索（支持 `/` 快捷键）
- ✅ 快速筛选标签
- ✅ 实时结果计数

### 5. 房源展示
- ✅ 玻璃拟态卡片设计
- ✅ 图片缩放+滤镜效果
- ✅ 悬停光效滑动
- ✅ 快速操作按钮（查看/分享）
- ✅ 收藏功能（心跳动画）
- ✅ 标签系统
- ✅ 价格悬停放大

### 6. 用户体验
- ✅ 平滑滚动返回顶部
- ✅ 键盘快捷键支持
- ✅ 响应式设计（桌面/平板/手机）
- ✅ 加载动画
- ✅ 通知系统（示例）

## 🔧 样式系统

### CSS 变量
```css
/* 颜色 */
--color-primary: #d4af37;
--color-accent: #e94560;
--color-success: #4ade80;

/* 阴影 */
--shadow-gold: 0 4px 30px rgba(212, 175, 55, 0.2);
--shadow-glow: 0 0 40px rgba(212, 175, 55, 0.15);

/* 过渡 */
--transition-spring: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

### 工具类
- `.glass-effect`: 玻璃拟态背景
- `.text-gradient`: 渐变文字
- `.glow-border`: 发光边框
- `.btn-luxury`: 奢华按钮
- `.btn-ghost`: 幽灵按钮

## 📦 性能优化

- 图片懒加载
- CSS 动画优先（GPU 加速）
- 组件按需渲染
- TypeScript 类型检查
- Vite 快速热更新

## 🔮 未来规划

### 功能增强
- [ ] 房源详情弹窗/页面
- [ ] 用户认证系统
- [ ] 收藏列表管理
- [ ] 房源对比功能
- [ ] 地图集成展示

### 技术升级
- [ ] 状态管理 (Pinia)
- [ ] 路由系统 (Vue Router)
- [ ] 后端 API 集成
- [ ] 单元测试
- [ ] E2E 测试

### 交互优化
- [ ] 拖拽排序
- [ ] 无限滚动
- [ ] 实时通知
- [ ] 主题切换

## 📚 学习资源

- [Vue 3 文档](https://v3.vuejs.org/)
- [Vite 指南](https://vitejs.dev/)
- [TypeScript 手册](https://www.typescriptlang.org/)
- [CSS 动画](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License - 自由使用、修改和分发。
