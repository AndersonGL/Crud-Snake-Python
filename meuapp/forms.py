from django.forms import ModelForm
from meuapp.models import Carro

# Create the form class.
class CarroForm(ModelForm):
	class Meta:
		model = Carro
		fields = ["modelo", "marca" ,"ano",]
  
  
  
  
  
  
  # busquei o modelo na documentação django Creating forms from models