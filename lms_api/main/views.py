# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeacherSerializer, teacherStudentChatSerializer, StudyMaterialSerializer, FAQsSerializer, AttemptQuizSerializer, CourseQuizSerializer, AssignQuizCourseSerializer, QuizQuestionSerializer, NotificationSerializer, QuizSerializer, StudentDashboardSerializer, StudentAssignmentSerializer, CourseRatingSerializer, TeacherDashboardSerializer, StudentCourseEnrollSerializer, CategorySerializer, CourseSerializer, ChapterSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
from . import models
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer


def get_queryset(self):
    if 'popular' in self.request.GET:
        sql = 'select *,count(c.id) as total_course from main_teacher as t  inner join main_course as c on c.teacher_id=t.id group by  t.id order by total_course desc'
    return models.Teacher.objects.raw(sql)
    # permission_classes = [IsAuthenticated] # permission class changed


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAuthenticated] # permission class changed


@csrf_exempt
def teacher_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        teacherData = models.Teacher.objects.get(
            email=email, password=password)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        if not teacherData.verify_status:
            return JsonResponse({'bool': False, 'teacher_id': teacherData.id, 'msg': 'account is not verified'})
        else:
            return JsonResponse({'bool': True, 'teacher_id': teacherData.id})
    else:
        return JsonResponse({'bool': False, 'msg': 'invalid email or password'})
    # sudent login


@csrf_exempt
def verify_teacher_via_otp(request, teacher_id):
    otp_digit = request.POST.get('otp_digit')
    verified = models.Teacher.objects.filter(
        id=teacher_id, otp_digit=otp_digit).first()

    if verified:
        models.Teacher.objects.filter(
            id=teacher_id, otp_digit=otp_digit).update(verify_status=True)
        return JsonResponse({'bool': True, 'teacher_id': verified.id})

    else:
        return JsonResponse({'bool': False, 'teacher_id': verified.id})


@csrf_exempt
def student_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        studentData = models.Student.objects.get(
            email=email, password=password)
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        return JsonResponse({'bool': True, 'student_id': studentData.id})
    else:
        return JsonResponse({'bool': False})


def fetch_enroll_status(request, student_id, course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    enrollStatus = models.StudentCourseEnrollment.objects.filter(
        course=course, student=student).count()
    if enrollStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


def fetch_rating_status(request, student_id, course_id):
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    ratingStatus = models.CourseRating.objects.filter(
        course=course, student=student).count()
    if ratingStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated] # permission class changed


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'student' in self.kwargs:
            student_id = self.kwargs['studentId']
            student = models.Student.objects.get(pk=student_id)
            queries = [Q(techs__iendswith=value)
                       for value in student.interested_categories]
            query = queries.pop()
            for item in queries:
                query |= item
            qs = models.Course.objects.filter(query)

        if 'searchString' in self.kwargs:
            search = self.kwargs['searchString']
            qs = models.Course.objects.filter(
                Q(title__icontains=search) | Q(techs__icontains=search))
        return qs
    # permission_classes = [IsAuthenticated] # permission class changed


class TeacherCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        try:
            teacher = models.Teacher.objects.get(pk=teacher_id)
        except TeacherList.DoesNotExist:
            teacher = None
        return models.Course.objects.filter(teacher=teacher)


class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = models.Course.objects.all()
# course chapters List


class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


