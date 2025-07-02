from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

# タスク一覧表示用ビュー
class IndexView(View):
    def get(self, request):
        # 未完了タスク → 完了タスク の順で並べる
        incomplete_tasks = Task.objects.filter(complete=False)
        complete_tasks = Task.objects.filter(complete=True)
        todo_list = list(incomplete_tasks) + list(complete_tasks)
        context = {"todo_list": todo_list}
        return render(request, "mytodo/index.html", context)

index = IndexView.as_view()

# タスク追加用ビュー
class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, "mytodo/add.html", {"form": form})

add = AddView.as_view()

# タスク完了・未完了の切り替え
class UpdateTaskComplete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        return redirect("/")

update_task_complete = UpdateTaskComplete.as_view()

# タスク編集ビュー
class EditView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, "mytodo/edit.html", {"form": form, "task_id": task.id})

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "mytodo/edit.html", {"form": form, "task_id": task.id})

edit = EditView.as_view()

# タスク削除ビュー
class DeleteView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect("/")

delete = DeleteView.as_view()
