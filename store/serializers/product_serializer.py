from rest_framework import serializers

from courses.models.course import Course

class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=500)
    slug = serializers.CharField(max_length=500)
    description = serializers.CharField()
    image_url = serializers.CharField(max_length=255)
    regular_price = serializers.DecimalField(max_digits=5, decimal_places=2)
    sale_price = serializers.DecimalField(max_digits=5, decimal_places=2)
    status = serializers.IntegerField()
    expired_at = serializers.DateTimeField()
    seo_title = serializers.CharField(max_length=500)
    seo_description = serializers.CharField(max_length=500)
    author = serializers.CharField(required=True) # Add required=True here later
    created_at = serializers.DateTimeField()



class ProductSaveSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField()
    image_url = serializers.URLField(required=False)
    regular_price = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    sale_price = serializers.DecimalField(max_digits=5, decimal_places=2)
    status = serializers.ChoiceField(choices=[1, 2, 3], default=2)
    expired_at = serializers.DateTimeField(required=False)
    seo_title = serializers.CharField(max_length=500, required=False)
    seo_description = serializers.CharField(max_length=500, required=False)
    courses = serializers.ListField(child=serializers.IntegerField(), min_length=1)


    def validate(self, data):
        user = self.context['request'].user
        courses = (Course.objects
                   .filter(id__in=data.get('courses'))
                   .filter(created_by_id=user))
        
        course_count = courses.count()
        requested_course_count = len(data.get('courses'))

        if course_count != requested_course_count:
            raise serializers.ValidationError('Course given is invalid!')

        return data
