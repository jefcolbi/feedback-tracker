import django_tables2 as tables
from django.template import loader
from django.utils import safestring

from .forms import TagFeatureForm
from .models import Feature, Feedback, Tag, TaggedFeature, User


class UserTable(tables.Table):

    features = tables.Column(empty_values=(), linkify={"viewname": "feature_list"})

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ("username", "email")

    def render_features(self, record):
        return Feature.objects.filter(feedbacks__user=record).count()


class TagTable(tables.Table):

    features = tables.Column(
        empty_values=(),
        linkify={"viewname": "feature_list"},
        verbose_name="Total tagged features",
    )

    class Meta:
        model = Tag
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "color")

    def render_features(self, record):
        return TaggedFeature.objects.filter(tag=record).count()

    def render_color(self, value):
        return safestring.SafeText(
            f'{value} <span class="ml-3 px-3" style="background-color: {value};"></span>'
        )


class FeatureTable(tables.Table):

    feedbacks = tables.Column(
        empty_values=(),
        linkify={"viewname": "feature_list"},
        verbose_name="Total feedback",
    )

    class Meta:
        model = Feature
        template_name = "django_tables2/bootstrap.html"
        fields = ("name",)

    def render_feedbacks(self, record):
        return Feedback.objects.filter(feature=record).count()

    def render_name(self, record):
        tags_html = ""
        for tagfeat in TaggedFeature.objects.filter(feature=record):
            tags_html += f'<span class="bg-primary text-white btn py-0 mx-1"">{tagfeat.tag.name}</span>'

        form = TagFeatureForm(feature=record)
        ctx = {"form": form, "feature": record}
        form_as_str = loader.render_to_string(
            "components/add_feature_tag_form.html", ctx
        )

        return safestring.SafeText(f"{record.name} {tags_html} {form_as_str}")
