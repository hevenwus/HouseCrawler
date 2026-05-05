
# HouseCrawler - 智能房产数据平台

采用 Vue 3 + TypeScript + Vite 构建的奢华风格房产数据展示平台。

## 技术栈

- Vue 3 (Composition API)
- TypeScript
- Vite 5
- CSS 变量 + 动画

## 项目结构

```
frontend/
├── src/
│   ├── components/          # Vue 组件
│   │   ├── Header.vue      # 页头导航
│   │   ├── Hero.vue        # 主视觉区
│   │   ├── StatCard.vue    # 统计卡片
│   │   ├── Filters.vue     # 筛选器
│   │   ├── PropertyCard.vue # 房源卡片
│   │   ├── Footer.vue      # 页脚
│   │   └── BackToTop.vue  # 返回顶部
│   ├── types/              # TypeScript 类型定义
│   │   └── property.ts
│   ├── data/               # 模拟数据
│   │   └── mockData.ts
│   ├── composables/        # 组合式函数
│   │   └── useCounterAnimation.ts
│   ├── App.vue             # 根组件
│   ├── main.ts             # 入口文件
│   └── style.css           # 全局样式
├── index.html
├── vite.config.ts
├── tsconfig.json
├── package.json
└── README.md
```

## 快速开始

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

访问 http://localhost:5173 查看应用

### 构建生产版本

```bash
npm run build
```

### 预览生产构建

```bash
npm run preview
```

## 功能特性

### 导航筛选
- 按数据来源筛选（全部/贝壳/豆瓣/巴乐兔）
- 优雅的导航按钮动画

### 数据展示
- 动态数字统计卡片
- 带趋势指示器的统计数据
- 页面入场动画效果

### 筛选系统
- 房源类型筛选（租房/二手房/成交记录）
- 区域筛选
- 关键词搜索（支持 `/` 快捷键聚焦）
- 快速筛选按钮（性价比高/新上房源/热门推荐）

### 视图切换
- 网格视图
- 列表视图

### 房源卡片
- 精美的悬停动画效果
- 图片缩放效果
- 收藏功能（❤️/🤍）
- 来源和标签展示
- 卡片延迟入场动画

### 用户体验
- 平滑滚动返回顶部
- 键盘快捷键支持
- 响应式设计，完美适配移动端
- 加载动画效果

## 设计亮点

### 配色方案
- 金色主色调（#d4af37）
- 深色背景（#0a0a14）
- 渐变和光影效果
- 金色阴影和光晕动画

### 字体
- Playfair Display（标题字体）
- Noto Sans SC（中文正文字体）

### 动画系统
- Logo 脉冲光晕动画
- 文字渐变闪烁
- 数字滚动计数
- 卡片延迟入场
- 按钮光效滑动

### 视觉效果
- 背景噪点纹理
- 径向渐变背景
- 卡片悬停放大
- 图片缩放效果

## 后续开发建议

1. **后端集成**
   - 连接真实的房源数据 API
   - 实现分页加载
   - 添加数据缓存机制

2. **功能增强**
   - 房源详情弹窗/页面
   - 用户账户系统
   - 收藏列表管理
   - 房源对比功能
   - 地图展示房源位置

3. **性能优化**
   - 图片懒加载
   - 虚拟列表（大量数据时）
   - 组件按需加载

4. **测试**
   - 单元测试
   - E2E 测试
   - 性能测试

5. **国际化**
   - 多语言支持
   - 地区适配

## License

MIT
