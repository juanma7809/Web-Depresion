from django.views import View

class PacienteView(View):

    def get(self, request):
        pacientes = Paciente.objects.all()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def  delete(self, request):
        pass