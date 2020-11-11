
# Modules
import pygame
import random
import sys


def draw_floor():

    screen.blit(floor_surface, (floor_X_pos, 400))
    screen.blit(floor_surface, (floor_X_pos + 288, 400))


def create_pipe():

    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(450, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(450, random_pipe_pos - 100))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 288:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


pygame.init()

screen = pygame.display.set_mode((288, 512))
# limit our frames
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0

# getting image for background
bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
# bg_surface = pygame.transform.scale2x(floor_surface)
floor_X_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
# bg_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(50, 256))

# Pipe
pipe_surface = pygame.image.load('assets/pipe-green.png')
# bg_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [100, 150, 200, 250, 300]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    floor_X_pos -= 1
    draw_floor()
    if floor_X_pos <= -288:
        floor_X_pos = 0

        # ------------------------------------------------------------
    pygame.display.update()
    # dont run faster than 120 frames
    clock.tick(120)
