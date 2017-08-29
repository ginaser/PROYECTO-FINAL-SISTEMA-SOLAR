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
        self.PrimeraVentanaPlanta()
        self.fondo()

    def fondo(self):
        self.fondoPantalla = Gtk.Image()
        self.canvas.attach(self.fondoPantalla,0,0,4,1)
        self.fondoPantalla.set_from_file('imagenes/maxresdefault.jpg')

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

    def PrimeraVentanaPlanta(self):
        for widget in self.canvas:
            self.canvas.remove(widget)
        self.planta = Gtk.Button('Clasificacion de las plantas')
        self.animales = Gtk.Button('Clasificacion de los animales')
        self.canvas.attach(self.planta, 1, 1, 1, 1)
        self.canvas.attach_next_to(self.animales,self.planta,Gtk.PositionType.RIGHT,1,1)
        self.planta.connect('clicked',self.SegundaVentanaPlanta)
        self.animales.connect('clicked',self.SegundaVentanaAnimal)
        self.canvas.show_all()


    def PrimeraVentanaPlantas(self,btn):
        for widget in self.canvas:
            self.canvas.remove(widget)

        self.fondoPantalla = Gtk.Image()
        self.canvas.attach(self.fondoPantalla,0,0,4,1)
        self.fondoPantalla.set_from_file('imagenes/maxresdefault.jpg')

        buf = self.fondoPantalla.get_pixbuf()
        self.fondoPantalla.set_from_pixbuf(
        buf.scale_simple(640, 390, GdkPixbuf.InterpType.BILINEAR))

        self.fondoPantalla.show()

        self.planta = Gtk.Button('Clasificacion de las plantas')
        self.animales = Gtk.Button('Clasificacion de los animales')
        
        self.canvas.attach_next_to(self.planta,self.fondoPantalla,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach_next_to(self.animales,self.planta,Gtk.PositionType.RIGHT,1,1)
        self.planta.connect('clicked',self.SegundaVentanaPlanta)
        self.animales.connect('clicked',self.SegundaVentanaAnimal)
        self.canvas.show_all()

    def SegundaVentanaPlanta(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_conflor_planta = Gtk.Label('Con Flor')
        self.label_sinflor_planta = Gtk.Label('sin Flor')

        self.boton_siguiente_planta = Gtk.Button('Siguinte')
        self.canvas.attach(self.label_conflor_planta,0,0,1,1)
        self.canvas.attach_next_to(self.label_sinflor_planta,self.label_conflor_planta,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach(self.boton_siguiente_planta,0,2,1,1)

        self.canvas.show_all()
        self.boton_siguiente_planta.connect('clicked',self.TerceraVentanaPlanta)
        


    def TerceraVentanaPlanta(self,b):
        
        for widget in self.canvas:
            self.canvas.remove(widget)
        
    
        self.boton_inicio_planta = Gtk.Button('Inicio')
        self.label_numero_planta = Gtk.Label('Numero de veces')
        self.numero_de_entrada_planta = Gtk.Entry() 
        self.canvas.attach(self.label_numero_planta,0,0,1,1)
        self.canvas.attach_next_to(self.numero_de_entrada_planta,self.label_numero_planta,Gtk.PositionType.RIGHT,1,1)
        self.canvas.attach_next_to(self.boton_inicio_planta,self.label_numero_planta,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.show_all()
        self.boton_inicio_planta.connect('clicked',self.CuartaVentanaPlanta)


    def CuartaVentanaPlanta(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_planta = Gtk.Label('las plantas de mi pais')
        self.canvas.attach(self.label_planta,0,0,1,1)
        self.canvas.show_all()

    #modificacioooon 
    def SegundaVentanaAnimal(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.fondoPantalla = Gtk.Image()
        self.canvas.attach(self.fondoPantalla,0,0,3,1)
        self.fondoPantalla.set_from_file('imagenes/clasificacionanimal.jpg')

        buf = self.fondoPantalla.get_pixbuf()
        self.fondoPantalla.set_from_pixbuf(
        buf.scale_simple(640, 380, GdkPixbuf.InterpType.BILINEAR))

        self.fondoPantalla.show()

        self.alineadoderecho = Gtk.Label('')
        self.interlineado = Gtk.Label('')
        
        self.canvas.attach_next_to(self.alineadoderecho,self.fondoPantalla,Gtk.PositionType.BOTTOM,1,1)

        self.label_clasf_animal = Gtk.Label()
        self.label_clasf_animal.set_markup('<i><b>Clasificacion de los animales:</b></i>')
        self.canvas.attach_next_to(self.label_clasf_animal,self.alineadoderecho,Gtk.PositionType.RIGHT,1,1)
        
        self.boton_anatomia_animal = Gtk.Button('Segun su Anatomia')
        self.boton_reprodicir_animal = Gtk.Button('Segun su forma de reproducirse')
        self.boton_alimentacion_animal = Gtk.Button('Segun su Alimentacion')
        self.boton_dondeviven_animal = Gtk.Button('Tipos de habitats')
        
        self.canvas.attach(self.boton_dondeviven_animal,0,2,1,1)
        self.canvas.attach_next_to(self.boton_anatomia_animal,self.boton_dondeviven_animal,Gtk.PositionType.RIGHT,1,1)
        self.canvas.attach_next_to(self.boton_alimentacion_animal,self.boton_anatomia_animal,Gtk.PositionType.RIGHT,1,1)
        self.canvas.attach_next_to(self.interlineado,self.boton_dondeviven_animal,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach_next_to(self.boton_reprodicir_animal,self.interlineado,Gtk.PositionType.BOTTOM,1,1)
        self.volver1 = Gtk.Button('Volver')
        self.canvas.attach_next_to(self.volver1,self.boton_reprodicir_animal,Gtk.PositionType.RIGHT,1,1)
        
        self.canvas.show_all()
        self.volver1.connect('clicked',self.PrimeraVentanaPlantas)
        self.boton_dondeviven_animal.connect('clicked',self.dondeViven)
        self.boton_alimentacion_animal.connect('clicked',self.TerceraVentanaAnimal)
        self.boton_anatomia_animal.connect('clicked',self.TerceraVentanaAnimal)
        self.boton_reprodicir_animal.connect('clicked',self.TerceraVentanaAnimal)
        
        


    def dondeViven(self,b):
        
        for widget in self.canvas:
            self.canvas.remove(widget)


        self.acuatico = Gtk.Image()
        self.canvas.attach(self.acuatico,0,0,1,1)
        self.acuatico.set_from_file('imagenes/animalesacuaticos.jpg')

        buf = self.acuatico.get_pixbuf()
        self.acuatico.set_from_pixbuf(
        buf.scale_simple(320,220, GdkPixbuf.InterpType.BILINEAR))

        self.acuatico.show()

        self.terrestre = Gtk.Image()
        self.canvas.attach_next_to(self.terrestre,self.acuatico,Gtk.PositionType.RIGHT,1,1)
        self.terrestre.set_from_file('imagenes/terrestre.jpg')

        buf = self.terrestre.get_pixbuf()
        self.terrestre.set_from_pixbuf(
        buf.scale_simple(320,220, GdkPixbuf.InterpType.BILINEAR))

        self.terrestre.show()


        self.space = Gtk.Label('')
        self.canvas.attach_next_to(self.space,self.acuatico,Gtk.PositionType.BOTTOM,1,1)
        self.labelac = Gtk.Label()
        self.labelac.set_markup("Los <b>animales acuaticos</b> son aquellos\n que viven en el agua, tanto en el mar\n como en agua dulce(Rios, Lagos)")
        self.canvas.attach_next_to(self.labelac,self.space,Gtk.PositionType.BOTTOM,1,1)

        self.labelterr = Gtk.Label()
        self.labelterr.set_markup("Los <b>Animales terrestre</b> son los\nanimales que viven en la tierra")
        self.canvas.attach_next_to(self.labelterr,self.terrestre,Gtk.PositionType.BOTTOM,10,10)
        
        self.canvas.show_all()

