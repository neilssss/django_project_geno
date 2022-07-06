from django.contrib import admin
from .models import Members
from .models import Fish
from .models import Fish2
from .models import Cart
from .models import Wishlist
from .models import Order
from .models import OrderItem
from .models import Profile

admin.site.register(Members)
admin.site.register(Fish)
admin.site.register(Fish2)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)

# Register your models here.
