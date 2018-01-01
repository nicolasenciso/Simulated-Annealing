# -*- coding: utf-8 -*-

# Clase pieza
# Atrbutos:
# s = Estado
# n = Numero de pieza
# l = Largo de la pieza
# w = Ancho de la pieza
# x1 = x inical
# x2 = x final
# y1 = y inicial
# y2 = y final
# c = contenido de la pieza
# p = piezas que contiene
class Piece:
    # Inicializa cada placa
    def __init__(self, s, n, l, w):
        self.s = s
        self.n = n
        self.l = l
        self.w = w
        self.x1 = 0
        self.x2 = l
        self.y1 = 0
        self.y2 = w
        self.c = [[0 for col in range(w)] for row in range(l)]
        self.p =[]

    # Ubica cada placa iniciando en la posición asignada
    def putAt(self, x, y):
        self.x1 = x
        self.x2 = x+self.l
        self.y1 = y
        self.y2 = y+self.w

    # Verifica si puede ubicar la pieza en esa posición
    def canPut(self, p, x, y):
        if x+p.l > self.l or y+p.w > self.w:
            return False
        else:
            for j in range(y,y+p.w):
                for i in range(x,x+p.l):
                    if self.c[i][j] != 0:
                        return False

        return True

    # Inserta la pieza en la placa
    def insert(self, p):
        for j in range(self.w):
            for i in range(self.l):
                if self.c[i][j] == 0 and self.canPut(p, i, j):
                    p.putAt(i, j)
                    p.s = False
                    self.p.append(p)
                    for y in range (p.w):
                        for x in range(p.l):
                            self.c[i+x][j+y] = p.n
                    return True
                # Si la pìeza no encaja la rota y prueba de nuevo
                else:
                    p.rotate()
                    if self.c[i][j] == 0 and self.canPut(p, i, j):
                        p.putAt(i, j)
                        p.s = False
                        self.p.append(p)
                        for y in range (p.w):
                            for x in range(p.l):
                                self.c[i+x][j+y] = p.n
                        return True
                    # Si no logra ubicarla la pone en su posición original
                    else: p.rotate()
        return False

    # Muestra la distribución de piezas en la placa
    def distribution(self):
        for j in range(self.w):
            for i in range(self.l):
                if self.c[i][j] == 0: print "--",
                else: print str(self.c[i][j]).zfill(2),
            print

    # Muestra las piezas insertadas en la placa
    def contains(self):
        print "Piezas:",
        for p in self.p:
            print p.n,
        print

    # Rota la posición de la pieza
    def rotate(self):
        t = [[0 for col in range(self.l)] for row in range(self.w)]
        for y in range(self.w):
            for x in range(self.l):
                t[y][x]=self.c[x][y]

        aux = self.l
        self.l = self.w
        self.w = aux
        self.c = t

    # Muestra la descripción de la pieza
    def description(self):
        print "s=", self.s, " n=", self.n, " l=", self.l, " w=", self.w, " x=(", self.x1,",",self.x2, ") y=(", self.y1,",",self.y2,")"


# Crea todas las piezas
p1 = Piece(True, 1, 8, 3)
p2 = Piece(True, 2, 5, 1)
p3 = Piece(True, 3, 2, 2)
p4 = Piece(True, 4, 1, 1)
p5 = Piece(True, 5, 9, 4)
p6 = Piece(True, 6, 6, 2)
p7 = Piece(True, 7, 4, 3)
p8 = Piece(True, 8, 5, 7)
p9 = Piece(True, 9, 3, 2)
p10 = Piece(True, 10, 4, 2)

pieces = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

# Crea las láminas que contienen las piezas pequeñas
plate = []
i=0
plate.append(Piece(True, i, 10,10))
# plate[i].description()

# Se insertan las piezas pequeñas en la lamina
while(len(pieces)>0):
    aux=[]
    for p in pieces:
        if not plate[i].insert(p):
            aux.append(p)

    pieces=[]
    if len(aux)>0:
        pieces.extend(aux)
        plate.append(Piece(True, 1, 10,10))
        i+=1

# Muestra los resultados
for l in plate:
    print "lamina:", l.n
    l.contains()
    l.distribution()
