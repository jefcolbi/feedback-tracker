from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import FeatureForm, TagFeatureForm, TagForm, UserForm
from .models import Feature, Tag, User
from .tables import FeatureTable, TagTable, UserTable


class BaseView(TemplateView):

    template_name = "core/base.html"


class FeatureListView(TemplateView):

    template_name = "core/feature_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx["table"] = FeatureTable(Feature.objects.all())
        ctx["form"] = FeatureForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = FeatureForm(self.request.POST)
        if form.is_valid():
            form.save()

        return render(request, "components/feature_table.html", self.get_context_data())


class TagListView(TemplateView):
    template_name = "core/tag_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx["table"] = TagTable(Tag.objects.all())
        ctx["form"] = TagForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = TagForm(self.request.POST)
        if form.is_valid():
            form.save()

        return render(request, "components/tag_table.html", self.get_context_data())


class UserListView(TemplateView):
    template_name = "core/user_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx["table"] = UserTable(User.objects.all())
        ctx["form"] = UserForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = UserForm(self.request.POST)
        if form.is_valid():
            form.save()

        return render(request, "components/user_table.html", self.get_context_data())


class TagFeatureView(TemplateView):

    template_name = "core/feature_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx["table"] = FeatureTable(Feature.objects.all())
        return ctx

    def post(self, request, *args, **kwargs):
        form = TagFeatureForm(self.request.POST)
        if form.is_valid():
            form.save()

        return render(request, "components/feature_table.html", self.get_context_data())
