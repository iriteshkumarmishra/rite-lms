from modules.models.module import Module
from modules.models.text_module import TextModule

class TextModuleService():

    def create_text_module(self, data, request):
        module = Module()
        module.name =data.get('name')
        module.slug =data.get('slug')
        module.description = data.get('description')
        module.type = Module.TYPE_TEXT
        module.created_by = request.user
        module.save()

        text_module = TextModule()
        text_module.module_id = module
        text_module.track_completion = data.get('track_completion') if data.get('track_completion') else False
        text_module.created_by = request.user
        text_module.save()

        return module

        