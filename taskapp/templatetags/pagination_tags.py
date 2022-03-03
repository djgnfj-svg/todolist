from django import template
from django.core.paginator import Page

register = template.Library()

@register.filter(name='slice_visible_pages')
def slice_visble_pages(paging: Page):
	min_page = int((paging.number -1) / 10) * 10 + 1
	min_page = max(min_page, 1)
	max_page = min(min_page+ 9, paging.paginator.num_pages)
	return range(min_page, max_page +1)