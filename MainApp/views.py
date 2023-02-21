from django.shortcuts import render, HttpResponse




def home(request):

    return HttpResponse(f"""<center><h1>Приветствую вас !!</h1></center>""")

