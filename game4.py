"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py

Explanation video: http://youtu.be/5-SbFanyUkQ

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
 """
import pygame
import random
import numpy as np
import matplotlib.pyplot as plt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Fire(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
    fire_list = None
    room_right = None
    room_left = None
    room_up = None
    room_down = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.fire_list = pygame.sprite.Group()
        self.fire_area = np.zeros((800,800))
        '''
        self.room_down = None
        self.room_up = None
        self.room_left = None
        self.room_right = None
        '''


class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]

        fire = [[100,100,50,50, YELLOW]]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in fire:
            fire = Fire(item[0], item[1], item[2], item[3], item[4])
            self.fire_list.add(fire)

        self.room_right = 2
        self.room_left = 5#4



class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        self.room_right = 3
        self.room_left = 1


class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)

        self.room_right = 4
        self.room_left = 2

class Room4(Room):
    """This creates all the walls in room 4"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE],
                 [200, 50, 20, 500, BLUE],
                 [500, 100, 20, 500, BLUE]
                ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        self.room_right = 5#1
        self.room_left = 3

class customRoom(Room):
    "Creates a custom room"
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE],
                 [200, 50, 20, 500, BLUE],
                 [500, 100, 20, 500, BLUE]
                ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        self.room_right = 4#1
        self.room_left = 3


def fire_spread(rooms):
    size_fire = 10

    for room_ind in range(0,len(rooms)):

        fire_room = rooms[room_ind]

        rect_xs = [i.rect.x for i in fire_room.fire_list]
        rect_ys = [i.rect.y for i in fire_room.fire_list]

        if len(rect_xs) > 0:

            rects = [(rect_xs[i],rect_ys[i]) for i in range(0,len(rect_xs))]

            while(1):
                rand_ind = random.randrange(0, len(rect_xs))
                fire_y = rect_ys[rand_ind]
                fire_x = rect_xs[rand_ind]
                if(fire_x + size_fire, fire_y  + size_fire) not in rects:
                    break
                if(fire_x + size_fire, fire_y  - size_fire) not in rects:
                    break
                if(fire_x - size_fire, fire_y  + size_fire) not in rects:
                    break
                if(fire_x - size_fire, fire_y  - size_fire) not in rects:
                    break
                if(fire_x, fire_y  + size_fire) not in rects:
                    break
                if(fire_x, fire_y  - size_fire) not in rects:
                    break
                if(fire_x + size_fire, fire_y) not in rects:
                    break
                if(fire_x - size_fire, fire_y) not in rects:
                    break

            if fire_x + size_fire < 800 and fire_x > 0 and fire_y + size_fire < 800 and fire_y - size_fire > 0:
                fire_room.fire_list.add(Fire(fire_x + size_fire , fire_y  + size_fire, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x + size_fire , fire_y  - size_fire, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x - size_fire , fire_y  + size_fire, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x - size_fire , fire_y  - size_fire, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x + 0 , fire_y  + size_fire, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x + 0 , fire_y  - size_fire, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x + size_fire, fire_y  + 0, size_fire, size_fire, YELLOW))
                fire_room.fire_list.add(Fire(fire_x- size_fire , fire_y  + 0, size_fire, size_fire, YELLOW))
                fire_room.fire_area[(fire_y  - size_fire):(fire_y  + size_fire),(fire_x - size_fire):(fire_x + size_fire)] = 1

            if fire_x - size_fire <= 0 and fire_y + size_fire < 800 and fire_y - size_fire > 0:
                rooms[fire_room.room_left-1].fire_list.add(Fire(774 , fire_y, size_fire, size_fire, YELLOW))

            if fire_x - size_fire >= 780 and fire_y + size_fire < 800 and fire_y - size_fire > 0:
                rooms[fire_room.room_right-1].fire_list.add(Fire(0 , fire_y, size_fire, size_fire, YELLOW))


def main():

    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object

    health = 100
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    room = customRoom()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    myfont = pygame.font.SysFont("monospace",16)

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)

        if player.rect.x < -15:

            current_room_no = current_room.room_left -1
            current_room = rooms[current_room_no]
            player.rect.x = 790
            '''
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
            '''

        if player.rect.x > 801:

            current_room_no = current_room.room_right-1
            current_room = rooms[current_room_no]
            player.rect.x = 0
            '''
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
            '''

        # --- Drawing ---
        screen.fill(BLACK)



        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        current_room.fire_list.draw(screen)

        print(np.sum(current_room.fire_area[player.rect.y:player.rect.y+15,player.rect.x:player.rect.x+15]) )
        #plt.imshow(current_room.fire_area)
        #plt.show()
        if np.sum(current_room.fire_area[player.rect.y:player.rect.y+15,player.rect.x:player.rect.x+15]) > 0:
            health = health - 1
        print(health)


        '''
        fire_x = random.randrange(0, 800)
        fire_y = random.randrange(0, 800)
        fire = Fire(fire_x , fire_y , 25, 25, YELLOW)
        current_room.fire_list.add(fire)
        '''
        fire_spread(rooms)

        scoretext = myfont.render("Health = " + str(health), 2, (255,0,0))
        screen.blit(scoretext, (5,10))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
