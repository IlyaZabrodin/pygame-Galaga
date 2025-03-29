import pygame
import sqlite3
import sys
import random
import os
import pygame_menu
from Galaxy_generator import galaxy_generator
from millineum_falcon import Millineum_falcon
from TIE_fighter import TIE_fighter
from StarDesroyer import star_destroyer
from lazer_bullet import lazer_bullet
from asteroid import asteroid
from spawned_TIE import spawned_TIE

pygame.init()
con = sqlite3.connect("Records.db")
cur = con.cursor()
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
img_dir = os.path.join(os.path.dirname(__file__), 'img')
snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
explosion_sound = pygame.mixer.Sound(os.path.join('data', 'explosion.flac'))
My_sql_query = """SELECT Health, Damage from Records WHERE Name = ?"""
result = cur.execute(My_sql_query, ("Gosha",))
record = result.fetchall()
pygame.mixer.music.load(os.path.join('data', 'star-wars-imperial-march.mp3'))
volume = 0.7
pygame.mixer.music.set_volume(volume)
health = record[0][0]
pygame.mixer.music.play(loops=-1)


def start_the_game():
    pause_text = pygame.font.SysFont('Consolas', 32).render('Пауза', True, pygame.color.Color('White'))

    RUNNING, PAUSE = 0, 1
    state = RUNNING

    global n
    global n_TIE
    global wave
    global boss
    global points
    global health

    galaxy_group = pygame.sprite.Group()
    played_ship = pygame.sprite.Group()
    empire_TIE_fighters = pygame.sprite.Group()
    empire_star_destroyers = pygame.sprite.Group()
    lazer_bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    destroyer_TIEs = pygame.sprite.Group()
    empire_lazer_bullets = pygame.sprite.Group()

    falcon = Millineum_falcon(played_ship)

    galaxy = galaxy_generator(galaxy_group)

    galaxy_group.draw(screen)
    galaxy_group.update()

    fps = 60
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 50)
    text = font.render(f"HP : {falcon.health}", True, pygame.Color('yellow'))
    text_x = 0
    text_y = 0
    screen.blit(text, (text_x, text_y))

    pygame.display.flip()

    game_over_bool = False

    cooldown = 60

    if not boss:
        for i in range(4):
            Ast = asteroid()
            asteroids.add(Ast)

    if boss:
        star_destr = star_destroyer(empire_star_destroyers)

    running = True

    while running:
        played_ship.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    falcon.speedx = -8
                if event.key == pygame.K_d:
                    falcon.speedx = 8
                if event.key == pygame.K_w:
                    falcon.speedy = -8
                if event.key == pygame.K_s:
                    falcon.speedy = 8
                if event.key == pygame.K_ESCAPE:
                    state = PAUSE
            if state == PAUSE:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 250):
                        if (pygame.mouse.get_pos()[0] <= 540) and (pygame.mouse.get_pos()[1] <= 300):
                            start_the_game()
                    if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 330):
                        if (pygame.mouse.get_pos()[0] <= 540) and (pygame.mouse.get_pos()[1] <= 380):
                            n = 5
                            n_TIE = 0
                            wave = 0
                            boss = False
                            points = 0
                            start_the_game()

                    if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 410):
                        if (pygame.mouse.get_pos()[0] <= 540) and (pygame.mouse.get_pos()[1] <= 460):
                            begin_game()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    falcon.speedx = 0
                if event.key == pygame.K_d:
                    falcon.speedx = 0
                if event.key == pygame.K_w:
                    falcon.speedy = 0
                if event.key == pygame.K_s:
                    falcon.speedy = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x_pli, y_pli = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    falcon.shoot(x_pli, y_pli, lazer_bullets)

        if state == RUNNING:
            if not empire_TIE_fighters and not empire_star_destroyers and not asteroids:
                wave += 1
                if wave >= 5:
                    n_TIE += 1
                n += 1

            if not asteroids and wave <= 5 and not wave % 10 == 0 and not empire_TIE_fighters \
                    and not empire_star_destroyers and not destroyer_TIEs:
                for i in range(n):
                    Ast = asteroid()
                    asteroids.add(Ast)

            elif wave > 4 and not wave % 10 == 0 and not empire_TIE_fighters and not empire_star_destroyers \
                    and not asteroids and not destroyer_TIEs:
                for i in range(n):
                    Ast = asteroid()
                    asteroids.add(Ast)
                for i in range(n_TIE):
                    TIE = TIE_fighter(empire_TIE_fighters)

            if wave % 10 == 0 and not empire_TIE_fighters and not empire_star_destroyers and not asteroids:
                star_destr = star_destroyer(empire_star_destroyers)
                boss = True

            if wave % 10 == 0 and not destroyer_TIEs and empire_star_destroyers and cooldown == 60:
                cooldown = 0
                sTIE_1 = spawned_TIE(destroyer_TIEs)
                sTIE_1.rect.x = 200
                sTIE_1.rect.y = 100
                sTIE_2 = spawned_TIE(destroyer_TIEs)
                sTIE_2.rect.x = 508
                sTIE_2.rect.y = 100

            elif wave % 10 == 0 and not destroyer_TIEs and empire_star_destroyers and cooldown != 60:
                cooldown += 1

            if wave % 10 == 0 and not empire_lazer_bullets and empire_star_destroyers:
                star_destr.shoot(falcon.rect.x, falcon.rect.y, empire_lazer_bullets)
                for el in destroyer_TIEs:
                    el.shoot(falcon.rect.x, falcon.rect.y, empire_lazer_bullets)

            if not empire_lazer_bullets and empire_TIE_fighters:
                for el in empire_TIE_fighters:
                    el.shoot(falcon.rect.x, falcon.rect.y, empire_lazer_bullets)

            hits_asteroids = pygame.sprite.groupcollide(asteroids, lazer_bullets, True, True)
            hits_TIE = pygame.sprite.groupcollide(empire_TIE_fighters, lazer_bullets, True, True)
            hits_asteroids_with_TIE = pygame.sprite.groupcollide(empire_TIE_fighters, asteroids, True, True)
            hits_destroyers = pygame.sprite.groupcollide(empire_star_destroyers, lazer_bullets, False, True)
            hits_TIE_spawned = pygame.sprite.groupcollide(destroyer_TIEs, lazer_bullets, True, True)

            for el in hits_asteroids:
                explosion_sound.play()

            for el in hits_TIE:
                explosion_sound.play()

            for el in hits_asteroids_with_TIE:
                explosion_sound.play()

            for el in hits_TIE_spawned:
                explosion_sound.play()

            for el in hits_TIE:
                points += 150

            for el in hits_asteroids:
                points += 50

            if pygame.sprite.spritecollide(falcon, empire_TIE_fighters, True):
                game_over_bool = True

            if not empire_star_destroyers:
                boss = False

            for el in hits_destroyers:
                star_destr.health -= falcon.damage
                if star_destr.health <= 0:
                    star_destr.kill()
                    sTIE_1.kill()
                    sTIE_2.kill()
                    points += 2000

            falcon.mask = pygame.mask.from_surface(falcon.image)

            for el in empire_star_destroyers:
                el.mask = pygame.mask.from_surface(el.image)
                if pygame.sprite.collide_mask(falcon, el):
                    game_over_bool = True

            for el in destroyer_TIEs:
                el.mask = pygame.mask.from_surface(el.image)
                if pygame.sprite.collide_mask(falcon, el):
                    game_over_bool = True

            if pygame.sprite.spritecollide(falcon, asteroids, True):
                health -= 50
                if health <= 0:
                    game_over_bool = True

            if pygame.sprite.spritecollide(falcon, empire_lazer_bullets, True):
                health -= 100
                if health <= 0:
                    game_over_bool = True

            if game_over_bool:
                My_sql_query = """SELECT Record from Records WHERE Name = ?"""
                result = cur.execute(My_sql_query, ("Gosha",))
                record = result.fetchall()
                if points > record[0][0]:
                    text = font.render(f"Congratulations! New record: : {points}!", True, pygame.Color('yellow'))
                    text_x = width // 2 - text.get_width() // 2
                    text_y = height // 2 - text.get_height() // 2 - 30
                    screen.blit(text, (text_x, text_y))
                    My_sql_query = """UPDATE Records SET record = ? WHERE Name = ?"""
                    cur.execute(My_sql_query, (points, "Gosha",))
                    con.commit()
                My_sql_query_2 = """SELECT Money from Records WHERE Name = ?"""
                result = cur.execute(My_sql_query_2, ("Gosha",))
                money = result.fetchall()
                new_money = money[0][0] + points
                My_sql_query = """UPDATE Records SET money = ? WHERE Name = ?"""
                cur.execute(My_sql_query, (new_money, "Gosha",))
                con.commit()
                explosion_sound.play()
                game_over()
                running = False

            galaxy_group.draw(screen)
            galaxy_group.update()

            empire_star_destroyers.draw(screen)
            empire_star_destroyers.update()

            played_ship.draw(screen)
            played_ship.update()

            empire_TIE_fighters.draw(screen)
            empire_TIE_fighters.update()

            lazer_bullets.draw(screen)
            lazer_bullets.update()

            empire_lazer_bullets.draw(screen)
            empire_lazer_bullets.update()

            asteroids.draw(screen)
            asteroids.update()

            destroyer_TIEs.draw(screen)
            destroyer_TIEs.update()

            text = font.render(f"HP : {health}", True, pygame.Color('yellow'))
            text_x = 0
            text_y = 0
            screen.blit(text, (text_x, text_y))
            text_2 = font.render(f"Wave : {wave + 1}", True, pygame.Color('yellow'))
            text_x_2 = 0
            text_y_2 = 30
            screen.blit(text_2, (text_x_2, text_y_2))
            text_3 = font.render(f"Points : {points}", True, pygame.Color('yellow'))
            text_x_3 = 0
            text_y_3 = 60
            screen.blit(text_3, (text_x_3, text_y_3))

        elif state == PAUSE:
            screen.blit(pause_text, (350, 200))

            continue_button = pygame.draw.rect(screen, (255, 255, 255), (260, 250, 280, 50))
            continue_game_text = pygame.font.SysFont('Consolas', 32).render('Продолжить игру', True,
                                                                            pygame.color.Color('Black'))
            screen.blit(continue_game_text, (265, 260))

            retur_button = pygame.draw.rect(screen, (255, 255, 255), (260, 330, 280, 50))
            retur_game_text = pygame.font.SysFont('Consolas', 32).render('Начать заново', True,
                                                                         pygame.color.Color('Black'))
            screen.blit(retur_game_text, (265, 340))

            exit_button = pygame.draw.rect(screen, (255, 255, 255), (260, 410, 280, 50))
            exit_game_text = pygame.font.SysFont('Consolas', 32).render('Выйти', True,
                                                                        pygame.color.Color('Black'))
            screen.blit(exit_game_text, (265, 420))

        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()


