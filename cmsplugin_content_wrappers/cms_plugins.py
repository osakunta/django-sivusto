from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ContentArea, ContentSection


class CMSContentArea(CMSPluginBase):
    model = ContentArea
    name = 'Content Area'
    render_template = 'cmsplugin_content_wrappers/content_area.html'
    allow_children = True


class CMSContentSection(CMSPluginBase):
    model = ContentSection
    name = 'Content Section'
    render_template = 'cmsplugin_content_wrappers/content_section.html'
    allow_children = True
    require_parent = True
    parent_classes = ['CMSContentArea']


plugin_pool.register_plugin(CMSContentArea)
plugin_pool.register_plugin(CMSContentSection)
