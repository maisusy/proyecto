from django.db import models

# Create your models here.
class Direccion(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return(" {} {} ".format(self.nombre, self.numero))

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    DUEÑO = "DÑ"
    ENCARGADO = "ENC"
    CAPATAZ = "CZ"
    PEONGENERAL = "PG"
    PEONCOMUN = "PC"
    CASERO = "CAS"
    PUESTERO = "PUES"
    QUINTERO = "QUIN"
    ESQUILADOR = "ESQ"
    COCINERO = "COC"
    tiporol = [
        (DUEÑO,'Dueño'),
        (ENCARGADO,'Encargado'),
        (CAPATAZ, 'Capataz'), 
        (PEONGENERAL,'Peon General'), 
        (PEONCOMUN,'Peon Comun'),
        (CASERO,'Casero'), 
        (PUESTERO,'Puestero'), 
        (QUINTERO,'Quintero'), 
        (ESQUILADOR,'Esquilador'),
        (COCINERO,'Cocinero')
    ]
    rol = models.CharField(max_length=4, choices=tiporol,default=PEONCOMUN)
    direccion = models.ManyToManyField(Direccion)
    def __str__(self):
        return  ("{} {}".format(self.nombre,self.apellido))
        

class Fecha(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    horadesde = models.DateTimeField()
    horahasta = models.DateTimeField()
    def __str__(self):
        return ("{} , {}".format(self.titulo,self.fecha))
    

class Amonestacion(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    razon = models.CharField(max_length=500)
    consecuencia = models.CharField(max_length=500)
    def __str__(self):
        return (self.persona)

class Rodado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    patente = models.CharField(max_length=9)
    marca = models.CharField(max_length=20)
    tipo_motor = models.CharField(max_length=20)
    tipo_rodado = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    def __str__(self):
        return ("tipo:{} marca:{}".format(self.tipo_rodado,self.marca))

class Insumo(models.Model):
    antiguedad = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Alimento(models.Model):
    fecha_de_compra = models.DateField()
    descripcion_de_cant_individual = models.CharField(max_length=200)
    stock = models.IntegerField()
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo,on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento,on_delete=models.CASCADE)
    fecha_de_entrega = models.DateField()
    fecha_de_devolucion = models.DateField()
    cantidad = models.IntegerField()
    def __str__(self):
        return ("{}".format(self.cantidad))

class Seccion(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Ovino(models.Model):
    peso = models.FloatField()
    calidad_de_lana = models.CharField(max_length=30)
    padre = models.CharField(max_length=10)
    madre = models.CharField(max_length=10) 
    PDP = models.BooleanField()
    cant_de_dientes = models.IntegerField()
    categoria_por_diente = models.CharField(max_length=10)
    fecha_de_registro = models.DateField() 
    fecha_de_nacimiento = models.DateField()
    raza = models.CharField(max_length=10)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    def __str__(self):
        return ("seccion:{} , raza:{}".format(self.seccion,self.raza))

class Avicola(models.Model):
    cantidad = models.IntegerField()
    raza = models.CharField(max_length=20)
    sexo = models.CharField(max_length=7)
    def __str__(self):
        return self.raza

class Manada(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
    

class Equino(models.Model):
    nombre = models.CharField(max_length=30)
    color_pelaje = models.CharField(max_length=20)
    condicion = models.CharField(max_length=30)
    causa_de_muerte = models.CharField(max_length=30)
    fecha_De_nacimiento = models.DateField()
    raza = models.CharField(max_length=30)
    sexo = models.CharField(max_length=6)
    manada = models.ForeignKey(Manada,on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE) 
    def __str__(self):
        return self.nombre

class Energia(models.Model):
    tipo = models.CharField(max_length=30)
    fecha_de_instalacion = models.DateField()
    estado = models.CharField(max_length=30)
    descripcion_del_estado = models.CharField(max_length=200)
    fecha_De_mantenimiento = models.DateField()
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    def __str__(self):
        return self.tipo

class Alambrado(models.Model):
    cant_kilometros = models.FloatField()
    materiales = models.CharField(max_length=200)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE) 
    def __str__(self):
        return self.seccion