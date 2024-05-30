class Tarea:
    def __init__(self, titulo, descripcion, estado='pendiente'):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}"
