from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import Warmup2, Logic2, String2, List2
from app.fix_teen import fix_teen
# Create your views here.

def warmup_2(request):
  form = Warmup2(request.GET)
  if form.is_valid():
    string = form.cleaned_data['string']
    n = form.cleaned_data['number']
    answer = ""
    if len(string) < 3:
      if len(string) == 2:
        for i in range(n):
          answer += string[0:2]
      elif len(string) == 1:
        for i in range(n):
          answer += string[0]
      else:
        print('invalid num of chars')
    else:
      for i in range(n):
        answer += string[0:3] 
    return render(request, "warmup2.html", {"form": form, "string": string, "number": n, "answer": answer})

  return render(request, "warmup2.html", {"form": form})


def logic_2(request):
  form = Logic2(request.GET)
  if form.is_valid():
    a = form.cleaned_data['a']
    b = form.cleaned_data['b']
    c = form.cleaned_data['c']

    new_a = fix_teen(a)
    new_b = fix_teen(b)
    new_c = fix_teen(c)

    total = new_a + new_b + new_c

    return render(request, "logic2.html", {"form": form, "a": a, "b": b, "c": c, "total": total})
  
  return render(request, "logic2.html", {"form": form })

def string_2(request):
  form = String2(request.GET)
  if form.is_valid():
    string = form.cleaned_data['string']
    if string.count("xyz") > string.count(".xyz"):
      answer = True
      return render(request, "string2.html", { "form": form, "string":string, "answer": answer })
  answer = False
  return render(request, "string2.html", { "form":form, "answer": answer })

def list_2(request):
  form = List2(request.GET)
  if form.is_valid():
    n1 = form.cleaned_data['n1']
    n2 = form.cleaned_data['n2']
    n3 = form.cleaned_data['n3']
    n4 = form.cleaned_data['n4']
    n5 = form.cleaned_data['n5']
    n6 = form.cleaned_data['n6']
    n7 = form.cleaned_data['n7']

    if n6 == None and n7 == None:
      nums = [n1, n2, n3, n4, n5]
      nums.sort()
      total = 0
      for i in range(1, len(nums) -1):
        total += nums[i]
        average = total/(len(nums) -2)
      return render(request, "list2.html", {"form": form, "average": average})

    elif n6 == None and n7 != None:
      nums = [n1, n2, n3, n4, n5, n7]
      nums.sort()
      total = 0
      for i in range(1, len(nums) -1):
        total += nums[i]
        average = total/(len(nums) -2)
      return render(request, "list2.html", {"form": form, "average": average})

    elif n6 != None and n7 == None:
      nums = [n1, n2, n3, n4, n5 ,n6]
      nums.sort()
      total = 0
      for i in range(1, len(nums) -1):
        total += nums[i]
        average = total/(len(nums) -2)
      return render(request, "list2.html", {"form": form, "average": average})

    elif n6 != None and n7 != None:
      nums = [n1, n2, n3, n4, n5, n6, n7]
      nums.sort()
      total = 0
      for i in range(1, len(nums) -1):
        total += nums[i]
        average = total/(len(nums) -2)
      return render(request, "list2.html", {"form": form, "average": average})

    else:
      average = "this is wrong"
      return render(request, "list2.html", {"form": form, "average": average })

  return render(request, "list2.html", {"form": form, })