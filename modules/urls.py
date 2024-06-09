from django.urls import path

from modules.views.modules_view import ModulesList
from modules.views.text_module_view import TextModuleList
from modules.views.video_module_view import VideoModuleList, VideoModuleDetails

urlpatterns = [
    path('', ModulesList.as_view(), name='modules-list'),
    path('text', TextModuleList.as_view(), name='text-modules-list'),
    # path('text/<int:id>', TextModuleList.as_view(), name='text-modules-details'),
    path('video', VideoModuleList.as_view(), name='video-modules-list'),
    path('video/<int:id>', VideoModuleDetails.as_view(), name='video-modules-details'),

]