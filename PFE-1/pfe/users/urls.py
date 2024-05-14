from django.urls import path
from . import views
from django.contrib.auth import views as mdp

urlpatterns=[
    path('',views.connectas,name='connectas'),
    path('client/',views.connectasclient,name='connectasclient'),
    path('supervisor/',views.connectassupervisor,name='connectassupervisor'),
    path('reset_password/', mdp.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('reset_password_done/', mdp.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', mdp.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', mdp.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('_<str:pk>/',views.compte,name='compte'),
    path('<str:variable>/add_client/<str:pseudo>', views.compte, name='add_client')
]

# path('<str:variable>/map/<str:pseudo>',views.stocker_polygone,name='map')
# path('<str:variable>/map/<str:pseudo>', include('map.urls')),
# path('<str:pk>/map', include('map.urls')),


