import pygame

def main():
    pygame.init()
    pygame.display.set_caption("minimal program")

    screenX, screenY = 600,600

    screen = pygame.display.set_mode((screenX, screenY))
    image = pygame.image.load("img/player.png")

    print(image.get_rect().size) 

    x,y = 0,0
    playerBottomY = y + image.get_rect().y/2
    screen.blit(image, (50,50))
    pygame.display.flip()

    running = True
    moveLeft = False
    moveRight = False
    gravity = 0

    groundRect = pygame.Rect(0, screenY - 50, screenX - 10, 20)
    

    while running:
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moveLeft = True
                elif event.key == pygame.K_d:
                    moveRight = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    # move left
                    moveLeft = False
                elif event.key == pygame.K_d:
                    # move right
                    moveRight = False
        screen.fill((0,0,0))
        if moveLeft : x -= 0.5
        if moveRight : x += 0.5
        y += gravity
        pygame.draw.rect(screen, (255,255,255), groundRect)
        screen.blit(image, (x,y))
        pygame.display.update()




if __name__=="__main__":
    main()