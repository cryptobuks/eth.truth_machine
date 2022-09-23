from django.contrib import admin

from blog.models import IndexInfo, MetamaskAccount, Transaction, IPFS

admin.site.register(IndexInfo)
admin.site.register(MetamaskAccount)
admin.site.register(Transaction)
admin.site.register(IPFS)


