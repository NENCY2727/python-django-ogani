from django.contrib import admin # type: ignore
from .models import*
from .models import User

# Register your models here.
admin.site.register(Employee)
admin.site.register(User)
admin.site.register(department)
admin.site.register(colorfilter)
admin.site.register(product)
admin.site.register(size)
admin.site.register(Wishlist)
admin.site.register(cart)


