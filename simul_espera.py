 #-*- coding:utf-8 -*-

import math, random, time

# Maquina_i = [estado, T_llegada]
# Mecanico_i = [estado, T_inactividad, T_ini_inactividad]
# estado = 0: si el Mecanico_i está desocupado
# estado = K > 0: si está atendiendo a la máquina K
# T_inactividad = Tiempo acumulado de inactividad del Mecanico_i
# T_inactividad = reloj - T_ini_inactividad
# T_ini_inactividad = Tiempo en que el Mecanico_i comenzó el
# último período de inactividad
# Matriz de Eventos Futuros (MEF):
#    Evento             T_evento        Entidad     Tipo
# 0. Fin_Simulacion     T_simulacion    -           1
# 1. Llegada_Maquina    T_llegada       Maquina_i   2  
# 2. Fin_Servicio       T_Servicio      Mecanico_i  3
# 3. ...

class SFM: # Simulación de Fallas de un conjunto de Máquinas
    def __init__(self, reloj, cap_max_sistema, N_Mecanicos):
        global MEF
        self.reloj = reloj
        self.cap_max_sistema = cap_max_sistema
        self.N_Mecanicos = N_Mecanicos
        
        # Inicialización del estado del sistema
        self.N_Maquinas_sistema = 0
        self.N_Maquinas_cola = 0
        self.N_Mecanicos_ocupados = 0
        self.Maquinas = {}
        self.Mecanicos = {}
        self.COLA_Maquinas = []
        self.COLA_Mecanicos = []
        for i in range(self.N_Mecanicos):
            self.COLA_Mecanicos.append(i+1)
            Mecanico_i = [0, 0, reloj]
            self.Mecanicos[i+1]= Mecanico_i
        print "Inicializacion" + "\n"
        print "COLA_Mecanicos: " + str(self.COLA_Mecanicos)
        print "Mecanicos: " + str(self.Mecanicos)
        
        # Inicialización de lista de eventos
        MEF = [] # Matriz de Eventos Futuros
        Evento_1 = [T_simulacion, None, 1]
        MEF.append(Evento_1)

        # Primera llegada
        self.T_llegada = 0
        Evento_2 = [self.T_llegada + self.reloj, 1, 2]
        MEF.append(Evento_2)
        self.N_eventos = 2 # Fin_Simulacion y Llegada_Maquina
        print "MEF: " + str(MEF)

        # Inicialización de estadísticas
        self.Tot_t_cola = 0
        self.Tot_t_sistema = 0
        self.T_Maquinas_sistema = 0
        self.T_Maquinas_cola = 0
        self.T_Mecanicos_ocupados = 0
        self.Tot_Maquinas_atendidas = 0
        self.Tot_Maquinas_esperando = 0

    def proximo_evento(self):
        global MEF, Min
        # Búsqueda próximo evento
        T_Eventos = []
        #Penultimo_evento = MEF[len(MEF)-1]
        for i in MEF[len(MEF)-1:len(MEF)]:
            T_Eventos.append(i[0])
        T_min_Eventos = min(T_Eventos)
        for i in range(len(MEF)):
            if MEF[i][0] <= T_min_Eventos:
                Min = i
        delta_t = MEF[Min][0] - self.reloj
        self.T_Maquinas_sistema += self.N_Maquinas_sistema * delta_t
        self.T_Maquinas_cola += self.N_Maquinas_cola * delta_t
        self.T_Mecanicos_ocupados += self.N_Mecanicos_ocupados * delta_t
        print "proximo_evento" + "\n"
        print """
        T_Maquinas_sistema = {}
        T_Maquinas_cola = {}
        T_Mecanicos_ocupados = {}
        Min: {}
        """.format(self.T_Maquinas_sistema, self.T_Maquinas_cola,self.T_Mecanicos_ocupados,Min)

    def llegada(self):
        global MEF, Min
        # Identificación de la Máquina
        Maquina_i = MEF[Min][1]

        # Programación próxima llegada
        r1 = random.random(); 
        self.T_llegada += round(-150 * math.log(r1), 2) # T_llegada = T_llegada_ant + t que tarda en llegar -> Generar
        Nuevo_Evento = [self.T_llegada + self.reloj, Maquina_i + 1, 2]
        MEF.append(Nuevo_Evento)

        # Verificación si la máquina puede entrar
        if (self.N_Maquinas_sistema < self.cap_max_sistema):
            # Verificación si la máquina puede ser atendida
            if (self.N_Mecanicos_ocupados < self.N_Mecanicos):
                Mecanico_i = self.COLA_Mecanicos[0] # selección de un mecánico
                self.N_Mecanicos_ocupados += 1
                N_Mecanicos_inactivos = self.N_Mecanicos - self.N_Mecanicos_ocupados
                # Reorganización cola de Mecánicos Inactivos
                if (N_Mecanicos_inactivos > 0):
                    self.COLA_Mecanicos = self.COLA_Mecanicos[1:] # Un mecánico sale de la inactividad
                T_ini_inactividad = self.Mecanicos[Mecanico_i][2]
                self.Mecanicos[Mecanico_i] = [Maquina_i, reloj - T_ini_inactividad, T_ini_inactividad]
                r2 = random.random();
                T_servicio = round(-15 * math.log(r2), 2) # -> Generar
                self.N_eventos += 1 # ????
                Nuevo_Evento = [T_servicio + self.reloj, Mecanico_i, 3]
                MEF.append(Nuevo_Evento)
                Maquina_i_estado = 2 # Maquina_i en servicio
            else:
                self.N_Maquinas_cola += 1 
                self.COLA_Maquinas.append(Maquina_i) # La máquina pasa al último puesto de la cola
                Maquina_i_estado = 1 # Maquina_i en cola

            self.N_Maquinas_sistema += 1
            self.Maquinas[Maquina_i] = [Maquina_i_estado, self.reloj]
        print "llegada" + "\n"
        print """
        MEF = {}
        COLA_Mecanicos = {}
        COLA_Maquinas = {}
        Mecanicos = {}
        Maquinas = {}
        """.format(MEF,self.COLA_Mecanicos,self.COLA_Maquinas,self.Mecanicos,self.Maquinas)

    def fin_servicio(self):
        global MEF, Min
        # Identificación de Mecánico y Máquina
        Mecanico_i = MEF[Min][1]
        Maquina_i = self.Mecanicos[Mecanico_i][0]
        self.Tot_Maquinas_atendidas += 1
        self.Tot_t_sistema += self.reloj - self.Maquinas[Maquina_i][1]

        # Reorganización Máquinas
        del self.Maquinas[Maquina_i]
        self.N_Maquinas_sistema -= 1

        # Si hay Máquinas en cola, se escoje una
        if (self.N_Maquinas_cola > 0):
            Maquina_i = self.COLA_Maquinas[0]
            self.N_Maquinas_cola -= 1
            # Reorganización Máquinas en cola
            self.COLA_Maquinas = self.COLA_Maquinas[1:]

            self.Tot_t_cola += self.reloj - self.Maquinas[Maquina_i][1]
            self.Tot_Maquinas_esperando += 1
            self.Mecanicos[Mecanico_i][0] = Maquina_i
            self.Maquinas[Maquina_i][0] = 2 # Estado en servicio
            r2 = random.random();
            T_servicio = round(-15 * math.log(r2), 2) # -> Generar
            MEF[Min][0] = self.reloj + T_servicio
        else:
            self.N_Mecanicos_ocupados -= 1
            #N_Mecanicos_inactivos = self.N_Mecanicos - self.N_Mecanicos_ocupados
            self.COLA_Mecanicos.append(Mecanico_i)
            self.Mecanicos[Mecanico_i][0] = 0
            self.Mecanicos[Mecanico_i][2] = self.reloj
            if (Min < len(MEF)):
                fila = MEF[Min]
                MEF.remove(fila)
            self.N_eventos -= 1
        print "fin_servicio" + "\n"
        print """
        MEF: {}
        Maquinas: {}
        Mecanicos: {}
        """

if __name__ == "__main__":
    reloj = 0; T_simulacion = 10; cap_max_sistema = 21; N_Mecanicos = 3
    MEF = []; Min = 0 # Posición Evento más próximo
        
    inicializar = SFM(reloj, cap_max_sistema, N_Mecanicos); n = 0
    #while (reloj <= T_simulacion):
    while (n <= 2):
        inicializar.proximo_evento()
        reloj = MEF[Min][0]
        Tipo_evento = MEF[Min][2]
        if (Tipo_evento == 2):
            inicializar.llegada()
        elif (Tipo_evento == 3):
            inicializar.fin_servicio()
        print "reloj: " + str(reloj)
        n += 1
