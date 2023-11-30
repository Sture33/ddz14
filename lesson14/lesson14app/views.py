from django.shortcuts import render, redirect
from lesson14app.form import FeedbackForm
from lesson14app.models import Feedback, Tag


def index_page_view(request):
    feedbacks = Feedback.objects.all()
    context = {'filter_list': Tag.objects.all(), 'filtered_list':feedbacks}

    if request.method == 'POST':
        filter_list = request.POST.getlist('filter')
        filtered_list = []
        for i in feedbacks:
            if set(filter_list).issubset(set(obj.title for obj in i.tags.all())):
                filtered_list.append(i)
        context['filtered_list'] = filtered_list
    return render(request,
                  'index.html',
                  context)

def form_page_view(request):
    context = {}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('Данные не валидны')

    form = FeedbackForm()
    context['form'] = form

    return render(request,
                  'form.html',
                  context)

def delete_page_view(request, pk):
    if request.method == 'POST':
        answer = request.POST.get('answer')

        if answer == "True":
            delete_obj = Feedback.objects.get(pk=pk)
            delete_obj.delete()
            return redirect('index')
        else:
            return redirect('index')

    return render(request, 'delete.html')



def update_page_view(request,pk):
    context = {}
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=Feedback.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('index')

    form = FeedbackForm(initial={'name': Feedback.objects.get(pk=pk).name,'email': Feedback.objects.get(pk=pk).email, 'text': Feedback.objects.get(pk=pk).text, 'tags': Feedback.objects.get(pk=pk).tags.all()})
    context['form'] = form

    return render(request,
                  'update.html',
                  context)

