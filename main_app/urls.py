from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/', views.characters_index, name='index'),
  path('characters/<int:character_id>/', views.characters_detail, name='detail'),
  path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
  path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
  path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),
  path('characters/<int:character_id>/add_healing', views.add_healing, name='add_healing'),
  path('characters/<int:character_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon'),
  path('characters/<int:character_id>/unassoc_weapon/<int:weapon_id>/', views.unassoc_weapon, name='unassoc_weapon'),
  path('weapons/', views.WeaponList.as_view(), name='weapons_index'),
  path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapons_detail'),
  path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
  path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
  path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
]