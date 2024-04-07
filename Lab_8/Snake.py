import pygame
from random import randint

pygame.init()

WIDTH = 720
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorWHITE = (255, 255, 255)
colorGRAY = (70, 70, 70)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

FPS = 5

clock = pygame.time.Clock()

CELL = 60

score = 0  

# Score text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

text_font = pygame.font.SysFont(None, 30)

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def generate():
        return Point(randint(0, WIDTH // CELL - 1) * CELL, randint(0, HEIGHT // CELL - 1) * CELL)

class Snake:
    def __init__(self):
        self.body = [Point.generate()]
        self.dx = 0
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx * CELL
        head.y += self.dy * CELL
        if head.x == WIDTH:
            head.x = 0
        if head.x < 0:
            head.x = (WIDTH // CELL - 1) * CELL
        if head.y == HEIGHT:
            head.y = 0
        if head.y < 0:
            head.y = (HEIGHT // CELL - 1) * CELL

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x, head.y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x, segment.y, CELL, CELL))

class Food:
    def __init__(self):
        self.pos = Point.generate()

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x, self.pos.y, CELL, CELL))

    def regenerate(self):
        self.pos = Point.generate()

def draw_grid():
    for i in range(0, HEIGHT, CELL):
        for j in range(0, WIDTH, CELL):
            pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)

snake = Snake()
food = Food()

done = False

while not done:
    print(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0

    screen.fill(colorBLACK)
    snake.move()
    draw_text('Score:', text_font, (255, 255, 255), WIDTH - 100, 10)
    draw_text(f'{score}', text_font, (255, 255, 255), WIDTH - 35, 10)

    if snake.check_collision(food):
        food.regenerate()
        score += 1  # Increase score by 1

    # Change FPS after reaching a score of 10 or 20
    
    for j in range(10, 100, 10):
        if j == score:
            FPS = 6
        

    snake.draw()
    food.draw()
    draw_grid()

    pygame.display.flip()
    clock.tick(FPS)