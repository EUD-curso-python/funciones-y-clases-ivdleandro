
def eval_test(d, var, modul):
    val = d[var]
    assert hasattr(modul, var), 'No has creado la variable "{}"'.format(var)
    assert getattr(modul, var) == val, 'La variable "{}" debería ser {} y no {}'.format(var, val, getattr(modul, var))