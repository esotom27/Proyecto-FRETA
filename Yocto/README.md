# meta-rpi-xfce

## Quick links

* Git repository web frontend:
  <https://github.com/marlol94/Proyecto-1-Taller-Embebidos/tree/master/Yocto/meta-rpi-xfce>
* Mailing list: <eve.soto@estudiantec.cr>

## Descripción

Estas son las especificaciones generales de BSP para raspberry pi3, incluyendo el soporte gráfico de xfce.

## Dependencias

Este meta depende de:

* URI: git://git.yoctoproject.org/poky
  * branch: warrior
  * revision: HEAD

* URI: git://git.openembedded.org/meta-openembedded
  * layers: meta-oe, meta-multimedia, meta-networking, meta-python, meta-gnome meta-raspberrypi
  * branch: warriror
  * revision: HEAD

## Quick Start

1. Buscar poky/oe-init-build-env build-rpi
2. Añadir este layer a bblayers.conf y las dependencias mencionadas
3. Modificar MACHINE en local.conf a raspberrypi3
4. bitbake rpi-xfce-image
5. Añadir a la SD el archivo sdimg 
6. Boot en su RPI.

## Maintainers

* Evelyn Soto `<eve.soto@estudiantec.cr>`
