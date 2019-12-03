from django.shortcuts import render, redirect
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
                                        valid_from_lte=now,
                                        valid_to_gte=now,
                                        active=True)
            request.session['voucher_id'] = voucher.voucher_id
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
    return redirect('cart:cart_detail')