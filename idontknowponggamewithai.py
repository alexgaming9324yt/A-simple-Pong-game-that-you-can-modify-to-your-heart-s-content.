import pygame 

pygame.init()
res = pygame.display.set_mode((800, 400))
ticks = pygame.time.Clock()

p1 = pygame.Rect(20, 150, 10, 80)
p2 = pygame.Rect(770, 150, 10, 80)
BALL = pygame.Rect(390, 190, 20, 20)

vx, vy = 5, 5 

ai_speed = 3
timer = pygame.time.get_ticks()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    k = pygame.key.get_pressed()

    if k[pygame.K_w]: p1.y -= 5
    if k[pygame.K_s]: p1.y += 5
    if BALL.centery > p2.centery:
        p2.y += ai_speed
    if BALL.centery < p2.centery:
        p2.y -= ai_speed
    BALL.x += vx
    BALL.y += vy

    if BALL.top <= 0 or BALL.bottom >= 400:
        vy *= -1

    if BALL.colliderect(p1) or BALL.colliderect(p2):
        vx *= -1

    if BALL.left <= 0 or BALL.right >= 800:
        BALL.center = (400, 200)
    now = pygame.time.get_ticks()
    if now - timer > 1000:
        timer = now
        ai_speed += 0.2



    res.fill((0, 0, 0))
    pygame.draw.rect(res, (255, 255, 255), p1)
    pygame.draw.rect(res, (255, 255, 255), p2)
    pygame.draw.ellipse(res, (255, 255, 255), BALL)

    pygame.display.flip()
    ticks.tick(60)