from django.db import models

# Create your models here.
class Seccion(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre          
class Fecha(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    Desde = models.DateTimeField()
    Hasta = models.DateTimeField()
    QUINTA = "QUINTA"
    ANIMALES = "ANIMALES"
    PERSONAL = "PERSONAL"
    COMPRA = "COMPRA"
    MANTENIMIENTO = "MANTENIMIENTO"
    OTRA = "OTRA"
    area = [
        (QUINTA,"Quinta"),
        (ANIMALES,"Animales"),
        (PERSONAL,"Personal"),
        (COMPRA,"Compra"),
        (MANTENIMIENTO,"Mantenimiento"),
        (OTRA,"Otra"),
    ]
    area_de_Trabajo = models.CharField(max_length=13, choices=area,default=OTRA)
    lugar = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    def __str__(self):
        return ("{}".format(self.titulo))   
class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    OVINO = "O"
    EQUINO = "E"
    AVICOLA = "A"
    TIPOr = [
        (OVINO,"Ovino"),
        (EQUINO,"Equino"),
        (AVICOLA,"Avicola"),
    ]
    tipo_animal = models.CharField(choices=TIPOr,max_length=1,default=OVINO)
    def __str__(self):
        return ("NOMBRE:{} , TIPO:{}".format(self.nombre,self.tipo_animal))      
class Ovino(models.Model):
    HEMBRA = "HEMBRA"
    MACHO = "MACHO"
    rolsexo = [
        (HEMBRA,"Hembra"),
        (MACHO,"Macho"),
    ]
    sexo = models.CharField(max_length=6,choices=rolsexo,default=MACHO)
    cant_de_dientes = models.IntegerField()
    CORDERO = "COR"
    BORREGO = "BOR"
    OVEJA = "OVJ"
    CARNERO = "CAR"
    OVEJAVIEJA = "OVJ V"
    CARNEROVIEJO = "CAR V"
    cd = [
        (CORDERO,"Cordero"),
        (BORREGO,"Borrego"),
        (OVEJA,"Oveja"),
        (CARNERO,"Carnero"),
        (OVEJAVIEJA,"Oveja vieja"),
        (CARNEROVIEJO,"Carnero viejo"),
    ]
    categoria_por_diente = models.CharField(max_length=5,default=OVEJA,choices=cd)
    fecha_de_registro = models.DateField() 
    fecha_de_nacimiento = models.DateField()
    raza =models.ForeignKey(Raza,on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    PDP = models.BooleanField(default=False)
    peso = models.FloatField()
    padre = models.CharField(max_length=10,blank=True)
    madre = models.CharField(max_length=10,blank=True) 
    calidad_de_lana = models.IntegerField()
    
    
    def __str__(self):
        return ("seccion:{} , raza:{}".format(self.seccion,self.raza))
class Avicola(models.Model):
    cantidad = models.IntegerField()
    raza = models.ForeignKey(Raza,on_delete=models.CASCADE)
    HEMBRA = "HEMBRA"
    MACHO = "MACHO"
    rolsexo = [
        (HEMBRA,"Hembra"),
        (MACHO,"Macho"),
    ]
    sexo = models.CharField(max_length=6,choices=rolsexo,default=HEMBRA)
    
    def __str__(self):
        return ("{}".format(self.raza))
class Manada(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre   
class Equino(models.Model):
    nombre = models.CharField(max_length=30)
    color_pelaje = models.CharField(max_length=20)
    condicion = models.CharField(max_length=30)
    fecha_De_nacimiento = models.DateField()
    HEMBRA = "HEMBRA"
    MACHO = "MACHO"
    rolsexo = [
        (HEMBRA,"Hembra"),
        (MACHO,"Macho"),
    ]
    sexo = models.CharField(max_length=6,choices=rolsexo,default=HEMBRA)
    raza =models.ForeignKey(Raza,on_delete=models.CASCADE)
    manada = models.ForeignKey(Manada,on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE) 
    causa_de_muerte = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.nombre
class Energia(models.Model):
    nombre = models.CharField(max_length=30,help_text="Molino,Panel Solar,etc.")
    fecha_de_instalacion = models.DateField()
    BUEN_ESTADO = "BUEN_ENSTADO"
    MAL_ESTADO = "MAL_ESTADO"
    EN_MANTENIMIENTO = "EN_MANTENIMIENTO"
    tipo_estado = [
        (BUEN_ESTADO,"Buen estado"),
        (MAL_ESTADO,"Mal estado"),
        (EN_MANTENIMIENTO,"En mantenimiento")
    ]
    estado = models.CharField(max_length=16, choices=tipo_estado,default=BUEN_ESTADO)
    descripcion_del_estado = models.CharField(max_length=200,blank=True)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    fecha_De_mantenimiento = models.ForeignKey(Fecha,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
class Alambrado(models.Model):
    cant_kilometros = models.FloatField()
    materiales = models.CharField(max_length=40)
    BUEN_ESTADO = "BUEN_ENSTADO"
    MAL_ESTADO = "MAL_ESTADO"
    EN_MANTENIMIENTO = "EN_MANTENIMIENTO"
    tipo_estado = [
        (BUEN_ESTADO,"Buen estado"),
        (MAL_ESTADO,"Mal estado"),
        (EN_MANTENIMIENTO,"En mantenimiento"),
    ]
    estado = models.CharField(max_length=16, choices=tipo_estado,default=BUEN_ESTADO)
    seccion = models.ManyToManyField(Seccion) 
    def __str__(self):
        return ("{}".format(self.seccion))