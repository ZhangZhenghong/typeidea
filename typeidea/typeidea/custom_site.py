from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
  site_header = 'Oligo synthesis platform management'
  site_title = 'OS synthesis'
  index_title = 'index_page'

custom_site = CustomSite(name = 'cus_admin')
