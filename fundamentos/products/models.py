from django.db import models

'''
# Create as tabelas no banco de dados.
 # No Django, o slug é uma string que 
 identifica uma página do site de forma
 amigável para os humanos. Ele é usado 
 para otimizar a URL e melhorar a relevância 
 da página nos mecanismos de busca.
'''

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    slug = models.SlugField()
    banner = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
