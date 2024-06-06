from django.urls import path
from .views import LectureView, DetailLessonView, LecturerView, CourseView, StudentDetailLessonsView

urlpatterns = [
    path('lecturers/', LecturerView.as_view()),
    path('courses/', CourseView.as_view()),

    path('lessons/', LectureView.as_view()),
    path('lessons/<int:pk>/', DetailLessonView.as_view()),

    path('student-lessons/', StudentDetailLessonsView.as_view()),

]
