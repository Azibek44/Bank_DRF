from django.urls import path
from .views import CreateTransferView


urlpatterns = [
    path('historytransfer/', CreateTransferView.as_view(), name = "history_transfer"),

]
