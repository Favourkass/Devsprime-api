from django.contrib import admin
from db.models import (user, learner, instructors,
                       course, course_type, course_category)


admin.site.register(course.Course)
admin.site.register(course_category.CourseCategory)
admin.site.register(course_type.CourseType)
admin.site.register(user.User)
admin.site.register(learner.LearnerProfile)
admin.site.register(instructors.Instructor)
