from enum import Enum
import legendre as legendre
import cauer as cauer
import gauss as gauss
from scipy import signal


class template():
    def __init__(self,type,approximation,A_p,A_a,w_p,w_a,gain):
        #type
        self.type=type
        self.approximation=approximation
        #building specs
        self.A_p=A_p
        self.A_a=A_a
        self.w_p=w_p
        self.w_a=w_a
        self.gain=gain
        self.wo=0
        self.bw=0
        self.Q=0
        self.actual_n=0
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

    def init_approx(self):

        if self.approximation==Approximation.Legendre:
            self.normalized_z, self.normalized_p, self.normalized_k=legendre.legendre(self.A_p,self.A_a,self.w_p,self.w_a,1e6) #dummy wmax
            self.normalized_num, self.normalized_den = signal.zpk2tf(self.normalized_z, self.normalized_p, self.normalized_k)

            if self.type==Type.LP:
                self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.w_p)
                self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.w_p)

            # if self.type==Type.HP:
            #     self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.w_p)
            #     self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.w_p)
            #
            # if self.type==Type.BP:
            #     self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.w_p)
            #     self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.w_p)
            #
            # if self.type==Type.BR:
            #     self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.w_p)
            #     self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.w_p)
            #
            # if self.type==Type.PT:
            #     self.actual_num, self.actual_den = signal.lp2lp(self.normalized_num, self.normalized_den, self.w_p)
            #     self.actual_z, self.actual_p,self.actual_k = signal.lp2lp_zpk(self.normalized_z, self.normalized_p, self.normalized_k, self.w_p)

        if self.approximation==Approximation.Cauer:
            self.normalized_z, normalized_p, normalized_k=cauer.cauer(self.A_p,self.A_a,self.w_p,self.w_a,1e6) #dummy wmax

        # if self.approximation==Approximation.Gauss:
        #     legendre.legendre(self.A_p,self.A_a,self.w_p,self.w_a,1e6) #dummy wmax
        #
        # if self.approximation==Approximation.Cheby1:
        #     legendre.legendre(self.A_p,self.A_a,self.w_p,self.w_a,1e6) #dummy wmax
        #
        # if self.approximation==Approximation.Cheby2:
        #     legendre.legendre(self.A_p,self.A_a,self.w_p,self.w_a,1e6) #dummy wmax
        #
        # if self.approximation == Approximation.Butterworth:
        #     legendre.legendre(self.A_p, self.A_a, self.w_p, self.w_a, 1e6)  # dummy wmax
        #
        # if self.approximation == Approximation.Bessel:
        #     legendre.legendre(self.A_p, self.A_a, self.w_p, self.w_a, 1e6)  # dummy wmax

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

    def make_me_a_PT(self):
        print('en proceso, bancala')




class Type(Enum):
    LP=0
    HP=1
    BP=2
    BR=3
    PT=4
    LPN=4

class Approximation(Enum):
    Legendre = 0
    Cauer = 1
    Gauss = 2
    Butterworth = 3
    Cheby1 = 4
    Cheby2=5
    Bessel=6



