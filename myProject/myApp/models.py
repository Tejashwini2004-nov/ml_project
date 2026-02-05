from django.db import models

class EcommerceSalesAudit(models.Model):
    profit = models.FloatField()
    predicted_sales = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profit: {self.profit} → Sales: {self.predicted_sales}"

