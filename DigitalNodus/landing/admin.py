from django.contrib import admin
from .models import Member,Reservation, Event, OpenSourceProject, SocialProofComment, Support, LinkGroupDigitalNodus

# Register your models here.



class AdminMember(admin.ModelAdmin):
    list_display = [
        "all_names",
        "whatsapp_number",
        "email",
        "profession",
        "sex",
        "institution",
        "reason",
        "created_at"
    ]

class AdminOpenSourceProject(admin.ModelAdmin):
    list_display = [
        "name",
        "created_at"
    ]


class AdminSocialProofComment(admin.ModelAdmin):
    list_display = [
        "name",
        "fonction",
        "created_at",
        "publish"
    ]

    list_editable = [
        "publish"
    ]


class AdminSupport(admin.ModelAdmin):
    list_display = [
        "name",
        "created_at"
    ]


class AdminLinkGroupDigitalNodus(admin.ModelAdmin):
    list_display = [
        'link'
    ]

class AdminEvent(admin.ModelAdmin):
    list_display = [
        "name",
        "date",
        "time",
        "place",
        "publish"    
    ]
    list_editable = [
        "publish"
    ]


admin.site.register(Member, AdminMember)
admin.site.register(OpenSourceProject, AdminOpenSourceProject)
admin.site.register(SocialProofComment, AdminSocialProofComment)
admin.site.register(Support, AdminSupport)
admin.site.register(Event, AdminEvent)
admin.site.register(LinkGroupDigitalNodus, AdminLinkGroupDigitalNodus)