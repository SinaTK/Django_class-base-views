from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, DeleteView, UpdateView, MonthArchiveView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Car
from .forms import CreateCarForm

class Home(View):
    http_method_names = ['get', 'post', 'options']

    def get(self, request):
        return render(request, 'home/home.html')
    
    def options(self, request, *args, **kwargs):
        response =  super().options(request, *args, **kwargs)
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, 'not_allowed.html')
    
class CarsView(TemplateView):
    template_name = 'home/cars.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class Redirect(RedirectView):
    # url = '/'
    pattern_name = 'home:home'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    

class CarListView(ListView):
    template_name = 'car_list.html'
    model = Car         # object_list
    ordering = 'year'   # when use get_queryset doesn't work

    allow_empty = True
      
    # queryset = Car.objects.filter(year__gte=2017)

    def get_queryset(self):         # for complecated queries
        cars = Car.objects.filter(year__gte=2017)
        return cars.order_by('year')

    context_object_name = 'cars'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['username'] = 'SinaTK'
        return context
    

class CarDetailsView(DetailView):
    template_name = 'home/car_details.html'
    model = Car
    context_object_name = 'car'

    # Do noting to use primary key

    # slug_field = 'brand'    # using slug 
    # slug_url_kwarg = 'my_slug'

    def get_object(self, queryset=None):        # customize 
        q = Car.objects.get(
            brand = self.kwargs['brand'],
            model = self.kwargs['model'],
            year = self.kwargs['year'],
        )
        return q
    

# class CreateCarView(FormView):
#     template_name = 'home/create_car.html'
#     form_class = CreateCarForm
#     success_url = reverse_lazy('home:cars')

#     def form_valid(self, form):
#         self._create_car(form.cleaned_data)
#         messages.success(self.request, 'Car created succesfully', 'success')
#         return super().form_valid(form)
    
#     def _create_car(self, data):
#         Car.objects.create(brand=data['brand'], model=data['model'], year=data['year'], owner=data['owner'])


class  CreateCarView(CreateView):
    template_name = 'home/create_car.html'
    model = Car
    fields = ['brand', 'model', 'year']
    success_url = reverse_lazy('home:cars')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user.username if self.request.user.username else "No one. It's fot sale"       
        car.save()
        messages.success(self.request, 'Car created succesfully', 'success')
        return super().form_valid(form)
    

class DeleteCarView(DeleteView):
    template_name = 'home/delete_car.html'
    model = Car
    success_url = reverse_lazy('home:cars')

class UpdateCarView(UpdateView):
    template_name = 'home/update_car.html'
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('home:cars') 

    def form_valid(self, form):
        messages.success(self.request, 'Car updated succesfully', 'success')
        return super().form_valid(form)
    
class MonthCarView(MonthArchiveView):
    model = Car
    date_field = 'created'
    month_format = '%m'
    template_name = 'home/cars.html'
    context_object_name = 'cars'

    allow_future = True