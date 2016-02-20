from cms.models import M_search_site_master,T_search_result

p = M_search_site_master(id=0, serch_site="hoge",request_url="fuga_url")
p.save()