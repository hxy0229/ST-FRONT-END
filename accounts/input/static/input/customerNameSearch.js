var searchByCustomerNameModal = document.getElementById("searchByCustomerNameModal");

// Get the button that opens the modal
var searchByCustomerNameBtn = document.getElementById("searchByCustomerNameBtn");

// Get the <span> element that closes the modal
// When the user clicks on the button, open the modal
searchByCustomerNameBtn.onclick = function(){
    searchByCustomerNameModal.style.display = "block";
}

var searchByCustomerNameModalCloseBtn = document.getElementById("searchByCustomerNameModalCloseBtn");
// When the user clicks on <span> (x), close the modal
searchByCustomerNameModalCloseBtn.onclick = function(){
    searchByCustomerNameModal.style.display = "none";
}

var customerNameSearchingBtn = document.getElementById("customerNameSearchingBtn");
     customerNameSearchingBtn.onclick = function(event){
     event.preventDefault();
     var c1 = "<li>Singtel</li>";
     $("#firstCustomerName").after(c1);
}

