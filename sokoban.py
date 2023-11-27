from Outils.cvt2 import *
from touches_sokoban import keys_j1
import keyboard as kb
class invalidLevel(Exception):
    def __init__(self) -> None:
        super().__init__('Le niveau est invalide')
class tableau:
    champs_infos = ['Nom du niveau', 'Niveau par', 'Date de création']
    def __init__(self, level=0, ly=layout()) -> None:
        self.infos = {}
        level_names = os.listdir('./Sokoban_levels')
        if level > 0 and level < len(level_names):
            nom = level_names[level]
            with open(f'./Sokoban_levels/{nom}', 'r', encoding='utf8') as file:
                lev = file.read()
        else:
            nom = level_names[level]
            with open(f'./Sokoban_levels/{nom}', 'r', encoding='utf8') as file:
                lev = file.read()
        format = nom[len(nom)-nom[::-1].index('.')::]
        print(f'Format "{format}"')
        if format == 'xsb':
            lev=lev.replace('-', '_')
            lev=lev.replace('@', 's')
            lev=lev.replace('+', 'S')
            lev=lev.replace('$', 'k')
            lev=lev.replace('*', 'K')
            lev=lev.replace('#', 'X')
            lev=lev.replace('.', '+')
            self.infos = nom[::-1].split('.',1)[1][::-1]
        if format == 'txt':
            lev2 = '';i=0
            for l in lev.splitlines():
                if l.count('#')==0:
                    lev2+=l+'\n'
                else:
                    self.infos[tableau.champs_infos[i]] = l.replace('#','')
                    i += 1
            lev = lev2
        r_l = [[c for c in l] for l in lev.split('\n')]
        lns = [len(l) for l in r_l]
        for ind in range(len(lns)):
            for _ in range(diff(lns[ind], max(lns))):
                r_l[ind].append(' ')
        self.level = np.array(r_l)
        self.pos = self.get_skbn_pos()
        nb = [0,0]
        for c in str(self):
            if c in 'SK+': nb[0] += 1
            if c in  'Kk': nb[1] += 1
        if nb[0] != nb[1]:
            print(lev)
            raise invalidLevel()
        self.size = [len(self.level[0]), len(self.level)]
        print(self.level, self.size)
        x, y = [[1920, 1080][n]//self.size[n] for n in (0,1)]
        self.s = s = min(x, y)
        lignes = []
        colonnes = []
        for x in range(0,1920,s)[0:self.size[0]:]: colonnes.append(x)
        for y in range(0,1080,s)[0:self.size[1]:]: lignes.append(y)
        cases = []
        for y, l in enumerate(lignes):
            cases.append([])
            for c in colonnes:
                cases[y].append([c,l])
        self.cases = np.array(cases)
        self.moves = 0
        self.pushes = 0
    def replaces(self, s='') -> str:
        s=s.replace(' ', '  ')
        s=s.replace('_', '  ')
        s=s.replace('X', '██')
        s=s.replace('s', '--')
        s=s.replace('S', '==')
        s=s.replace('k', '[]')
        s=s.replace('K', '##')
        s=s.replace('+', '<>')
        return s
    def __str__(self) -> str:
        s = ""
        for l in self.level:
            s += ''.join(i for i in l) + "\n"
        return s[:len(s)-1:]
    def imprimme(self) -> None:
        print(self.replaces(self.__str__()))
    def get_skbn_pos(self) -> list:
        for y in range(len(self.level)):
                for x in range(len(self.level[y])):
                    if self.level[y,x].lower() == 's':
                        return [x, y]
    def move(self, v=[0,0]) -> None:
        if abs(sum(v)) != 1 : return
        else:
            pos = self.pos
            a = [pos[i]+v[i] for i in [0,1]]
            if self.level[a[1], a[0]] in '+_ ':
                self.level[a[1], a[0]] = 's' if self.level[a[1], a[0]] != '+' else 'S'
                self.level[pos[1], pos[0]] = '+' if self.level[pos[1], pos[0]].isupper() else '_'
                self.pos = a
                self.moves += 1
            elif self.level[a[1], a[0]].lower() == 'k':
                if self.level[a[1]+v[1], a[0]+v[0]].lower() in '+_ ':
                    self.level[a[1]+v[1], a[0]+v[0]] = 'k' if self.level[a[1]+v[1], a[0]+v[0]] != '+' else 'K'
                    self.level[a[1], a[0]] = 'S' if self.level[a[1], a[0]].isupper() else 's'
                    self.level[pos[1], pos[0]] = '+' if self.level[pos[1], pos[0]].isupper() else '_'
                    self.pos = a
                    self.moves += 1
                    self.pushes += 1
    def is_fini(self) -> bool:
        for c in self.__str__():
            if c in 'k+': return False
        return True
    def montre(self):
        img = img=image(img=image.new_img(fond=col.white))
        for x in range(len(self.cases)):
            for y in range(len(self.cases[0])):
                a,b=self.cases[x,y],[v+self.s for v in self.cases[x,y]]
                kase = self.level[x,y]
                match kase:
                    case 'k' | 'K':
                        img.rectangle(a,b,col.new('808080'), 0)
                    case 's' | 'S':
                        img.rectangle(a,b,col.green, 0)
                    case 'X':
                        img.rectangle(a,b,col.new('101010'), 0)
                    case '-':
                        img.rectangle(a,b,col.cyan, 0)
                    case '+':
                        img.ligne(a,b,col.red, 2)
                if kase != ' ':
                    img.rectangle(a, b, col.black, 2)
                #img.ecris(self.level[x,y], ct_sg(a,b))
        if type(self.infos) == str:
            img.ecris(f'{self.infos}', cd)
        else:
            txt = '\n'.join(f'{s}: {self.infos[s]}' for s in tableau.champs_infos)
            img.ecris(txt, cd)
        return img.montre(fullscreen=True, attente=1)

def main() -> None:
    minimum, maximum = 0, len(os.listdir('./Sokoban_levels'))
    try:
        n_lev = 0
        while n_lev < maximum:
            arr=tableau(n_lev);r=False
            clear_terminal();print(f'Level {n_lev:0>2}\nMoves {arr.moves:0>4}');arr.imprimme()
            h=False;arr.montre()
            while True:
                if True in [kb.is_pressed(k) for k in keys_j1.keys_left ]: r=True;val=[-1, 0]
                if True in [kb.is_pressed(k) for k in keys_j1.keys_right]: r=True;val=[ 1, 0]
                if True in [kb.is_pressed(k) for k in keys_j1.keys_up   ]: r=True;val=[ 0,-1]
                if True in [kb.is_pressed(k) for k in keys_j1.keys_down ]: r=True;val=[ 0, 1]
                if True in [kb.is_pressed(k) for k in keys_j1.keys_reset]: arr=tableau(n_lev);r=True
                if True in [kb.is_pressed(k) for k in keys_j1.keys_prev ]: n_lev=n_entre(n_lev-1,minimum,maximum-1);arr=tableau(n_lev);r=True;val=[0,0];h=False
                if True in [kb.is_pressed(k) for k in keys_j1.keys_next ]: n_lev=n_entre(n_lev+1,minimum,maximum-1);arr=tableau(n_lev);r=True;val=[0,0];h=False
                if True in [kb.is_pressed(k) for k in keys_j1.keys_endg ]: clear_terminal(); return
                if r:
                    arr.move(val);clear_terminal();print(f'Level {n_lev:0>2}\nMoves {arr.moves:0>4}\nPushes: {arr.pushes:0>4}');arr.imprimme()
                    r=False
                    if h: print(arr.help)
                    arr.montre()
                    time.sleep(0.3)
                arr.montre()
                if arr.is_fini(): break
                if kb.is_pressed('esc'): return
            n_lev+=1
        print('Well done!')
    except invalidLevel as e:
        arr.imprimme()
        print(e)
    except KeyboardInterrupt: pass
if __name__ == '__main__': main()