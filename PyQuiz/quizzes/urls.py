from rest_framework import routers
from .api import QuizViewSet, QuestionViewSet, AnswerViewSet, SubmissionViewSet

router = routers.DefaultRouter()
router.register('api', QuizViewSet, 'quizzes')
router.register('question/api', QuestionViewSet, 'question')
router.register('answer/api', AnswerViewSet, 'answer')
router.register('submission/api', SubmissionViewSet, 'submission')

urlpatterns = router.urls
