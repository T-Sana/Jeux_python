a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=[i+10 for i in range(26)]
if True: ### MONOMINOS ###
    _1o1 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,a,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _1O = [_1o1, _1o1, _1o1, _1o1]
if True: ### DOMINOS ###
    _2i1 = [[0,0,0,0,0],
            [0,0,b,0,0],
            [0,0,b,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _2i2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,b,b,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _2O = [_2i1, _2i2, _2i1, _2i2]
if True: ### TRIOMINOS ###
    _3i1 = [[0,0,0,0,0],
            [0,0,8,0,0],
            [0,0,8,0,0],
            [0,0,8,0,0],
            [0,0,0,0,0]]
    _3i2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,8,8,8,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _3l1 = [[0,0,0,0,0],
            [0,0,9,0,0],
            [0,0,9,9,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _3l2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,9,9,0],
            [0,0,9,0,0],
            [0,0,0,0,0]]
    _3l3 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,9,9,0,0],
            [0,0,9,0,0],
            [0,0,0,0,0]]
    _3l4 = [[0,0,0,0,0],
            [0,0,9,0,0],
            [0,9,9,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _3I = [_3i1, _3i2, _3i1, _3i2]
    _3L = [_3l1, _3l2, _3l3, _3l4]
if True: ### TETRAMINOS ###
    _4s1 = [[0,0,0,0,0],
            [0,0,1,1,0],
            [0,1,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4s2 = [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,1,0],
            [0,0,0,1,0],
            [0,0,0,0,0]]
    _4z1 = [[0,0,0,0,0],
            [0,2,2,0,0],
            [0,0,2,2,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4z2 = [[0,0,0,0,0],
            [0,0,0,2,0],
            [0,0,2,2,0],
            [0,0,2,0,0],
            [0,0,0,0,0]]
    _4l1 = [[0,0,0,0,0],
            [0,0,0,3,0],
            [0,3,3,3,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4l2 = [[0,0,0,0,0],
            [0,0,3,0,0],
            [0,0,3,0,0],
            [0,0,3,3,0],
            [0,0,0,0,0]]
    _4l3 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,3,3,3,0],
            [0,3,0,0,0],
            [0,0,0,0,0]]
    _4l4 = [[0,0,0,0,0],
            [0,3,3,0,0],
            [0,0,3,0,0],
            [0,0,3,0,0],
            [0,0,0,0,0]]
    _4j1 = [[0,0,0,0,0],
            [0,4,0,0,0],
            [0,4,4,4,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4j2 = [[0,0,0,0,0],
            [0,0,4,4,0],
            [0,0,4,0,0],
            [0,0,4,0,0],
            [0,0,0,0,0]]
    _4j3 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,4,4,4,0],
            [0,0,0,4,0],
            [0,0,0,0,0]]
    _4j4 = [[0,0,0,0,0],
            [0,0,4,0,0],
            [0,0,4,0,0],
            [0,4,4,0,0],
            [0,0,0,0,0]]
    _4i1 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,5,5,5,5],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4i2 = [[0,0,5,0,0],
            [0,0,5,0,0],
            [0,0,5,0,0],
            [0,0,5,0,0],
            [0,0,0,0,0]]
    _4o1 = [[0,0,0,0,0],
            [0,0,6,6,0],
            [0,0,6,6,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4t1 = [[0,0,0,0,0],
            [0,0,7,0,0],
            [0,7,7,7,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _4t2 = [[0,0,0,0,0],
            [0,0,7,0,0],
            [0,0,7,7,0],
            [0,0,7,0,0],
            [0,0,0,0,0]]
    _4t3 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,7,7,7,0],
            [0,0,7,0,0],
            [0,0,0,0,0]]
    _4t4 = [[0,0,0,0,0],
            [0,0,7,0,0],
            [0,7,7,0,0],
            [0,0,7,0,0],
            [0,0,0,0,0]]
    _4Z = [_4z1, _4z2, _4z1, _4z2] ## Z ##
    _4S = [_4s1, _4s2, _4s1, _4s2] ## S ##
    _4L = [_4l1, _4l2, _4l3, _4l4] ## L ##
    _4J = [_4j1, _4j2, _4j3, _4j4] ## J ##
    _4I = [_4i1, _4i2, _4i1, _4i2] ## I ##
    _4O = [_4o1, _4o1, _4o1, _4o1] ## O ##
    _4T = [_4t1, _4t2, _4t3, _4t4] ## T ##
if True: ### PENTAMINOS ###
    _5i1 = [[0,0,c,0,0],
            [0,0,c,0,0],
            [0,0,c,0,0],
            [0,0,c,0,0],
            [0,0,c,0,0]]
    _5i2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [c,c,c,c,c],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5l1 = [[0,0,d,0,0],
            [0,0,d,0,0],
            [0,0,d,0,0],
            [0,0,d,d,0],
            [0,0,0,0,0]]
    _5l2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,d,d,d,d],
            [0,d,0,0,0],
            [0,0,0,0,0]]
    _5l3 = [[0,0,0,0,0],
            [0,d,d,0,0],
            [0,0,d,0,0],
            [0,0,d,0,0],
            [0,0,d,0,0]]
    _5l4 = [[0,0,0,0,0],
            [0,0,0,d,0],
            [d,d,d,d,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5j1 = [[0,0,e,0,0],
            [0,0,e,0,0],
            [0,0,e,0,0],
            [0,e,e,0,0],
            [0,0,0,0,0]]
    _5j2 = [[0,0,0,0,0],
            [0,e,0,0,0],
            [0,e,e,e,e],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5j3 = [[0,0,0,0,0],
            [0,0,e,e,0],
            [0,0,e,0,0],
            [0,0,e,0,0],
            [0,0,e,0,0]]
    _5j4 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [e,e,e,e,0],
            [0,0,0,e,0],
            [0,0,0,0,0]]
    _5f1 = [[0,0,f,0,0],
            [0,0,f,f,0],
            [0,0,f,0,0],
            [0,0,f,0,0],
            [0,0,0,0,0]]
    _5f2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,f,f,f,f],
            [0,0,0,f,0],
            [0,0,0,0,0]]
    _5f3 = [[0,0,0,0,0],
            [0,0,f,0,0],
            [0,0,f,0,0],
            [0,f,f,0,0],
            [0,0,f,0,0]]
    _5f4 = [[0,0,0,0,0],
            [0,f,0,0,0],
            [f,f,f,f,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5g1 = [[0,0,g,0,0],
            [0,0,g,0,0],
            [0,0,g,g,0],
            [0,0,g,0,0],
            [0,0,0,0,0]]
    _5g2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,g,g,g,g],
            [0,0,g,0,0],
            [0,0,0,0,0]]
    _5g3 = [[0,0,0,0,0],
            [0,0,g,0,0],
            [0,g,g,0,0],
            [0,0,g,0,0],
            [0,0,g,0,0]]
    _5g4 = [[0,0,0,0,0],
            [0,0,g,0,0],
            [g,g,g,g,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5m1 = [[0,0,0,0,0],
            [0,h,0,h,0],
            [0,h,h,h,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5m2 = [[0,0,0,0,0],
            [0,0,h,h,0],
            [0,0,h,0,0],
            [0,0,h,h,0],
            [0,0,0,0,0]]
    _5m3 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,h,h,h,0],
            [0,h,0,h,0],
            [0,0,0,0,0]]
    _5m4 = [[0,0,0,0,0],
            [0,h,h,0,0],
            [0,0,h,0,0],
            [0,h,h,0,0],
            [0,0,0,0,0]]
    _5x1 = [[0,0,0,0,0],
            [0,0,i,0,0],
            [0,i,i,i,0],
            [0,0,i,0,0],
            [0,0,0,0,0]]
    _5b1 = [[0,0,j,0,0],
            [0,0,j,j,0],
            [0,0,j,j,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5b2 = [[0,0,0,0,0],
            [0,0,j,j,j],
            [0,0,j,j,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5b3 = [[0,0,0,0,0],
            [0,0,j,j,0],
            [0,0,j,j,0],
            [0,0,0,j,0],
            [0,0,0,0,0]]
    _5b4 = [[0,0,0,0,0],
            [0,0,j,j,0],
            [0,j,j,j,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5d1 = [[0,0,0,k,0],
            [0,0,k,k,0],
            [0,0,k,k,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5d2 = [[0,0,0,0,0],
            [0,0,k,k,0],
            [0,0,k,k,k],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5d3 = [[0,0,0,0,0],
            [0,0,k,k,0],
            [0,0,k,k,0],
            [0,0,k,0,0],
            [0,0,0,0,0]]
    _5d4 = [[0,0,0,0,0],
            [0,k,k,k,0],
            [0,0,k,k,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5t1 = [[0,0,0,0,0],
            [0,l,l,l,0],
            [0,0,l,0,0],
            [0,0,l,0,0],
            [0,0,0,0,0]]
    _5t2 = [[0,0,0,0,0],
            [0,0,0,l,0],
            [0,l,l,l,0],
            [0,0,0,l,0],
            [0,0,0,0,0]]
    _5t3 = [[0,0,0,0,0],
            [0,0,l,0,0],
            [0,0,l,0,0],
            [0,l,l,l,0],
            [0,0,0,0,0]]
    _5t4 = [[0,0,0,0,0],
            [0,l,0,0,0],
            [0,l,l,l,0],
            [0,l,0,0,0],
            [0,0,0,0,0]]
    _5sb1= [[0,0,0,0,0],
            [0,m,m,0,0],
            [0,0,m,m,0],
            [0,0,m,0,0],
            [0,0,0,0,0]]
    _5sb2= [[0,0,0,0,0],
            [0,0,0,m,0],
            [0,m,m,m,0],
            [0,0,m,0,0],
            [0,0,0,0,0]]
    _5sb3= [[0,0,0,0,0],
            [0,0,m,0,0],
            [0,m,m,0,0],
            [0,0,m,m,0],
            [0,0,0,0,0]]
    _5sb4= [[0,0,0,0,0],
            [0,0,m,0,0],
            [0,m,m,m,0],
            [0,m,0,0,0],
            [0,0,0,0,0]]
    _5sa1= [[0,0,0,0,0],
            [0,0,n,n,0],
            [0,n,n,0,0],
            [0,0,n,0,0],
            [0,0,0,0,0]]
    _5sa2= [[0,0,0,0,0],
            [0,0,n,0,0],
            [0,n,n,n,0],
            [0,0,0,n,0],
            [0,0,0,0,0]]
    _5sa3= [[0,0,0,0,0],
            [0,0,n,0,0],
            [0,0,n,n,0],
            [0,n,n,0,0],
            [0,0,0,0,0]]
    _5sa4= [[0,0,0,0,0],
            [0,n,0,0,0],
            [0,n,n,n,0],
            [0,0,n,0,0],
            [0,0,0,0,0]]
    _5nb1= [[0,0,0,0,0],
            [0,o,0,0,0],
            [0,o,o,0,0],
            [0,0,o,0,0],
            [0,0,o,0,0]]
    _5nb2= [[0,0,0,0,0],
            [0,0,o,o,0],
            [o,o,o,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5nb3= [[0,0,o,0,0],
            [0,0,o,0,0],
            [0,0,o,o,0],
            [0,0,0,o,0],
            [0,0,0,0,0]]
    _5nb4= [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,o,o,o],
            [0,o,o,0,0],
            [0,0,0,0,0]]
    _5za1= [[0,0,0,0,0],
            [0,p,p,0,0],
            [0,0,p,0,0],
            [0,0,p,p,0],
            [0,0,0,0,0]]
    _5za2= [[0,0,0,0,0],
            [0,0,0,p,0],
            [0,p,p,p,0],
            [0,p,0,0,0],
            [0,0,0,0,0]]
    _5zb1= [[0,0,0,0,0],
            [0,0,q,q,0],
            [0,0,q,0,0],
            [0,q,q,0,0],
            [0,0,0,0,0]]
    _5zb2= [[0,0,0,0,0],
            [0,q,0,0,0],
            [0,q,q,q,0],
            [0,0,0,q,0],
            [0,0,0,0,0]]
    _5w1 = [[0,0,0,0,0],
            [0,r,0,0,0],
            [0,r,r,0,0],
            [0,0,r,r,0],
            [0,0,0,0,0]]
    _5w2 = [[0,0,0,0,0],
            [0,0,r,r,0],
            [0,r,r,0,0],
            [0,r,0,0,0],
            [0,0,0,0,0]]
    _5w3 = [[0,0,0,0,0],
            [0,r,r,0,0],
            [0,0,r,r,0],
            [0,0,0,r,0],
            [0,0,0,0,0]]
    _5w4 = [[0,0,0,0,0],
            [0,0,0,r,0],
            [0,0,r,r,0],
            [0,r,r,0,0],
            [0,0,0,0,0]]
    _5na1= [[0,0,0,0,0],
            [0,0,0,s,0],
            [0,0,s,s,0],
            [0,0,s,0,0],
            [0,0,s,0,0]]
    _5na2= [[0,0,0,0,0],
            [0,0,0,0,0],
            [s,s,s,0,0],
            [0,0,s,s,0],
            [0,0,0,0,0]]
    _5na3= [[0,0,s,0,0],
            [0,0,s,0,0],
            [0,s,s,0,0],
            [0,s,0,0,0],
            [0,0,0,0,0]]
    _5na4= [[0,0,0,0,0],
            [0,s,s,0,0],
            [0,0,s,s,s],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    _5I = [_5i1, _5i2, _5i1, _5i2]
    _5L = [_5l1, _5l2, _5l3, _5l4]
    _5J = [_5j1, _5j2, _5j3, _5j4]
    _5F = [_5f1, _5f2, _5f3, _5f4]
    _5G = [_5g1, _5g2, _5g3, _5g4]
    _5M = [_5m1, _5m2, _5m3, _5m4]
    _5X = [_5x1, _5x1, _5x1, _5x1]
    _5B = [_5b1, _5b2, _5b3, _5b4]
    _5D = [_5d1, _5d2, _5d3, _5d4]
    _5T = [_5t1, _5t2, _5t3, _5t4]
    _5W = [_5w1, _5w2, _5w3, _5w4]
    _5SA = [_5sa1, _5sa2, _5sa3, _5sa4]
    _5SB = [_5sb1, _5sb2, _5sb3, _5sb4]
    _5NA = [_5na1, _5na2, _5na3, _5na4]
    _5NB = [_5nb1, _5nb2, _5nb3, _5nb4]
    _5ZA = [_5za1, _5za2, _5za1, _5za2]
    _5ZB = [_5zb1, _5zb2, _5zb1, _5zb2]
if True: ### SPECIALMINOS ###
    '''
    Here will be polyminos that changes shape when rotating.
    Like a _4O turning into _9O when rotates.
    '''
monominos = [_1O]
dominos = [_2O]
triominos = [_3I, _3L]
tetraminos = [_4S, _4Z, _4L, _4J, _4I, _4O, _4T]
pentaminos = [_5I, _5L, _5J, _5F, _5G, _5M, _5X, _5B, _5D, _5T, _5W, _5SA, _5SB, _5NA, _5NB, _5ZA, _5ZB]
specialminos = []
miniminos = monominos + dominos + triominos