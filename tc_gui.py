import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
from gi.repository import Gtk

# we can call it just about anything we want
class Gui:

    def on___glade_unnamed_1_destroy (self, object, data=None):
        print ("quit with cancel")
        Gtk.main_quit()

    # This is the same as above but for our menu item.
    def on_Quit_activate(self, menuitem, data=None):
        print ("quit from menu")
        Gtk.main_quit()

    # This is our init part where we connect the signals
    def __init__(self):
        self.gladefile = "model.glade" # store the file name
        self.builder = Gtk.Builder() # create an instance of the Gtk.Builder
        self.builder.add_from_file(self.gladefile) # add the xml file to the Builder

        self.builder.connect_signals(self)

        self.window = self.builder.get_object("Window1") # This gets the 'window1' object
        self.window.show() # this shows the 'window1' object
        self.aboutdialog = self.builder.get_object("aboutdialog1")
        # TextBuffer 
        self.chatEntry = self.builder.get_object("chatEntry")
        self.model = Gtk.ListStore (str)
        self.treeview = Gtk.TreeView(self.model)
        self.treeview = self.builder.get_object("treeView")
        self.treeview.set_model(self.model)
        render1 = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("peers", render1, text = 0)
        self.treeview.append_column(column1)
        self.textBox = self.builder.get_object("textBox")


        t = Gtk.TextBuffer()
        t.set_text('tnoeu\nnigga')
        self.textBox.set_buffer(t)

    def add_peer(self, id):
        self.model.append((id))

    def on_gtk_about_activate(self, menuitem, data=None):
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()

    def on_chatentry_insert_text(self,*args,**kwargs):
        pass

    def on_chatentry_delete_from_cursor(self, *args, **kwargs):
        pass

    def on_chatentry_backspace(self, *args, **kwargs):
        pass

    def on_chatentry_insert_at_cursor(self, *args, **kwargs):
        pass

    def on_chatentry_move_cursor(self, *args, **kwargs):
        pass

    def on_chatentry_activate(self, *args, **kwargs):
        print (self.chatEntry.get_text())
        self.chatEntry.set_text('')

    def on_chatentry_changed(self, *args, **kwargs):
        pass

    def on_chatentry_delete_text(self, *args, **kwargs):
        pass

if __name__ == "__main__":
    main = Gui()
    Gtk.main()
