from .models import IP
import datetime
from pytz import timezone

def save_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    eastern = timezone('US/Eastern')
    naive_dt = datetime.datetime.now()
    loc_dt = datetime.datetime.now(eastern)

    client_ip = IP()
    client_ip.ip_address= ip
    client_ip.pub_date = loc_dt
    client_ip.save()