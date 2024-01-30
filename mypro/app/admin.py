from django.contrib import admin

from .models import Watch
from .models import CartItem
from .models import Checkout
admin.site.register(Watch)
admin.site.register(CartItem)
admin.site.register(Checkout)
# Register your models here.
