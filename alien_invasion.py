import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button 
import game_functions as gf
from scoreboard import Scoreboard

def run_game():
    # 初始化pygame、设置和屏幕对象
    #   Nsimsun   Front
    pygame.init()
    ai_settings: object=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    
    #创建一个储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)        

    
    # 创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个子弹编组
    bullets=Group()
    # 创建一个外星人编组
    aliens=Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    # 设置背景色
    bg_color=(ai_settings.bg_color)
    
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        

        
            
run_game()
