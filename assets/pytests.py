from funciones_fisica import *
import pytest

def test_cargar_datos():
    
    fichero='aceleracion_1.xlsx'
    
    t,aceleracion_abs,aceleracion_y=cargar_datos(fichero)
    
    assert t[0] == 0.00397
    assert aceleracion_abs[0]== 10.070947
    assert aceleracion_y[0] == 9.139319
    
def test_aceleracion_correcta():
    
    resultado=calcular_aceleracion_correcta(2,-1)
    
    assert resultado == -2

def test_gravedad():
    fichero='aceleracion_1.xlsx'
    t,aceleracion_abs,aceleracion_y=cargar_datos(fichero)
    a_correcta= calcular_gravedad(aceleracion_abs)
    
    assert a_correcta== 9.79853738
    
def test_fuerza():
    fuerza= calcular_fuerza(2,2)
    assert fuerza == 4

def test_aceleracion_corr():
    aceleracion_correcta = calcular_aceleracion_corr(5,2)
    assert aceleracion_correcta == 3

def test_velocidad():
    v_max=calcular_velocidad_maxima([1,2,3,1])
    assert v_max == 3

def test_duracion():
    fichero='aceleracion_1.xlsx'
    t,aceleracion_abs,aceleracion_y=cargar_datos(fichero)
    t_max,t_min,dur=calcular_duracion_vuelo(aceleracion_abs,t)
    
    assert t_max==1.977323
    assert t_min==1.758944
    assert dur ==-0.21837899999999988

def test_potencia():
    potencia= calcular_potencia(2,3)
    assert potencia==6

def test_altura():
    altura=calcular_altura(2,1)
    assert altura == 2

def test_primitiva ():
    fichero='aceleracion_1.xlsx'
    t,aceleracion_abs,aceleracion_y=cargar_datos(fichero)
    v= primitiva_numerica(aceleracion_abs, t,0)
    
    assert v[0]==0.00000000e+00
    