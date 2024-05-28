from django.db import models
# from shops.models import Shop


# class Product(models.Model):
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=30)
#     image = models.ImageField()
#     # user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='product')

#     def __str__(self):
#             return self.title



# # class Meta:
# #     db_table = product





# class Product(models.Model):
#     shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
