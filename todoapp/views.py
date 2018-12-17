from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from .models import TodoItem
from django.contrib import messages


# Create your views here.
def todoView(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        all_todo_items = TodoItem.objects.filter(created_by=request.user)
        count = all_todo_items.count()
        context = {
            'all_items': all_todo_items,
            'count_items': count,
        }
        return render(request, 'todoapp/todo.html',
                      context)


def addTodo(request):
    if request.method == "POST" and request.is_ajax():

        if request.user.is_authenticated:
            all_todo = TodoItem.objects.filter(created_by=request.user)
            count = all_todo.count()
            if count < 10:
                new_item = TodoItem(content = request.POST.get('content'), created_by = request.user, )
                new_item.save()
            # return HttpResponseRedirect('/todo/')
            all_todo_items = TodoItem.objects.filter(created_by=request.user)
            
            html = render_to_string('todoapp/todo_list.html', 
                {'all_items': all_todo_items, 'count_items': all_todo_items.count()}, request=request)
            return JsonResponse({'form':html})
        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def deleteTodo(request, todo_id):
    
    if request.method == "POST" and request.is_ajax():

        if request.user.is_authenticated:

            item_to_del = TodoItem.objects.get(id = todo_id)
            item_to_del.delete()
            all_todo_items = TodoItem.objects.filter(created_by=request.user)
            count = all_todo_items.count()
            
            html = render_to_string('todoapp/todo_list.html', 
                {'all_items': all_todo_items, 'count_items': count}, 
                request=request)
            # messages.success(request, f'Successfully Deleted Item !')
            # return HttpResponseRedirect('/todo/')
            return JsonResponse({'form':html})

        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))