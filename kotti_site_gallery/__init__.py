from kotti.resources import Image


def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_site_gallery.views'
    settings['kotti.available_types'] += (
        ' kotti_site_gallery.resources.SiteGallery')
    settings['kotti.available_types'] += ' kotti_site_gallery.resources.Site'
    Image.type_info.addable_to.append(u'Site')
