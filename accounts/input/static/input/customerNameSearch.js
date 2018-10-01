var searchByCustomerNameModal = document.getElementById("searchByCustomerNameModal");

// Get the button that opens the modal
var searchByCustomerNameBtn = document.getElementById("searchByCustomerNameBtn");

// Get the <span> element that closes the modal
var closeModalBtn = document.getElementById("closeModalBtn");

// When the user clicks on the button, open the modal
searchByCustomerNameBtn.onclick = function(){
    searchByCustomerNameModal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
closeModalBtn.onclick = function(){
    searchByCustomerNameModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
/*window.onclick = function(event){
    if (event.target == modal) {
        searchByCustomerNameModal.style.display = "none";
    }
}*/