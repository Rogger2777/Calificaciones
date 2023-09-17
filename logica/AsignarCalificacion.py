class AsignarCalificacion:
    def __init__(self, calificacion, rango):
        self.calificacion = calificacion
        self.rango = rango

    def checarcalificacion(self):
        if self.calificacion > 9.0:
            self.rango = "La calificacion es A. \n Excelente."
        elif self.calificacion > 8.0:
            self.rango = "la calificacion es B. \n Muy Bien."
        elif self.calificacion >= 7.5:
            self.rango = "la calificacion es C. \n Bien."
        else:
            self.rango = "La calificacion es R. \n Reprobado."
        return self

    def imprimircalificacion(self):
        print(self.rango)
