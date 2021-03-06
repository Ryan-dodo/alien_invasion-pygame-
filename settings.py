class Settings():
    '''存储设置的类'''
    
    def __init__(self):
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (169, 169,169)
        
        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit=3
        
        # 子弹的设置
        self.bullet_speed_factor=0.0001
        self.bullet_width=10
        self.bullet_height=12000000
        self.bullet_color=255,0,0
        self.bullets_allowed=50
        
        # 外星人的设置
        self.alien_speed_factor=0.5
        self.fleet_drop_speed =25
        # fleet_direction为1表示向右移动-1向左移动
        self.fleet_direction = 1
        
        # 以什么样的速度加快游戏节奏
        self.speedup_scale=1.1
        self.score_scale=1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''初始化游戏变化的设置'''
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.alien_points = 50
        
        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
        
    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        
        self.alien_points=int(self.alien_points*self.score_scale)
