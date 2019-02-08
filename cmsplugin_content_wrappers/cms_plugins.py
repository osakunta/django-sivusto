from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template import Template
from django.utils.safestring import mark_safe

from .models import ContentArea


class CMSContentArea(CMSPluginBase):
    model = ContentArea
    name = 'Content Area'
    render_template = 'cmsplugin_content_wrappers/content_area.html'
    allow_children = True


plugin_pool.register_plugin(CMSContentArea)
