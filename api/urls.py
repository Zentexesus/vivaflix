from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, WatchlistViewSet, signup, LoginView, LogoutView, upload_video, VideoListView, RegisterView, MyTokenObtainPairView, CollectionViewSet, MovieDetailView, MainPageView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'watchlist', WatchlistViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('upload/', upload_video, name='upload_video'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('videos/', VideoListView.as_view(), name='video_list'),
    path('movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('mainpage/', MainPageView.as_view(), name='mainpage'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
