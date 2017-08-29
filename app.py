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
        self.sistemasolar = Gtk.Button('Sistema Solar')
        self.planetas = Gtk.Button('Planetas')
        self.juego = Gtk.Button('Juego')
        self.canvas.attach(self.sistemasolar, 1, 1, 1, 1)
        self.canvas.attach(self.planetas, 1, 1, 2, 1)
        self.canvas.attach_next_to(self.juego,self.planetas,self.sistemasolar,Gtk.PositionType.RIGHT,1,1)
        self.sistemasolar.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.planetas.connect('clicked',self.SegundaVentanaPlanetas)
        self.juego.connect('clicked',self.SegundaVentanajuego)

        self.canvas.show_all()


    def PrimeraVentanaSistemaSolars(self,btn):
        for widget in self.canvas:
            self.canvas.remove(widget)

        self.fondoPantalla = Gtk.Image()
        self.canvas.attach(self.fondoPantalla,0,0,4,1)
        self.fondoPantalla.set_from_file('imagenes/sistemasolar.png')

        buf = self.fondoPantalla.get_pixbuf()
        self.fondoPantalla.set_from_pixbuf(
        buf.scale_simple(640, 390, GdkPixbuf.InterpType.BILINEAR))

        self.fondoPantalla.show()

        self.sistemasolar = Gtk.Button('Sistema Solar')
        self.planetas = Gtk.Button('Planetas')
        self.juego = Gtk.Button('Juego')
        
        self.canvas.attach_next_to(self.sistemasolar,self.fondoPantalla,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach_next_to(self.planetas,self.sistemasolar,Gtk.PositionType.RIGHT,1,1)
        self.canvas.attach_next_to(self.juego,self.sistemasolar,Gtk.PositionType.RIGHT,1,1)
        self.sistemasolar.connect('clicked',self.SegundaVentanaSistemaSolar)
        self.planetas.connect('clicked',self.SegundaVentanaPlanetas)
        self.juego.connect('clicked',self.SegundaVentanajuego)
        self.canvas.show_all()
