import pygame
import simpleGE
import random

pygame.init()

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("still.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 10

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.position = (self.position[0] - self.moveSpeed, self.position[1],self.setImage("Left.png"))

        elif self.isKeyPressed(pygame.K_RIGHT):
            self.position = (self.position[0] + self.moveSpeed, self.position[1],self.setImage("Right.png"))

        elif self.isKeyPressed(pygame.K_UP):
            self.position = (self.position[0], self.position[1] - self.moveSpeed,self.setImage("Forward.png"))

        elif self.isKeyPressed(pygame.K_DOWN):
            self.position = (self.position[0], self.position[1] + self.moveSpeed,self.setImage("Down.png"))




class Enemy(simpleGE.Sprite):
    def __init__(self, scene, player):
        super().__init__(scene)
        self.setImage("enemy.png")
        self.setSize(150, 150)
        self.player = player
        self.moveSpeed = 3

    def process(self):
        # Chasing behavior towards the player
        if self.position[0] < self.player.position[0]:
            self.position = (self.position[0] + self.moveSpeed, self.position[1])
        elif self.position[0] > self.player.position[0]:
            self.position = (self.position[0] - self.moveSpeed, self.position[1])
        if self.position[1] < self.player.position[1]:
            self.position = (self.position[0], self.position[1] + self.moveSpeed)
        elif self.position[1] > self.player.position[1]:
            self.position = (self.position[0], self.position[1] - self.moveSpeed)



def checkCollision(self, other_sprite):

    player_rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
    other_rect = pygame.Rect(other_sprite.position[0], other_sprite.position[1],
                             other_sprite.width, other_sprite.height)

    # Define a smaller collision area (e.g., a smaller rectangle around the player)
    collision_margin = 2  # Adjust as needed
    player_rect.inflate_ip(-collision_margin, -collision_margin)

    # Check for collision
    return player_rect.colliderect(other_rect)
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.screen_width = 700  # Set screen width
        self.screen_height = 1000  # Set screen height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.setImage("field.png")


        self.player = Player(self)
        self.sprites = [self.player]

        self.enemies = []
        for _ in range(5):
            enemy = Enemy(self, self.player)
            self.sprites.append(enemy)
            self.enemies.append(enemy)

    def update(self):
        super().update()

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        super().draw()

    def update(self):
        super().update()
        for enemy in self.enemies:
            if self.player.collidesWith(enemy):
                pygame.quit()
                print("GAME OVER! TRY AGAIN?")
def main():
    game = Game()
    game.start()
    pygame.quit()

if __name__ == '__main__':
    main()
