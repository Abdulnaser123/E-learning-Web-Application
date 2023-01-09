from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Teacher)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.Student)
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.CourseRating)
admin.site.register(models.StudentAssignment)
admin.site.register(models.NotificationModel)
admin.site.register(models.Quiz)
admin.site.register(models.QuizQuestions)
admin.site.register(models.CourseQuiz)
admin.site.register(models.AttemptQuiz)
admin.site.register(models.studyMaterials)
admin.site.register(models.FAQ)
admin.site.register(models.TeacherStudentChat)
