from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

import io
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import FileResponse

from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm


# Create your views here.
class ProduceListView(LoginRequiredMixin, ListView):
    model = Produce
    template_name = 'market/produce_list.html'

class ProduceListView1(LoginRequiredMixin, ListView):
    model = Produce
    template_name = 'market/produce_list.html'

    def get_queryset(self):
         queryset = super().get_queryset()
         return queryset.filter(user=self.request.user)


class ProduceUpdateView(LoginRequiredMixin, UpdateView):
    model = Produce
    fields = ('produce_name', 'price', 'description', 'qty')
    template_name = 'market/produce_edit.html'
    success_url = reverse_lazy('market:produce_list')

class ProduceDeleteView(LoginRequiredMixin, DeleteView):
    model = Produce
    template_name = 'market/produce_delete.html'
    success_url = reverse_lazy('market:produce_list')

class ProduceCreateView(LoginRequiredMixin, CreateView):
    model = Produce
    template_name = 'market/produce_new.html'
    fields = ('produce_name', 'price', 'description', 'qty')
    success_url = reverse_lazy('market:produce_list1')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/Signup.html'


@login_required
def view_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    # orders = WorkOrder.objects.filter(workorder_name=request.user.id)

    orders = Produce.objects.all()

    lines = []

    lines.append("Here is your generated Report of listed Produce!")
    for order in orders:
        # print(order.customer_name)
        lines.append(" ")
        lines.append("Listed Produce:    " + "          " + str(order.produce_name))
        lines.append("Description:       " + "          " + str(order.description))
        lines.append("Quantity (Tons):   " + "          " + str(order.qty))
        lines.append("Price (/Ton):      " + "          " + str(order.price))
        lines.append("Date listed:       " + "          " + str(order.created))

        lines.append(" ")

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='report.pdf')


class ChangePwView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/change_password.html'

class PwResetView(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('market:pw_reset_done')
    template_name = 'registration/pw_reset.html'


class PwResetDoneView(PasswordResetDoneView):
    template_name = 'registration/pw_reset_done.html'


class PwResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('market:pw_reset_complete')
    template_name = 'registration/pw_reset_confirm.html'


class PwResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/pw_reset_complete.html'