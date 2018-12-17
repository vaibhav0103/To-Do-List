$(document).ready(function(event){
	
    $(function(){
        setTimeout(function(){
            $('.alert').slideUp(2000);
        }, 5000);
    });

    // Delete Item From To Do List
	$(document).on('click', '#deltodo', function(event){
	// $('#deltodo').click(function(){

		event.preventDefault();

        var url = $(this).parent().attr("action");
        console.log(url);
        csrf = $('input[name="csrfmiddlewaretoken"]').val()

        $.ajax({
            type:'POST',
            url: url,
            data: { 'csrfmiddlewaretoken': csrf },
            dataType: 'json',
            success: function(response){
            	console.log(response['form'])
                $('.list-section').html(response['form']);
            },
            error: function(rs, e){
                console.log(rs.responseText);
            }
        });
	});

    // Add Item to the To Do List
    $(document).on('click', '#addtodo', function(event){

        event.preventDefault();

        var url = $(this).parent().attr("action");
        csrf = $('input[name="csrfmiddlewaretoken"]').val()
        content = $('input[name="content"]').val()

        $.ajax({
            type:'POST',
            url: url,
            data: {'content': content, 'csrfmiddlewaretoken': csrf },
            dataType: 'json',
            success: function(response){
                $('.list-section').html(response['form']);
                $('input[name="content"]').val('');
            },
            error: function(rs, e){
                console.log(rs.responseText);
            }
        });
    });

    //    to add active class on nav items
    var path = location.pathname.split("/")[1];
    //    console.log(path)
    if(path != ""){
        $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
    }else{
        $('nav a[href="/"').addClass('active');
    }

});