import pygame

import sys

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

from circleshape import CircleShape

from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0, 0, 0))
        updatable.update(dt)

        for obj in asteroids:
            if obj.collision_check(player) == True:
                print("Game over!")
                sys.exit()
            

        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()
        
        
        # Limit framerate to 60FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
