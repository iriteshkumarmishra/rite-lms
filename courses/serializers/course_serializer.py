from rest_framework import serializers

from courses.models.course import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'name', 'slug', 'featured_image_url', 'instructions', 'credits',
            'is_archived', 'status', 'min_passing_percentage', 'certificate_template_id',
            'grading_rules', 'duration_rules', 'duration_specific_date', 'duration_days',
            'created_by', 'updated_by', 'deleted_by'
        ]
        # fields = '__all__'
        read_only_fields = ['created_by', 'updated_by']


class EmptyCourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class CourseModuleSerialzer(serializers.Serializer):
    module_id = serializers.IntegerField()
    display_order = serializers.IntegerField()
    is_locked = serializers.BooleanField(default=False)
    drip_fixed_date = serializers.DateField(default=None)
    min_spent_hour = serializers.IntegerField(min_value=0, required=False)
    min_spent_min = serializers.IntegerField(min_value=0, required=False)


class CourseSaveSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[0, 1])
    name = serializers.CharField(max_length=255)
    grading_rules = serializers.IntegerField(default=0)
    credits = serializers.DecimalField(max_digits=3, decimal_places=2, default=None)
    modules = serializers.ListField(child=CourseModuleSerialzer())
    duration_rule = serializers.ChoiceField([0, 1, 2, 3])
    duration_specific_date = serializers.DateField(required=False)
    duration_days = serializers.IntegerField(required=False)
    certificate_expire_after = serializers.IntegerField(required=False)

    def validate(self, data):
        if data['duration_rule'] == 1 and data.get('duration_specific_date') is None :
            raise serializers.ValidationError('duration_specific_date is required when duration_rule is on_specific_date')
        
        if data['duration_rule'] in [2, 3] and data.get('duration_days') is None :
            raise serializers.ValidationError('duration_days is required when duration_rule is after days')
        
        return data



