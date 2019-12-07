from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher
from django.http import HttpResponse
from .serializers import TeacherSerializer
from teacher.forms import TeacherForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
# -*- coding: utf-8 -*-

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('teacher_code')
    serializer_class = TeacherSerializer

@method_decorator(csrf_exempt, name='dispatch')
def teacher_show(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all().order_by('teacher_code')
        teachers_serializer = TeacherSerializer(teachers, many=True)
        return HttpResponse(status=HttpResponse.status_code)
    elif request.method == 'POST':
        teacher_data = HttpResponse(request)
        teacher_serializer = TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return HttpResponse(status=HttpResponse.status_code)
        return HttpResponse(status=HttpResponse.status_code)

@method_decorator(csrf_exempt, name='dispatch')
def teacher_list(request, template_name='teacher_list.html'):
    teacher = Teacher.objects.all()
    data = {}
    data['object_list'] = teacher
    return render(request, template_name, data)

@method_decorator(csrf_exempt, name='dispatch')
def teacher_create(request, template_name='teacher_form.html'):
    form = TeacherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('teacher:teacher_list')
    return render(request, template_name, {'form':form})

@method_decorator(csrf_exempt, name='dispatch')
def teacher_update(request, teacher_code, template_name='teacher_form.html'):
    teacher = get_object_or_404(Teacher, teacher_code=teacher_code)
    form = TeacherForm(request.POST or None, request.FILES or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher:teacher_list')
    return render(request, template_name, {'form':form})

@method_decorator(csrf_exempt, name='dispatch')
def teacher_delete(request, teacher_code, template_name='teacher_confirm_delete.html'):
    teacher = get_object_or_404(Teacher, teacher_code=teacher_code)    
    if request.method=='POST':
        teacher.delete()
        return redirect('teacher:teacher_list')
    return render(request, template_name, {'object':teacher})