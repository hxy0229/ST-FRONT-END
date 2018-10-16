var searchByCustomerNameModal = document.getElementById("searchByCustomerNameModal");

// Get the button that opens the modal
var searchByCustomerNameBtn = document.getElementById("searchByCustomerNameBtn");

// Get the <span> element that closes the modal
// When the user clicks on the button, open the modal
searchByCustomerNameBtn.onclick = function(){
    searchByCustomerNameModal.style.display = "block";
}

var closeModalBtn = document.getElementByClassName("closeModalBtn");
// When the user clicks on <span> (x), close the modal
closeModalBtn.onclick = function(){
    searchByCustomerNameModal.style.display = "none";
}