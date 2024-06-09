from django.db import transaction

from store.models import Product, ProductCourse
from courses.models.course import Course

class ProductService():
    
    def create_product(self, data, user):
        response = {
            'success': True,
        }

        product = Product()
        try:
            courses = Course.objects.filter(id__in=data.get('courses'))
            with transaction.atomic():
                product.title = data.get('title')
                product.slug = data.get('slug')
                product.description = data.get('description')
                product.image_url = data.get('image_url')
                product.regular_price = data.get('regular_price')
                product.sale_price = data.get('sale_price')
                product.status = data.get('status')
                product.expired_at = data.get('expired_at')
                product.seo_title = data.get('seo_title')
                product.seo_description = data.get('seo_description')
                product.created_by = user
                product.updated_by = user
                product.save()

                # now have to save relation data between product and course
                for course in courses:
                    product_course = ProductCourse()
                    product_course.product = product
                    product_course.course = course
                    product_course.created_by = user
                    product_course.save()

        except Exception as e:
            response['success'] = False
        
        return response


    def get_product(self, id):
        product = Product.objects.filter(id=id).first()
        return product
    
    def update_product(self, product, data, user):
        response = {
            'success': True
        }
        courses = Course.objects.filter(id__in=data.get('courses'))

        try:
            with transaction.atomic():
                product.title = data.get('title')
                product.slug = data.get('slug')
                product.description = data.get('description')
                product.image_url = data.get('image_url')
                product.regular_price = data.get('regular_price')
                product.sale_price = data.get('sale_price')
                product.status = data.get('status')
                product.expired_at = data.get('expired_at')
                product.seo_title = data.get('seo_title')
                product.seo_description = data.get('seo_description')
                product.created_by = user
                product.updated_by = user
                product.save()

                # now save product_courses, first delete all existing and then create new ones.
                product.course_product.all().delete()

                for course in courses:
                    product_course = ProductCourse()
                    product_course.product = product
                    product_course.course = course
                    product_course.created_by = user
                    product_course.save()
        
        except Exception as e:
            response['success'] = False
        
        return response


