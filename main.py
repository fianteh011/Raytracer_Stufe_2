"""Einfacher raytracer
Stufe_0: Es werden nur die Objektfarben ermittelt"""
from Help.color import Color
from Help.point import Point
from Help.image import MyImage
from Render.light import Light
from Render.material import Material
from Render.engine import RenderEngine
from Render.scene import Scene
from Render.camera import Camera
from Geometry.sphere import Sphere

##### Anzeige des Renderfortschritts (True: mit Anzeige, False: ohne Anzeige)
ZAEHLER = True
##### Ausgabe am Bildschirm (True) oder in der angegebenen Datei (False)
RENDERED_IMG = "2balls.bmp"
SHOW = True
##### Bildformat festlegen (für Tests kleines Ausgabeformat, um Renderzeit zu sparen)
# Grossbuchstaben sind Konstanten !
WIDTH = 320
HEIGHT = 200


def main():
    ##### Augpunkt/Camera setzen
    CAMERA = Camera(0, 0, -1)

    ##### Objekte der Szene lokal erzeugen

    ##FARBEN
    rot = Color.from_hex("#FF0000")
    gelb = Color.from_hex("#FFFF00")

    ##Kugeln
    kugel1 = Sphere(Point(0.75, -0.1, 1.0), 0.6, Material(rot))
    kugel2 = Sphere(Point(-0.75, -0.1, 2.5), 0.6, Material(gelb))

    testKugel = Sphere(Point(0, 0, 0), 0.5, Material(rot))

    OBJECTS = [
        # rote Kugel1
        kugel1,
        # gelbe kugel2
        kugel2
        #testKugel
    ]
    # Punktlichter: Keine Beleuchtung nur Objektfarbe
    ##Farben
    weiss = Color.from_hex("#FFFFFF")
    grau = Color.from_hex("#F0F0F0")

    licht1 = Light(Point(1.5, -0.5, -10.0), weiss)
    licht2 = Light(Point(-0.5, -10.5, 0.0), grau)
    LIGHTS = [
        #weisses Licht
        licht1,
        #graues Licht
        licht2
    ]

    ##### Szene einrichten
    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)

    ##### Render-Engine instanzieren (starten)
    engine = RenderEngine()

    ##### Bild rendern (berechnen)
    image = engine.rendertask(scene, ZAEHLER)

    ##### gerendertes Bild anzeigen/speichern
    if (SHOW):
        image.show_image()
    else:
        image.write_image(RENDERED_IMG)


if __name__ == "__main__":
    main()
