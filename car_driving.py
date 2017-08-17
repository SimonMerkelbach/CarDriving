import pygame
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_TITLE = 'car_driving'
FPS = 60

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)


def main():
    # init all important pygame modules
    pygame.init()

    # create screen surface
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)

    # create sprites
    all_sprites_list = pygame.sprite.Group()
    car = Car(200, 200, 100, 50)
    all_sprites_list.add(car)

    # limit fps
    clock = pygame.time.Clock()

    # main game loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys_pressed = pygame.key.get_pressed()
        car.handle_keys(keys_pressed)

        # clear screen
        screen.fill(BLACK)

        # update sprites and draw them to screen
        all_sprites_list.update()
        all_sprites_list.draw(screen)

        # draw everything to screen
        pygame.display.flip()

        # limit fps
        clock.tick(FPS)
    
    # uninit all pygame modules
    pygame.quit()


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self._original_image = pygame.Surface((width, height))
        self._original_image.fill(GRAY)
        self._original_image.set_colorkey(BLACK)  # make background 'transparent' (same as background color)
        
        self.image = self._original_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.angle = 0
        self.speed = 0
    
    def update(self):
        self.rotate()
        self.move()

    def rotate(self):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self._original_image, self.angle)
        self.rect = self.image.get_rect(center=old_center)

    def move(self):
        rads = math.radians(self.angle)
        dy = math.sin(rads) * self.speed
        dx = math.cos(rads) * self.speed
        self.rect.y -= dy
        self.rect.x += dx

    def handle_keys(self, keys_pressed):
        # accelerate when pressing up
        if keys_pressed[pygame.K_UP]:
            if self.speed < 10:
                self.speed += 0.1
        # decelerate when not pressing up
        if not keys_pressed[pygame.K_UP]:
            if self.speed > 0:
                self.speed -= 0.1
        # brake when pressing down
        if keys_pressed[pygame.K_DOWN]:
            if self.speed > 0:
                self.speed -= 0.2
        # turn left when pressing left
        if keys_pressed[pygame.K_LEFT]:
            self.angle += 4
        # turn right when pressing right
        if keys_pressed[pygame.K_RIGHT]:
            self.angle -= 4

if __name__ == '__main__':
    main()
