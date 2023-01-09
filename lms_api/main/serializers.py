from rest_framework import serializers
from . import models
from django.core.mail import send_mail


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'password', 'qualification',
                  'mobile_no', 'skills', 'profile_img', 'verify_status', 'otp_digit', 'teacher_courses', 'total_courses']

    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

    def create(self, validate_date):
        instance = super(TeacherSerializer, self).create(validate_date)
        otp_digit = self.validated_data['otp_digit']
        print(otp_digit)
        return instance
    # def create(self, validate_date):
    #     email = self.validated_data['email']
    #     otp_digit = self.validated_data['otp_digit']
    #     instance = super(TeacherSerializer, self).create(validate_date)
    #     send_mail(
    #         'verify account',
    #         'please verify account',
    #         'apedopaid.com@gmail.com',
    #         [email],
    #         fail_silently=False,
    #         html_message=f'<p>your otp is : </p><p>{otp_digit}</p>'
    #     )
    #     return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title', 'description', 'featured_img', 'techs',
                  'course_chapters', 'related_videos', 'total_enrolled_students', 'course_rating']
        depth = 1


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id', 'course', 'title', 'description', 'video', 'remarks']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['full_name', 'email', 'password',
                  'username', 'interested_categories']
        depth = 1


class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ['course', 'student', 'enrolled_time']
        # depth=1

    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2
    #     depth=1


class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ['id', 'course', 'student', 'rating', 'review', 'review_time']

    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['total_courses', 'total_chapters', 'total_students']


class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['enrolled_courses',
                  'pending_assignments', 'complete_assignment']


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAssignment
        fields = ['id', 'teacher', 'student',
                  'title',
                  'detail', 'student_status', 'add_time']

    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2
    #     depth=1


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotificationModel
        fields = ['teacher', 'student',
                  'notif_subject',
                  'notif_for']
        depth = 1

    def __init__(self, *args, **kwargs):
        super(NotificationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ['id', 'teacher', 'title',
                  'detail', 'assign_status', 'add_time']

    def __init__(self, *args, **kwargs):
        super(QuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class CourseQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseQuiz
        fields = ['id', 'teacher', 'course',
                  'quiz',  'add_time']

    def __init__(self, *args, **kwargs):
        super(CourseQuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestions
        fields = ['id', 'quiz', 'question', 'ans1',
                  'ans2', 'ans3', 'ans4', 'rightAns']

    def __init__(self, *args, **kwargs):
        super(QuizQuestionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        depth = 1


class AssignQuizCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseQuiz
        fields = ['teacher', 'course',  'quiz', 'add_time']
        # depth=1

    def __init__(self, *args, **kwargs):
        super(AssignQuizCourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2
    #     depth=1


class AttemptQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttemptQuiz
        fields = ['id', 'student', 'quiz',
                  'question', 'right_ans', 'add_time']
        depth = 5

    def __init__(self, *args, **kwargs):
        super(AttemptQuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2
    #     depth=1


class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.studyMaterials
        fields = ['id', 'course', 'title', 'description', 'upload', 'remarks']

    def __init__(self, *args, **kwargs):
        super(StudyMaterialSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ['id', 'question', 'answer']


class teacherStudentChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherStudentChat
        fields = ['id', 'teacher', 'student',
                  'msg_from', 'msg_text', 'msg_time']
