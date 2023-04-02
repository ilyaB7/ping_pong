from pygame import *
window = display.set_mode((700, 500))
display.set_caption('тенис')
background = transform.scale(image.load('pesok2.png'),(800, 600))
sprite1 = transform.scale(image.load('raketka2.png'),(100, 100))
sprite2 = transform.scale(image.load('raketka2.png'),(100, 100))
x1=40
y1=350
x2=550
y2=350
s=5
clock = time.Clock()
FPS = 60

window.blit(background,(0, 0))

game = True
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed=key.get_pressed()

    if keys_pressed[K_UP] and y1>5:
        y1-=s
    if keys_pressed[K_DOWN] and y1<400:
        y1+=s

    if keys_pressed[K_w] and y2>5:
        y2-=s
    if keys_pressed[K_s] and y2<400:
        y2+=s   
    display.update()
    clock.tick(FPS)