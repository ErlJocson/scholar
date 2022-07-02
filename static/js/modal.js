function closeModal(id) {
  var modal = document.getElementById(id).style;
  if (modal.display === "none") {
    modal.display = "flex";
  } else {
    modal.display = "none";
  }
}