def set_shop(selected, value):
    global t
    fl = 1
    t = tuple('Set difficulty to {} ({})'.format(selected[0][0][0], value))


def buy():
    hp = 50
    damag = 10
    My_sql_query_2 = """SELECT Money from Records WHERE Name = ?"""
    result = cur.execute(My_sql_query_2, ("Gosha",))
    mon = result.fetchall()
    m = mon[0][0]
    if m > 5000:
        if fl == 1:
            if (int(t[-2]) == 1) or (t == 0):
                My_sql_query = """SELECT Health from Records WHERE Name = ?"""
                res = cur.execute(My_sql_query, ("Gosha",))
                rec = res.fetchall()
                recc = rec[0][0] + hp
                My_sql_query2 = """UPDATE Records SET Health = ? WHERE Name = ?"""
                res2 = cur.execute(My_sql_query2, (recc, "Gosha",))
                con.commit()
            else:
                My_sql_query = """SELECT Health from Records WHERE Name = ?"""
                res2 = cur.execute(My_sql_query, ("Gosha",))
                rec2 = res2.fetchall()
                recc2 = rec2[0][0] + damag
                My_sql_query2 = """UPDATE Records SET Damage = ? WHERE Name = ?"""
                res2 = cur.execute(My_sql_query2, (recc2, "Gosha",))
                con.commit()
        else:
            My_sql_query = """SELECT Health from Records WHERE Name = ?"""
            res = cur.execute(My_sql_query, ("Gosha",))
            rec = res.fetchall()
            recc = rec[0][0] + hp
            My_sql_query2 = """UPDATE Records SET Health = ? WHERE Name = ?"""
            res2 = cur.execute(My_sql_query2, (recc, "Gosha",))
            con.commit()


