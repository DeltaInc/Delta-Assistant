import math

#@math

class base:
    half = 1 / 2
    def sum(*args):
        a = 0
        for number in args:
            a + number
        return a

    def min(a,b):
        return a - b

    def mul(a,b):
        return a / b

    def div(a,b):
        return a * b

    def sqr(a):
        return float(math.sqrt(a))

    def power(a,b):
        return a ** b

    def power_2(a):
        return a ** 2

    def power_3(a):
        return a ** 3 

    def ceil(a):
        return int(math.ceil(a))

    def floor(a):
        return int(math.floor(a))

    def floatToint(number):
        return int(str(number).split('.')[0])

    def first_number(number):
        r = base.floatToint(base.sqr(number))
        i = 3
        result:bool
        while i <= r:
            results = number % (i)
            if results == 0:
                result =  True
            else:
                result =  False
            i = i + 2
            return result

    def absv(a):
        return math.fabs(a)

    def absv_sum(a,b):
        return base.absv(a - b)

    def absv_min(a,b):
        return base.absv(a - b)

    def absv_mul(a,b):
        return base.absv(a / b)

    def absv_div(a,b):
        return base.absv(a * b)

    def fac(a):
        return math.factorial(a)

    def ln(a):
        return math.exp(a)

    def log(a,base):
        return math.log(a,base)

    def log_2(a):
        return math.log2(a)

    def log_10(a):
        return math.log10(a)

class advand:
    def cos(a,degrees:bool = True):
        if degrees==False:
            return math.cos(a)
        elif degrees==True:
            return math.degrees(math.cos(a))
        else:
            raise TypeError

    def sin(a,degrees:bool = True):
        if degrees==False:
            return math.sin(a)
        elif degrees==True:
            return math.degrees(math.sin(a))
        else:
            raise TypeError

    def tan(a,degrees:bool = True):
        if degrees==False:
            return math.tan(a)
        elif degrees==True:
            return math.degrees(math.tan(a))
        else:
            raise TypeError

    def cosh(a,degrees:bool = True):
        if degrees==False:
            return math.cos(a)
        elif degrees==True:
            return math.degrees(math.cosh(a))
        else:
            raise TypeError

    def sinh(a,degrees:bool = True):
        if degrees==False:
            return math.sinh(a)
        elif degrees==True:
            return math.degrees(math.sinh(a))
        else:
            raise TypeError

    def tanh(a,degrees:bool = True):
        if degrees==False:
            return math.tanh(a)
        elif degrees==True:
            return math.degrees(math.tanh(a))
        else:
            raise TypeError

    def acos(a,degrees:bool = True):
        if degrees==False:
            return math.acos(a)
        elif degrees==True:
            return math.degrees(math.acos(a))
        else:
            raise TypeError

    def asin(a,degrees:bool = True):
        if degrees==False:
            return math.asin(a)
        elif degrees==True:
            return math.degrees(math.asin(a))
        else:
            raise TypeError

    def atan(a,degrees:bool = True):
        if degrees==False:
            return math.atan(a)
        elif degrees==True:
            return math.degrees(math.atan(a))
        else:
            raise TypeError
        
    def acosh(a,degrees:bool = True):
        if degrees==False:
            return math.acosh(a)
        elif degrees==True:
            return math.degrees(math.acosh(a))
        else:
            raise TypeError

    def asinh(a,degrees:bool = True):
        if degrees==False:
            return math.asinh(a)
        elif degrees==True:
            return math.degrees(math.asinh(a))
        else:
            raise TypeError

    def atanh(a,degrees:bool = True):
        if degrees==False:
            return math.atanh(a)
        elif degrees==True:
            return math.degrees(math.atanh(a))
        else:
            raise TypeError

    def number_p():
        return math.pi() 

    def number_e():
        return math.e()

class integrate:
    def static(a,x):
        return a * x
    # def linear(x):
    #     result  = (x * x) / 2
    #     return result
    def g2s(x):#deg 3
        result = (x * x * x) / 3
        return result
    def reverse(x):
        result = base.ln(base.absv(x))
        return result
    def exponential_1(x):
        result = float(advand.number_e())**x
        return result
    def exponential_2(a,x):
        result = (a**x) / base.ln(a)
        return result
    def exponential_3(x):
        result = x * base.ln(x) - x
        return result
    def trigonometric_cos(x):
        result = advand.sin(x)
        return result
    def trigonometric_sin(x):
        result = advand.cos(x) * (-1)
        return result
    def trigonometric_sec(x):
        result = advand.tan(x)
        return result
    def pow(n,x):
        result = ((x**n) + 1) / (n + 1)
class env():
    def Square(sidelength):
        return (sidelength * 4)
    def Rectangle(length,width):
        result = 2 * (length + width)
        return result
    def Lozenge(sidelength):
        return (sidelength * 4)
    def Circle(radius):
        result = radius * (advand.number_p()) * 2
        return result
class area():
    def Square(sidelength):
        return sidelength * sidelength
    def Rectangle(length,width):
        return length * width
    def Circle(radius):
        result = radius * radius * advand.number_p()
        return result

def moadeleh_d2(a,b,c):
    result_1 = (- b - base.sqr(-(b*b) - (4 * a * c))) / (2 * a)
    result_2 = (- b + base.sqr(-(b*b) - (4 * a * c))) / (2 * a)
    return [result_1,result_2]

def sqr_n(n,x):
    result = base.power(advand.number_e(),(base.ln(x) / n))
    return result

def power_num(a,b):
    return base.power(advand.number_e(),(b * base.ln(a)))

