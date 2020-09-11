all: linux

gui:
	pyuic5 -o ui/py/ui_main.py ui/ui/main.ui
	pyuic5 -o ui/py/ui_finished.py ui/ui/finished.ui
	pyuic5 -o ui/py/ui_password.py ui/ui/password.ui
	pyuic5 -o ui/py/ui_settings.py ui/ui/settings.ui
	pyuic5 -o ui/py/ui_drink.py ui/ui/drink.ui
	pyuic5 -o ui/py/ui_loading.py ui/ui/loading.ui

ressources:
	pyrcc5 images/resources.qrc -o resources_rc.py

linux: gui ressources

clean:
	rm -rf dist build ui.py
