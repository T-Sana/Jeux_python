from koma import *
from Outils.cvt2 import *

def dessine_kanji_roi(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2, koma='R') -> image:
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    lines = [
        [pt_sg(p1, ch, 7), pt_sg(p2, ch, 7)],
        [pt_sg(cg, ct, 3), pt_sg(cd, ct, 3)],
        [ch, cb], [p3, p4]
    ]
    if koma.upper() == 'J':
        lines.append([pt_sg(ct, p4, 5, 2), pt_sg(p4, ct, 5, 4)])
    for pa, pb in lines: img.ligne(pa, pb, c, ep, l_t) ## Dessin des lignes ##
    return img
def dessine_kanji_soleil(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    cg, cd = ct_sg(p1, p3), ct_sg(p2, p4)
    lines = [ [p1, p3], [p1, p2], [p2, p4], [cg, cd], [p3, p4] ]
    for a, b in lines:
        img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_cereale(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb = ct_sg(p1, p2), ct_sg(p3, p4)
    ah, ab = ch, cb
    pa = pt_sg(ah, ab, 3, 2)
    d1 = dist(p1, ch) * 0.6
    d2 = dist(p1, ch) * 0.9
    d3 = dist(p1, p3) * 0.8
    hag, had = coosCercle(ah, d1, 180+ori), coosCercle(ah, d1, ori)
    a1, a2 = coosCercle(pa, d2, 180+ori), coosCercle(pa, d2, ori)
    a3, a4 = coosCercle(pa, d3, 150+ori), coosCercle(pa, d3, 30+ori)
    lines = [ [had, hag], [a1, a2], [ah, ab], [pa, a3], [pa, a4] ]
    for a, b in lines:
        img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_encens(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    cg, cd = ct_sg(p1, p3), ct_sg(p2, p4)
    dessine_kanji_cereale(img, p1, p2, cg, cd, c, ep, ori, l_t)
    dessine_kanji_soleil(img, cg, cd, p3, p4, c, ep, ori, l_t)
    return img
def dessine_kanji_arbre(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ah, ab = ct_sg(p1, p2), ct_sg(p3, p4)
    pa = pt_sg(ah, ab, 3)
    d = dist(p1, ah) * 0.9
    d2 = dist(p1, p3) * 0.7
    a1, a2 = coosCercle(pa, d, 180+ori), coosCercle(pa, d, ori)
    a3, a4 = coosCercle(pa, d2, 110+ori), coosCercle(pa, d2, 70+ori)
    lines = [ [a1, a2], [ah, ab], [pa, a3], [pa, a4] ]
    for a, b in lines:
        img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_terre(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb = ct_sg(p1, p2), ct_sg(p3, p4)
    cg, cd = ct_sg(p1, p3), ct_sg(p2, p4)
    a, b = 17, 2
    lines = [[pt_sg(cg, cd, a, b), pt_sg(cd, cg, a, b)], [pt_sg(ch, cb, a, b*2), cb], [p3, p4]]
    for a, b in lines:
        img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_cannellier(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb = ct_sg(p1, p2), ct_sg(p3, p4)
    ct, cd = ct_cr(p1, p2, p3, p4), ct_sg(p2, p4)
    dessine_kanji_arbre(img, p1, ch, p3, cb, c, ep, ori, l_t)
    dessine_kanji_terre(img, ch, p2, ct, cd, c, ep, ori, l_t)
    dessine_kanji_terre(img, ct, cd, cb, p4, c, ep, ori, l_t)
    return img
def dessine_kanji_or(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb = ct_sg(p1, p2), ct_sg(p3, p4)
    cg, cd = ct_sg(p1, p3), ct_sg(p2, p4)
    a = 20
    pcg = coosCercle(ch, dist(ch, p1), ori+180-a)
    pcd = coosCercle(ch, dist(ch, p1), ori+a)
    img.ligne(ch, pcg, c, ep, l_t)
    img.ligne(ch, pcd, c, ep, l_t)
    clh, clb = coosCercle(ch, tailles_koma['O'][1]/2/5, 90+ori), cb
    ctl = ct_sg(clh, clb)
    pts = [clh, ctl, clb]
    dts = [dist(p1, ch)*i for i in [0.8, 0.7, 1]]
    for i in range(3):
        img.ligne(coosCercle(pts[i], dts[i], ori), coosCercle(pts[i], dts[i], ori+180), c, ep, l_t)
    img.ligne(clh, clb, c, ep, l_t)
    pt1 = coosCercle(pts[1], dts[1], ori)
    pt2 = coosCercle(pts[1], dts[1], ori+180)
    a, b = 5, 3
    img.ligne(pt_sg(pt1, clb, a, b), pt_sg(pt1, clb, b, a), c, ep, l_t)
    img.ligne(pt_sg(pt2, clb, a, b), pt_sg(pt2, clb, b, a), c, ep, l_t)
    return img
def dessine_kanji_argent(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    dessine_kanji_or(img, p1, ct_sg(p1, p2), p3, ct_sg(p3, p4), c, ep, ori, l_t)
    d = dist(p1, p2)/10
    p1, p3 = coosCercle(ct_sg(p1, p2), d, ori), coosCercle(ct_sg(p3, p4), d, ori)
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4)
    ct = ct_cr(p1, p2, p3, p4); pt1, pt2 = ct_sg(cg, ct), pt_sg(cb, p4, 1, 4)
    LINES = [[p1, p3], [p1, p2], [p2, cd], [cg, cd], [ct_sg(p1, cg), ct_sg(p2, cd)], [pt1, pt2],
        [pt_sg(pt1, pt2), pt_sg(pt_sg(cd, ct, 2), p4, 2)], [p3, pt_sg(cb, ct, 3)]]
    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_promu(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## TODO ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    a, b = 3, 2; pt = pt_sg(p1, p3, a, b); ctg, ctd = pt_sg(pt, pt_sg(ch, cb, a, b)), pt_sg(p2, p4, a, b)
    ptt = pt_sg(ctd, ctg, 4); d = dist(p1, p2)/4
    img.ellipse(pt, (dist(pt, ctg), dist(pt, p3)), c, ep, l_t, 0, 90, ori)
    img.ellipse(ptt, (dist(ptt, ct)*0.75, dist(ptt, p4)), c, ep, l_t, 90, 225, ori-20)
    peg = coosEllipse(pt, (dist(pt, ctg), dist(pt, p3)), 20+ori); pfeg = coosCercle(peg, d, ori)
    img.ellipse(peg, (dist(peg, pfeg), dist(peg, p3)*0.85), c, ep, l_t, 0, 100, ori)
    img.ellipse(ct, (dist(ct, cd)*0.7, dist(ct, cb)), c, ep, l_t, 30, 110, -20+ori)
    ctb = ct_sg(ct, cb)
    img.ellipse(ctb, (dist(ctb, cd)*0.8, dist(ctb, ch)), c, ep, l_t, 0, 360, -20+ori)
    LINES = [[ctg, ctd], [peg, pfeg]]
    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_diagonale(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## TODO ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    img.ellipse(p1, (dist(p1, ch)*0.8, dist(p1, ct_sg(ct_sg(p1, ch), cg))/2), c, ep, l_t, 0, 110, ori-20)
    img.ellipse(ct_sg(p1, cg), (dist(p1, ch)/4, dist(ct_sg(p1, cg), p3)), c, ep, l_t, 0, 90, ori)
    p = coosEllipse(p1, (dist(p1, ch)*0.8, dist(p1, ct_sg(ct_sg(p1, ch), cg))/2), 45-180+ori)
    d = dist(p1, p); a = angleEntrePoints(p1, p)
    pt = coosCercle(p1, d, a-20)
    LINES = [
        [ct_sg(ct_sg(p1, ch), cg), ct_sg(p2, cd)], [ct_sg(p2, cd), p4], [p4, ct_sg(p4, cb)],
        [pt, pt_sg(ch, p2, 2)], [pt_sg(ch, p2, 2), ct_sg(ct_sg(ct_sg(p1, ch), cg), ct_sg(p2, cd))],
        [ct_sg(ct_sg(ct_sg(p1, ch), cg), ct_sg(p2, cd)), cb],
        [coosEllipse(ct_sg(p1, cg), (dist(p1, ch)/4, dist(ct_sg(p1, cg), p3)), 17+ori), pt_sg(ct_sg(p2, cd), p4, 3)],
        [coosEllipse(ct_sg(p1, cg), (dist(p1, ch)/4, dist(ct_sg(p1, cg), p3)), 35+ori), pt_sg(ct_sg(p2, cd), p4, 4, 5)]
    ]

    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_volant(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    a, b = 2, 3
    an = -20
    pt = ct_sg(ch, cg)
    d = dist(p1, p2)/6
    LINES = [
        [p1, pt_sg(p2, ch, a, b)],
        [cg, pt_sg(cd, ct, a, b)],
        [ct_sg(ch, ct), cb], [pt, ct_sg(p3, cb)],
        [coosCercle(pt, d, an+ori), coosCercle(pt, d, an+180+ori)],
        [coosEllipse(p2, (dist(pt_sg(p2, ch, a, b), p2), dist(p2, cd)), 135+ori), p2],
        [ct_sg(coosEllipse(p2, (dist(pt_sg(p2, ch, a, b), p2), dist(p2, cd)), 135+ori), p2), ct_sg(p2, cd)],
        [coosEllipse(cd, (dist(pt_sg(cd, ct, a, b), cd), dist(cd, p4)), 135+ori), cd],
        [ct_sg(coosEllipse(cd, (dist(pt_sg(cd, ct, a, b), cd), dist(cd, p4)), 135+ori), cd), ct_sg(cd, p4)],
    ]
    img.ellipse(p2, (dist(pt_sg(p2, ch, a, b), p2), dist(p2, cd)), c, ep, l_t, 90, 180, ori)
    img.ellipse(cd, (dist(pt_sg(cd, ct, a, b), cd), dist(cd, p4)), c, ep, l_t, 90, 180, ori)
    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_marcheur(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    an = -20
    pt = ct_sg(cg, ct_sg(ch, ct))
    ptb = ct_sg(p1, ct_sg(ch, ct))
    d = dist(p1, p2)/6
    LINES = [
        [coosCercle(pt, d, an+ori), coosCercle(pt, d, an+180+ori)],
        [coosCercle(ptb, d, an+ori), coosCercle(ptb, d, an+180+ori)],
        [pt, ct_sg(p3, cb)], [pt_sg(ch, ct, 3), pt_sg(p2, cd, 3)],
        [pt_sg(ch, ct, 1, 2), pt_sg(p2, cd, 1, 2)],
        [pt_sg(pt_sg(ch, ct, 1, 2), pt_sg(p2, cd, 1, 2), 1, 2), pt_sg(cb, p4, 1, 2)],
        [pt_sg(cb, p4, 1, 2), pt_sg(p4, p3, 2)]
    ]
    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_lune(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    a, b = 1, 2
    LINES = [[p1, p3], [p1, p2], [p2, p4], [p4, pt_sg(p4, cb, 2)],
        [pt_sg(p1, cg, a, b), pt_sg(p2, cd, a, b)], [pt_sg(p3, cg, a, b), pt_sg(p4, cd, a, b)]
    ]
    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_debout(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    col = c
    a, b = 7, 2
    c, d = 7, 4
    cth = pt_sg(ch, ct, 3, 2)
    phg, phd = pt_sg(p1, cg, 3, 2), pt_sg(p2, cd, 3, 2)
    pbg, pbd = pt_sg(p3, cg, 3, 2), pt_sg(p4, cd, 3, 2)
    LINES = [
        [ch, cth], [phg, phd], [pbg, pbd],
        [pt_sg(phg, phd, a, b), pt_sg(pbg, pbd, c, d)],
        [pt_sg(phg, phd, b, a), pt_sg(pbg, pbd, d, c)]
    ]
    for a, b in LINES: img.ligne(a, b, col, ep, l_t)
    return img
def dessine_kanji_brutal(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    col = c; a, b = 3, 1; c, d = 2, 1; e, f = 3, 1; g = 10
    LINES = [
        [pt_sg(p1, cg, a, b), pt_sg(p2, cd, a, b)], [p1, pt_sg(cg, p1, c, d)], [pt_sg(cg, p1, c, d), pt_sg(cd, p2, c, d)],
        [pt_sg(cd, p2, c, d), cd], [cd, cg], [cg, p3], [p3, p4], [p4, pt_sg(p4, cd, 5)], 
        [pt_sg(cg, p3, e, f), pt_sg(pt_sg(cd, p4, e, f), pt_sg(cg, p3, e, f), g)],
        [ct_sg(cg, p3), pt_sg(ct_sg(cd, p4), ct_sg(cg, p3), g)],
        [pt_sg(cg, p3, f, e), pt_sg(pt_sg(cd, p4, f, e), pt_sg(cg, p3, f, e), g)]
    ]
    for a, b in LINES: img.ligne(a, b, col, ep, l_t)
    return img
def dessine_kanji_dragon_t(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    dessine_kanji_debout(img, p1, ch, cg, ct, c, ep, ori, l_t)
    dessine_kanji_lune(img, cg, ct, p3, cb, c, ep, ori, l_t)
    a,b = 4, 1
    dessine_kanji_brutal(img, pt_sg(ch, p2, a, b), p2, pt_sg(cb, p4, a, b), p4, c, ep, ori, l_t)
    return img
def dessine_kanji_dragon_s(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb, cg, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p1, p3), ct_sg(p2, p4); ct = ct_cr(p1, p2, p3, p4)
    dessine_kanji_debout(img, p1, p2, cg, cd, c, ep, ori, l_t)
    LINES = [[cg, pt_sg(p3, cg, 2)], [cg, cd], [cd, pt_sg(p4, cd, 2)],
        [pt_sg(cg, p3, 2), pt_sg(cd, p4, 2)],
        [pt_sg(p3, cg, 2), pt_sg(p4, cd, 2)],
        [ct, cb], [cb, p4], [p4, pt_sg(p4, cd, 4)]]
    for a, b in LINES: img.ligne(a, b, c, ep, l_t)
    return img
def dessine_kanji_dragon(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2, option:int=0) -> image: ## DONE ##
    '''`option` must be `0` or `1` for Simplified or Trditional kanji form.'''
    if option==0: dessine_kanji_dragon_s(img, p1, p2, p3, p4, c, ep, ori, l_t)
    else: dessine_kanji_dragon_t(img, p1, p2, p3, p4, c, ep, ori, l_t)
    return img
def dessine_kanji_charriot(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb = ct_sg(p1, p2), ct_sg(p3, p4)
    pts = []
    for i, y in enumerate(float_range(p1[1], p3[1], 6)):
        match i:
            case b if b in [i for i in range(2, 5)]:
                pt1, pt2 = [pt_sg(p1, ch, 5, 3)[0], y], [pt_sg(p2, ch, 5, 3)[0], y]
                img.ligne(pt1, pt2, c, ep, l_t)
                pts.append([pt1, pt2])
            case a if a in [i for i in range(1, 6)]:
                img.ligne([p1[0], y], [p2[0], y], c, ep, l_t)
    img.ligne(pts[0][0], pts[-1][0], c, ep, l_t)
    img.ligne(pts[0][1], pts[-1][1], c, ep, l_t)
    img.ligne(ch, cb, c, ep, l_t)
    return img
def dessine_kanji_cheval(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## DONE ##
    ch, cb = ct_sg(p1, p2), ct_sg(p3, p4)
    cg, cd = ct_sg(p1, p3), ct_sg(p2, p4)
    ct = ct_cr(p1, p2, p3, p4)
    ptbd, pttbd = pt_sg(p4, pt_sg(cb, ct, 2), 2), pt_sg(p4, cd, 4.5)
    ptcg, ptcd = pt_sg(cg, ct, 2), pt_sg(cd, ct, 2)
    ptsh = [ptcg, pt_sg(ptcg, ptcd, 2), pt_sg(ptcd, ptcg, 2), ptcd]
    ptsb = [p3, pt_sg(p3, ptbd, 2), pt_sg(ptbd, p3, 2), ptbd]
    lines = [
        [p2, p1], [p1, cg], [cg, cd], [cd, pttbd], [pttbd, ptbd], [ch, ct],
        [pt_sg(p1, cg, 2), pt_sg(p2, cd, 2)], [pt_sg(cg, p1, 2), pt_sg(cd, p2, 2)],
    ]
    a, b = 5, 2
    lines += [[pt_sg(ptsh[i], ptsb[i], a, b), pt_sg(ptsh[i], ptsb[i], b, a)] for i in range(4)]
    for pa, pb in lines: img.ligne(pa, pb, c, ep, l_t)
    return img
def dessine_kanji_general(img:image, p1, p2, p3, p4, c=col.black, ep=1, ori=0, l_t=2) -> image: ## TODO ##
    ch, cb, cd = ct_sg(p1, p2), ct_sg(p3, p4), ct_sg(p2, p4)
    ct = ct_cr(p1, p2, p3, p4)
    d = dist(p1, p2)/6; a, b = 5, 4
    plgh, plgb = coosCercle(p1, d, ori), coosCercle(p3, d, ori)
    plgch, plgcb = (pt_sg(plgh, plgb, [a,b][i], [b,a][i]) for i in range(2))
    plhdg = pt_sg(p1,pt_sg(ch,ct,2),2,3)
    lines = [[plgh,plgb],[plgch,coosCercle(plgch,d*1.5,245+ori)],[plgch,coosCercle(plgcb,d,170+ori)],[p2,plhdg]]
    a, b = 4, 11
    lines += [[pt_sg(p3, ct, a, b), pt_sg(p4, cd, a, b)], [pt_sg(cb, p4, a, b), pt_sg(ct, cd, a, b)], [ct_sg(plhdg, ct), ct]]
    for pa, pb in lines: img.ligne(pa, pb, c, ep, l_t) ## Dessin des lignes ##
    return image