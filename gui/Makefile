all: linux

gui:
	pyuic5 -o ui.py ui/main.ui

ressources:
	pyrcc5 images/resources.qrc -o resources_rc.py

linux: gui ressources

clean:
	rm -rf dist build ui.py