def open_the_shop():
    global fl
    fl = 0
    menu2 = pygame_menu.Menu(
        height=550,
        theme=pygame_menu.themes.THEME_DARK,
        title='Магазин',
        width=750
    )

    menu2.add_selector('Выбор: ', [('Увеличение здоровья', 1), ('Увеличение урона', 2)], onchange=set_shop)
    menu2.add_button('Купить', buy)
    menu2.add_button('Выйти из магазина', begin_game)

    menu2.mainloop(screen)


points = 0
n = 5
n_TIE = 0
wave = 0
boss = False


def game_over():
    font = pygame.font.Font(None, 50)
    text = font.render("Game over!", True, pygame.Color('yellow'))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    fps = 60
    clock = pygame.time.Clock()
    waiting = True
    cyberbulling = False
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cyberbulling = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    begin_game()
                    waiting = False

        if not cyberbulling:
            pygame.display.flip()

        global points
        global n
        global n_TIE
        global wave
        global boss
        global health
        points = 0
        n = 5
        n_TIE = 0
        wave = 0
        boss = False
        My_sql_query = """SELECT Health, Damage from Records WHERE Name = ?"""
        result = cur.execute(My_sql_query, ("Gosha",))
        record = result.fetchall()
        health = record[0][0]

def begin_game():
    menu = pygame_menu.Menu(
        height=550,
        theme=pygame_menu.themes.THEME_DARK,
        title='Galaga',
        width=750
    )

    menu.add_text_input('Логин: ', maxchar=10)
    # menu.add_button('Об игре', playing_the_game)
    menu.add_button('Магазин', open_the_shop)
    menu.add_button('Начать Игру', start_the_game)
    menu.add_button('Включитьму музыку', turn_on)
    menu.add_button('Выключить музыку', turn_of)
    menu.add_button('Увеличить громкость музыки', increase)
    menu.add_button('Уменьшить громкость музыки', reduce)
    menu.add_button('Выйти', pygame_menu.events.EXIT)

    if __name__ == '__main__':
        menu.mainloop(screen)


def turn_on():
    pygame.mixer.music.unpause()


def turn_of():
    pygame.mixer.music.pause()


def increase():
    global volume
    if volume < 1:
        volume += 0.1
    pygame.mixer.music.set_volume(volume)


def reduce():
    global volume
    if volume > 0:
        volume -= 0.1
    pygame.mixer.music.set_volume(volume)


begin_game()
con.close()