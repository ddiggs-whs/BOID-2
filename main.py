import pygame
import random
import math
pygame.init()

window_width = 400
window_height = 300

DISPLAY = pygame.display.set_mode((window_width, window_height))
FPSCLOCK = pygame.time.Clock()
FPS = 30

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



class Boid(pygame.sprite.Sprite):
  def __init__(self, color, size):
    super().__init__()
    self.image = pygame.Surface([size, size])
    self.image.set_colorkey((0,0,0))
    self.rect = self.image.get_rect()
    self.size = size
    pygame.draw.polygon(self.image, color, [(self.size, self.size//2), (0, self.size), (0, 0)])

    self.velocity = [10, 0]
  
  def update(self, objects):
    self.rect.x += self.velocity[0] * math.cos(self.velocity[1]*math.pi/180)
    self.rect.y += self.velocity[0] * math.sin(self.velocity[1]*math.pi/180)


    if self.rect.x >= window_width:
      self.rect.x -= window_width
    elif self.rect.x <= 0:
      self.rect.x += window_width
    
    if self.rect.y >= window_height:
      self.rect.y -= window_height
    elif self.rect.y <= 0:
      self.rect.y += window_height
    
    #pygame.draw.line(DISPLAY, blue, self.rect.center, (self.rect.centerx + self.velocity[0] * math.cos(self.velocity[1]*math.pi/180),self.rect.centery + self.velocity[0] * math.sin(self.velocity[1]*math.pi/180) ), 5)


my_objects = pygame.sprite.Group()
for i in range(10):
  new_boid = Boid(red, 10)
  new_boid.rect.center = [random.randint(0, window_width), random.randint(0, window_height)]
  new_boid.velocity[0] = 5
  new_boid.velocity[1] = random.randint(0,360)
  my_objects.add(new_boid)

new_boid = Boid(blue, 10)
new_boid.rect.center = [random.randint(0, window_width), random.randint(0, window_height)]
new_boid.velocity[0] = 5
new_boid.velocity[1] = random.randint(0,360)
my_objects.add(new_boid)







while True:

  for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
      mos_pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      quit()
  
  DISPLAY.fill(white)

  pygame.draw.circle(DISPLAY, green, new_boid.rect.center, 60)
  pygame.draw.circle(DISPLAY, red, new_boid.rect.center, 15)
  my_objects.draw(DISPLAY)
  my_objects.update(my_objects)

  
  FPSCLOCK.tick(FPS)
  pygame.display.update()
        