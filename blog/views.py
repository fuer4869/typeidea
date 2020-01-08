"""说明."""
from django.views.generic import DetailView, ListView

from django.shortcuts import get_object_or_404

from config.models import SideBar

from .models import Category, Post, Tag


class CommonViewMixin:
    """docstring for CommonViewMixin."""

    def get_context_data(self, **kwargs):
        """Docstring for get_context_data."""
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):
    """docstring for IndexView."""

    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    """docstring for CategoryView."""

    def get_context_data(self, **kwargs):
        """Docstring for get_context_data."""
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        """重写queryset, 根据分类过滤."""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    """docstring for TagView."""

    def get_context_data(self, **kwargs):
        """Docstring for get_context_data."""
        context = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        """重写queryset，根据标签过滤."""
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    """postdetailview."""

    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class PostListView(ListView):
    """docstring for PostListView."""

    queryset = Post.latest_posts()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'
