from enum import Enum

import control as control

import legendre as legendre
import butterworth as butterworth
import cauer as cauer
import cheby1 as cheby1
import cheby2 as cheby2
import gauss as gauss
from scipy import signal
import numpy as np


#implementar un diccionario
##vamos a tener que usar un container para mandar todos los datos
class template():
    def __init__(self,type,approximation,data):
        #type
        self.type=type
        self.approximation=approximation
        #building specs
        self.data=data
        self.A_p=0
        self.A_a=0
        self.w_p=0
        self.w_a=0
        self.w_p_m=0
        self.w_a_m=0
        self.gain=0
        self.wo=0
        self.bw=0
        self.w_a_n = 0
        self.Q=0
        self.k=0
        self.actual_n=0
        self.n=0
        self.min_n=0
        #to store the original aproximation
        self.normalized_num=0
        self.normalized_den=0
        self.normalized_z=0
        self.normalized_p=0
        self.normalized_k=0
        #to store the actual aproximation
        self.actual_num=0
        self.actual_den=0
        self.actual_z=0
        self.actual_p=0
        self.actual_k=0
        #design stages
        self.stages_list= []
        #flags
        self.__template_flag=True      #template squares on or off
        self.__visible=True            #if its going to be displayed
        self.actual_displayed=Type.LP   #what is actually being displayed
        self.__att_mode=False
        #self.singularidades = np.array([[1],[1],[1]])
        self.singularidades = {
            "polos": list(),
            "ceros": list(),
            "ganancias": list(),
            "sos": list(),

        }

        self.init_approx()

    def should_draw_template(self):
        return self.__template_flag
    def should_be_drawn(self):
        return self.__visible
    def should_be_att(self):
        return self.__att_mode

    def change_template_visibility(self,bool):
         self.__template_flag=bool

    def change_visibility(self,bool):
        self.__visible = bool

    def change_to_att_mode(self,bool):
        self.__att_mode = bool


    def turn_on_template(self):
        self.__template_flag=True

    def turn_off_template(self):
        self.__template_flag=False

    def turn_the_approx_visible(self):
        self.__visible = True

    def turn_the_approx_invisible(self):
        self.__visible = False

    def draw_in_att_mode(self):
        self.__att_mode = True

    def draw_in_trans_mode(self):
        self.__att_mode = False

    def draw_my_approximation(self):
        print('to do')

    def get_w_a_n(self):
        if self.type == Type.LP:
            self.w_a_n=self.data["w_a"]/self.data["w_p"]

        if self.type == Type.HP:
            self.w_a_n=self.data["w_p"]/self.data["w_a"]

        if self.type == Type.BR:
            #calculo w0 y bw

            self.wo = np.sqrt(self.data["w_a"] * self.data["w_a_m"])

            if (self.data["w_p"]*self.data["w_p_m"]) >= self.wo**2:
                self.data["w_p"] = (self.wo ** 2) / self.data["w_p_m"]
            else:
                self.data["w_p_m"] = (self.wo ** 2) / self.data["w_p"]

            self.bw = self.data["w_p"] - self.data["w_p_m"]
            print(self.bw)
            print(self.wo)
            print(self.data["w_a_m"])
            print(self.data["w_a"])
            print(self.data["w_p_m"])
            print(self.data["w_p"])

            self.w_a_n=(self.data["w_p"]-self.data["w_p_m"])/(self.data["w_a"]-self.data["w_a_m"])

        if self.type == Type.BP:
            #calculo w0 y bw
            self.bw = self.data["w_p"] - self.data["w_p_m"]
            self.wo = np.sqrt(self.data["w_p"] * self.data["w_p_m"])

            if (self.data["w_a"]*self.data["w_a_m"]) >= self.wo**2:
                self.data["w_a"] = (self.wo ** 2) / self.data["w_a_m"]
            else:
                self.data["w_a_m"] = (self.wo ** 2) / self.data["w_a"]


            print(self.bw)
            print(self.wo)
            print(self.data["w_a_m"])
            print(self.data["w_a"])
            print(self.data["w_p_m"])
            print(self.data["w_p"])

            self.w_a_n = (self.data["w_a"] - self.data["w_a_m"]) / (self.data["w_p"]-self.data["w_p_m"])

        self.k=1/self.w_a_n

    def split_list(self,alist, wanted_parts=1):
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    def get_sos(self):
        #me fijo la cantidad de secciones para el filtro desnormalizado buscado
        self.number_of_sections=int(np.floor(self.actual_n/2)+self.actual_n%2)


        index=0
        #si la ganancia es unitaria, asigno ganancia unitaria a todas las etapas
        if self.actual_k==1:
            while self.number_of_sections>index:
                self.singularidades["ganancias"].append({1})
                index+=1
        # si la ganancia no es unitaria se la asigno a la ultima etapa
        else:
            while self.number_of_sections>index:
                if index+1 == self.number_of_sections:
                    self.singularidades["ganancias"].append({self.actual_k})
                    break
                self.singularidades["ganancias"].append({1})
                index += 1
        #estas ganancias individuales se podrían editar más adelante de manera inidividual

        #cargo una lista de polos conjugados y el posible polo simple(si aplica)
        index=0
        auxiliar_p=list(self.actual_p)
        while len(auxiliar_p) > 0:
            aux=auxiliar_p.pop(0) #saco un polo de la lista de polos
            if aux.imag == 0:
                self.singularidades["polos"].append({aux})  # appendeo polo simple
            for x in auxiliar_p: #busco su conjugado
                if x==np.conjugate(aux):
                    self.singularidades["polos"].append({aux,x}) #appendeo polos conjugados
                    auxiliar_p.remove(x) #remuevo el conjugado de la lista
                    break

        index = 0
        auxiliar_z=list(self.actual_z)
        while len(auxiliar_z) > 0:
            aux=auxiliar_z.pop(0) #saco un cero de la lista de ceros
            for x in auxiliar_z: #busco su conjugado
                if x==np.conjugate(aux):
                    self.singularidades["ceros"].append({aux,x}) #appendeo ceros conjugados
                    auxiliar_z.remove(x) #remuevo el conjugado de la lista
                    break


        index=0
        while self.number_of_sections > index:
            if not self.singularidades["ceros"]:
                sos_to_be_append=signal.zpk2tf(1,np.asarray(self.singularidades["polos"][index]),np.asarray(self.singularidades["ganancias"][index]))
                self.singularidades["sos"].append({sos_to_be_append})
            else:
                num,den=signal.zpk2tf(np.array(list(self.singularidades["ceros"][index]),dtype=np.complex128),np.array(list(self.singularidades["polos"][index]),dtype=np.complex128),np.asarray(list(self.singularidades["ganancias"][index])))
                d1,damp_coef,d2=control.damp(control.TransferFunction(num,den))
                Q=1/2*damp_coef
                self.singularidades["sos"].append(list([num,den,Q]))
            index+=1

        self.check_for_q()

    def check_for_q(self):
        recalculate=False
        if self.data["Q_max"] !=0:
            for x in self.singularidades["sos"]:
                if x[2][0] >= self.data["Q_max"] :  #Q mayor al permitido
                    recalculate=True

        if recalculate:
            self.data["n"]=self.n-1 #hardcodeo el n por uno menos restrictivo
            self.init_approx() #vuelvo a realizar la aproximacion
            print('Hay que recalcular el filtro')
        else: #ordeno de Q menor a mayor
            self.singularidades["sos"].sort(key=lambda q: q[2][0])






    def recalculate_filter(self):
        print('dummy')

    def init_approx(self):
        self.get_w_a_n()

        if self.approximation==Approximation.Legendre:
            self.normalized_z, self.normalized_p, self.normalized_k,self.n=legendre.legendre(self.data["A_p"],self.data["A_a"],1,self.w_a_n,self.data["n"],self.data["d"]) #dummy wmax
            self.normalized_num, self.normalized_den = signal.zpk2tf(self.normalized_z, self.normalized_p, self.normalized_k)

            if self.type==Type.LP:
                self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.data["w_p"])
                self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.data["w_p"])

            if self.type==Type.HP:
                self.actual_num, self.actual_den = signal.lp2hp(self.normalized_num, self.normalized_den, self.data["w_p"])
                self.actual_z, self.actual_p,self.actual_k = signal.lp2hp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.data["w_p"])

            if self.type==Type.BP:
                self.actual_num, self.actual_den = signal.lp2bp(self.normalized_num, self.normalized_den, self.wo,self.bw)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2bp_zpk(self.normalized_z, self.normalized_p, self.normalized_k,self.wo,self.bw)

            if self.type==Type.BR:
                self.actual_num, self.actual_den = signal.lp2bs(self.normalized_num, self.normalized_den, self.wo,self.bw)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2bs_zpk(self.normalized_z, self.normalized_p, self.normalized_k,self.wo,self.bw)

        if self.approximation==Approximation.Cauer:
            self.normalized_z, self.normalized_p, self.normalized_k, self.n=cauer.cauer(self.data["A_p"],self.data["A_a"],1,self.w_a_n,self.data["n"],self.data["d"]) #dummy wmax
            self.normalized_num, self.normalized_den = signal.zpk2tf(self.normalized_z, self.normalized_p, self.normalized_k)

            if self.type==Type.LP:
                self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.data["w_p"])
                self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.data["w_p"])

            if self.type==Type.HP:
                self.actual_num, self.actual_den = signal.lp2hp(self.normalized_num, self.normalized_den, self.data["w_p"])
                self.actual_z, self.actual_p,self.actual_k = signal.lp2hp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.data["w_p"])

            if self.type==Type.BP:
                self.actual_num, self.actual_den = signal.lp2bp(self.normalized_num, self.normalized_den, self.wo,self.bw)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2bp_zpk(self.normalized_z, self.normalized_p, self.normalized_k,self.wo,self.bw)

            if self.type==Type.BR:
                self.actual_num, self.actual_den = signal.lp2bs(self.normalized_num, self.normalized_den, self.wo,self.bw)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2bs_zpk(self.normalized_z, self.normalized_p, self.normalized_k,self.wo,self.bw)

        if self.approximation==Approximation.Butterworth:
            self.normalized_z, self.normalized_p, self.normalized_k, self.n=butterworth.butterworth(self.data["A_p"],self.data["A_a"],1,self.w_a_n,self.data["n"],self.data["d"]) #dummy wmax
            self.normalized_num, self.normalized_den = signal.zpk2tf(self.normalized_z, self.normalized_p, self.normalized_k)

            if self.type==Type.LP:
                self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.data["w_p"])
                self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.data["w_p"])

            if self.type==Type.HP:
                self.actual_num, self.actual_den = signal.lp2hp(self.normalized_num, self.normalized_den, self.data["w_p"])
                self.actual_z, self.actual_p,self.actual_k = signal.lp2hp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.data["w_p"])

            if self.type==Type.BP:
                self.actual_num, self.actual_den = signal.lp2bp(self.normalized_num, self.normalized_den, self.wo,self.bw)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2bp_zpk(self.normalized_z, self.normalized_p, self.normalized_k,self.wo,self.bw)

            if self.type==Type.BR:
                self.actual_num, self.actual_den = signal.lp2bs(self.normalized_num, self.normalized_den, self.wo,self.bw)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2bs_zpk(self.normalized_z, self.normalized_p, self.normalized_k,self.wo,self.bw)

        if self.approximation == Approximation.Cheby1:
            self.normalized_z, self.normalized_p, self.normalized_k, self.n = cheby1.cheby1(self.data["A_p"],
                                                                                            self.data["A_a"], 1,
                                                                                            self.w_a_n, self.data["n"],
                                                                                            self.data[
                                                                                                "d"])  # dummy wmax
            self.normalized_num, self.normalized_den = signal.zpk2tf(self.normalized_z, self.normalized_p,
                                                                     self.normalized_k)

            if self.type == Type.LP:
                self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den,
                                                                self.data["w_p"])
                self.actual_z, self.actual_p, self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.data["w_p"])

            if self.type == Type.HP:
                self.actual_num, self.actual_den = signal.lp2hp(self.normalized_num, self.normalized_den,
                                                                self.data["w_p"])
                self.actual_z, self.actual_p, self.actual_k = signal.lp2hp_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.data["w_p"])

            if self.type == Type.BP:
                self.actual_num, self.actual_den = signal.lp2bp(self.normalized_num, self.normalized_den, self.wo,
                                                                self.bw)
                self.actual_z, self.actual_p, self.actual_k = signal.lp2bp_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.wo, self.bw)

            if self.type == Type.BR:
                self.actual_num, self.actual_den = signal.lp2bs(self.normalized_num, self.normalized_den, self.wo,
                                                                self.bw)
                self.actual_z, self.actual_p, self.actual_k = signal.lp2bs_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.wo, self.bw)

        if self.approximation == Approximation.Cheby2:
            self.normalized_z, self.normalized_p, self.normalized_k, self.n = cheby2.cheby2(self.data["A_p"],self.data["A_a"], 1,self.w_a_n, self.data["n"], self.data["d"])  # dummy wmax
            self.normalized_num, self.normalized_den = signal.zpk2tf(self.normalized_z, self.normalized_p,
                                                                     self.normalized_k)

            if self.type == Type.LP:
                self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den,
                                                                self.data["w_p"])
                self.actual_z, self.actual_p, self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.data["w_p"])

            if self.type == Type.HP:
                self.actual_num, self.actual_den = signal.lp2hp(self.normalized_num, self.normalized_den,
                                                                self.data["w_p"])
                self.actual_z, self.actual_p, self.actual_k = signal.lp2hp_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.data["w_p"])

            if self.type == Type.BP:
                self.actual_num, self.actual_den = signal.lp2bp(self.normalized_num, self.normalized_den, self.wo,
                                                                self.bw)
                self.actual_z, self.actual_p, self.actual_k = signal.lp2bp_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.wo, self.bw)

            if self.type == Type.BR:
                self.actual_num, self.actual_den = signal.lp2bs(self.normalized_num, self.normalized_den, self.wo,
                                                                self.bw)
                self.actual_z, self.actual_p, self.actual_k = signal.lp2bs_zpk(self.normalized_z, self.normalized_p,
                                                                               self.normalized_k, self.wo, self.bw)
        self.actual_n=len(self.actual_p)
        self.get_sos()

    def make_me_a_LP(self):
        self.actual_num, self.actual_dem, =signal.lp2lp(self.normalized_num,self.normalized_den,self.w_p)
        self.actual_z,self.actual_p,self.actual_k=signal.lp2lp_zpk(self.normalized_z,self.normalized_p,self.normalized_k,self.w_p)

    def make_me_a_HP(self):
        self.actual_num, self.actual_dem, =signal.lp2hp(self.normalized_num,self.normalized_den,self.w_p)
        self.actual_z,self.actual_p,self.actual_k=signal.lp2hp_zpk(self.normalized_z,self.normalized_p,self.normalized_k,self.w_p)

    def make_me_a_BP(self):
        self.actual_num, self.actual_dem, =signal.lp2bp(self.normalized_num,self.normalized_den,self.wo,self.bw)
        self.actual_z,self.actual_p,self.actual_k=signal.lp2bp_zpk(self.normalized_z,self.normalized_p,self.normalized_k,self.w_p,self.wo,self.bw)

    def make_me_a_BR(self):
        self.actual_num, self.actual_dem, =signal.lp2bs(self.normalized_num,self.normalized_den,self.wo,self.bw)
        self.actual_z,self.actual_p,self.actual_k=signal.lp2bs_zpk(self.normalized_z,self.normalized_p,self.normalized_k,self.w_p,self.wo,self.bw)







class Type(Enum):
    LP=0
    HP=1
    BP=2
    BR=3
    PT=4
    LPN=5
class Singularidad(Enum):
    ganancia = 0
    polos = 1
    ceros = 2

class Approximation(Enum):
    Legendre = 0
    Cauer = 1
    Gauss = 2
    Butterworth = 3
    Cheby1 = 4
    Cheby2=5
    Bessel=6




