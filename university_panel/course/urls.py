from django.urls import path
from .views import LectureView, DetailLectureView, LecturerView, CourseView, StudentDetailLectureView

urlpatterns = [
    path('lecturers/', LecturerView.as_view()),
    path('courses/', CourseView.as_view()),

    path('lectures/', LectureView.as_view()),
    path('lectures/<int:pk>/', DetailLectureView.as_view()),

    path('student-lectures/', StudentDetailLectureView.as_view()),

]
