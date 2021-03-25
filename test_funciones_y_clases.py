from datetime import date
import random

import pytest

import funciones_y_clases_solved as md

def assert_attr(obj, attr):
    assert hasattr(obj, attr), 'Falta implementar "{}"'.format(attr)

def assert_function(func_name, expected, args, kwargs):
    assert_attr(md, func_name)
    try: result = getattr(md, func_name)(*args, **kwargs)
    except: raise Exception('Función "{}" genera error'.format(func_name))
    assert expected == result, '{}: input -> args:{}, kwargs:{}'.format(
        func_name, args, kwargs)

@pytest.mark.parametrize(('var'), [98, 35, 76, 'asdf', [1,2,3]])
def test_cambiar_global(var):
    func_name = 'cambiar_global'
    assert_attr(md, func_name)
    try: md.cambiar_global(var)
    except: raise Exception('Función "{}" genera error'.format(func_name))
    assert md.global1 == var, '{}: No se cambió correctamente "global1"'.format(func_name)

bisiesto_fn = lambda x: False if not x % 4 == 0 else (True if not x % 100 == 0 else (False if not x % 400 == 0 else True))
anio_bisiesto = [
    ('anio_bisiesto', True if bisiesto_fn(year) else False, [year], {})
    for year in random.sample(range(1584, 2100), 70)
]

contar_valles = []
saltando_rocas = []
pares_medias = []
for i in range(20):
    ej = [random.randint(-1, 1) for i in range(30)]
    e = ej[0] == -1; l = 0
    for s in ej:
        if s == 0: continue
        if e and s == 1: l += 1
        e = s == -1
    contar_valles.append(('contar_valles', l, [ej], {}))

    ll = [0]
    for i in range(1, random.randint(25, 40)):
        ll.append(1 if random.random() > 0.7 and ll[i-1] != 1 else 0)
    ll.append(0)
    c = 0; i = 0; l = len(ll)
    while i < l-1:
        c += 1; i += 2 if i+2 < l and ll[i+2] == 0 else 1
    saltando_rocas.append(('saltando_rocas', c, [ll], {}))

    ll = []
    res = {}
    sup = {}
    for i in range(1, random.randint(25, 40)):
        el = random.randint(1, 10)
        if sup.get(el, False):
            res[el] = res.get(el, 0) + 1; sup[el] = False
        else: sup[el] = True
        ll.append(el)
   
    pares_medias.append(('pares_medias', res, [ll], {}))

@pytest.mark.parametrize(('func_name', 'output', 'args', 'kwargs'), 
    anio_bisiesto + contar_valles + saltando_rocas + pares_medias)
def test_eval(func_name, output, args, kwargs):
    assert_function(func_name, output, args, kwargs)


@pytest.mark.parametrize(('lista'), [[random.randint(0,100) for i in range(20)] for i in range(4)]
)
def test_ListaComa(lista):
    class_name = 'ListaComa'
    assert_attr(md, class_name)
    try: ll = md.ListaComa(lista)
    except: raise Exception('Clase "{}" genera error'.format(class_name))
    assert str(ll) == ','.join([str(el) for el in lista]), 'Clase {} no es correcta'.format(class_name)

ff = lambda: ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k = random.randint(3,8)))
ff1 = lambda x: ' '.join(str(el).capitalize() for el in x)

@pytest.mark.parametrize(('nombres','apellidos'),
    [[[ff() for i in range(random.randint(1,3))], [ff() for i in range(2)]] for i in range(20)]
)
def test_Persona(nombres, apellidos):
    class_name = 'Persona'
    assert_attr(md, class_name)
    try: ll = md.Persona(nombres, apellidos)
    except: raise Exception('Clase "{}" genera error'.format(class_name))
    assert_attr(ll, 'nombre_completo')
    assert ll.nombre_completo() == ff1(nombres + apellidos), 'Clase {} no es correcta'.format(class_name)

def fn3( d ):
    t = date.today()
    return (t.year - d.year) - (1 if t < date(t.year, d.month, d.day) else 0)

persona1 = [
    [
        [ff() for i in range(random.randint(1,3))],
        [ff() for i in range(2)],
        date(random.randint(1950, 2001), random.randint(1, 12), random.randint(1,28))
    ] for i in range(20)]

@pytest.mark.parametrize(('nombres','apellidos','fecha'), persona1)
def test_Persona1(nombres, apellidos, fecha):
    class_name = 'Persona1'
    assert_attr(md, class_name)
    assert issubclass(md.Persona1, md.Persona), 'Clase Persona1 no hereda de Persona'
    try: ll = md.Persona1(nombres, apellidos, fecha)
    except: raise Exception('Clase "{}" genera error'.format(class_name))
    assert_attr(ll, 'edad')
    assert ll.edad() == fn3(fecha), 'Clase {} no es correcta'.format(class_name)
