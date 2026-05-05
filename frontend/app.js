
const mockProperties = [
    {
        id: 1,
        title: '徐汇区精装两室一厅 南北通透 近地铁',
        address: '徐汇区 - 衡山路',
        type: 'rent',
        source: 'beike',
        sourceName: '贝壳',
        price: 8500,
        priceUnit: '/月',
        area: '85㎡',
        rooms: '2室1厅',
        floor: '中层/18层',
        time: '2小时前',
        image: 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&q=80',
        badge: '热门'
    },
    {
        id: 2,
        title: '肥西优质房源 三室两厅 学区房',
        address: '肥西区 - 金寨路',
        type: 'sell',
        source: 'beike',
        sourceName: '贝壳',
        price: 280,
        priceUnit: '万',
        area: '120㎡',
        rooms: '3室2厅',
        floor: '高层/25层',
        time: '5小时前',
        image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80',
        badge: '新上'
    },
    {
        id: 3,
        title: '上海浦东新区独立卫生间 朝南主卧',
        address: '浦东新区 - 张江',
        type: 'rent',
        source: 'douban',
        sourceName: '豆瓣',
        price: 3200,
        priceUnit: '/月',
        area: '18㎡',
        rooms: '主卧',
        floor: '中层/6层',
        time: '1天前',
        image: 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80',
        badge: '个人'
    },
    {
        id: 4,
        title: '巴乐兔精选 温馨一室户 拎包入住',
        address: '上海 - 静安区',
        type: 'rent',
        source: 'baletu',
        sourceName: '巴乐兔',
        price: 4500,
        priceUnit: '/月',
        area: '45㎡',
        rooms: '1室1厅',
        floor: '低层/12层',
        time: '3小时前',
        image: 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800&q=80',
        badge: '精选'
    },
    {
        id: 5,
        title: '肥西成交记录 精装三居室 成交价优',
        address: '肥西区 - 翡翠路',
        type: 'deal',
        source: 'beike',
        sourceName: '贝壳',
        price: 245,
        priceUnit: '万',
        area: '110㎡',
        rooms: '3室1厅',
        floor: '中层/20层',
        time: '成交于3天前',
        image: 'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&q=80',
        badge: '已成交'
    },
    {
        id: 6,
        title: '豆瓣小组 徐汇区次卧转租 限女生',
        address: '徐汇区 - 漕溪路',
        type: 'rent',
        source: 'douban',
        sourceName: '豆瓣',
        price: 2800,
        priceUnit: '/月',
        area: '15㎡',
        rooms: '次卧',
        floor: '高层/8层',
        time: '6小时前',
        image: 'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=800&q=80',
        badge: '转租'
    },
    {
        id: 7,
        title: '巴乐兔 高端公寓 家电齐全 安保完善',
        address: '上海 - 长宁区',
        type: 'rent',
        source: 'baletu',
        sourceName: '巴乐兔',
        price: 7200,
        priceUnit: '/月',
        area: '65㎡',
        rooms: '1室1厅',
        floor: '中层/22层',
        time: '1天前',
        image: 'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=800&q=80',
        badge: '公寓'
    },
    {
        id: 8,
        title: '肥西二手房 毛坯四室 可自由装修',
        address: '肥西区 - 繁华大道',
        type: 'sell',
        source: 'beike',
        sourceName: '贝壳',
        price: 320,
        priceUnit: '万',
        area: '140㎡',
        rooms: '4室2厅',
        floor: '低层/11层',
        time: '2天前',
        image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80',
        badge: '毛坯'
    }
];

function animateCounter(element, target, duration = 1500) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const isFloat = target % 1 !== 0;
    
    const timer = setInterval(() => {
        current += increment;
        if (current &gt;= target) {
            current = target;
            clearInterval(timer);
        }
        
        element.textContent = isFloat ? current.toFixed(1) : Math.floor(current);
    }, 16);
}

