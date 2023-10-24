"""Views for {{cookiecutter.package_name}}."""

# from django.core.paginator import Paginator
# from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
# from django.template.response import TemplateResponse

# from .forms import MyModelForm
# from .models import MyModel


# def create_view(request):
#     template = "create_view.html"
#     context = {}

#     form = MyModelForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thanks/")
#     context["form"] = form
#     return TemplateResponse(request, template, context)


# def list_view(request):
#     template = "list_view.html"
#     context = {}
#     context["dataset"] = MyModel.objects.all()
#     return TemplateResponse(request, template, context)


# def detail_view(request, id):
#     template = "detail_view.html"
#     context = {}
#     context["data"] = MyModel.objects.get(id=id)
#     return TemplateResponse(request, template, context)


# def update_view(request, id):
#     template = "update_view.html"
#     context = {}
#     obj = get_object_or_404(MyModel, id=id)
#     form = MyModelForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/" + id)
#     context["form"] = form
#     return TemplateResponse(request, template, context)


# def delete_view(request, id):
#     template = "delete_view.html"
#     context = {}
#     obj = get_object_or_404(MyModel, id=id)
#     if request.method == "POST":
#         obj.delete()
#         return HttpResponseRedirect("/")
#     return TemplateResponse(request, template, context)


# def htmx_example_view(request, arg):
#     template = "fragments/example.html"
#     context = {}
#     context["key"] = "value"
#     return TemplateResponse(request, template, context)


# def htmx_example_view2(request, arg):
#     """if using django-htmx"""
#     if request.htmx:
#         template = "partial.html"
#     else:
#         template = "complete.html"
#     context = {}
#     context["key"] = "value"
#     return TemplateResponse(request, template, context)


# def paginated_list_view(request):
#     contact_list = MyModel.objects.all()
#     paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "list.html", {"page_obj": page_obj})
