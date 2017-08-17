import pygame


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

    # limit fps
    clock = pygame.time.Clock()

    # main game loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # clear screen
        screen.fill(BLACK)

        # draw everything to screen
        pygame.display.flip()

        # limit fps
        clock.tick(FPS)
    
    # uninit all pygame modules
    pygame.quit()


if __name__ == '__main__':
    main()