function createPropertyCard(property, index) {
    const card = document.createElement('div');
    card.className = 'property-card';
    card.style.animationDelay = `${index * 0.1}s`;
    
    card.innerHTML = `
        &lt;div class="property-image-container"&gt;
            &lt;img src="${property.image}" alt="${property.title}" class="property-image"&gt;
            &lt;span class="property-badge"&gt;${property.badge}&lt;/span&gt;
            &lt;span class="property-source"&gt;${property.sourceName}&lt;/span&gt;
        &lt;/div&gt;
        &lt;div class="property-content"&gt;
            &lt;h3 class="property-title"&gt;${property.title}&lt;/h3&gt;
            &lt;div class="property-address"&gt;
                &lt;span&gt;📍&lt;/span&gt;
                &lt;span&gt;${property.address}&lt;/span&gt;
            &lt;/div&gt;
            &lt;div class="property-info"&gt;
                &lt;span class="info-item"&gt;🏠 ${property.rooms}&lt;/span&gt;
                &lt;span class="info-item"&gt;📐 ${property.area}&lt;/span&gt;
                &lt;span class="info-item"&gt;🏢 ${property.floor}&lt;/span&gt;
            &lt;/div&gt;
            &lt;div class="property-footer"&gt;
                &lt;div class="property-price"&gt;
                    ${property.price}&lt;span class="unit"&gt;${property.priceUnit}&lt;/span&gt;
                &lt;/div&gt;
                &lt;div class="property-time"&gt;${property.time}&lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    `;
    
    return card;
}

function renderProperties(properties) {
    const grid = document.getElementById('propertiesGrid');
    grid.innerHTML = '';
    
    properties.forEach((property, index) =&gt; {
        const card = createPropertyCard(property, index);
        grid.appendChild(card);
    });
}

function initNavButtons() {
    const navButtons = document.querySelectorAll('.nav-btn');
    
    navButtons.forEach(btn =&gt; {
        btn.addEventListener('click', () =&gt; {
            navButtons.forEach(b =&gt; b.classList.remove('active'));
            btn.classList.add('active');
            
            const source = btn.dataset.source;
            let filtered = mockProperties;
            
            if (source !== 'all') {
                filtered = mockProperties.filter(p =&gt; p.source === source);
            }
            
            renderProperties(filtered);
        });
    });
}

function initViewToggle() {
    const viewButtons = document.querySelectorAll('.view-btn');
    const grid = document.getElementById('propertiesGrid');
    
    viewButtons.forEach(btn =&gt; {
        btn.addEventListener('click', () =&gt; {
            viewButtons.forEach(b =&gt; b.classList.remove('active'));
            btn.classList.add('active');
            
            const view = btn.dataset.view;
            if (view === 'list') {
                grid.classList.add('list-view');
            } else {
                grid.classList.remove('list-view');
            }
        });
    });
}

function initFilters() {
    const typeSelect = document.querySelectorAll('.filter-select')[0];
    const areaSelect = document.querySelectorAll('.filter-select')[1];
    const searchInput = document.querySelector('.search-input');
    
    function applyFilters() {
        const type = typeSelect.value;
        const area = areaSelect.value;
        const search = searchInput.value.toLowerCase();
        
        let filtered = mockProperties;
        
        if (type !== 'all') {
            filtered = filtered.filter(p =&gt; p.type === type);
        }
        
        if (search) {
            filtered = filtered.filter(p =&gt; 
                p.title.toLowerCase().includes(search) || 
                p.address.toLowerCase().includes(search)
            );
        }
        
        renderProperties(filtered);
    }
    
    typeSelect.addEventListener('change', applyFilters);
    areaSelect.addEventListener('change', applyFilters);
    searchInput.addEventListener('input', applyFilters);
}

function initLoadMore() {
    const loadMoreBtn = document.querySelector('.btn-primary');
    
    loadMoreBtn.addEventListener('click', () =&gt; {
        loadMoreBtn.textContent = '加载中...';
        
        setTimeout(() =&gt; {
            loadMoreBtn.textContent = '没有更多了';
            loadMoreBtn.disabled = true;
            loadMoreBtn.style.opacity = '0.5';
        }, 1000);
    });
}

function initStatsAnimation() {
    const statValues = document.querySelectorAll('.stat-value');
    
    const observer = new IntersectionObserver((entries) =&gt; {
        entries.forEach(entry =&gt; {
            if (entry.isIntersecting) {
                const target = parseFloat(entry.target.dataset.count);
                animateCounter(entry.target, target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    statValues.forEach(el =&gt; observer.observe(el));
}

function init() {
    renderProperties(mockProperties);
    initNavButtons();
    initViewToggle();
    initFilters();
    initLoadMore();
    initStatsAnimation();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
