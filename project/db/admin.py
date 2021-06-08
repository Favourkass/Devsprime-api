from django.contrib import admin
from db.models import user, learner, instructors
from .models.instructor_course import CourseType, CourseCategory, Course


admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(CourseType)
admin.site.register(user.User)
admin.site.register(learner.LearnerProfile)
admin.site.register(instructors.Instructor)
