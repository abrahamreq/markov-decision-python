# -*- coding: utf-8 -*-
#TRABAJO FINAL AIA
#NOMBRE: ABRAHAM REQUENA MESA
#Grupo: 1

import random,copy

class MDP (object):
        def __init__(self,e,ei,d):
                self.estados = e
                self.estado_inicial = ei
                self.descuento = d
        def a(self, s):
                pass
        def r(self,s):
                pass
        def t(self,s,ac,pr):
                pass


class Cuadricula(MDP):
    def __init__(self,e,ei,d,c,rec,ru):
        MDP.__init__(self,e,ei,d)
        self.cuadricula = c
        self.rec = rec
        self.ruido = ru
    def a(self,s):
        c = self.cuadricula
        if(c[s[0]][s[1]] == ' ' or c[s[0]][s[1]] == 'S'):
            return ["Arriba", "Abajo", "Derecha", "Izquierda"]
        else:
            return ["exit"]
    def r(self,s):
        c = self.cuadricula
        if(c[s[0]][s[1]] == ' ' or c[s[0]][s[1]] == 'S'):
            return self.rec
        elif(c[s[0]][s[1]] == '#'):
            return 0
        else:
            return float(c[s[0]][s[1]])
    def t(self,s,ac):
        t = []
        p = float(1 - self.ruido)
        r = float(self.ruido/2)
        recompensa_finales = []
        estados = sum(self.cuadricula,[])
        for e in estados:
            if (isinstance(e,int)):
                recompensa_finales.append(e)
        bloqueados = self.elimina_bloqueados()
        if(ac=="Arriba"):
            b = tarriba(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,p))
            else:
                t.append((s,p))
            b = tderecha(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
            b = tizquierda(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
        elif(ac=="Abajo"):
            b = tabajo(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,p))
            else:
                t.append((s,p))
            b = tderecha(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
            b = tizquierda(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
        elif(ac=="Derecha"):
            b = tderecha(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,p))
            else:
                t.append((s,p))
            b = tarriba(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
            b = tabajo(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
        elif(ac=="Izquierda"):
            b = tizquierda(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,p))
            else:
                t.append((s,p))
            b = tarriba(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
            b = tabajo(s)
            if(b in self.estados and b not in bloqueados):
                t.append((b,r))
            else:
                t.append((s,r))
        elif(ac=="exit"):
            t.append((s,0))
        if(self.r(s) in recompensa_finales or (s in bloqueados)):
            del t[:]
            t.append((s,0))
        return t
    def elimina_bloqueados(self):
        c = self.cuadricula
        fila = c[0]
        bloqueados = []
        for f in range(0,len(c)-1):
            for col in range(0,len(fila)-1):
                if(c[f][col] == '#'):
                    bloqueados.append((f,col))
        return bloqueados
    def bloq_y_termi(self):
        fila = self.cuadricula[0]
        bloq_o_ter = []
        for e0,e1 in self.estados:
            if(self.cuadricula[e0][e1] != ' ' and self.cuadricula[e0][e1]!='S'):
                bloq_o_ter.append((e0,e1))
        return bloq_o_ter

def creaEstados(l):
    estados = []
    f = len(l)
    c = len(l[0])
    for i in range(0,f):
        for j in range(0,c):
            estados.append((i,j))
    return estados

cTema4 = Cuadricula([],
 (0,0), 0.9, [['S',' ',' ',' '],
[' ','#',' ',-1], [' ',' ',' ',+1]] ,-0.04 , 0.2)
        
cTema4.estados = creaEstados(cTema4.cuadricula)

e1 = MDP([(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1),(0,2),(1,2),(2,2),(3,2)], (1,1), 0.8)

# def bloq_y_termi(pr):
#     fila = pr.cuadricula[0]
#     bloq_o_ter = []
#     for e0,e1 in pr.estados:
#         if(pr.cuadricula[e0][e1] != ' ' and pr.cuadricula[e0][e1]!='S'):
#             bloq_o_ter.append((e0,e1))
#     return bloq_o_ter
# #(c[f][col] == '#') or 
# def elimina_bloqueados(pr):
#     c = pr.cuadricula
#     fila = c[0]
#     bloqueados = []
#     for f in range(0,len(c)-1):
#         for col in range(0,len(fila)-1):
#             if(c[f][col] == '#'):
#                 bloqueados.append((f,col))
#     return bloqueados


def tarriba(s):
    return (s[0]+1,s[1])

def tabajo(s):
    return (s[0]-1,s[1])

def tderecha(s):
    return (s[0],s[1]+1)

def tizquierda(s):
    return (s[0],s[1]-1)


def iteracion_valores_k(proceso,k):
    v = {} #diccionario que recoge las valoraciones i
    val = {} #diccionario que recoge las valoraciones i+1
    #aux = {} #diccionario auxiliar del cual nos ayudamos para calcular el maximo
    for i in (proceso.estados):
        v[i] = 0 #valoraciones iniciales
    for i in range(0,k): #iteramos k veces
        for e in proceso.estados: #para cada estado
            aux = {} #diccionario auxiliar del cual nos ayudamos para calcular el maximo
            for a in proceso.a(e): #y para todas las acciones posibles
                tr = proceso.t(e,a) #miramos los posibles estados donde podemos llegar con su probabilidad
                suma = 0
                for t in tr: #cada t es el par (estado, probabilidad)
                    suma = suma + v[t[0]]*t[1] #vamos añadiendo a suma la multiplicacion de cada elemento del par
                aux[a] = suma 
            maximo = max(y for x,y in aux.items()) #calculamos maximo
            #print("estado", e , "maximo" , maximo)
            #print(aux)
            val[e] = proceso.r(e) + proceso.descuento*maximo #calculamos valoración
        v = copy.deepcopy(val)
    politica = calculaPolitica(proceso,val) #llamamos a funcion auxiliar calcula politica
    imprime_val(val,proceso)
    imprime_politica(politica,proceso) 
    return val,politica

def iteracion_valores_e(proceso,errorPermitido):
    v = {} #diccionario que recoge las valoraciones i
    val = {} #diccionario que recoge las valoraciones i+1
    #aux = {} #diccionario auxiliar del cual nos ayudamos para calcular el maximo
    errores = []
    for i in (proceso.estados):
        v[i] = 0
    error = 1e100 #comenzamos con un error muy grande para que entre la primera vez en el while
    b = float(proceso.descuento)
    errorMaximo = errorPermitido*(1-proceso.descuento)/proceso.descuento #aplicamos la formulita de las diapositivas
    while(error > float(errorMaximo)): #mientras se cumpla la condicion
        error = 0 #en cada iteracion comenzamos con el error a cero, y calcularemos cual es el maximo error
        errores = []
        for e in proceso.estados: #para cada estado
            aux = {} #diccionario auxiliar del cual nos ayudamos para calcular el maximo
            for a in proceso.a(e): #y para todas las acciones posibles
                tr = proceso.t(e,a) #miramos los posibles estados donde podemos llegar con su probabilidad
                suma = 0
                for t in tr: #cada t es el par (estado, probabilidad)
                    suma = suma + v[t[0]]*t[1] 
                aux[a] = suma
            maximo = max(y for x,y in aux.items()) #calculamos el maximo
            val[e] = proceso.r(e) + proceso.descuento*maximo #almacenamos su valoracion
            er = abs(val[e] - v[e]) #calculamos el error de ese estado
            errores.append(er) # y lo almacenamos en una lista para luego ver el error más grande
        error = max(errores) 
        v = copy.deepcopy(val)
        print(error)
    print(val)
    politica = calculaPolitica(proceso,val) #llamamos a calculaPolitica, que es una funcion auxiliar la cual 
                                            #pasandole una valoración te devuelve la política optima
    imprime_val(val,proceso)
    imprime_politica(politica,proceso) #imprimimos la politica
    return val,politica


def calculaPolitica(proceso,val): 
    print(val)
    #aux = {} #diccionario auxiliar para guardarnos las sumas de las distintas acciones
    politica = {} #diccionario donde almacenaremos las politicas
    for e in proceso.estados: #para cada estado
            aux = {} #diccionario auxiliar para guardarnos las sumas de las distintas acciones
            for a in proceso.a(e): #y para todas las acciones posibles
                tr = proceso.t(e,a) #miramos los posibles estados donde podemos llegar con su probabilidad
                suma = 0
                for t in tr:
                    suma = suma + val[t[0]]*t[1] #calculamos la suma para cada accion
                aux[a] = suma
            maximo = -1e100
            for x,y in aux.items():
                if(y>maximo): #calculamos el máximo, y la accion de dicho maximo
                    maximo = y
                    acc = x
            politica[e] = acc #almacenamos en política la accion
    return politica

def iteracion_politica(proceso,k):
    acciones = proceso.a(proceso.estado_inicial) #todas las acciones posibles excepto exit
    #print(acciones)
    polInicial = {} #aqui almacenamos politica aleatoria inicial
    polFinal = {} #será la politica final
    v = {}
    val = {}
    aux = {}
    for e in proceso.estados:
        polInicial[e] = random.choice(acciones) #politica aleatoria inicial, en los estados terminales tendremos una accion
                                #del tipo arriba, abajo,... pero como no cambian no importa, la cambiamos por exit al final
    for e in proceso.estados:
        v[e] = 0 #valoracion inicial
    actualiza = True #Para que entre la primera vez en el while
    #print(polInicial)
    polFinal = copy.deepcopy(polInicial) #copia para que la primera vez no este vacia
    while(actualiza!=False):
        polInicial = copy.deepcopy(polFinal) 
        print("Esta es la pol inicial cada vez",polInicial)#copia para las iteraciones
        #print(polInicial)
        for i in range(0,k): #iteramos k veces para el calcula de la valoracion
            for e in proceso.estados:
                accionAntigua = polInicial[e] #accion de la politica antigua
                tr = proceso.t(e,accionAntigua) #transicion de la politica antigua
                suma = 0 #inicializamos la suma
                for t in tr:
                    suma = suma + v[t[0]]*t[1] #para cada elemento de la transicion vamos actualizando suma
                #print("La suma con la accion antigua para el estado ", e, "es ",suma)
                val[e] = proceso.r(e) + proceso.descuento * suma #calculamos la nueva valoracion
            v = copy.deepcopy(val) #copiamos val como v, para poder seguir iterando
        #print("La valoracion actual es" ,val)
            ##Aqui ya tenemos en val las Vpi despues de iterar las k veces
        actualiza = False #lo ponemos a false
        print('val final', val)
        #print(actualiza)
        for e in proceso.estados: #para cada estado
            aux = {} #diccionario auxiliar donde vamos almacenando todas las sumas
            for a in acciones: #y para todas las acciones posibles
                #print("estado " , e, "accion ",a) 
                tr = proceso.t(e,a) #miramos los posibles estados donde podemos llegar con su probabilidad
                suma = 0
                for t in tr: 
                    suma = suma + val[t[0]]*t[1] #recorriendo la transicion calculamos la suma
                aux[a] = suma # y lo almacenamos en un diccionario auxiliar
                #print("Estamos en la transicion del estado " , e, "-->", tr)
                #print("La suma para la accion ", a , "es ", suma)
            print("Cada suma de las 4 acciones anteriores son ", aux)
            maximo = max(y for x,y in aux.items()) #calculamos el maximo de todas las posibles acciones
            trAnt = proceso.t(e,polInicial[e]) #probabilidad con la politica antigua que estamos comparando
            #print(trAnt)
            #print("estado ", e, "accionAntigua" ,polInicial[e] )
            sumaAnt = 0
            for t in trAnt: 
                sumaAnt = sumaAnt + val[t[0]]*t[1] #recorriendo la transicion calculamos la suma
            # print("La suma de la accion antigua, ",polInicial[e], " es ", sumaAnt)
            # #val[e] = rec(e) + proceso.descuento * maximo
            # print("El actual maximo de", e ,"es ",maximo)
            # print("El actual sumaAnt de", e ,"es ",sumaAnt)
            # print("Mi actual politica es ",polInicial[e] )
            if(maximo>sumaAnt): # y si la politica del maximo es mejor que la antigua, la cambiamos
                for x,y in aux.items():
                    if(y==maximo):
                        acc = x 
                        #print("Mi nueva politica es ",acc)
                        actualiza = True #avisamos de que hemos cambiado
                        polFinal[e] = acc #cambiamos la politica
            #print(actualiza)
        v = copy.deepcopy(val) #copiamos val para seguir iterando
        polInicial = copy.deepcopy(polFinal)
        #print(actualiza)
    byq = proceso.bloq_y_termi() # en las 3 lineas siguientes, cambiamos la accion inicial para los estados terminales por exit
    for e in byq:
        polFinal[e] = 'exit'
    imprime_val(val,proceso)
    imprime_politica(polFinal,proceso) #imprimimos la politica
    return val,polFinal


def imprime_politica(pol,proc):
    n=len(proc.cuadricula) #numero de filas de la cuadricula
    tamFila = len(proc.cuadricula[0]) #numero de columnas
    while(n>0): #imprimimos cada fila desde la ultima a la primera para que esten bien representadas como nos dicen
        cadena = " |"
        for c in range(0,tamFila): 
            cadena += pol[(n-1,c)] + " | " #añadimos a cadena la politica de la fila n y columna c
        print(("|"+"-"*(8*tamFila-1)+"|")) #separacion entre filas
        print(cadena)
        n = n-1 #disminuimos n para acabar saliendo del while
    print(("|"+"-"*(8*tamFila-1)+"|")) 

def imprime_val(val,proc):
    n=len(proc.cuadricula) #numero de filas de la cuadricula
    tamFila = len(proc.cuadricula[0]) #numero de columnas
    while(n>0): #imprimimos cada fila desde la ultima a la primera para que esten bien representadas como nos dicen
        cadena = " |"
        for c in range(0,tamFila): 
            cadena += str(val[(n-1,c)]) + " | " #añadimos a cadena la politica de la fila n y columna c
        print(("|"+"-"*(8*tamFila-1)+"|")) #separacion entre filas
        print(cadena)
        n = n-1 #disminuimos n para acabar saliendo del while
    print(("|"+"-"*(8*tamFila-1)+"|")) 




cuadriculaPuente = Cuadricula([], (1,1), 0.9, 
                            [['#',-100,-100,-100,-100,-100,'#'],
                            [+1,'S',' ',' ',' ',' ',+10],
                            ['#',-100,-100,-100,-100,-100,'#']] , -0.04 ,0.01)

cuadriculaPuente.estados = creaEstados(cuadriculaPuente.cuadricula)

cuadriculaPrecipicio = Cuadricula([], (1,0), 0.9, 
                            [[-100,-100,-100,-100,-100],
                            ['S',' ',' ',' ',+10],
                            [' ',' ',' ',' ',' ']] , -0.04 , 0.2)

cuadriculaPrecipicio.estados = creaEstados(cuadriculaPrecipicio.cuadricula)

cuadriculaLaberinto = Cuadricula([], (0,0), 0.9, 
                            [['S',' ',' ',' '],
                            [' ','#','#',' '],
                            [' ','#',' ',' '],
                            ['#','#',' ','#'],
                            [' ',' ',' ',1]] , -0.04 , 0.2)

cuadriculaLaberinto.estados = creaEstados(cuadriculaLaberinto.cuadricula)

cuadriculaDescuento = Cuadricula([], (1,0), 0.6, 
                            [[-10,-10,-10,-10,-10],
                            ['S',' ',' ',' ',' '],
                            [' ','#',1,'#',10],
                            [' ','#',' ',' ',' '],
                            [' ',' ',' ',' ',' ']], -1.5 , 0.3)

cuadriculaDescuento.estados = creaEstados(cuadriculaDescuento.cuadricula)

miCuadricula = Cuadricula([], (1,0), 0.8, 
                            [[' ',' ','S',' ',' '],
                            [' ',-20,'#',1,' '],
                            [' ',-20,' ',' ',' '],
                            [' ',-20,' ',' ',35],
                            [' ',100,' ',' ',' '],
                            [-100,-100,-100,-100,-100]], -0.04, 0.8)

miCuadricula.estados = creaEstados(miCuadricula.cuadricula)

miCuadriculaLaberinto = Cuadricula([], (1,0), 0.9, 
                            [[' ','S',' ',-10 ,5, ' '],
                            [' ',-10,' ',-10,' ', 2],
                            [1,-10,' ',' ',' ', ' '],
                            [' ',' ',-10,-10,-10, ' '],
                            [1000,-10,' ',-20,-20, ' '],
                            [' ',-10,' ',' ',' ', ' ']], -0.04, 0.2)

miCuadriculaLaberinto.estados = creaEstados(miCuadriculaLaberinto.cuadricula)

# a)Calcular las políticas optimas que aparecen en las diapositivas del tema 4 y comprobar que salen
#iguales a las que se muestran

#Las valoraciones del tema 4 son: 

# |-------------------------------|
#  |0.812 | 0.868 | 0.918 | 1.0 | 
# |-------------------------------|
#  |0.762 | 0 | 0.660 | -1.0 | 
# |-------------------------------|
#  |0.705 | 0.655 | 0.611 | 0.388 | 
# |-------------------------------|

#Mientras que las valoraciones que obtenemos con los algoritmos implementados son:

# |-----------------------------------------------------------------------------------|
#  |0.8115582191780822 | 0.8678082191780823 | 0.9178082191780822 | 1.0 | 
# |-----------------------------------------------------------------------------------|
#  |0.7615582191780823 | 0 | 0.6602739726027398 | -1.0 | 
# |-----------------------------------------------------------------------------------|
#  |0.7053082191780823 | 0.6553082191780822 | 0.6114155251141552 | 0.3879249112125825 | 
# |-----------------------------------------------------------------------------------|

#Como podemos observar, son las mismas.

# b)En el caso de la cuadrícula puente, dar varios ejemplos de políticas que se pueden obtener con distintos
# valores de los parámetros
# descuento = 0.9
# rec = -0.04
# ruido = 0.2

# |-------------------------------------------------------|
#  |exit | exit | exit | exit | exit | exit | exit | 
# |-------------------------------------------------------|
#  |exit | Izquierda | Izquierda | Derecha | Derecha | Derecha | exit | 
# |-------------------------------------------------------|
#  |exit | exit | exit | exit | exit | exit | exit | 
# |-------------------------------------------------------|

#Si existe un poco de ruido, aun con la recompensa pequeña, no conviene cruzar el puente.
#En cambio:

# descuento = 0.9
# rec = -0.00001
# ruido = 0.01

# |-------------------------------------------------------|
#  |exit | exit | exit | exit | exit | exit | exit | 
# |-------------------------------------------------------|
#  |exit | Derecha | Derecha | Derecha | Derecha | Derecha | exit | 
# |-------------------------------------------------------|
#  |exit | exit | exit | exit | exit | exit | exit | 
# |-------------------------------------------------------|
#Si ponemos una recompensa muy muy pequeña y un ruido casi 0, es decir que nunca se equivoque, si nos conviene
#cruzar el puente ya que no nos caeremos.

#Asi y todo, el problema no esta en la recompensa, esta solo en el ruido. Si los parametros por defecto(descuento = 0.9,
    #rec=-0.04, ruido = 0.2), modificamos solo el ruido y lo ponemos muy pequeño (r=0.01), ya si nos conviene cruzar el puente,
    #ya que no tenemos apenas riesgo de caernos.

# c)Las mismas experimentaciones para la cuadrícula precipicio, en las que para ciertos valores de los
# parametros se aconseje ir pegado al precipicio y para otros valores se aconseje alejarse del precipicio.

# Con los parametros por defecto, nos aconsejan alejarnos del precipicio, ya que no penalizamos mucho la tardanza en 
# llegar al punto terminal

# descuento = 0.9
# rec = -0.04
# ruido = 0.2

# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | Arriba | Arriba | Arriba | exit | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

#En cambio si aumentamos la rec y el descuento para penalizar más el tiempo, y disminuimos un poco el ruido, obtenemos
#la recomendación de cruzar el puente.

# descuento = 1
# rec = -8
# ruido = 0.1

# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | exit | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

#Si intentaramos que cambiando un único parámetro se pasara de alejarse del precipicio a no alejarse, nos basta con 
#cambiar de los parametros por defecto, la recompensa desde -0.04 hasta un valor bastante más pequeño, como -15

# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | exit | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

# d) En la cuadrícula del laberinto, lo normal es que la política aconseje acciones que apuntan hacia la
# salida. Comprobarlo para algunos valores de los parametros, y tratar tambien de buscar valores de los
# parametros que aconsejen algo distinto.

# Con los parámetros por defecto, la política nos aconseja salir del laberinto por su única salida:

# |-------------------------------|
#  |Derecha | Derecha | Derecha | exit | 
# |-------------------------------|
#  |exit | exit | Arriba | exit | 
# |-------------------------------|
#  |Abajo | exit | Arriba | Izquierda | 
# |-------------------------------|
#  |Abajo | exit | exit | Arriba | 
# |-------------------------------|
#  |Derecha | Derecha | Derecha | Arriba | 
# |-------------------------------|

# Si cambiamos estos parametros, a descuento = 0.5 , rec = -1 penalizando un poco más y el ruido = 0.4 , 
# obtenemos una politica que no consigue salir del laberinto

# |-------------------------------|
#  |Derecha | Derecha | Derecha | exit | 
# |-------------------------------|
#  |exit | exit | Derecha | exit | 
# |-------------------------------|
#  |Abajo | exit | Arriba | Arriba | 
# |-------------------------------|
#  |Abajo | exit | exit | Arriba | 
# |-------------------------------|
#  |Derecha | Derecha | Derecha | Arriba | 
# |-------------------------------|


# e) En la cuadrícula descuento, dar valores de los parametros para los que las políticas optimas sugieran
# los siguientes tipos de caminos:

#           1)Preferir salir por +1, evitando el precipicio (estados -10)
#     descuento = 0.6
#     rec = -1.5
#     ruido = 0.3

# |---------------------------------------|
#  |Derecha | Derecha | Abajo | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | Abajo | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Arriba | Derecha | Arriba | Derecha | Arriba | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

#             2) Preferir salir por +1, arriesgandose a pasar cerca del precipicio
#         descuento = 0.9
#         rec = -4
#         ruido = 0.2

# |---------------------------------------|
#  |Arriba | exit | Abajo | Derecha | Abajo | 
# |---------------------------------------|
#  |Abajo | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Derecha | Derecha | Arriba | Derecha | Arriba | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

#             3) Preferir salir por +10, evitando el precipicio
#         (Parametros por defecto)
#         descuento = 0.9
#         rec = -0.04
#         ruido = 0.2

# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Arriba | Arriba | Derecha | Derecha | Arriba | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

#             4)Preferir salir por +10, arriesgandose a pasar cerca del precipicio

#         descuento = 0.9
#         rec = -1
#         ruido = -0.2

# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | Derecha | Derecha | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Derecha | Derecha | Derecha | Derecha | Arriba | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|


#             5) Evitar ambas salidas, y el precipicio.
#         descuento = 0.5
#         rec = -4
#         ruido = 0.5
# |---------------------------------------|
#  |Derecha | Derecha | Abajo | Abajo | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | Abajo | Derecha | Abajo | 
# |---------------------------------------|
#  |Abajo | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Arriba | Arriba | Arriba | Arriba | Arriba | 
# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|

#     Con estos valores se queda bloqueado, de abajo a arrriba y de arriba a abajo

# f)Se pide ademas inventar una cuadrícula, y mostrar políticas distintas en esa cuadrícula, dependiendo
# del valor de los parametros. Se valorara que el ejemplo sea interesante y novedoso respecto de los
# anteriores ejemplos.

# Yo he propuesto la siguiente cuadrícula:

# |---------------------------------------|
#  |-100 | -100 | -100 | -100 | -100 | 
# |---------------------------------------|
#  |     | 100 |       |      |      | 
# |---------------------------------------|
#  |    | -20 |        |      |  35  | 
# |---------------------------------------|
#  |    | -20 |       |      |      | 
# |---------------------------------------|
#  |    | -20 |   #  |   1   |      | 
# |---------------------------------------|
#  |    |     |  S  |       |        | 

# Lo he querido enfocar como un juego de televisión, en el cual si aciertas 2 preguntas pudiendo fallar consigues 1 punto.
# Si quieres, te puedes arriesgar a contestar 6 para ganar 35 puntos pudiendo fallar 2 preguntas antes de perder(caer al -20).
# Otra opcion es responder 7 preguntas sin opción a fallo para ganar 100. La última, también para ganar 100 puntos sería 
# contestar 9 preguntas pudiendo fallar alguna.

# Con los parámetros por defecto, obtenemos que el concursante prefiere responder las 9 preguntas, fallando algunas, 
# para buscar los 100 puntos.

# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Derecha | exit | Izquierda | Izquierda | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Izquierda | exit | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Arriba | Izquierda | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | Arriba | 
# |---------------------------------------|
#  |Arriba | Izquierda | Derecha | Derecha | Arriba | 
# |---------------------------------------|

# Si disminuimos el ruido(preguntas más faciles), el concursante prefiere las 7 sin poder fallar para buscar los 100 puntos.

# descuento = 0.9
# rec = -0.04
# ruido = 0.1

# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Derecha | exit | Izquierda | Izquierda | Izquierda | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Izquierda | exit | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Arriba | Izquierda | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | Arriba | 
# |---------------------------------------|
#  |Arriba | Izquierda | Izquierda | Derecha | Arriba | 
# |---------------------------------------|

# Si disminuimos el descuento a 0.5 y la recompensa a -1 dejando el ruido a 0.1, el concursante se conformaría con 
# los 35 puntos.

# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Derecha | exit | Izquierda | Izquierda | Abajo | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Derecha | exit | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Arriba | Arriba | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | Arriba | 
# |---------------------------------------|
#  |Arriba | Izquierda | Derecha | Derecha | Arriba |


# Por ultimo, en el juego por cada pregunta respondida se descontara muchos puntos(rec) , el concursante preferiria 
# ganar un punto a arriesgarse a fallar. En nuestro ejemplo, exagerando con una recompensa a -10, y dejando igual tanto
# ruido con descuento, obtenemos este resultado.

# |---------------------------------------|
#  |exit | exit | exit | exit | exit | 
# |---------------------------------------|
#  |Derecha | exit | Izquierda | Izquierda | Izquierda | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Izquierda | exit | 
# |---------------------------------------|
#  |Arriba | exit | Arriba | Arriba | Arriba | 
# |---------------------------------------|
#  |Arriba | exit | exit | exit | Arriba | 
# |---------------------------------------|
#  |Arriba | Izquierda | Derecha | Arriba | Arriba | 
# |---------------------------------------|

# --------
# Mi cuadriculaLaberinto:

# |-----------------------------------------------|
#  |       |      |       |      |      |         | 
# |-----------------------------------------------|
#  |1000   | -10  |       | -20  | -20  |         | 
# |-----------------------------------------------|
#  |       |      |  -10   | -10  | -10  |         | 
# |-----------------------------------------------|
#  |  1    |-10   |       |      |      |         | 
# |-----------------------------------------------|
#  |       | -10  |       |  -10 |      |   2     | 
# |-----------------------------------------------|
#  |       |  S   |       |  -10 |  5   |         | 
# |-----------------------------------------------|


# Respecto a mi cuadricula laberinto, es casi imposible llegar hasta el 1000, el hecho de tener tantos terminales negativos
# por el camino, hacen que la politica nunca se atreva a caer en uno de ellos, y prefiere no recorrer el laberinto completo.

# Con los parámetros por defecto, nos quedamos en el +1: 

# |-----------------------------------------------|
#  |Izquierda | exit | Derecha | Arriba | Derecha | Abajo | 
# |-----------------------------------------------|
#  |exit | exit | Arriba | exit | exit | Derecha | 
# |-----------------------------------------------|
#  |Arriba | Izquierda | exit | exit | exit | Abajo | 
# |-----------------------------------------------|
#  |exit | exit | Derecha | Derecha | Abajo | Izquierda | 
# |-----------------------------------------------|
#  |Arriba | exit | Arriba | exit | Abajo | exit | 
# |-----------------------------------------------|
#  |Arriba | Izquierda | Arriba | exit | exit | Izquierda | 
# |-----------------------------------------------|


# Aún estableciendo una recompensa y ruido casi nulo, la política se conforma con el +5

# |-----------------------------------------------|
#  |Abajo | exit | Derecha | Derecha | Derecha | Abajo | 
# |-----------------------------------------------|
#  |exit | exit | Arriba | exit | exit | Abajo | 
# |-----------------------------------------------|
#  |Arriba | Izquierda | exit | exit | exit | Abajo | 
# |-----------------------------------------------|
#  |exit | exit | Derecha | Derecha | Abajo | Izquierda | 
# |-----------------------------------------------|
#  |Abajo | exit | Arriba | exit | Abajo | exit | 
# |-----------------------------------------------|
#  |Derecha | Derecha | Arriba | exit | exit | Izquierda | 
# |-----------------------------------------------|



def estima_valor_muestreo(e,pol,proceso,n):
    c = proceso.cuadricula #cuadricula del proceso al que hacemos referencia
    #acciones = proceso.a(proceso.estado_inicial) 
    #i = 0
    valFinal = 0 #variable donde almacenamos la valoración final
    secuenciasDistintas = [] #lista para no repetir secuencias
    for i in range(n):
        print("He comprobado ya ", i , " secuencias")
        secuencia = [] #lista donde almacenar cada secuencia
        secuencia.append(e) 
        print("comenzamos a buscar una nueva secuencia")
        estado_inicial = e
        estado = estado_inicial #para que entre la primera vez
        val = proceso.r(e) #valoracion del estado inicial
        print("comenzamos con val = ", val)
        iteracion = 1  #nos ayudamos de esta variable para poder elevar el descuento según la iteracion
        probabilidad = 1 #inicializamos la probabilidad
        while(c[estado[0]][estado[1]]==' ' or c[estado[0]][estado[1]]=='S'): #condicion hasta llegar a un estado terminal
            estados_a_elegir = [] 
            print("estado inicial: ",estado_inicial)  
            transicion = proceso.t(estado_inicial,pol[estado_inicial]) #la transicion del estado actual segun la politica
            for a in transicion:
                p = int(a[1]*10)
                for i in range(0,p):
                    estados_a_elegir.append(a) #introducimos tantos elementos como diga su prob, para que sea mas real
            print("los estados a elegir son ",estados_a_elegir)
            t = random.choice(estados_a_elegir) #elegimos un estado al alzar, respetando la probabilidad
            estado = t[0]
            secuencia.append(estado) #vamos almacenando los distintos estados por los que pasamos
            probabilidad = probabilidad * t[1] #actualizamos la probabilidad
            print("la probabilidad de llegar al nuevo estado", t[0], " es: ", t[1])
            val = val + proceso.r(estado)*pow(proceso.descuento,iteracion) #actualizamos la valoracion de esa secuencia
            print("Estoy en el estado ", estado , "en la iteracion ",iteracion)
            print("mi val actual es, " ,val)
            iteracion+=1
            estado_inicial = copy.deepcopy(estado) #copiamos el estado a estado inicial para poder realizar la siguiente iteracion
        if(secuencia not in secuenciasDistintas): #solo consideramos la secuencia si no la hemos considerado antes
            secuenciasDistintas.append(secuencia)
            print("He obtenido una valoracion de " , val, " con una probabilidad de ", probabilidad)
            valFinal = valFinal + val*probabilidad #si aun no la hemos tenido en cuenta, se la sumamos a la val final por su probabilidad
            print("mi actual valoracionFinal es ",valFinal)
    print("Todas estas han sido las secuencias distintas " , secuenciasDistintas, " con tamaño ",len(secuenciasDistintas))
    return valFinal

val = {(1, 2): 0.0, (3, 2): 38.45901458326267, (0, 0): 11.645339568840706, (5, 0): -100.0, (3, 0): 39.33517495395949, (0, 4): 13.519701139733575, (5, 4): -100.0, (1, 4): 18.316009419694705, (1, 3): 1.0, (2, 3): 22.567780719328635, (2, 1): -20.0, (2, 4): 26.266763540811183, (4, 2): 59.03672116666102, (1, 0): 16.01286349378758, (0, 3): 9.448487749379607, (4, 0): 59.10681399631676, (0, 1): 6.318497091367447, (3, 3): 28.943912957495417, (4, 1): 100.0, (3, 1): -20.0, (5, 2): -100.0, (4, 4): 27.09208822463154, (0, 2): 7.151228761431339, (2, 0): 25.580991272319647, (4, 3): 32.05901458326267, (2, 2): 24.779191790834403, (5, 1): -100.0, (5, 3): -100.0, (3, 4): 35.0, (1, 1): -20.0}


pol = {(1, 2): 'exit', (3, 2): 'Arriba', (0, 0): 'Arriba', (5, 0): 'exit', (3, 0): 'Arriba', (0, 4): 'Arriba', (5, 4): 'exit', (1, 4): 'Arriba', (1, 3): 'exit', (2, 3): 'Arriba', (2, 1): 'exit', (2, 4): 'Arriba', (4, 2): 'Izquierda', (1, 0): 'Arriba', (0, 3): 'Derecha', (4, 0): 'Derecha', (0, 1): 'Izquierda', (3, 3): 'Izquierda', (4, 1): 'exit', (3, 1): 'exit', (5, 2): 'exit', (4, 4): 'Abajo', (0, 2): 'Derecha', (2, 0): 'Arriba', (4, 3): 'Izquierda', (2, 2): 'Arriba', (5, 1): 'exit', (5, 3): 'exit', (3, 4): 'exit', (1, 1): 'exit'}



# la cuadricula (miCuadricula) con las valoraciones de los algoritmos implementados sería:

# >>> imprime_val(val,miCuadricula)

# |-------------------------------------------------------------------------------------------------------|
#  |-100.0             | -100.0            | -100.0             | -100.0             | -100.0             | 
# |-------------------------------------------------------------------------------------------------------|
#  |59.10681399631676  | 100.0             | 59.03672116666102  | 32.05901458326267  | 27.09208822463154  | 
# |-------------------------------------------------------------------------------------------------------|
#  |39.33517495395949  | -20.0             | 38.45901458326267  | 28.943912957495417 | 35.0               | 
# |-------------------------------------------------------------------------------------------------------|
#  |25.580991272319647 | -20.0             | 24.779191790834403 | 22.567780719328635 | 26.266763540811183 | 
# |-------------------------------------------------------------------------------------------------------|
#  |16.01286349378758  | -20.0             | 0.0                | 1.0                | 18.316009419694705 | 
# |-------------------------------------------------------------------------------------------------------|
#  |11.645339568840706 | 6.318497091367447 | 7.151228761431339  | 9.448487749379607  | 13.519701139733575 | 
# |-------------------------------------------------------------------------------------------------------|

# >>> estima_valor_muestreo((2,0),pol,miCuadricula,1000) 

# 25.569533215318845

#con el estado (0,2) no nos hace falta muchas iteraciones, ya que tiene pocas secuencias distintas que hacer.

#en cambio, si lo buscamos con un estado con "mas libertad", si necesitamos muchas iteraciones:

# >>> estima_valor_muestreo((0,2),pol,miCuadricula,10000)

# 6.483337721049723

# >>> estima_valor_muestreo((0,3),pol,miCuadricula,30000)

# 9.421215225554436


# Probemos ahora con la cuadricula del tema 4
#Las valoraciones del tema 4 son: 

# |-------------------------------|
#  |0.812 | 0.868 | 0.918 | 1.0 | 
# |-------------------------------|
#  |0.762 | 0 | 0.660 | -1.0 | 
# |-------------------------------|
#  |0.705 | 0.655 | 0.611 | 0.388 | 
# |-------------------------------|

#Vamos a probar ahora algunos de los estados de la cuadricula del tema 4:

# >>> estima_valor_muestreo((2,2),pol,cTema4,1000)

# 0.9161189836800002

# >>> estima_valor_muestreo((2,0),pol,cTema4,10000)

# 0.7167020893298692

# >>> estima_valor_muestreo((1,2),pol,cTema4,15000)

# 0.6597178284800003



