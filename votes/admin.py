import csv
from django.contrib import admin
from .models import Movie

@admin.action(description='导入数据')
def import_data(self, request, queryset):
    with open('./spider/douban.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Movie(image_url=row['海报图片'], title=row['电影名称'])
            movie.save()
    self.message_user(request, 'Data imported successfully')

class MovieAdmin(admin.ModelAdmin):
    actions = [import_data] 

admin.site.register(Movie, MovieAdmin)

