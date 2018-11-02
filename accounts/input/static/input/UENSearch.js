var searchByUENModal = document.getElementById("searchByUENModal");

// Get the button that opens the modal
var searchByUENBtn = document.getElementById("searchByUENBtn");

// Get the <span> element that closes the modal
// When the user clicks on the button, open the modal
searchByUENBtn.onclick = function(){
    searchByUENModal.style.display = "block";
}

var searchByUENModalCloseBtn = document.getElementById("searchByUENModalCloseBtn");
// When the user clicks on <span> (x), close the modal
searchByUENModalCloseBtn.onclick = function(){
    searchByUENModal.style.display = "none";
}