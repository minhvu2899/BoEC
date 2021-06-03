
  var shipping_id
  var payment_id
  var subtotal=$('#total').text();
  var total
  $('#shipping').change(function(){
    shipping_id=  $('#shipping').val()
    var fee =$("#shipping option:selected").data('fee')
   
    total = Number(subtotal)+ Number(fee)
    $('#total').html(total)
     $('.shipping-fee').html(fee)
   })
  var btn_payment=$('button[name="payment_method"]')
      btn_payment.click(function(){
        btn_payment.removeClass('btn-outline-danger')
        $(this).addClass("btn-outline-danger")
        payment_id= $(this).data('id')
        console.log(payment_id);
  })
  

 
  $('#order').click(function(){

    $.post("/order/addOrder/",
        {
          shipping_id:shipping_id,
          payment_id: payment_id,
          total: total,
          'csrfmiddlewaretoken':'{{csrf_token}}',
        }, 
        function(data, status){
          if(status =='success'){
            window.location="{% url 'user:purchase'%}"
          }
        }); 
  })
 
 
  $('#total').html(total)

    $('a[name="addCart"]').click(function(){
        var id= $(this).data('id');
        // alert(id);
        var number =$('#product_number').val();
        if(!number){
          number =1;
        }
        $.post("/cart/addCart/",
        {
          product_id: id,
          product_number: number,
          'csrfmiddlewaretoken':'{{csrf_token}}',
        },
        function(data, status){
          if(status =='success'){
            alert("Thêm vào giỏ hàng thành công!");
            alert(data)
          }
        }); 
    })

    let x = document.querySelectorAll(".price-product");
    for (let i = 0, len = x.length; i < len; i++) {
        let num = Number(x[i].innerHTML)
                  .toLocaleString('en');
        x[i].innerHTML = num;
        x[i].classList.add("currSign");
    }
    var quantity =$("input[name='quantity']")
    console.log(quantity);
  
    $(".decrease").click(function() {
      var input_el=$(this).data('id');
    

      var v=   $(`#${input_el}`).val()*1 -1;
      if(v>=$(`#${input_el}`).attr('min'))
      $(`#${input_el}`).val(v)
      $.post("/cart/update/",
        {
          cart_id:  input_el,
          quantity: $(`#${input_el}`).val(),
          'csrfmiddlewaretoken':'{{csrf_token}}',
        },
        function(data, status){
          if(status =='success'){
           
            location.reload();
          }
        }); 
    });
    

    $(".increase").click(function() {
      var input_el=$(this).data('id');
      var v=   $(`#${input_el}`).val()*1 + 1;
      $(`#${input_el}`).val(v)
      if(v<= $(`#${input_el}`).attr('max'))
      $(`#${input_el}`).val(v)
      $.post("/cart/update/",
        {
          cart_id:  input_el,
          quantity: $(`#${input_el}`).val(),
          'csrfmiddlewaretoken':'{{csrf_token}}',
        },
        function(data, status){
          if(status =='success'){
              location.reload();
          }
        }); 
    });
    quantity.change(function(){
        alert();
        $.post("/cart/update/",
        {
          cart_id: $(this).attr("id"),
          quantity: $(this).val(),
          'csrfmiddlewaretoken':'{{csrf_token}}',
        },
        function(data, status){
          if(status =='success'){
            location.reload();
          }
        }); 
    })
    var delete_item =$('a[name="delete_item"]')
    delete_item.click(function(e){
        e.preventDefault();
        alert($(this).data('id'))
    })
    var btn_default_address= $('button[name="btn-default-address"]');
    btn_default_address.click(function(){
      address_id= $(this).data('id');
      $.post("/user/address/",
        {
          address_id: address_id,
          'csrfmiddlewaretoken':'{{csrf_token}}',
        },
        function(data, status){
          if(status =='success'){
            alert("Thay doi thanh cong!");
            location.reload();
          }
        }); 
    })

