from django.urls import path
from . import views

urlpatterns = [
    path('comments/<str:video_id>', views.VideoComments.as_view()),
    path('comment/<int:pk>', views.CommentDetails.as_view())
]