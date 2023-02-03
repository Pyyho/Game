import pygame, management
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def go():
    pygame.init()
    screen = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Angry christmas toys")
    background_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    management.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        management.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            management.update(background_color, screen, stats, sc, gun, inos, bullets)
            management.update_bullets(screen, stats, sc, inos, bullets)
            management.update_inos(stats, screen, sc,  gun, inos, bullets)


go()
