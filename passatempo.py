import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
SPEED = 5
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ACORDA PEDRINHOOOO")

# Fonte para as mensagens
font = pygame.font.Font(None, 36)

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 30)
        self.speed = SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - 40)
        self.rect.y = random.randrange(100, HEIGHT - 30)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = random.randrange(-30, -10)
            self.rect.x = random.randrange(0, WIDTH - 40)

all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()

frog = Frog()
all_sprites.add(frog)

for _ in range(10):
    car = Car()
    all_sprites.add(car)
    cars.add(car)

# Inicialize as variáveis de controle de estado
game_over = False
victory = False

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        hits = pygame.sprite.spritecollide(frog, cars, False)
        if hits:
            game_over = True  # O jogador perdeu

        # Verifique se o jogador chegou ao topo da tela (vitória)
        if frog.rect.y <= 0:
            victory = True

    screen.fill(WHITE)
    all_sprites.draw(screen)

    if game_over:
        text = font.render("Você perdeu! Pressione R para reiniciar", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        # Verifique se o jogador pressionou "R" para reiniciar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            victory = False
            frog.rect.center = (WIDTH // 2, HEIGHT - 30)

            # Reposicione os carros
            for car in cars:
                car.rect.x = random.randrange(0, WIDTH - 40)
                car.rect.y = random.randrange(100, HEIGHT - 30)

    if victory:
        text = font.render("Você venceu! Pressione R para jogar novamente", True, GREEN)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        # Verifique se o jogador pressionou "R" para reiniciar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            victory = False
            frog.rect.center = (WIDTH // 2, HEIGHT - 30)

            # Reposicione os carros
            for car in cars:
                car.rect.x = random.randrange(0, WIDTH - 40)
                car.rect.y = random.randrange(100, HEIGHT - 30)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
