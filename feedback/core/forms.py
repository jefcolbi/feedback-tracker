from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, ButtonHolder, Fieldset, Layout
from django import forms
from django.urls import reverse

from .models import Feature, Feedback, Tag, TaggedFeature, User


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "",
                "name",
                ButtonHolder(
                    Button(
                        "Create",
                        "Create",
                        hx_trigger="click",
                        hx_target="#model-table",
                        hx_swap="outerHTML",
                        hx_post="",
                        css_class="btn btn-primary",
                    )
                ),
            )
        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name", "color"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "",
                "name",
                "color",
                ButtonHolder(
                    Button(
                        "Create",
                        "Create",
                        hx_trigger="click",
                        hx_target="#model-table",
                        hx_swap="outerHTML",
                        hx_post="",
                        css_class="btn btn-primary",
                    )
                ),
            )
        )


class TagFeatureForm(forms.ModelForm):
    class Meta:
        model = TaggedFeature
        fields = ["feature", "tag"]

    def __init__(self, *args, feature=None, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        self.fields["feature"].initial = feature
        self.fields["feature"].widget.attrs.update(
            {"readonly": "readonly", "disabled": "disabled"}
        )

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "",
                "feature",
                "tag",
                ButtonHolder(
                    Button(
                        "Add",
                        "Add",
                        hx_trigger="click",
                        hx_target="#model-table",
                        hx_swap="outerHTML",
                        hx_post=reverse("tag_feature"),
                        css_class="btn btn-primary",
                    )
                ),
            )
        )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["feature", "content", "user"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_show_labels = False
        self.helper.layout = Layout(Fieldset("", "feature", "content", "user"))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "",
                "username",
                "email",
                ButtonHolder(
                    Button(
                        "Create",
                        "Create",
                        hx_trigger="click",
                        hx_target="#model-table",
                        hx_swap="outerHTML",
                        hx_post="",
                        css_class="btn btn-primary",
                    )
                ),
            )
        )
