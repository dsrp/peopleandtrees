from django.db import models
from django.utils.translation import gettext_lazy as _


class NamedMixin(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Product(NamedMixin):
    pass


class Species(NamedMixin):
    plants_per_area = models.FloatField()
    products = models.ManyToManyField(Product, through='SpeciesProduct')


class SpeciesProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    yield_per_plant = models.FloatField()

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class Culture(NamedMixin):
    species = models.ManyToManyField(Species, through='CultureSpecies')


class CultureSpecies(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    ratio = models.FloatField()


class Forest(NamedMixin):
    cultures = models.ManyToManyField(Culture, through='ForestCulture')


class ForestCulture(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE)

    area = models.FloatField()
