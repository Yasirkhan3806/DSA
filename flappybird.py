import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
GAP = 150
GROUND_HEIGHT = 50
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image or you can draw a rectangle
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill(YELLOW)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.vel = 0

    def draw(self, screen):
        screen.blit(bird_image, (self.x, self.y))

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

        if self.y + BIRD_HEIGHT >= SCREEN_HEIGHT - GROUND_HEIGHT:
            self.y = SCREEN_HEIGHT - GROUND_HEIGHT - BIRD_HEIGHT
            self.vel = 0

    def jump(self):
        self.vel = -JUMP_STRENGTH

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.top_pipe = pygame.Surface((PIPE_WIDTH, self.height))
        self.top_pipe.fill(GREEN)
        self.bottom_pipe = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_pipe.fill(GREEN)

    def draw(self, screen):
        # Draw top pipe
        screen.blit(self.top_pipe, (self.x, 0))
        # Draw bottom pipe
        screen.blit(self.bottom_pipe, (self.x, self.height + GAP))

    def update(self):
        self.x -= 5

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
        top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        bottom_rect = pygame.Rect(self.x, self.height + GAP, PIPE_WIDTH, PIPE_HEIGHT)

        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

# Main game function
def game():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Update bird
        bird.update()
        bird.draw(screen)

        # Update pipes
        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)

            if pipe.collide(bird):
                running = False

            if pipe.x + PIPE_WIDTH < bird.x and not hasattr(pipe, 'scored'):
                score += 1
                pipe.scored = True

        # Remove pipes that are off the screen
        pipes = [pipe for pipe in pipes if not pipe.off_screen()]

        # Add new pipes
        if len(pipes) == 0 or pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())

        # Draw ground
        pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

        # Display score
        font = pygame.font.SysFont(None, 50)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

# Run the game
if __name__ == '__main__':
    game()
 