class CourseChaptersList(generics.ListCreateAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class SpecificChapter(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated] # permission class changed


class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer
    # permission_classes = [IsAuthenticated] # permission class changed


class StudentEnrollStudentList(generics.ListAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer
    # permission_classes = [IsAuthenticated] # permission class changed

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            return models.StudentCourseEnrollment.objects.filter(course=course)
        elif 'teacher_id' in self.kwargs:
            teacher_id = self.kwargs['teacher_id']
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
        elif 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(student=student).distinct()
        elif 'studentId' in self.kwargs:
            student_id = self.kwargs['studentId']
            student = models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(course__techs__icontains=student.interested_categories)


class CourseRatingList(generics.ListCreateAPIView):
    queryset = models.CourseRating.objects.all()
    serializer_class = CourseRatingSerializer

    def get_queryset(self):
        if 'popular' in self.request.GET:
            print('---------...-----------')
            sql = 'select *,AVG(cr.rating) as avg_rating from main_courserating as cr inner join main_course as c on  cr.course_id=c.id group by c.id  order by avg_rating desc limit 4'
            return models.CourseRating.objects.raw(sql)
        if 'all' in self.request.GET:
            sql = 'select *,AVG(cr.rating) as avg_rating from main_courserating as cr inner join main_course as c on  cr.course_id=c.id group by c.id  order by avg_rating desc limit 4'
            return models.CourseRating.objects.raw(sql)


class TeacherDashboard(generics.RetrieveAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherDashboardSerializer


class StudentDashboard(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentDashboardSerializer


class AssignmentsList(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        teacher_id = self.kwargs['teacher_id']
        student = models.Student.objects.get(pk=student_id)
        teacher = models.Teacher.objects.get(pk=teacher_id)

        return models.StudentAssignment.objects.filter(student=student, teacher=teacher)


class MyAssignmentsList(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        student_id = self.kwargs['studentId']
        student = models.Student.objects.get(pk=student_id)
        models.NotificationModel.objects.filter(
            student=student, notif_for='student', notif_subject='assignment').update(notif_status=True)
        return models.StudentAssignment.objects.filter(student=student)


class UpdateAssignmentsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer


class NotificationsList(generics.ListCreateAPIView):
    queryset = models.NotificationModel.objects.all()
    serializer_class = NotificationSerializer

    # def get_queryset(self):
    #     if 'student_id' in self.kwargs:
    #         student_id=self.kwargs['student_id']
    #         student=models.Student.objects.get(pk=student_id)
    #         return models.NotificationModel.objects.filter(student=student,notif_for='student',notif_subject='assignment',notif_status=False)


class QuizList(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = [IsAuthenticated] # permission class changed


def FetchQuizAssignStatus(request, quiz_id, course_id):
    quiz = models.Quiz.objects.filter(id=quiz_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    assignStatus = models.CourseQuiz.objects.filter(
        course=course, quiz=quiz).count()
    if assignStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class QuizDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = [IsAuthenticated] # permission class changed


class TeacherQuizList(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        try:
            teacher = models.Teacher.objects.get(pk=teacher_id)
        except TeacherList.DoesNotExist:
            teacher = None
        return models.Quiz.objects.filter(teacher=teacher)


class TeacherQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = models.Quiz.objects.all()


class QuizQuestionList(generics.ListCreateAPIView):
    serializer_class = QuizQuestionSerializer

    def get_queryset(self):
        quizId = self.kwargs['quiz_id']
        quiz = models.Quiz.objects.get(pk=quizId)
        if 'limit' in self.kwargs:
            return models.QuizQuestions.objects.filter(quiz=quiz).order_by('id')[:1]
        elif 'question_id' in self.kwargs:
            current_question = self.kwargs['question_id']
            return models.QuizQuestions.objects.filter(quiz=quiz, id__gt=current_question).order_by('id')[:1]
        else:
            return models.QuizQuestions.objects.filter(quiz=quiz)


class AssignQuizCourseList(generics.ListCreateAPIView):
    queryset = models.CourseQuiz.objects.all()
    serializer_class = AssignQuizCourseSerializer


class CourseQuizList(generics.ListCreateAPIView):
    queryset = models.CourseQuiz.objects.all()
    serializer_class = CourseQuizSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            return models.CourseQuiz.objects.filter(course=course)


class AttemptQuizList(generics.ListCreateAPIView):
    queryset = models.AttemptQuiz.objects.all()
    serializer_class = AttemptQuizSerializer

    def get_queryset(self):
        if 'quiz_id' in self.kwargs:
            quiz_id = self.kwargs['quiz_id']
            quiz = models.Quiz.objects.get(pk=quiz_id)
            return models.AttemptQuiz.objects.raw(f'select * from  main_attemptquiz WHERE quiz_id={int(quiz_id)} group by student_id')


def fetch_quiz_result(request, quiz_id_for_result, student_id):
    quiz = models.Quiz.objects.filter(id=quiz_id_for_result).first()
    student = models.Student.objects.filter(id=student_id).first()
    attemptStatus = models.AttemptQuiz.objects.filter(
        student=student, question__quiz=quiz).count()
    if attemptStatus > 0:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


def fetch_quiz_result(request, quiz_id_for_result, student_id):
    quiz = models.Quiz.objects.filter(id=quiz_id_for_result).first()
    student = models.Student.objects.filter(id=student_id).first()
    total_questions = models.QuizQuestions.objects.filter(quiz=quiz).count()
    total_attempted_questions = models.AttemptQuiz.objects.filter(
        quiz=quiz, student=student).values('student').count()
    attempted_questions = models.AttemptQuiz.objects.filter(
        quiz=quiz, student=student)
    total_correct_questions = 0
    for attempt in attempted_questions:
        if attempt.right_ans == attempt.question.rightAns:
            total_correct_questions += 1
    return JsonResponse({'total_questions': total_questions, 'total_attempted_questions': total_attempted_questions, 'total_correct_questions': total_correct_questions})


def FetchQuizAttemptStatus(request, quiz_id, student_id):
    quiz = models.Quiz.objects.filter(id=quiz_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    AttemptStatus = models.AttemptQuiz.objects.filter(
        student=student, question__quiz=quiz).count()
    if AttemptStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class StudyMaterialList(generics.ListCreateAPIView):
    serializer_class = StudyMaterialSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.studyMaterials.objects.filter(course=course)


class StudyMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.studyMaterials.objects.all()
    serializer_class = StudyMaterialSerializer


def update_view(request, course_id):
    queryset = models.Course.objects.filter(pk=course_id).first()
    queryset.course_views += 1
    queryset.save()
    return JsonResponse({'views': queryset.course_views})


class FAQsList(generics.ListAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = FAQsSerializer


@csrf_exempt
def save_teacher_student_msg(request, teacher_id, student_id):
    teacher = models.Teacher.objects.get(id=teacher_id)
    student = models.Student.objects.get(id=student_id)
    msg_text = request.POST.get('msg_text')
    msg_from = request.POST.get('msg_from')
    msgRes = models.TeacherStudentChat.objects.create(
        teacher=teacher,
        student=student,
        msg_text=msg_text,
        msg_from=msg_from
    )
    if msgRes:
        return JsonResponse({'msg': 'msg has been send'})


class MessageList (generics.ListAPIView):
    queryset = models.TeacherStudentChat.objects.all()
    serializer_class = teacherStudentChatSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        student_id = self.kwargs['student_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        student = models.Student.objects.get(pk=student_id)
        return models.TeacherStudentChat.objects.filter(student=student, teacher=teacher)
