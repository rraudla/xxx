from django.http import HttpResponse


def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session
    request.session['num_visits'] = num_visits
    if num_visits > 3:
        del (request.session['num_visits'])
    resp = HttpResponse('view count=' + str(num_visits))
    resp.set_cookie('dj4e_cookie', '715e8ba4', max_age=1000)
    return resp

