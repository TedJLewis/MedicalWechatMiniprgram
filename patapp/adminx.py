import xadmin
from .models import user
from .models import image
from .models import imagereal
from .models import doctor
from xadmin import views

# class userAdmin(object):
#     pass

xadmin.site.register(doctor)
xadmin.site.register(user)
xadmin.site.register(image)
xadmin.site.register(imagereal)

class GlobalSiteSetting(object):
    # 设置后台顶部标题
    site_title = '皮肤病愈后管理系统'
    # 设置后台底部标题
    site_footer = 'Powered by sophrieet'
    # 设置可折叠
    menu_style = 'accordion'


# 启用主题管理器
class BaseXadminSetting(object):
    enable_themes = True
    # 使用主题
    use_bootswatch = True

# 配置图标
class SafeAdmin(object):
    model_icon = 'fa fa-key'

# 注册
# xadmin.site.register(views.CommAdminView, GlobalSiteSetting)
# xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# xadmin.site.register(user)
# xadmin.site.register(image)
# xadmin.site.register(imagereal)

# 注册密码库后台管理
# xadmin.site.register(YourModel, SafeAdmin)

"""
list_display 控制列表展示的字段
search_fields 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
list_filter 可以进行过滤操作的列
ordering 默认排序的字段
readonly_fields 在编辑页面的只读字段
exclude 在编辑页面隐藏的字段
list_editable 在列表页可以快速直接编辑的字段
show_detail_fileds 在列表页提供快速显示详情信息
refresh_times 指定列表页的定时刷新
list_export 控制列表页导出数据的可选格式
show_bookmarks 控制是否显示书签功能
data_charts 控制显示图标的样式
model_icon 控制菜单的图标
"""