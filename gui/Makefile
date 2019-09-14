all: linux

gui:
	pyuic5 -o ui_main.py ui/main.ui
	pyuic5 -o ui_password.py ui/password.ui

ressources:
	pyrcc5 images/resources.qrc -o resources_rc.py

linux: gui ressources

clean:
	rm -rf dist build ui.py
