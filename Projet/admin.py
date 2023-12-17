from django.contrib import admin
from Projet.models import Projet, Developpeur

admin.site.register(Developpeur)


class type_filter(admin.SimpleListFilter):
    title = 'Type de projet et effectif'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return (

            ('Web', ('Projet Web')),
            ('Mobile', ('Projet Mobile')),
            ('Desktop', ('Projet Desktop')),
            ('Manque_effectif', ('Projet sans effectif')),

        )

    def queryset(self, request, queryset):
        if self.value() == 'Web':
            return queryset.filter(type='w')
        if self.value() == 'Mobile':
            return queryset.filter(type='m')
        if self.value() == 'Desktop':
            return queryset.filter(type='d')
        if self.value() == 'Manque_effectif':
            return queryset.filter(effectif='manque')




class Developpeur_Inline(admin.TabularInline):
    model = Developpeur
    extra = 2

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('date_debut','date_fin','besoin','createur','type','effectif')
    search_fields = ('createur',)
    list_per_page = 2
    list_filter = (type_filter,)
    inlines = [Developpeur_Inline]



