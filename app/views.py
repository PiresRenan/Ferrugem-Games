
from django.shortcuts import render
from .models import Mensagem, Usuario
from .send_messages import sendMessage

# Create your views here.
def index(request):
        if request.method == "POST":
                nome = request.POST.get("nome")
                email = request.POST.get("email")
                phone = request.POST.get("phone")
                message = request.POST.get("message")
                username = request.POST.get("username")
                password = request.POST.get("password")
                if nome and email and phone and message != None:
                        Mensagem.objects.create(name=nome, email=email, phone=phone, mensagem=message)
                        body = f"Mensagem de {nome}" + "\n" + f"Email= {email}" + "\n" + f"Telefone={phone}" + "\n" + f"Mensagem = {message}"
                        sendMessage(body)
                elif username and password != None:
                        try:
                                user = Usuario.objects.get(nome=username)
                                if password == user.senha:
                                        return render(request, 'games.html')
                        except:
                                print("Não encontrado")
                else:
                        email_change = request.POST.get("email_rec")
                        pass_change = request.POST.get("password_rec")
                        conf_pass_change = request.POST.get("confirm_password_rec")
                        user_change = Usuario.objects.get(email=email_change)
                        if pass_change == conf_pass_change:
                                user_change.senha = pass_change
                                user_change.save()
                return render(request, 'index.html')
        else:
                return render(request, 'index.html')

def games(request):
        return render(request, "games.html")

def cadastro(request):
        if request.method == "POST":
                nome = request.POST.get("name")
                dt_nasc = request.POST.get("birth_date")
                email = request.POST.get("email")
                cidade = request.POST.get("cidade")
                pais = request.POST.get("pais")
                senha = request.POST.get("password")
                confirm_senha = request.POST.get("conf_password")
                if confirm_senha == senha:
                        Usuario.objects.create(nome=nome, dt_nasc=dt_nasc, email=email, cidade=cidade, pais=pais, senha=senha)
                return render(request, 'index.html')
        else:
                return render(request, 'cadastro.html')

def shopping(request):
        return render(request, "shopping.html")