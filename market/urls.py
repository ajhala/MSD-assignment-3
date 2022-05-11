from django.urls import path
from .views import *


app_name = 'market'

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path('produce_list', ProduceListView.as_view(), name='produce_list'),
    path('produce_list1', ProduceListView1.as_view(), name='produce_list1'),
    path('<int:pk>/edit/', ProduceUpdateView.as_view(), name='produce_edit'),
    path('<int:pk>/delete/', ProduceDeleteView.as_view(), name='produce_delete'),
    path('new/', ProduceCreateView.as_view(), name='produce_new'),
    path('view_pdf', view_pdf, name='view_pdf'),

    path('change-password/', ChangePwView.as_view(), name='change_password'),
    path('password-reset/', PwResetView.as_view(), name='pw_reset'),
    path('password-reset/done/', PwResetDoneView.as_view(), name='pw_reset_done'),
    path('reset/<uidb64>/<token>/', PwResetConfirmView.as_view(), name='pw_reset_confirm'),
    path('reset/done/', PwResetCompleteView.as_view(), name='pw_reset_complete'),

]