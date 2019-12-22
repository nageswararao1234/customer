import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import View
from django.shortcuts import render, reverse, get_object_or_404

from unitedlayerproject.utils import render_to_pdf
from .models import Coustomer
from .forms import CoustomerForm


def index(request):
    """

    :param request:Do something depending of HTTP method.
    :return:Returns a page
    """
    coustomer_list=Coustomer.objects.all()
    return render(request, 'coustomers/index.html', {'coustomer_list': coustomer_list})


def display(request, coustomer_id):
    """

    :param request:Do something depending of HTTP method.
    :param coustomer_id:if the customer_id created
    :return:Returns a page
    """
    coustomer=get_object_or_404(Coustomer, pk=coustomer_id)
    return render(request,'coustomers/display.html',{'coustomer': coustomer})


def createform(request):
    """

    :param request:request from the user to createform
    :return:if form is valid page will  redirected to customer,home
    in case form is not valid  page will goes to create. html and display
    """
    if request.method == "POST":
        form = CoustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('coustomers:index'))
    form = CoustomerForm()
    return render(request, "coustomers/create.html", {'form': form})


class GeneratePDF(View):
    """
    create a GeneratePdf on a customer model
    """
    model = Coustomer

    def get(self, request, coustomer_id, *args, **kwargs):
        """

        :param request:Do something depending of HTTP method.
        :param coustomer_id:if the customer_id created
        :param args: to return the tuple values
        :param kwargs:to return the dictionary values
        :return: return the page
        """
        coustomer = get_object_or_404(Coustomer, pk=coustomer_id)
        template = get_template('coustomers/invoice.html')
        context = {
            'coustomer': coustomer
        }
        html = template.render(context)
        pdf = render_to_pdf('coustomers/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
