from datetime import datetime


def experience():
    # Obtén la fecha actual
    fecha_actual = datetime.now()
    fecha_referencia = datetime(2009, 1, 1)
    diferencia_anos = fecha_actual.year - fecha_referencia.year
    resultado_string = str(diferencia_anos)
    return resultado_string