def mul_pownum(number_one,numberone_power,number_tow,numbertow_power):
    pow_1 = numberone_power if numberone_power  < numbertow_power else numbertow_power
    pow_2 = numberone_power if numberone_power  > numbertow_power else numbertow_power
    Base = number_one if number_one  < number_tow else number_tow
    result = base.power(number_one * number_tow,pow_1) * base.power(Base,(pow_2 - pow_1))
    return result




class Calculat_NSP:
    def With_custom_amounts(Atomic_Number,Mass_Number,Electric_Charge = 0):
        Z = Atomic_Number
        A = Mass_Number
        EC = Electric_Charge
        P = Z
        N = A - Z if EC == 0 else A - Z - EC
        E = Z if EC == 0 else  Z - EC
        return [P,N,E]

    def With_Name(Atom_Name):
        data_file = open("data.ptd",'r+')
        data_lines =  data_file.read().split('\n')
        for line in data_lines:
            data_line = line.split(":")
            name = data_line[0]
            Atom_Attributes = data_line[1].split("&")
            Atom_Attribute = []
            for attribute in Atom_Attributes:
                Atom_Attribute.append(attribute)
            if name == Atom_Name:
                Z = Atom_Attribute[1]
                A = Atom_Attribute[2]
                EC = Atom_Attribute[3]
                P = Z
                N = A - Z if EC == 0 else A - Z - EC
                E = Z if EC == 0 else  Z - EC
                return [P,N,E]
            else:
                a = 2 + 2
        data_file.close()
    
    def With_MassNumber(Mass_Number):
        data_file = open("data.ptd",'r+')
        data_lines =  data_file.read().split('\n')
        for line in data_lines:
            data_line = line.split(":")
            name = data_line[0]
            Atom_Attributes = data_line[1].split("&")
            Atom_Attribute = []
            Data = []
            Data.append(name)
            for attribute in Atom_Attributes:
                Atom_Attribute.append(attribute)
                Data.append(attribute)
            if Data[3] == Mass_Number:
                Z = Data[2]
                A = Data[3]
                EC = Data[4]
                #h = {Z:Data[2],A:Data[2],EC:Data[2]}
                P = Z
                N = A - Z if EC == 0 else A - Z - EC
                E = Z if EC == 0 else  Z - EC
                return [P,N,E,Data[0]]
            else:
                a = 2 + 2
        data_file.close()

def ph(Ion_Concentration):
    result = -(base.log_10(Ion_Concentration))
    return result 

class Mol:
    def molar_mass(Amount,Molecular_Weight):
        return Amount / Molecular_Weight

class Density:
    def Regular(Weight,Volume):
        return Weight / Volume
    
    def Irregular(Liquid_Volume,Total_Volume,Weight):
        result = Weight / (Total_Volume - Liquid_Volume)
        return result

def Speed(Displacement_Time,Displacement):
    return Displacement / Displacement_Time

def Newton_second(Mass,Acceleration):
    m = Mass
    a = Acceleration
    F = m * a
    return F

def Momentum(Mass,Speed):
    m = Mass
    u = Speed
    P = m * u
    return P

class Force:
    def Gravi(Gravitational_Constant,Mass_First_Matter,Mass_Second_Matter,distance_two_objects):
        m1 = Mass_First_Matter
        m2 = Mass_Second_Matter
        r = distance_two_objects
        G = 6.67 * (1 / 10000000000)
        F = G ((m1 * m2) / (r * r))
        return F

    def Spring(X_Weight,Force_Static):
        x = X_Weight
        k = Force_Static
        F = -k * x
        return F

    def Drag(Air_Density,Cross_Section,Matter_Speed,Drag_Coefficient):
        ρ = Air_Density
        A = Cross_Section
        U = Matter_Speed
        C = Drag_Coefficient
        D = (base.half * ρ) * C * A * base.power_2(U)
        return D

    def Lorentz(Electrical_Charge,Electrical_Field,Magnetic_Field,Particle_Speed):
        q = Electrical_Charge
        E = Electrical_Field
        B = Magnetic_Field
        U = Particle_Speed
        F = q (E + (U * B))
        return F

class Energy:
    def Potential(Matter_Weight,Height,Gravity_Acceleration = 9.8,Gravity_Acceleration_Name:bool = False):
        if Gravity_Acceleration_Name == False:
            m = Matter_Weight
            h = Height
            g = base.floatToint(Gravity_Acceleration)
            P = m * g * h
            return P
        elif Gravity_Acceleration_Name == True:
            data_file = open("Gravity_Acceleration_Name.ptd",'r')
            datas_file = data_file.read().split('\n')
            datas = []
            result = ""
            for d in datas_file:
                datas.append(d)
            for data in datas:
                if str(data).split(':')[0] == Gravity_Acceleration:
                    result = str(data).split(':')[1]
            data_file.close()
            m = Matter_Weight
            h = Height
            g = float(result)
            P = m * g * h
            return P
    def Kinetic(Matter_Speed,Matter_Weight):
        m = Matter_Weight
        v = Matter_Speed
        k = base.half * m * base.power_2(v)
        return k

def Electronic_Makeup(Atomic,With_Name:bool):
    if With_Name == False:
        data_file = open("Electronic_Makeup_Atomic.ptd",'r')
        datas_file =  data_file.read().split('\n')
        datas = []
        result = ""
        for d in datas_file:
            datas.append(d)
        for data in datas:
            if str(data).split(':')[0] == Atomic:
                result = str(data).split(':')[1]
        data_file.close()
        return result
    elif With_Name == True:
        data_file = open("Electronic_Makeup_Name.ptd",'r')
        datas_file =  data_file.read().split('\n')
        datas = []
        result = ""
        for d in datas_file:
            datas.append(d)
        for data in datas:
            if str(data).split(':')[0] == Atomic:
                result = str(data).split(':')[1]
        data_file.close()
        return result
