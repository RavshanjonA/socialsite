from django.contrib import admin


from group.models import Group,GroupMember

admin.site.register(Group)
admin.site.register(GroupMember)