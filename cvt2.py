# Required packages:
# >>> opencv-python
# >>> numpy
# >>> sty

import numpy as np, cv2, random as rd, copy, time
from couleurs import *
from sty import Style, RgbFg, fg
from calculs import *
from _vars_ import *
def fusionImages(petite_img, grande_img, pos=[0, 0]):
    '''
    Prend:
    ------
    :petite_img: ``np.array``\n
    :grande_img: ``np.array``\n
    Renvoie:
    --------
    ``np.array``\nImage.
    '''
    s_img = petite_img
    img = grande_img
    x_offset, y_offset = [round(v) for v in pos]
    img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img
    return(img)
class image:
    class boutton:
        def __init__(self, nom='-', coos=[[0, 0], []]):
            self.nom = nom
    def new_img(self=None, dimensions=screen, fond=[256 for _ in range(3)]) -> np.array:
        return(np.full([round(v) for v in dimensions[::-1]]+[3], fond[::-1], np.uint8))
    def __init__(self, nom='image_python', img=None) -> None:
        self.nom = nom
        if type(img) == type(None):
            img = self.new_img()
        self.img = img
    def __str__(self, ordre=True) -> str:
        img_str = ''
        n = 0
        cmb = len(self.img)*len(self.img[0])
        if ordre:
            mn_x, mx_x, st_x = 0, len(self.img), 1
            mn_y, mx_y, st_y = 0, len(self.img[0]), 1
        else:
            mn_x, mx_x, st_x = len(self.img)-1, -1, -1
            mn_y, mx_y, st_y = len(self.img[0])-1, -1, -1
        for x in range(mn_x, mx_x, st_x):
            for y in range(mn_y, mx_y, st_y):
                b, g, r = self.img[x, y]
                fg.custom = Style(RgbFg(r, g, b))
                img_str += f'{fg.custom}██'
                n += 1
            print(f'{len(self.img)}, {len(self.img[0])} - {n/cmb*100:4f}%', end='\r')
            img_str += '\n'
        img_str += fg.custom+fg.rs
        print(' '*20, end='\r')
        return(img_str)
    def montre(self, attente=0, destroy=False, fullscreen=False) -> int:
        '''
        In:
        ---
        :attente: ``int`` miliseconds\n
        :destroy: ``bool`` the canvas\n
        :relocalisage_de_l_img: ``list | tuple `` of ``int`` [x, y]\n
        Out:
        ----
        ``None``
        '''
        if fullscreen:
            cv2.namedWindow(self.nom, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(self.nom, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(self.nom, self.img)
        wk = cv2.waitKeyEx(attente)
        if destroy == True: cv2.destroyWindow(self.nom)
        return(wk)
    def imprime(self, ordre=True) -> None:
        print(self.__str__(ordre), end='')
    def ligne(self, p1, p2, col=col.noir, ep=1) -> None:
        p1, p2 = [round(p) for p in p1], [round(p) for p in p2]
        cv2.line(self.img, p1, p2, col[::-1], ep)
    def rectangle(self, p1, p2, col=col.noir, ep=1) -> None:
        p1, p2 = [round(p) for p in p1], [round(p) for p in p2]
        cv2.rectangle(self.img, p1, p2, col[::-1], ep if ep != 0 else -1)
    def triangle(self, p1=ct_sg(p3, ct), p2=ct_sg(p4, ct), p3=ct_sg(ct, ch), couleur=col.noir, epaisseur=1):
        couleur = couleur[::-1]
        img = self.img
        p1 = [round(i) for i in p1]
        p2 = [round(i) for i in p2]
        p3 = [round(i) for i in p3]
        epaisseur = int(epaisseur)
        if epaisseur <= 0:
            if epaisseur == 0:
                epaisseur = 1
            else:
                epaisseur = abs(epaisseur)
            points = points_segment(p2, p3)
            for i in points:
                cv2.line(img, p1, i, couleur, epaisseur)
        cv2.line(img, p1, p2, couleur, epaisseur)
        cv2.line(img, p2, p3, couleur, epaisseur)
        cv2.line(img, p3, p1, couleur, epaisseur)
        self.img = img
    def cercle(self, ct, rayon=10, col=col.noir, ep=1) -> None:
        ct = [round(p) for p in ct]; ep = round(ep)
        cv2.circle(self.img, ct, rayon, col[::-1], ep if ep != 0 else -1)
    def ellipse(self, ct, rayons=[10, 10], col=col.noir, ep=1) -> None:
        ct = [round(p) for p in ct]; ep = round(ep)
        cv2.ellipse(self.img, ct, rayons, 0, 360, 0, col[::-1], ep if ep != 0 else -1)
    def ecris(self, texte, ct, couleur=col.red, epaisseur=1, taille=1, police=cv2.FONT_HERSHEY_SCRIPT_COMPLEX):
        if True: ## Vars ##
            x1, y1 = ct
            x2, y2 = ct
            epaisseur = round(epaisseur)
            textes = list(enumerate(str(texte).split('\n')))
            valdef = cv2.getTextSize('Agd', police, taille, epaisseur)
            xxx = (x1+x2)/2
            yyy = (y1+y2)/2
            yyy -= round(valdef[0][1]*(len(textes)-1))
        for i, line in textes:
            tailles = cv2.getTextSize(line, police, taille, epaisseur)
            x = round(xxx-tailles[0][0]/2)
            y = round(yyy+tailles[1]/2)
            yy = y + i*tailles[0][1]*2
            cv2.putText(self.img, line, (x, yy), police, taille, couleur, epaisseur)
        return self.img
if __name__ == '__main__':
    img = image('Test')
    pt = pt_sg([0, 0], screen); print(pt)
    img.ellipse(pt, [500, 100], col.magenta, 10)
    img.ligne([0, 0], screen, col.white, 10)
    img.cercle([0, 0], 100, col.red, 0)
    img.cercle(screen, 1000, col.red, 0)
    img.montre()