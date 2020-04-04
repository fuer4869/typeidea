"""doc for admin."""
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site

from .adminforms import PostAdminForm
from .models import Category, Post, Tag


class PostInline(admin.TabularInline):
    """postinline."""

    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    """CategoryAdmin."""

    list_display = ('name', 'status', 'is_nav',
                    'post_count', 'created_time', 'owner')
    fields = ('name', 'status', 'is_nav')
    inlines = [PostInline, ]

    def post_count(self, obj):
        u"""返回文章数量."""
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    """tagadmin."""

    list_display = ('name', 'status', 'created_time', 'owner')
    fields = ('name', 'status', 'owner')


class CategoryOwnerFilter(admin.SimpleListFilter):
    u"""自定义过滤器 只展示当前用户创建的分类."""

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        """lookups."""
        return Category.objects.filter(owner=request.user).values_list('id',
                                                                       'name')

    def queryset(self, request, queryset):
        """queryset."""
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    u"""配置文章后台管理."""

    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator', 'owner'
    ]
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fileds = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    exclude = ['owner', ]

# 文章详情页面配置参数
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

# 文章详情页面配置参数
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status'
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content'
            )
        }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': ('tag', ),
        })
    )

    filter_horizontal = ('tag', )

    class Meta:  # NOQA
        css = {
            'all': ("""https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/
                    bootstrap.min.css""", ),
        }
        js = ("""https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/
              bootstrap.bundle.js""",)

    def operator(self, obj): # NOQA
        return format_html(
            '<a href="()">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin): # NOQA
    list_display = ['object_repr',
                    'object_id',
                    'action_flag',
                    'user',
                    'change_message']
