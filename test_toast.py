import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib

class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.example.test')
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        win = Adw.ApplicationWindow(application=app)
        self.overlay = Adw.ToastOverlay()
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        btn1 = Gtk.Button(label="Show Toast 2s")
        btn1.connect('clicked', self.show_toast_2)
        btn2 = Gtk.Button(label="Show Toast Default")
        btn2.connect('clicked', self.show_toast_default)
        
        box.append(btn1)
        box.append(btn2)
        
        self.overlay.set_child(box)
        win.set_content(self.overlay)
        win.present()
        
        # exit after 5 seconds to not hang
        GLib.timeout_add_seconds(6, lambda: app.quit())

    def show_toast_2(self, btn):
        toast = Adw.Toast.new("Toast 2s")
        toast.set_timeout(2)
        self.overlay.add_toast(toast)

    def show_toast_default(self, btn):
        toast = Adw.Toast.new("Toast Default")
        self.overlay.add_toast(toast)

app = MyApp()
app.run(None)
