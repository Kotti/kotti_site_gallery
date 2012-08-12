def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_site_gallery.views'
    settings['kotti.available_types'] += ' kotti_site_gallery.resources.SiteGallery'
    settings['kotti.available_types'] += ' kotti_site_gallery.resources.Site'
