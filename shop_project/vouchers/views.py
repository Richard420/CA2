from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import VoucherApplyForm
# Create your views here.
@require_POST
def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code,
                                        valdi_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['voucher_id'] = voucher.id
        except Voucher.DoesNotExist:
            request.ssession['voucher_id'] = None
    return redirect('cart:cart_detail')