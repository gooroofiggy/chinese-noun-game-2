import pygame

pygame.init()
window_hight, window_width = 400, 400
window = pygame.display.set_mode([window_hight, window_width])

pygame.display.set_caption("中文 verb game")


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":
    main()
