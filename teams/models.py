from django.db import models


class Team(models.Model):

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
        )

    titles = models.IntegerField(
        default=0,
        null=True
        )

    top_scorer = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )

    fifa_code = models.CharField(
        max_length=3,
        unique=True,
        null=False,
        blank=False
        )

    founded_at = models.DateField(
        null=True
        )

    def __repr__(self) -> str:

        return f"<{[self.pk]} {self.name} - {self.fifa_code}>"
