from django.contrib import admin
from db.models import user, learner, instructors

admin.site.register(user.User)
admin.site.register(learner.LearnerProfile)
admin.site.register(instructors.Instructor)
