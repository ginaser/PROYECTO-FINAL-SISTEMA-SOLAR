import random
import gi

#import logging


# importar modulo que contiene clase base de actividad.
'''
from sugar3.activity import activity

from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
from sugar3.activity.widgets import (
    ActivityToolbarButton,
    StopButton
)

#from ppt_utils import OPCIONES  agrega el modulo ppt_utils que contiene el diccionario llamado OPCIONES
'''
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#logger = logging.getLogger(__name__)

class sistemasolar(Gtk.Window):
	"""docstring for ClassName"""
	def __init__(self, *args, **kwargs):
		super(Inicio, self).__init__(*args,**kwargs)
		self.set_default_size(500,500)
		self.agregar_contenedor()
		self.PrimeraVentanaSistemaSolar()
		self.SegundaVentanaPlanetas()
		

	def agregar_contenedor(self):
        
		self.contenedor = Gtk.Grid()
		self.contenedor.set_row_homogeneous(False)

		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def PrimeraVentanaSistemaSolar(self):

		
		self.sistemasolar = Gtk.Button('Sistema Solar')
		self.planetas= Gtk.Button('Planetas')
		self.juego = Gtk.Button('Juego')
		self.contenedor.attach(self.sistemasolar,0,0,1,1)
		self.contenedor.attach(self.planetas,0,0,2,1)
		self.contenedor.attach_next_to(self.juego,self.planetas,self.sistemasolar,Gtk.PositionType.RIGHT,1,1)	
		self.sistemasolar.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.planetas.connect('clicked',self.SegundaVentanaPlanetas)
        self.juego.connect('clicked',self.SegundaVentanajuego)
		

	def SegundaVentanaSistemaSolar(self,btn):

		#self.gtk_window_set_title (title="hola")

		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.label_def = Gtk.Label(' texto prueba')
		self.contenedor.attach(self.label_def,0,0,1,1)

		self.contenedor.show_all()


	def SegundaVentanaPlanetas(self,b):
		
		for widget in self.contenedor:
			self.contenedor.remove(widget)
		
		self.label_pl = Gtk.Label(' texto prueba1')
		self.contenedor.attach(self.label_pl,0,0,1,1)

		self.contenedor.show_all()
	
		
		

	def SegundaVentanajuego(self,btn):

		for widget in self.contenedor:
			self.contenedor.remove(widget)

		self.label_ju= Gtk.Label('juega')
		self.contenedor.attach(self.label_ju,0,0,1,1)
		self.contenedor.show_all()



if __name__ == '__main__':
	init = Inicio()
	init.show_all()
	Gtk.main()
