from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import BaseView, FeatureListView, TagFeatureView, TagListView, UserListView

urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("features/", FeatureListView.as_view(), name="feature_list"),
    path("tagfeature/", csrf_exempt(TagFeatureView.as_view()), name="tag_feature"),
]
