import pygame
import math

# pygame options
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_TITLE = 'car_driving'
FPS = 60

# colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

# car options
MAX_SPEED = 10  # higher = greater max speed
ACCELERATION = 1/10  # higher = greater acceleration
DECELERATION = 1/10  # higher = greater deceleration
BRAKE = 2/10  # higher = stronger brake
TURN_SPEED = 4  # higher = faster turn = smaller turn radius


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
        # limit fps and get deltatime
        deltatime = clock.tick(FPS)

        # poll input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # fps and deltatime testing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    FPS = 10
                elif event.key == pygame.K_2:
                    FPS = 20
                elif event.key == pygame.K_3:
                    FPS = 30
                elif event.key == pygame.K_4:
                    FPS = 40
                elif event.key == pygame.K_5:
                    FPS = 50
                elif event.key == pygame.K_6:
                    FPS = 60
                elif event.key == pygame.K_7:
                    FPS = 70
                elif event.key == pygame.K_8:
                    FPS = 80
                elif event.key == pygame.K_9:
                    FPS = 90
                elif event.key == pygame.K_0:
                    FPS = 1000
        keys_pressed = pygame.key.get_pressed()
        car.handle_keys(keys_pressed)

        # clear screen
        screen.fill(BLACK)

        # update sprites and draw them to screen
        all_sprites_list.update()
        all_sprites_list.draw(screen)

        # draw everything to screen
        pygame.display.flip()
    
    # uninit all pygame modules
    pygame.quit()


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # must keep original to copy from
        self._original_image = pygame.Surface((width, height))
        self._original_image.fill(GRAY)
        self._original_image.set_colorkey(BLACK)  # make background 'transparent' (same as background color)
        # copy original, this copy will be used for editing (e.g. rotating)
        self.image = self._original_image
        # 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # no movement at creation
        self.angle = 0
        self.speed = 0
    
    def update(self):
        self.rotate()
        self.move()

    def rotate(self):
        # this allows rotation around the center instead of top left corner
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
            if self.speed < MAX_SPEED:
                self.speed += ACCELERATION
        # decelerate when not pressing up
        if not keys_pressed[pygame.K_UP]:
            if self.speed > 0:
                self.speed -= DECELERATION
        # brake when pressing down
        if keys_pressed[pygame.K_DOWN]:
            if self.speed > 0:
                self.speed -= BRAKE
        # turn left when pressing left
        if keys_pressed[pygame.K_LEFT]:
            self.angle += TURN_SPEED
        # turn right when pressing right
        if keys_pressed[pygame.K_RIGHT]:
            self.angle -= TURN_SPEED


if __name__ == '__main__':
    main()
