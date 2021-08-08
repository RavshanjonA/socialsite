from django.forms import ModelForm

from group.models import Group
from post.models import Post


class PostForm(ModelForm):
    class Meta:
        fields = ("message", "group")
        model = Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (
                Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )