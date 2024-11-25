from operator import add, sub
from pyimager import *
import time

highscores_path = "/".join(__file__.split("/")[:-1:])+"/highscores.txt"

class config:
    n = 2
    t_x, t_y = 192*n, 108*n

def sumL(l1, l2): return tuple(map(add, l1, l2))
def subL(l1, l2): return tuple(map(sub, l1, l2))

class game:
    with open(highscores_path, "r", encoding="utf8") as file:
        highscores = eval(file.read())
    def new_highscore(self):
        with open(highscores_path, "w", encoding="utf8") as file:
            file.write(self.highscores)
    def tile_(self, x, y): return [[RES.resolution[i]/[config.t_x, config.t_y][i]*([x, y][i]+[0, 1][j]) for i in [0, 1]] for j in [0, 1]]
    def get_tile(self, x, y): return [round(v) for v in [[x, y][i]/RES.resolution[i]*[config.t_x, config.t_y][i] for i in [0, 1]]]
    def tile(self, x, y): return self.tile_(*self.get_tile(x, y))
    laser_speed = 10
    bomb_speed = 8
    cooldown = 0.5
    bg_color = COL.black
    max_n_l = 1
    ground = [(0, RES.resolution[1]*0.92), (RES.resolution[0], RES.resolution[1]*0.925)]
    class bunker: ... ## TODO Build the bunkers
    class explosion:
        def __init__(self, pos, size) -> None: ... ## TODO Make explosion when bombs hit anything
    class bomb:
        score = 1
        carres = [[0, y] for y in range(-1, 3)]+[[1,2],[-1,2]]
        def __init__(self, pos, vel): self.pos, self.vel = pos, vel
        def get_tiles(self, jeu): return [[jeu.get_tile(*self.pos)[i]-c[i]for i in[0,1]] for c in self.carres]
        def update(self, gam):
            self.pos = coosCircle(self.pos, self.vel, 90)
            if not clicked_in(self.pos, [[0, 0], RES.resolution]): gam.bombs.pop(gam.bombs.index(self))
            if dist(gam.player.pos, self.pos)>30:
                if any(i in gam.player.get_tiles(gam) for i in self.get_tiles(gam)):
                    gam.player.pos[0] = RES.resolution[0]/2
                    gam.bombs.pop(gam.bombs.index(self))
                    gam.lives -= 1
        def tile(self, which, jeu): return jeu.tile_(*subL(jeu.get_tile(*self.pos), which))
        def draw(self, img:image, jeu) -> None:
            for c in [(self.tile(self.carres[0], jeu)[1], self.tile(self.carres[2], jeu)[0]), (self.tile(self.carres[-2],jeu)[0], self.tile(self.carres[-1],jeu)[1])]:
                img.rectangle(*c, COL.blue, 0)
    class Invader:
        last_shoot_t = time.time()
        def __init__(self, pos): self.pos = pos
        def update(self, vel, ang): self.pos = coosCircle(self.pos, vel, ang)
        def bomb(self, jeu) -> None:
            if diff(jeu.last_bomb_t, time.time()) > jeu.cooldown*2:
                jeu.bombs.append(game.bomb(self.pos, game.bomb_speed))
                jeu.last_bomb_t = time.time()
        def draw(self, img:image, jeu):
            ## TODO Optimize it
            ## TRY something
            for c in self.carres1 if int(jeu.frame)%2==0 else self.carres2:
                img.rectangle(*jeu.tile_(*[jeu.get_tile(*self.pos)[i]-c[i]for i in[0,1]]), self.color, 0)
        def get_tiles(self, jeu): return [[jeu.get_tile(*self.pos)[i]-c[i]for i in[0,1]] for c in self.carres]
    class squid(Invader):
        score, color, carres = 30, COL.lime, [[x, y] for i, y in enumerate(range(0, 3)[::-1]) for x in range(0-i, i+2)]+[[x, y] for x in range(-3, 5) for y in [-1, -2] if y!=-1 or x not in [-1, 2]]
        carres1, carres2 = [[x, y+2] for x, y in carres + [[-1, -3], [2, -3]]+[[x, -4] for x in range(-2, 4) if not x in [-1, 2]]+[[x, -5] for x in [-3, -1, 2, 4]]], [[x, y+2] for x, y in carres + [[x, -3] for x in range(-2, 4) if not x in [-1, 2]]+[[-3, -4],[4, -4]]+[[-2, -5], [3, -5]]]
    class crab(Invader):
        score, color, carres = 20, COL.cyan, [[-3,4],[3,4],[-2,3],[2,3]]+[[x,2]for x in range(-4,5)]+[[x,1]for x in range(-5,6)if not x in[-2,2]]+[[x,0]for x in range(-6,7)]+[[x,-1]for x in range(-4,5)]
        carres1, carres2 = carres + [[-6,-1],[6,-1],[-6,-2],[6,-2],[-4,-2],[4,-2]]+[[x,-3]for x in range(-3,4)if x!=0], carres + [[[-6,6][i],y]for y in[3,2,1]for i in[0,1]]+[[[-3,-4][i],y]for i,y in enumerate([-2,-3])]+[[[3,4][i],y]for i,y in enumerate([-2,-3])]
    class octopus(Invader):
        score, color, carres = 10, COL.yellow, [[x,4]for x in range(-1,3)]+[[x,3]for x in range(-4,6)]+[[x,y]for x in range(-5,7)for y in [2,1,0]if not(y==1 and x in[-2,-1,2,3])]+[[x,-1]for x in[-2,-1,2,3]]+[[0,-2],[1,-2],[-3,-2],[4,-2]]
        carres1, carres2 = carres + [[-3,-1],[4,-1],[-4,-2],[5,-2],[-3,-3],[-2,-3],[4,-3],[3,-3]], carres + [[-5,-3],[-4,-3],[6,-3],[5,-3],[-2,-2],[3,-2]]
    class UFO(Invader): ## TODO appear sometimes randomly
        carres = [[x, 6] for x in range(-2, 4)]+[[x, 5] for x in range(-4, 6)]+[[x, 4] for x in range(-5, 7)]+[[x, 3] for x in range(-6, 8) if not x in (-4, -1, 2, 5)]+[[x, 2] for x in range(-7, 9)]+[[x, 1] for x in range(-5, 7) if not x in (-2, -1, 2, 3)]+[[-4, 0], [5, 0]]
        def __init__(self, *args, **kwargs) -> None:
            self.score = rd.choice((50, 100, 150, 200, 300))
            game.Invader.__init__(self, *args, **kwargs)
        def draw(self, img:image, jeu): ## TODO Optimize it
            for c in self.carres: img.rectangle(*jeu.tile_(*[jeu.get_tile(*self.pos)[i]-c[i]for i in[0,1]]), COL.purple, 0)
    class laser:
        carres = [[0, y] for y in range(-3, 2)]
        def __init__(self, pos, vel): self.pos, self.vel = pos, vel
        def get_tiles(self, jeu): return [[jeu.get_tile(*self.pos)[i]-c[i]for i in[0,1]] for c in self.carres]
        def update(self, gam) -> None:
            self.pos = coosCircle(self.pos, self.vel, 270)
            if not clicked_in(self.pos, [[0, 0], RES.resolution]): gam.lasers.pop(gam.lasers.index(self))
            for inv in [inv for inv in gam.invaders if dist(inv.pos, self.pos)<50]:
                if any(i in inv.get_tiles(gam) for i in self.get_tiles(gam)):
                    gam.score += gam.invaders.pop(gam.invaders.index(inv)).score
                    gam.lasers.pop(gam.lasers.index(self))
            for bomb in [b for b in gam.bombs if dist(b.pos, self.pos)<30]:
                if any(i in bomb.get_tiles(gam) for i in self.get_tiles(gam)):
                    gam.score += gam.bombs.pop(gam.bombs.index(bomb)).score
                    gam.lasers.pop(gam.lasers.index(self))
        def draw(self, img:image, jeu) -> None:
            img.rectangle(*[jeu.tile_(*self.get_tiles(jeu)[i])[j] for i, j in [(0, -1), (-1, 0)]], COL.white, 0)
    class canon:
        carres = [[x, y] for x in range(-6, 7) for y in range(-3, 1)]+[[x, 1] for x in range(-5, 6)]+[[x, y] for x in [-1, 0, 1] for y in [2, 3]]+[[0, 4]]
        def get_tiles(self, jeu): return [[jeu.get_tile(*self.pos)[i]-c[i]for i in[0,1]] for c in self.carres]
        def __init__(self, vel, pos=[RES.resolution[0]/2, RES.resolution[1]*0.9], hitbox=[20, 20]):
            self.pos, self.hitbox, self.vel, self.last_shoot_t = pos, hitbox, vel, time.time()
        def move_(self, ang): self.pos = coosCircle(self.pos, self.vel, ang)
        def move(self, ang):
            self.move_(ang)
            if not clicked_in(self.pos, [[0, 0], RES.resolution]):
                self.pos = [min(self.pos[i], RES.resolution[i]) for i in [0, 1]]
                self.pos = [max(self.pos[i], 0) for i in [0, 1]]
        def tile(self, which, jeu): return jeu.tile_(*subL(jeu.get_tile(*self.pos), which))
        def draw(self, img:image, jeu) -> None:
            for a, b in ((0, 51), (52, 62), (63, -2), (-1, -1)):
                img.rectangle(self.tile(self.carres[a], jeu)[-1], self.tile(self.carres[b], jeu)[0], COL.lime, 0)
        def shoot(self, jeu) -> None:
            if diff(self.last_shoot_t, time.time()) > game.cooldown and len(jeu.lasers)<jeu.max_n_l:
                self.last_shoot_t = time.time()
                jeu.lasers.append(game.laser(self.pos, game.laser_speed))
    def new_wave(self) -> None:
        esp = 150/config.n
        offsetx, offsety = 100, 100
        squids = [self.squid([offsetx+esp*x, offsety]) for x in range(11)]
        crabs = [self.crab([offsetx+esp*x, offsety+esp+y]) for x in range(11) for y in [0, esp]]
        octopuses = [self.octopus([offsetx+esp*x, offsety+3*esp+y]) for x in range(11) for y in [0, esp]]
        self.invaders = squids+crabs+octopuses
    def __init__(self):
        self.player, self.score, self.frame, self.bombs, self.lasers, self.lives = self.canon(vel=dist(self.tile_(0, 0)[0], self.tile_(1, 0)[0])), 0, 0, [], [], 3
        self.invaders = []
        self.last_bomb_t = time.time()
    def update(self):
        self.frame += 1/5
        for i in self.bombs+self.lasers: i.update(self)
        if int(self.frame)%5==0:
            try:
                inv = rd.choice(self.invaders)
                if type(inv) != game.UFO: inv.bomb(self)
            except: ...
        if len(self.invaders)==0: self.new_wave()
    def image(self) -> image:
        img = new_img(background=self.bg_color)
        img.rectangle(*(self.tile(*self.ground[i])[i] for i in [0, -1]), COL.darkGreen, 0)
        for i in self.bombs+self.lasers: i.draw(img, self)
        for INV in self.invaders: INV.draw(img, self)
        self.player.draw(img, self)
        img.write(f"{self.score:0>6}", [10, 30], COL.white, 2, 2, FONT_HERSHEY_PLAIN)
        img.write(f"{self.lives}", [10, RES.resolution[1]-30], COL.white, 2, 2, FONT_HERSHEY_PLAIN)
        return img
    def reset(self):
        self.__init__()
    def play(self, img):
        tick, last_tick = 1/30, time.time()
        while img.is_opened() and self.lives>0:
            wk = img.show(built_in_functs=False)
            match wk:
                case 27: img.close()
                case 8: img.fullscreen = not img.fullscreen
                case 65363: self.player.move(0) ## Right arrow
                case 65361: self.player.move(180) ## Left arrow
                case 32: self.player.shoot(self) ## Space bar
                case 65470: cv2.moveWindow(img.name, 0, 0) #f1
                case 65471: cv2.moveWindow(img.name, 1920, 0) #f2
            if diff(time.time(), last_tick) > tick:
                self.update()
                last_tick = time.time()
            img.img = self.image().img
    def titlescreen(self, img) -> None: ...
    def save_highscore(self) -> None: ...

def main():
    jeu = game()
    img = new_img(name="Space Invaders").build()
    while img.is_opened():
        jeu.titlescreen(img)
        jeu.play(img)
        jeu.reset()
        jeu.save_highscore()

if __name__ == "__main__":
    main()