import pygame

if __name__ == '__main__':
    pygame.init()

    anim = list()

    display = pygame.display.set_mode((700,700))

    sprite = pygame.image.load('images/3.png').convert_alpha()

    #вот так мы вырезаем кадры из нашего спрайта
    anim.append(sprite.subsurface((0,0,96,96)))
    anim.append(sprite.subsurface((96,0,96,96)))
    anim.append(sprite.subsurface((192,0,96,96)))
    anim.append(sprite.subsurface((96,0,96,96)))

    clock = pygame.time.Clock()

    done = False
    dt = 0
    while not done:
        for s in anim:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    done = True

            display.fill((255,255,255))

            news = pygame.transform.scale(s,(196, 196))
            display.blit(news, news.get_rect())


            pygame.display.flip()

            pygame.time.wait(180)