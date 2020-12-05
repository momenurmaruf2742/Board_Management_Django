from django.db import models


class RecruitInfo(models.Model):
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    height_cm = models.FloatField()

    class Meta:
        db_table = "recruit_info"

