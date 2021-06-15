from django.contrib import admin
from db.models import (user, learner, instructors,
                       course, course_type, 
                       course_category, order_status,
                       blogs, comment, contact, reply, orders
                       ,learner_course)



admin.site.register(course.Course)
admin.site.register(course_category.CourseCategory)
admin.site.register(course_type.CourseType)
admin.site.register(user.User)
admin.site.register(learner.LearnerProfile)
admin.site.register(instructors.Instructor)

admin.site.register(blogs.Blog)
admin.site.register(comment.Comment)
admin.site.register(reply.Reply)
admin.site.register(contact.Contact)
admin.site.register(order_status.OrderStatus)
admin.site.register(orders.Order)
admin.site.register(learner_course.LearnerCourse)
