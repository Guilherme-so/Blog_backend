from . import views
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', views.PostList, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.PostList.as_view() , name='listaCreate'),
#     path('<int:pk>/', views.PostDetail.as_view(), name='detailCreate'),
# ]