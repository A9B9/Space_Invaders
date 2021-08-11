import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, constrains, speed:float):
        super().__init__()
        self.max_x_constrains = constrains
        self.speed = speed
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.laser_time = 0
        self.ready = True
        self.laser_cooldown = 600
        self.laser_sound = pygame.mixer.Sound('../audio/laser.wav')
        self.laser_sound.set_volume(0.2)

        self.laser = pygame.sprite.Group()


    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.laser.update()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            print(f'Ship Postion :{self.rect.x}')
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            print(f'Ship Postion :{self.rect.x}')

        elif keys[pygame.K_SPACE]:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def shoot_laser(self):
        self.laser.add(Laser(self.rect.center, -9, self.rect.bottom))

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.x = 0
        elif self.rect.right >= self.max_x_constrains:
            self.rect.x = 0

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True



