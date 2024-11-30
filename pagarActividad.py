from cargarActividad import cargarActividad

def pagarActividad(archivoActividad, nombreUsuario):
    actividad_dict = cargarActividad(archivoActividad)
    if (nombreUsuario in actividad_dict):
        if(actividad_dict[nombreUsuario] == "pagado"):
            mensaje = "El usuario ya ha pagado la cuota de la actividad."
        else:
            actividad_dict[nombreUsuario] = "pagado"
            mensaje = "Se ha realizado el pago de la actividad correctamente."
    else:
        mensaje = "El usuario no se encuentra apuntado a esta actividad."
    return resultado

