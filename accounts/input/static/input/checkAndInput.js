function searchCustomerByName(){
    $.ajax({
        //url: your_url,
        type:"GET",
        url:'/input/searchCustomerByName'
        datatype:"json",
        async:true,
        data: {
            data: $('#customerNameSearchInputBox').val(),
        }
        success: function (data) {

            // success callback
            // you can process data returned by function from views.py
        }
    });
});

function searchCustomerByName(){
    $.ajax({
        //url: your_url,
        type:"GET",
        url:'/input/searchCustomerByUEN'
        datatype:"json",
        async:true,
        data: {
            data: $('#customerNameSearchInputBox').val(),
        }
        success: function (data) {

            // success callback
            // you can process data returned by function from views.py
        }
    });
});