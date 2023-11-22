import os
import sys
import random
import collections
import pygame as pg

try:
    import Queue as queue
except ImportError:
    import queue


CAPTION = "Змейка"
SCREEN_SIZE = (544, 544)
PLAY_RECT = pg.Rect(16, 16, 512, 512)
CELL = pg.Rect(0, 0, 16, 16)
BOARD_SIZE = (PLAY_RECT.w//CELL.w, PLAY_RECT.h//CELL.h)
GROWTH_PER_APPLE = 3


COLORS = {"background" : (30, 40, 50), "walls" : pg.Color("blue"),
          "snake" : pg.Color("limegreen"), "head" : pg.Color("darkgreen"),
          "apple" : pg.Color("tomato")}

DIRECT_DICT = {"left" : (-1, 0), "right" : ( 1, 0),
               "up" : ( 0,-1), "down" : ( 0, 1)}

OPPOSITES = {"left" : "right", "right" : "left",
             "up" : "down", "down" : "up"}

KEY_MAPPING = {(pg.K_LEFT, pg.K_a) : "left", (pg.K_RIGHT, pg.K_d) : "right",
               (pg.K_UP, pg.K_w) : "up", (pg.K_DOWN, pg.K_s) : "down"}


class Apple(object):
    """Яблоко длинна+1."""
    def __init__(self, walls, snake):
        self.position = self.respawn(snake.body_set | walls)
        self.walls = walls
        self.color = COLORS["apple"]

    def collide_with(self, snake):
        """Респавн яблока на карте ."""
        self.position = self.respawn(snake.body_set | self.walls)

    def respawn(self, obstacles):
        """Рандом спавн не в snake и не в walls."""
        position = tuple(random.randrange(BOARD_SIZE[i]) for i in (0,1))
        while position in obstacles:
            position = tuple(random.randrange(BOARD_SIZE[i]) for i in (0,1))
        return position


class Snake(object):

    def __init__(self):
        self.color = COLORS["snake"]
        self.speed = 8 # Cells per second
        self.direction = "up"
        self.vector = DIRECT_DICT[self.direction]
        self.body = [(10, 25), (10, 24)]
        self.body_set = set(self.body)
        self.growing = False
        self.grow_number = 0
        self.timer = 0
        self.dead = False
        self.direction_queue = queue.Queue(5)

    def update(self, now):
        """+1 в head змеи."""
        if not self.dead and now-self.timer >= 1000.0/self.speed:
            self.timer = now
            self.change_direction()
            next_cell = [self.body[-1][i]+self.vector[i] for i in (0,1)]
            self.body.append(tuple(next_cell))
            if not self.growing:
                del self.body[0]
            else:
                self.grow()
            self.body_set = set(self.body)

    def change_direction(self):
        """
        Проверить очередь на наличие нового направления
        """
        try:
            new = self.direction_queue.get(block=False)
        except queue.Empty:
            new = self.direction
        if new not in (self.direction, OPPOSITES[self.direction]):
            self.vector = DIRECT_DICT[new]
            self.direction = new

    def grow(self):
        """Увеличть grow_number и сбросить по готовке."""
        self.grow_number += 1
        if self.grow_number == GROWTH_PER_APPLE:
            self.grow_number = 0
            self.growing = False

    def check_collisions(self, apple, walls):
        """логика вхождения в wall,apple,в себя."""
        if self.body[-1] == apple.position:
            apple.collide_with(self)
            self.growing = True
        elif self.body[-1] in walls:
            self.dead = True
        elif any(val > 1 for val in collections.Counter(self.body).values()):
            self.dead = True

    def get_key_press(self, key):
        """
        Добавить направления в очередь направлений, если нажата клавиша  KEY_MAPPING.
        """
        for keys in KEY_MAPPING:
            if key in keys:
                try:
                    self.direction_queue.put(KEY_MAPPING[keys], block=False)
                    break
                except queue.Full:
                    pass

    def draw(self, surface, offset=(0,0)):
        """Рисовка туловища, затем головы."""
        for cell in self.body:
            Makedraw.draw_cell(surface, cell, self.color, offset)
        Makedraw.draw_cell(surface, self.body[-1], COLORS["head"], offset)



class _Scene(object):
    """Сцена."""
    def __init__(self, next_state=None):
        self.next = next_state
        self.done = False
        self.start_time = None
        self.screen_copy = None

    def startup(self, now):
        """старт."""
        self.start_time = now
        self.screen_copy = pg.display.get_surface().copy()

    def reset(self):
        """Рестарт игры."""
        self.done = False
        self.start_time = None
        self.screen_copy = None

    def get_event(self, event):
        """перегруз."""
        pass

    def update(self, now):
        """запуск."""
        if not self.start_time:
            self.startup(now)

c
class AnyKey(_Scene):
    """Сцены: старт,смерть."""
    def __init__(self, title):
        _Scene.__init__(self, "GAME")
        self.blink_timer = 0.0
        self.blink = False
        self.make_text(title)
        self.reset()

    def make_text(self, title):
        """Текст."""
        self.main = FONTS["BIG"].render(title, True, pg.Color("white"))
        self.main_rect = self.main.get_rect(centerx=PLAY_RECT.centerx,
                                            centery=PLAY_RECT.centery-150)
        text = "Нажмите любую кнопку"
        self.ne_key = FONTS["SMALL"].render(text, True, pg.Color("white"))
        self.ne_key_rect = self.ne_key.get_rect(centerx=PLAY_RECT.centerx,
                                                centery=PLAY_RECT.centery+150)

    def draw(self, surface):
        """мигание."""
        surface.blit(self.screen_copy, (0,0))
        surface.blit(self.main, self.main_rect)
        if self.blink:
            surface.blit(self.ne_key, self.ne_key_rect)

    def update(self, now):
        """обновить мигалку."""
        _Scene.update(self, now)
        if now-self.blink_timer > 1000.0/5:
            self.blink = not self.blink
            self.blink_timer = now

    def get_event(self, event):
        """старт после нажатия кнопки."""
        if event.type == pg.KEYDOWN:
            self.done = True


class Game(_Scene):
    """сцена игры."""
    def __init__(self):
        _Scene.__init__(self, "DEAD")
        self.reset()

    def reset(self):
        """Подготовка к следующей попытке."""
        _Scene.reset(self)
        self.snake = Snake()
        self.walls = self.make_walls()
        self.apple = Apple(self.walls, self.snake)

    def make_walls(self):
        """Сделать границы и загрузить случайный уровень."""
        walls = set()
        for i in range(-1, BOARD_SIZE[0]+1):
            walls.add((i, -1))
            walls.add((i, BOARD_SIZE[1]))
        for j in range(-1, BOARD_SIZE[1]+1):
            walls.add((-1, j))
            walls.add((BOARD_SIZE[0], j))
        walls |= random.choice(LEVELS)
        return walls

    def get_event(self, event):
        """Нажать любую клавишу."""
        if event.type == pg.KEYDOWN:
            self.snake.get_key_press(event.key)

    def update(self, now):
        """Смерть."""
        _Scene.update(self, now)
        self.snake.update(now)
        self.snake.check_collisions(self.apple, self.walls)
        if self.snake.dead:
            self.done = True

    def draw(self, surface):
        """Прорисовка элементов."""
        surface.fill(COLORS["background"])
        Makedraw.draw_cell(surface, self.apple.position,
                  self.apple.color, PLAY_RECT.topleft)
        for wall in self.walls:
            Makedraw.draw_cell(surface, wall, COLORS["walls"], PLAY_RECT.topleft)
        self.snake.draw(surface, offset=PLAY_RECT.topleft)


class Control(object):
    """Содержит основной цикл, цикл событий и логику переключения сцен."""
    def __init__(self):
        """Стандартная настройка и создание начальной сцены."""
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.state_dict = {"START" : AnyKey("Начать"),
                           "GAME" : Game(),
                           "DEAD" : AnyKey("Конец")}
        self.state = self.state_dict["START"]

    def event_loop(self):
        """Обработка выхода."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def update(self):
        """Обновить текущую сцену и переключиться при необходимости."""
        now = pg.time.get_ticks()
        self.state.update(now)
        if self.state.done:
            self.state.reset()
            self.state = self.state_dict[self.state.next]

    def draw(self):
        """Нарисуйте текущую сцену, если она готова."""
        if self.state.start_time:
            self.state.draw(self.screen)

    def display_fps(self):
        """Показать fps, для проверки."""
        caption = "{} - FPS: {:.2f}".format(CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)

    def main_loop(self):
        """Run-a-round."""
        self.screen.fill(COLORS["background"])
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)
            self.display_fps()

class Makedraw():
    def draw_cell(surface, cell, color, offset=(0,0)):
        """surface."""
        pos = [cell[i]*CELL.size[i] for i in (0,1)]
        rect = pg.Rect(pos, CELL.size)
        rect.move_ip(*offset)
        surface.fill(color, rect)


    def make_levels():

        w, h = BOARD_SIZE
        r = range
        levels = [
            ({(w//2,i) for i in r(h//2-3)}|{(w//2,i) for i in r(h//2+3,h)}),
            ({(w//4,i) for i in r(3*h//5)}|{(3*w//4,i) for i in r(2*h//5,h)}),
            ({(w//2,i) for i in r(5,h-5)}|{(i,h//2) for i in r(3,w//2-3)}|
                {(i+w//2+3, h//2) for i in r(3,w//2-3)})]
        return levels

class Start():
    def main(self):
        """
        Подготовка pygame на экран.
        """
        global FONTS,LEVELS
        os.environ["SDL_VIDEO_CENTERED"] = "True"
        pg.init()
        pg.display.set_caption(CAPTION)
        pg.display.set_mode(SCREEN_SIZE)
        FONTS = {"BIG" : pg.font.SysFont("helvetica", 100, True),
                 "SMALL" : pg.font.SysFont("helvetica", 50, True)}
        LEVELS = Makedraw.make_levels()
        Control().main_loop()
        pg.quit()
        sys.exit()





abc=Start()
abc.main()
