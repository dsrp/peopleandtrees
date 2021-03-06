from django.db import models
from django.utils.translation import gettext_lazy as _


class NamedBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class CategorizedYearBase(models.Model):
    """
    Base model for elements relating to a year, having a category field.
    """

    class Meta:
        abstract = True

    year = models.IntegerField(db_index=True)

    def __str__(self):
        print('lalalalals')
        assert hasattr(self, 'category')

        return '{0} - year {1}'.format(str(self.category), self.year)


class CategoryBase(NamedBase):
    """ Abstract base class for categories. """

    class Meta:
        abstract = True


class CostCategoryBase(CategoryBase):
    """ ABS for cost categories. """

    class Meta:
        abstract = True
        verbose_name = _('cost category')
        verbose_name_plural = _('cost categories')


class LabourCategoryBase(CategoryBase):
    """ ABS for labour categories. """

    class Meta:
        abstract = True
        verbose_name = _('labour category')
        verbose_name_plural = _('labour categories')


class CostBase(CategorizedYearBase):
    class Meta:
        abstract = True
        verbose_name = _('costs')
        verbose_name_plural = _('costs')

    amount = models.FloatField()


class LabourBase(CategorizedYearBase):
    class Meta:
        abstract = True
        verbose_name = _('labour')
        verbose_name_plural = _('labour')

    amount = models.FloatField()


class ProductionBase(CategorizedYearBase):
    class Meta:
        abstract = True
        verbose_name = _('production')
        verbose_name_plural = _('productions')

    amount = models.FloatField()
