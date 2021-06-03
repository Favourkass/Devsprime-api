from django.contrib import admin
from db.models import user, learner



admin.site.register(user.User)
admin.site.register(learner.LearnerProfile)
