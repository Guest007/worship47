from typing import Any

from django.contrib import admin
from django.contrib.admin import register
from django.contrib.admin.widgets import AdminFileWidget
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe

from tagulous import admin as tagadmin

from .models import Category, Song


class AdminImageWidget(AdminFileWidget):
    def render(self, name: str, value: Any, attrs: dict = None, renderer: Any = None) -> str:
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" style="width: 150px;"/></a> Change: '
            )
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe("".join(output))


class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []

    def __init__(self, model: Any, admin_site: Any) -> None:
        self.request = None
        super().__init__(model, admin_site)

    def get_queryset(self, request: HttpRequest) -> HttpRequest:
        self.request = request
        return super().get_queryset(request)

    @property
    def base_url(self) -> str:
        return f'{self.request.scheme}://{self.request.META.get("HTTP_HOST")}'

    def formfield_for_dbfield(self, db_field: Any, **kwargs: dict) -> Any:
        if db_field.name in self.image_fields:
            _ = kwargs.pop("request", None)
            kwargs["widget"] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)


@register(Category)
class CategAdmin(ImageWidgetAdmin):
    list_display = ["priority", "slug", "title", "admin_image"]
    list_display_links = ["slug"]
    list_editable = ["priority"]
    image_fields = ["image"]

    def admin_image(self, obj: Category) -> str:
        try:
            url = f"{obj.image.url}"
        except Exception:
            url = f"{obj.image}"
        return mark_safe(f'<img src="{self.base_url}{url}" style="width: 50px;"/>')

    admin_image.allow_tags = True


class SongAdmin(admin.ModelAdmin):
    list_display = ["title", "title_eng", "translator", "categ", "user", "modified"]
    search_fields = ["title", "title_eng", "text", "text_eng"]
    readonly_fields = ["created", "modified"]

    def categ(self, obj: Song) -> str:
        categs = []
        for c in obj.category.all():
            categs.append(f"{c.title} ({c.slug})")
        return " || ".join(categs)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super(SongAdmin, self).get_queryset(request)
        qs = qs.prefetch_related(
            "category",
        ).select_related(
            "user",
        )
        return qs


tagadmin.register(Song, SongAdmin)
tagadmin.register(Song.translator)
