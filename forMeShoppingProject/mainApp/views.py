from django.shortcuts import render

# main.html을 띄우는 함수
def main(request):
    return render(request, 'main.html')
