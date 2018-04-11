from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import (
    NamedBase, CostBase, TaskBase, ProductionBase, CategoryBase
)


class Species(NamedBase):
    plants_per_area = models.FloatField(
        help_text=_('per square meter')
    )


class SpeciesBase(models.Model):
    """ Abstract base class for elements relating to species. """

    class Meta:
        abstract = True

    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.species)


class SpeciesCostsCategory(CategoryBase):
    pass


class SpeciesCosts(SpeciesBase, CostBase):
    category = models.ForeignKey(
        SpeciesCostsCategory, on_delete=models.SET_NULL, null=True
    )


class SpeciesTaskCategory(CategoryBase):
    pass


class SpeciesTask(SpeciesBase, TaskBase):
    category = models.ForeignKey(
        SpeciesTaskCategory, on_delete=models.SET_NULL, null=True
    )


class SpeciesProduction(SpeciesBase, ProductionBase):
    pass
