from django.urls import path
from . import views

app_name = 'users_'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('user_register_action/', views.user_register_action, name='user_register_action'),
    path('user_data_view/', views.user_data_view, name='user_data_view'),
    path('linear_regression/', views.linear_regression, name="linear_regression"),
    path('decision_tree/', views.decision_tree, name="decision_tree"),
    path('random_forest/', views.random_forest, name="random_forest"),
    path('support_vector_classifier/', views.support_vector_classifier, name="support_vector_classifier"),
    path('naive_bayes/', views.naive_bayes, name="naive_bayes"),
    path('k_nearest_neighbour/', views.k_nearest_neighbour, name="k_nearest_neighbour"),
    path('ann_results/', views.ann_results, name="ann_results"),
    path('user_prediction/', views.user_prediction, name="user_prediction"),


]
