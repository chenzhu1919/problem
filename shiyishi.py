import pygame
import sys

pygame.init()
screen_info = pygame.display.Info()
size= width,height=600,400
screen = pygame.display.set_mode(size)
speed= [-2,1]
bg = (255,255,255)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("试一试")
p = pygame.image.load("burger.png")
position = p.get_rect()
img_width = 120
img_height = 120
p= pygame.transform.smoothscale(p,(img_width,img_height))
step = 0
while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # print("==========================================")
    # print("before move: position left is {}, right is {}, top is {}, bottom is {}".format(position.left, position.right,
    #                                                                                       position.top, position.bottom))
    position = position.move(speed)
    step += 1
    # print("step is {}".format(step))
    # print("after move: position left is {}, right is {}, top is {}, bottom is {}".format(position.left, position.right,
    #
    #         position.top, position.bottom))
    if position.left < 0 or position.left > width-img_width:
        # print("in if position.left <0 or position.right> width")
        p = pygame.transform.flip(p,True, False)
        # print("old speed is {}".format(speed[0]))
        speed[0] = -speed[0]
        # print("updated speed is {}".format(speed[0]))
    if position.top < 0 or position.top > height-img_height:
        # print("in if position.top < 0 or position.bottom > height")
        # print("old speed is {}".format(speed[1]))
        speed[1] = -speed[1]
        # print("updated speed is {}".format(speed[1]))
    screen.fill(bg)
    screen.blit(p,position)
    pygame.display.flip()
    pygame.time.delay(10)
