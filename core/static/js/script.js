function mostrar(id) {
    if (id == "ida") {
        $("#ida").show();
        $("#idayvuelta").hide();
        $("#puntoapunto").hide();
    }

    if (id == "idayvuelta") {
        $("#ida").hide();
        $("#idayvuelta").show();
        $("#puntoapunto").hide();
    }

    if (id == "puntoapunto") {
        $("#ida").hide();
        $("#idayvuelta").hide();
        $("#puntoapunto").show();
    }

}