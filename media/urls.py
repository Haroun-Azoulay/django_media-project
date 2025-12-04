from django.urls import path
from .views import UploadMedia

urlpatterns = [path("upload", UploadMedia.as_view(), name="upload")]
