from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from blog.models import Blog


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/detail_view.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object
