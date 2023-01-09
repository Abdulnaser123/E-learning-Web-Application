from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # teacher
    path('teacher/', views.TeacherList.as_view()),

    path('student-assignment/<int:teacher_id>/<int:student_id>',
         views.AssignmentsList.as_view()),
    path('my-assignments/<int:studentId>', views.MyAssignmentsList.as_view()),

    path('update-assignments/<int:pk>', views.UpdateAssignmentsList.as_view()),

    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login', views.teacher_login),
    path('student-login', views.student_login),
    path('student-enroll-course/', views.StudentEnrollCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>/',
         views.fetch_enroll_status),
    path('fetch-enrolled-students/<int:course_id>/',
         views.StudentEnrollStudentList.as_view()),
    path('fetch-enrolled-courses/<int:student_id>/',
         views.StudentEnrollStudentList.as_view()),
    path('fetch-recommended-courses/<int:studentId>/', views.CourseList.as_view()),

    path('fetch-all-enrolled-students/<int:teacher_id>',
         views.StudentEnrollStudentList.as_view()),

    # category
    path('category/', views.CategoryList.as_view()),
    # course url
    path('course/', views.CourseList.as_view()),
    path('student/', views.StudentList.as_view()),

    path('course/<int:pk>', views.CourseDetailView.as_view()),
    path('chapter/', views.ChapterList.as_view()),

    path('chapter/<int:pk>', views.SpecificChapter.as_view()),
    path('course-chapters/<int:course_id>',
         views.CourseChaptersList.as_view()),

    path('teacher-courses/<int:teacher_id>',
         views.TeacherCourseList.as_view()),
    path('popular-courses/', views.CourseRatingList.as_view()),
    path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),
    path('rating/<int:course_id>', views.CourseRatingList.as_view()),
    path('rating-status/<int:student_id>/<int:course_id>/',
         views.fetch_rating_status),

    path('teacher/dashboard/<int:pk>', views.TeacherDashboard.as_view()),

    path('student/dashboard/<int:pk>', views.StudentDashboard.as_view()),
    path('student/fetch-all-notification/<int:student_id>/',
         views.NotificationsList.as_view()),
    path('save-notification/', views.NotificationsList.as_view()),
    path('quiz/', views.QuizList.as_view()),
    path('quiz/<int:pk>', views.QuizDetailList.as_view()),

    path('teacher-quiz/<int:teacher_id>', views.TeacherQuizList.as_view()),
    path('teacher-quiz-detail/<int:pk>', views.TeacherQuizDetail.as_view()),
    path('quizQuestions/<int:quiz_id>',
         views.QuizQuestionList.as_view()),
    path('quizQuestions/<int:quiz_id>/<int:limit>',
         views.QuizQuestionList.as_view()),
    path('quiz-assign-course/',
         views.AssignQuizCourseList.as_view()),
    path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>/',
         views.FetchQuizAssignStatus),


    path('fetch-assigned-quiz/<int:course_id>/',
         views.CourseQuizList.as_view()),
    path('fetch-quiz-attempt-status/<int:quiz_id>/<int:student_id>',
         views.FetchQuizAttemptStatus),
    path('attempt-quiz/', views.AttemptQuizList.as_view()),
    path('quizQuestions/<int:quiz_id>/next-question/<int:question_id>',
         views.QuizQuestionList.as_view()),

    path('search-courses/<str:searchString>',
         views.CourseList.as_view()),

    path('study-materials/<int:course_id>',
         views.StudyMaterialList.as_view()),

    path('study-material/<int:pk>',
         views.StudyMaterialDetailView.as_view()),
    path('attempted_students/<int:quiz_id>',
         views.AttemptQuizList.as_view()),


    path('fetch-quiz-result/<int:quiz_id_for_result>/<int:student_id>',
         views.fetch_quiz_result),
    path('update-view/<int:course_id>',
         views.update_view),
    path('popular-teachers/',
         views.TeacherList.as_view()),
    path('FAQs/',
         views.FAQsList.as_view()),

    path('verify-teacher/<int:teacher_id>',
         views.verify_teacher_via_otp),
    path('send-msg/<int:teacher_id>/<int:student_id>',
         views.save_teacher_student_msg),

    path('get-msg/<int:teacher_id>/<int:student_id>',
         views.MessageList.as_view()),
]
