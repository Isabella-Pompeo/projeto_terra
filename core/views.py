from django.shortcuts import render

def cadastro_view(request):
    if request.method == 'POST':
        # Aqui você processaria os dados (nome, data, telefone)
        pass
    return render(request, 'core/hello.html')