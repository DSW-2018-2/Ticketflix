from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Room, Seat
from .forms import AddSeatRowForm


class RoomList(ListView):
    model = Room


class RoomView(DetailView):
    model = Room

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """

        seats = Seat.objects.filter(room=self.object)
        context['seats'] = seats

        print("===============================")
        print(context)
        print("===============================")

        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
            


class RoomCreate(CreateView):
    model = Room
    fields = [
        'name'
    ]
    success_url = reverse_lazy('room:room_list')


class RoomUpdate(UpdateView):
    model = Room
    fields = [
        'name'
    ]
    success_url = reverse_lazy('room:room_list')


class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('room:room_list')


class AddSeatRow(FormView):
    
    form_class = AddSeatRowForm

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """

        room_id = kwargs['pk']
        room = Room.objects.get(id=room_id)

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, room)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, room):
        """If the form is valid, redirect to the supplied URL."""

        row = form.cleaned_data.get('row')
        seats_quantity = form.cleaned_data.get('seats_quantity')

        for i in range(1, seats_quantity + 1):
            seat = Seat.objects.create(row=row,
                                       number=i,
                                       room=room)
            seat.save()

        return HttpResponseRedirect(self.get_success_url(room.id))

    def get_success_url(self, room_id):
        """Return the URL to redirect to after processing a valid form."""
        
        self.success_url = reverse_lazy('room:room_view', kwargs={'pk': room_id})

        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy

