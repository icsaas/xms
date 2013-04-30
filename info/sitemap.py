from django.contrib.sitemaps import Sitemap
from models import Cquenv

class StaticSitemap(Sitemap):
    priority=0.5
    lastmod=None

    def items(self):
        return [
            "/cquenv",
            "/cquenv/direction",

        ]
    def location(self, obj):
        return obj[0] if isinstance(obj,tuple) else obj

    def changefreq(self,obj):
        return obj[1] if isinstance(obj,tuple) else "monthly"

sitemaps=dict(
    static=StaticSitemap
)