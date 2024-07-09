from django.urls import path
from .views import LectureView, DetailLectureView, LecturerView, CourseView, StudentLectureView, StudentDetailLectureView

urlpatterns = [
    path('lecturers/', LecturerView.as_view()),
    path('courses/', CourseView.as_view()),

    path('lectures/', LectureView.as_view()),
    path('lectures/<int:pk>/', DetailLectureView.as_view()),

    path('student-lectures/', StudentLectureView.as_view()),
    path('student-lectures/<int:pk>/', StudentDetailLectureView.as_view()),

]
