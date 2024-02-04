import pygame
import sys
import random

class DiceSimulator:
    def __init__(self, num_faces):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Simulateur de Dés By LucasTylczak ")

        self.num_faces = num_faces
        self.dice_size = 100
        self.dice_pos = [self.width // 2 - self.dice_size // 2, self.height // 2 - self.dice_size // 2]
        self.font = pygame.font.Font(None, 36)

        self.rolling = False
        self.roll_duration = 1000 # en millisecondes

    def draw_dice(self, face):
        pygame.draw.rect(self.screen, (255, 255, 255), (*self.dice_pos, self.dice_size, self.dice_size))
        
        if face == 1:
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 2, self.dice_pos[1] + self.dice_size // 2), 10)
        elif face == 2:
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
        elif face == 3:
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 2, self.dice_pos[1] + self.dice_size // 2), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
        elif face == 4:
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
        elif face == 5:
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 2, self.dice_pos[1] + self.dice_size // 2), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
        elif face == 6:
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + self.dice_size // 2), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + self.dice_size // 2), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + 2 * self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + self.dice_size // 3), 10)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.dice_pos[0] + self.dice_size // 3, self.dice_pos[1] + 2 * self.dice_size // 3), 10)

    def lancer_de(self):
        self.rolling = True
        start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start_time < self.roll_duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((255, 255, 255))
            random_face = random.randint(1, self.num_faces)
            self.draw_dice(random_face)

            pygame.display.flip()

        self.rolling = False

        # Affiche la face finale après l'arrêt du dé
        self.screen.fill((255, 255, 255))
        final_face = random.randint(1, self.num_faces)
        self.draw_dice(final_face)

        pygame.display.flip()
        pygame.time.wait(1000)

if __name__ == "__main__":
    simulator = DiceSimulator(6)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not simulator.rolling:
            simulator.lancer_de()

        pygame.display.flip()
