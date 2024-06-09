from modules.models.module import Module
from modules.models.video_module import VideoModule

class VideoService():
    
    def create_module(self, data, request):
        module = Module()
        module.name = data.get('name')
        module.slug = data.get('slug')
        module.description = data.get('description')
        module.type = Module.TYPE_VIDEO
        module.created_by = request.user
        module.save()

        video_module = VideoModule()
        video_module.module_id = module
        video_module.url = data.get('url')
        video_module.cover_url = data.get('cover_url')
        video_module.provider = data.get('provider')
        video_module.track_completion = data.get('track_completion') if data.get('track_completion') else False
        video_module.disable_skip = data.get('disable_skip') if data.get('disable_skip') else False
        video_module.created_by = request.user
        video_module.save()

        return module