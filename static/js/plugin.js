$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url : btn.attr("data.url"),
			type:'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-book').modal('show'); 
			},
			success: function(data){
				$('#modal-book .modal.content').html(data.html_form);
			}	
			
		});
	};
    
    var SaveForm = function(){
    	var form = $(this);
    	$.ajax({
    		url: form.attr('data.url'),
    		data: form.serialize(),
    		type: form.attr(method),
    		dataType: 'json',
    		success: function(data){
    			if(data.form_is_valid){
    				$('#myTable tbody').html(data.list_client);
    			}else{
    				$('#modal-book .modal-content').html(data.html_form)
    			}

    		}
    	})
    	return false;
    }
    //create
     $(".ShowForm").click(ShowForm)
    
     $('#modal-book').on("submit",".create-form",SaveForm)
 
    //update
     $('#myTable').on("click",".show-form-update",ShowForm);
    
     $('#modal-book').on("submit",".update-form",SaveForm)
}); 