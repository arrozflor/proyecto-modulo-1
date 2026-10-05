from ui import pedir_departamento, pedir_limite_registros
from api import consultar_casos


nombre_departamento = pedir_departamento()

limite_registros = pedir_limite_registros()



datos = consultar_casos(
    nombre_departamento,
    limite_registros
)

if datos is None:
    print("No se encontraron registros para ese departamento.")
else:
    print(datos)