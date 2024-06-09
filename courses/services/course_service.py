from django.db import transaction

from courses.models.course import Course
from courses.models.course_module import CourseModule
from modules.models.module import Module

class CourseService():
    
    def create_course(self, data, user):
        response = {
            'success': True,
            
        }
        course = Course()
        try:
            with transaction.atomic():
            # we are in DB transaction to create course and it's modules together
                course.name = data['name']
                course.status = data['status']
                course.credits = data['credits']
                course.created_by = user
                course.save()

                # Now saving course_modules table data
                for module in data.get('modules'):
                    module_object = Module.objects.get(pk=module['module_id'])
                    course_module = CourseModule()
                    course_module.course = course
                    course_module.module = module_object
                    course_module.display_order = module['display_order']
                    course_module.is_locked = module['is_locked']
                    course_module.drip_fixed_date = module['drip_fixed_date']
                    hour = module.get('min_spent_hour') * 3600 if module.get('min_spent_hour') else 0
                    min = module.get('min_spent_min') * 60 if module.get('min_spent_min') else 0
                    course_module.min_spent_time = hour + min
                    course_module.created_by = user
                    course_module.updated_by = user
                    course_module.save()
                
                response['course'] = course

        except Exception as e:
            response['success'] = False
            print(e)
        
        return response

