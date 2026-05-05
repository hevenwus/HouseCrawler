
export type PropertySource = 'all' | 'beike' | 'douban' | 'baletu'

export type PropertyType = 'all' | 'rent' | 'sell' | 'deal'

export type QuickFilter = 'all' | 'low' | 'new' | 'hot'

export interface Property {
  id: number
  title: string
  address: string
  type: PropertyType
  source: PropertySource
  sourceName: string
  price: number
  priceUnit: string
  area: string
  rooms: string
  floor: string
  time: string
  image: string
  badge: string
}

export interface StatItem {
  value: number
  label: string
  icon: string
  trend?: 'up' | 'down'
  trendValue?: string
}
