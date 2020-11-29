from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import linn, vald, mk
from .form import form_locator


@login_required
def test_view(request):
    form = form_locator()

    if request.method == "POST":
        selected_mk = request.POST.get('valik_mk')
        selected_linn = request.POST.get('valik_linn')

        if selected_mk == '':
            if selected_linn == ' ':
                pass
            else:
                form.fields['valik_mk'].initial = vald.objects.get(
                    id=linn.objects.get(id=selected_linn).vald_id_id
                ).maakond_id

                form.fields['valik_linn'].queryset = linn.objects.filter(
                    vald_id_id=linn.objects.get(id=selected_linn).vald_id_id)

        else:
            form.fields['valik_mk'].initial = selected_mk
            form.fields['valik_linn'].initial = selected_linn

            get_vallad = vald.objects.filter(maakond_id=selected_mk).values_list('id', flat=True)
            get_linnad = linn.objects.filter(vald_id_id__in=get_vallad)

            form.fields['valik_linn'].queryset = get_linnad

        form.fields['valik_linn'].initial = selected_linn

    return_test_view = {
        'form': form
    }
    return render(request, 'maakonnad/test.html', return_test_view)

