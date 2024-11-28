from django.db import models
from django.conf import settings
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
import pint 

User = settings.AUTH_USER_MODEL

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    
    """def get_absolute_url(self):
        return "/pantry/recipes"""


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True )
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    
    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)  

    def convert_to_system(self, system=None):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement

    def as_mks(self):
        measurement = self.convert_to_system(system='mks')
        return measurement.to('kilogram')

    def as_imperial(self):
        measurement = self.convert_to_system(system='imperial')
        return measurement.to('pound')