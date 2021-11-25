// Gtk Version: 3
#include <gtk/gtk.h>

static void on_app_activate(GApplication *app, gpointer data) {
    GtkWidget *window = gtk_application_window_new(GTK_APPLICATION(app));
    GtkWidget *btn = gtk_button_new_with_label("Hello, World!");
    gtk_container_add(GTK_CONTAINER(window), btn);
    gtk_widget_show_all(GTK_WIDGET(window));
}

int main(int argc, char *argv[]) {
    GtkApplication *app = gtk_application_new("org.miniprime1.hello_world", G_APPLICATION_FLAGS_NONE);
    g_signal_connect(app, "activate", G_CALLBACK(on_app_activate), NULL);
    int status = g_application_run(G_APPLICATION(app), argc, argv);
    g_object_unref(app);
    return status;
}