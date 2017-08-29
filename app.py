import random
import gi
import logging
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import (ActivityToolbarButton, StopButton)

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
logger = logging.getLogger(__name__)


import pygtk
pygtk.require('2.0')
import gtk


import sys


class sistemasolar(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.set_default_size(640,480)
        self.agregar_toolbar()
        self.agregar_contenedor()
        self.PrimeraVentanaSistemaSolar()
        self.fondo()

    def fondo(self):
        self.fondoPantalla = Gtk.Image()
        self.canvas.attach(self.fondoPantalla,0,0,4,1)
        self.fondoPantalla.set_from_file('imagenes/sistemasolar.png')

        buf = self.fondoPantalla.get_pixbuf()
        self.fondoPantalla.set_from_pixbuf(
        buf.scale_simple(640, 390, GdkPixbuf.InterpType.BILINEAR))

        self.fondoPantalla.show()

    def agregar_toolbar(self):
        toolbar_box = ToolbarBox()
        aplicacion_toolbar_boton = ActivityToolbarButton(self)
        aplicacion_stop_boton = StopButton(self)
        toolbar_box.toolbar.insert(aplicacion_toolbar_boton, 0)
        aplicacion_toolbar_boton.show()
        toolbar_box.toolbar.insert(aplicacion_stop_boton, -1)
        aplicacion_stop_boton.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()


    def agregar_contenedor(self):
        self.canvas = Gtk.Grid()
        self.canvas.set_column_homogeneous(False)
        self.add(self.canvas)

    def PrimeraVentanaSistemaSolar(self):
        for widget in self.canvas:
            self.canvas.remove(widget)
        self.sistema = Gtk.Button('El Sistema Solar')
        self.planetas = Gtk.Button('Los Planetas')
        self.canvas.attach(self.planta, 1, 1, 1, 1)
        self.canvas.attach_next_to(self.planetas,self.sistema,Gtk.PositionType.RIGHT,1,1)
        self.sistema.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.planetas.connect('clicked',self.SegundaVentanaPlanetas)
        self.canvas.show_all()


    def PrimeraVentanaPlantas(self,btn):
        for widget in self.canvas:
            self.canvas.remove(widget)

        self.fondoPantalla = Gtk.Image()
        self.canvas.attach(self.fondoPantalla,0,0,4,1)
        self.fondoPantalla.set_from_file('imagenes/sistemasolar.png')

        buf = self.fondoPantalla.get_pixbuf()
        self.fondoPantalla.set_from_pixbuf(
        buf.scale_simple(640, 390, GdkPixbuf.InterpType.BILINEAR))

        self.fondoPantalla.show()

        self.sistema = Gtk.Button('El Sistema Solar')
        self.planetas = Gtk.Button('Los Planetas')
        
        self.canvas.attach_next_to(self.sistema,self.fondoPantalla,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach_next_to(self.planetas,self.sistema,Gtk.PositionType.RIGHT,1,1)
        self.sistema.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.planetas.connect('clicked',self.SegundaVentanaPlanetas)
        self.canvas.show_all()

    def SegundaVentanaSistemaSolar(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_definicion_solar = Gtk.Label('dios')
        

        self.canvas.show_all()

    def SegundaVentanaPlanetas(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_definicion_planetas = Gtk.Label('poder')
        

        self.canvas.show_all()
       