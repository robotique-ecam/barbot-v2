all: linux

gui:
	pyuic5 -o ui.py ui/main.ui

ressources:
	# pyrcc5 icons/icons.qrc -o icons_rc.py

linux: gui ressources

clean:
	rm -rf dist build ui.py
