from Bullet import Bullet
from Enemy import Enemy
from GameOver import GameOver
from Music import Music
from Player import Player
from Score import Score
from Screen import Screen
import pygame


def main():

    # Jalankan pygame
    pygame.init()

    # Instance Object
    bullet = Bullet('./src/bullet.png', './src/laser.wav', (0, 480))
    game_over = GameOver('freesansbold.ttf', 64, (200, 250))
    music = Music('./src/background.wav')
    player = Player('./src/player.png', (370, 480))
    score = Score('freesansbold.ttf', 32, (10, 10))
    screen = Screen('Space Invaders', './src/background.png',
                    './src/ufo.png', (800, 600))

    # Buat Layar
    display = screen.make_window()
    screen.make_caption_icon()

    # Jalankan music
    music.play_bg_music()

    # Buat Musuh
    total_enemy = 6
    enemies = []
    for i in range(total_enemy):
        enemies.append(Enemy('./src/enemy.png', './src/explosion.wav'))
        enemies[i].set_location((0, 735), (50, 150))

    # Jalankan Game
    running = True
    while running:
        screen.show_screen(display)

        # Cek Exit Game
        for event in pygame.event.get():
            running = player.is_exit_game(event)

        # Pergerakan Player
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.shoot(keys, bullet, display)

        # Musuh Menang
        for i in range(total_enemy):
            if enemies[i].is_enemy_win():
                for j in range(total_enemy):
                    enemies[j].gone()
                game_over.show(display)
                break
            enemies[i].move()

            # Musuh Mati
            collision = bullet.is_collision(enemies[i])
            enemies[i].death(bullet, score, collision)

            # Summon Musuh
            enemies[i].draw(display)

        # Summon Object
        bullet.move(display)
        player.draw(display)
        score.show(display)
        pygame.display.update()


if __name__ == '__main__':
    main()
