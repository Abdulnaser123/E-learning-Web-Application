from django.db import models
from django.core import serializers
# Create your models here.
# Teacher model


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    skills = models.TextField()
    profile_img = models.ImageField(
        upload_to='teacher_profile_imgs/', null=True)
    verify_status = models.BooleanField(default=False)
    otp_digit = models.CharField(max_length=10, null=True)
    # profile_img = models.ImageField(upload_to='teacher_imgs/',null=True)

    # ['full_name','email','password','qualification','mobile_no','skills']
    class Meta:
        verbose_name_plural = "1. Teacher"

    def skill_list(self):
        skill_list = self.skills.split(',')
        return skill_list

    def total_courses(self):
        total_courses = Course.objects.filter(teacher=self).count()
        return total_courses

    def total_chapters(self):
        total_chapters = Chapter.objects.filter(course__teacher=self).count()
        return total_chapters

    def total_students(self):
        total_students = StudentCourseEnrollment.objects.filter(
            course__teacher=self).count()
        return total_students

    # Course category model


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "2. Course Categories"

    def __str__(self):
        return self.title
# course model


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='teacher_courses')
    featured_img = models.ImageField(upload_to='course_imgs/', null=True)
    techs = models.TextField(null=True)
    course_views = models.BigIntegerField(default=0)

    class Meta:
        verbose_name_plural = "3. Course"

    def related_videos(self):
        related_videos = Course.objects.filter(techs__icontains=self.techs)
        return serializers.serialize('json', related_videos)

    def __str__(self):
        return self.title

    def total_enrolled_students(self):
        total_enrolled_students = StudentCourseEnrollment.objects.filter(
            course=self).count()
        return total_enrolled_students

    def course_rating(self):
        course_rating = CourseRating.objects.filter(
            course=self).aggregate(models.Avg('rating'))
        return course_rating
# course model


class Chapter(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150)
    description = models.TextField()
    video = models.FileField(upload_to='chapter_videos', null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "4. Chapters"

    # student model


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    interested_categories = models.TextField()

    def __str__(self):
        return self.full_name

    def enrolled_courses(self):
        total_courses = StudentCourseEnrollment.objects.filter(
            student=self).count()
        return total_courses

    def pending_assignments(self):
        pending_assignment = StudentAssignment.objects.filter(
            student=self, student_status=False).count()
        return pending_assignment

    def complete_assignment(self):
        complete_assignment = StudentAssignment.objects.filter(
            student=self, student_status=True).count()
        return complete_assignment

    class Meta:
        verbose_name_plural = "5. Students"


class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='enrolled_courses')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='enrolled_student')
    enrolled_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '6. Enrolled  Course'

    def __str__(self):
        return f"{self.course} - {self.student}"


class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    rating = models.PositiveBigIntegerField(default=0)
    review = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"

    class Meta:
        verbose_name_plural = "8. Course Rating"


class StudentAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    student_status = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name_plural = "9. Student Assignment"

# Notifications Model


class NotificationModel(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    notif_for = models.CharField(
        max_length=200, verbose_name='Notification For')
    notif_subject = models.CharField(
        max_length=200, verbose_name='Notification Subject')
    notif_created_time = models.DateTimeField(
        auto_now_add=True, verbose_name='Notification Time')
    notif_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "10. Notifications Assignment"


class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def assign_status(self):
        return CourseQuiz.objects.filter(quiz=self).count()

    class Meta:
        verbose_name_plural = "11. Quiz"


class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    rightAns = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "12. Quiz Questions"

# add quiz to course


class CourseQuiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "13. Course Quiz"


class AttemptQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(
        QuizQuestions, on_delete=models.CASCADE, null=True)
    right_ans = models.CharField(max_length=200, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "14. Attempt Quiz"


class studyMaterials(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    upload = models.ImageField(upload_to='study_materials/', null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "15. Study material"


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "16. FAQ page "


class TeacherStudentChat(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    msg_text = models.TextField()
    msg_from = models.CharField(max_length=100)
    msg_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "17. teacher student messages "
