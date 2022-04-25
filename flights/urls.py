from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flight', FlightViewset)
router.register('passenger', PassengerViewset)
router.register('reservation', ReservationViewset)


urlpatterns = [
    path('flight-services/', include(router.urls)),
    path('flight-services/find-flight/', findFlight),
    path('flight-services/save-reservation/', save_reservation),
]