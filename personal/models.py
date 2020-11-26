from django.db import models

# Create your models here.

class Direccion(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    
    def __str__(self):
        return(" {} {} ".format(self.nombre, self.numero))

class Personal(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    FEMENINO = "F"
    MASCULINO = "M"
    OTRO = "O"
    rolsexo = [
        (FEMENINO,"Femenino"),
        (MASCULINO,"Masculino"),
        (OTRO,"Otro")
    ]
    sexo = models.CharField(max_length=1,choices=rolsexo,default=OTRO)
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
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return  ("{} {}".format(self.nombre,self.apellido))   


class Asistencia(models.Model):
    empleado = models.ForeignKey(Personal,on_delete=models.CASCADE)
    ENFERMO = "E"
    LICENCIA = "L"
    TRABAJO = "T"
    NOTRABAJO = "NT"
    TIPOS = [
        (ENFERMO,"Enfermo"),
        (LICENCIA,"Licencia"),
        (TRABAJO,"Dia trabajado"),
        (NOTRABAJO,"Dia no trabajado"),
    ]
    tipo = models.CharField(choices=TIPOS,default=TRABAJO,max_length=2)
    fecha = models.DateField() 
    def __str__(self):
        return  ("{}".format(self.empleado))  

class Amonestacion(models.Model):
    empleado = models.ForeignKey(Personal,on_delete=models.CASCADE)
    razon = models.CharField(max_length=200,help_text="Faltar el respeto a los compañeros del trabajo")
    consecuencia = models.CharField(max_length=500,help_text="Suspecion por 3 dias sin paga")
    def __str__(self):
        return ("{}".format(self.empleado))

class Rodado(models.Model):
    conductor = models.ManyToManyField(Personal)
    patente = models.CharField(max_length=9)
    marca = models.CharField(max_length=20)
    tipo_motor = models.CharField(max_length=20)
    CAMIONETA = "CAMIONETA"
    MOTO = "MOTO"
    TRACTOR = "TRACTOR"
    ESCAVADORA = "ESCAVADORA"
    CUATRICICLO = "CUATRICICLO"
    OTRO = "OTRO"
    tipos = [
        (CAMIONETA,"Camioneta"),
        (MOTO,"Moto"),
        (TRACTOR,"Tractor"),
        (ESCAVADORA,"Escavadora"),
        (CUATRICICLO,"Cuatriciclo"),
        (OTRO,"Otro")
    ]
    tipo_rodado = models.CharField(max_length=11,choices=tipos,default=CAMIONETA)
    BUEN_ESTADO = "BUEN_ENSTADO"
    MAL_ESTADO = "MAL_ESTADO"
    EN_MANTENIMIENTO = "EN_MANTENIMIENTO"
    tipo_estado = [
        (BUEN_ESTADO,"Buen estado"),
        (MAL_ESTADO,"Mal estado"),
        (EN_MANTENIMIENTO,"En mantenimiento")
    ]
    estado = models.CharField(max_length=16, choices=tipo_estado,default=BUEN_ESTADO)
    def __str__(self):
        return ("tipo:{} marca:{}".format(self.tipo_rodado,self.marca))

class Insumo(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    BUEN_ESTADO = "BUEN_ENSTADO"
    MAL_ESTADO = "MAL_ESTADO"
    PRESTADO = "PRESTADO"
    tipo_estado = [
        (BUEN_ESTADO,"Buen estado"),
        (MAL_ESTADO,"Mal estado"),
        (PRESTADO,"Prestado"),
    ]
    estado = models.CharField(max_length=16, choices=tipo_estado,default=BUEN_ESTADO)
    def __str__(self):
        return ("{}".format(self.nombre))
class Alimento(models.Model):
    nombre = models.CharField(max_length=60)
    ANIMAL = "A"
    HUMANO = "H"
    tipo_ = [
        (ANIMAL,"Animal"),
        (HUMANO,"Humano"),
    ]
    tipo = models.CharField(max_length=1,choices=tipo_,default=ANIMAL)
    fecha_de_compra = models.DateField()
    descripcion_de_cant_individual = models.CharField(max_length=200)
    stock = models.IntegerField()
    def __str__(self):
        return ("{}".format(self.nombre))
class Prestamo(models.Model):
    empleado = models.ForeignKey(Personal,on_delete=models.CASCADE)
    INSUMO = "I"
    ALIMENTO = "A"
    TIPOP = [
        (INSUMO,"Insumo"),
        (ALIMENTO,"Alimento"),
    ]
    tipo_prestamo = models.CharField(choices=TIPOP,max_length=1,default=ALIMENTO)
    alimento = models.ManyToManyField(Alimento,through="Prestamo_Alimento")
    insumo = models.ManyToManyField(Insumo)
    fecha_de_entrega = models.DateField()
    fecha_de_devolucion = models.DateField(blank=True)
    cantidad = models.IntegerField()
    def __str__(self):
        return ("{}".format(self.fecha_de_entrega))


class Prestamo_Alimento (models.Model):
    alimento = models.ForeignKey(Alimento,on_delete=models.CASCADE)
    prestamo = models.ForeignKey(Prestamo,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.cantidad
    