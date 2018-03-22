from django.db import models
from django.utils.translation import ugettext_lazy
from places.models import Place
from labels.models import Label
from regions.models import Region


class PrisonStation(models.Model):
    name = models.CharField(
        max_length=200, help_text="Bezeichnung des Gefangenenlagers",
        verbose_name=ugettext_lazy("Kriegsgefangenenlager")
        )
    alt_name = models.ManyToManyField(
        Label, max_length=200, blank=True, help_text="weitere Bezeichnung für das Gefangenenlager",
        verbose_name=ugettext_lazy("alternative Ortsbezeichnung")
        )
    legacy_id = models.CharField(max_length=50, blank=True,
        help_text="Kennzeichen für das Gefangenenlager", verbose_name=ugettext_lazy("Kennzeichen")
        )
    located_in_place = models.ForeignKey(
        Place, blank=True, null=True, help_text="Ort, in dem das Gefangenenlager liegt",
        on_delete=None, verbose_name=ugettext_lazy("Ort des Lagers")
        )
    located_in_region = models.ForeignKey(
        Region, blank=True, null=True, help_text="Region, in der das Gefangenenlager liegt",
        on_delete=None, verbose_name=ugettext_lazy("Region des Lagers")
        )
    part_of = models.ForeignKey("self", blank=True, null=True,
        help_text="Lager, dessen Teil dieses Gefangenenlager ist",
        on_delete=None, verbose_name=ugettext_lazy("übergeordnetes Lager")
        )
    start_date = models.DateField(
        blank=True, null=True, help_text="Gründungsdatum des Gefangenenlagers",
        verbose_name=ugettext_lazy("Gründungsdatum")
        )
    end_date = models.DateField(
        blank=True, null=True, help_text="Auflösungsdatum des Gefangenenlagers",
        verbose_name=ugettext_lazy("Auflösungsdatum")
        )

    def __str__(self):
        return self.name
