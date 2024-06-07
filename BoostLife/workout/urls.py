from .views import *
from django.urls import path

urlpatterns = [
    path('backend/workout_list/', workout_list, name='workout_list'),
    path('backend/add_workout/add/', add_workout, name='add_workout'),
    path('backend/edit_workout/edit/<int:workout_id>/', edit_workout, name='edit_workout'),
    path('backend/delete_workout/delete/<int:workout_id>/', delete_workout, name='delete_workout'),
    path('backend/view_workout/view/<int:workout_id>/', view_workout, name='view_workout'),
    # path('backend/influencers/update/<int:workout_id>/', update_influencer, name='update_influencer'),
    path('backend/activate_workout/activate/<int:workout_id>/', activate_workout, name='activate_workout'),
    path('backend/deactivate_workout/deactivate/<int:workout_id>/', deactivate_workout, name='deactivate_workout'),

    path('api/workouts/', WorkoutByLevelAPIView.as_view(), name='get_workouts_by_level'),
# http://192.168.29.213:8000/api/workouts/?id=2
# http://192.168.29.213:8000/api/workouts/?level=2

    path('backend/video_list/', video_list, name='video_list'),
    path('backend/add_video/add/', add_video, name='add_video'),
    path('backend/edit_video/edit/<int:video_id>/', edit_video, name='edit_video'),
    path('backend/delete_video/delete/<int:video_id>/', delete_video, name='delete_video'),
    path('backend/view_video/view/<int:video_id>/', view_video, name='view_video'),
    # path('backend/influencers/update/<int:video_id>/', update_influencer, name='update_influencer'),
    path('backend/activate_video/activate/<int:video_id>/', activate_video, name='activate_video'),
    path('backend/deactivate_video/deactivate/<int:video_id>/', deactivate_video, name='deactivate_video'),
    path('api/workout/video-details/', VideoDetailsView.as_view(), name='video_details'),
    path('api/workout/video/', VideoDetailView.as_view(), name='workoutvideo_details'),

    path('backend/workbanners/', workbanner_list, name='workbanner_list'),
    path('backend/workadd/', workadd_banner, name='workadd_banner'),
    path('backend/workactivate/<int:add_id>/', workactivate_add, name='workactivate_add'),
    path('backend/workdeactivate/<int:add_id>/', workdeactivate_add, name='workdeactivate_add'),
    path('backend/workdelete/<int:add_id>/',workdelete_add, name='workdelete_add'),
    path('backend/workview/<int:add_id>/', workview_add, name='workview_add'),
    path('backend/workupdate/<int:add_id>/',workupdate_add, name='workupdate_add'),
    path('backend/workedit/<int:add_id>/', workedit_add, name='workedit_add'),

    path('api/banners/by-level/', WorkOutBannerListByLevel.as_view(), name='banners-by-level'),
    path('api/banners/by-workout-id/', WorkOutBannerListByWorkoutID.as_view(), name='banners-by-workout-id'),

    path('api/recommended-videos/', RecommendedVideoList.as_view(), name='recommended-videos'),
    path('api/recommended-videos/five/', RecommendedVideoListFive.as_view(), name='recommended-videosfive'),

]