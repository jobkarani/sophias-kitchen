// var updateBtns = document.getElementsByClassName('update-cart')

// for(var i=0; i<updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', function() {
//         var productId = this.dataset.product
//         var action = this.dataset.action
//         console.log('productId: ', productId, 'action: ', action)

//         console.log('User: ', user)
//         if(user == 'AnonymousUser') {
//             addCookieItem(productId, action)
//         }
//         else {
//             updateUserOrder(productId, action)
//         }
//     })
// }

// function addCookieItem(productId, action) {
//     console.log('Not logged in!')

//     if(action == 'add') {
//         if(cart[productId] == undefined) {
//             cart[productId] = {'quantity': 1}
//         }
//         else {
//             cart[productId]['quantity'] += 1
//         }
//     }

//     if(action == 'remove') {
//         cart[productId]['quantity'] -= 1

//         if(cart[productId]['quantity'] <= 0) {
//             console.log("Remove Item")
//             delete cart[productId]
//         }
//     }

//     console.log('Cart: ', cart)
//     document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
//     location.reload()
// }

// function updateUserOrder(productId, action){
// 	console.log('User is authenticated, sending data...')

// 		var url = '/update_item/'

// 		fetch(url, {
// 			method:'POST',
// 			headers:{
//                 'Content-Type':'application/json',
//                 'X-CSRFToken':csrftoken,
// 			}, 
// 			body:JSON.stringify({'productId':productId, 'action':action})
//         })
        
// 		.then((response) => {
// 		   return response.json();
//         })
        
// 		.then((data) => {
//             console.log('Data:', data)
//             location.reload()
// 		});
// }

// document.querySelector('#cakes').addEventListener('click', function(){
//     const display = document.querySelector('.cat1').textContent;
//     console.log(display);
//     document.querySelector('body').style.backgroundColor = '#60b347';
//   })

// $(function() {
// 	'use strict';
	
//   $('.form-control').on('input', function() {
// 	  var $field = $(this).closest('.form-group');
// 	  if (this.value) {
// 	    $field.addClass('field--not-empty');
// 	  } else {
// 	    $field.removeClass('field--not-empty');
// 	  }
// 	});

// });


// //Menu toggle-effect
// $(document).ready(function(){
// 	$(".menu-icon").on("click",function(){
// 	  $("nav ul").toggleClass("showing");
// 	});
//   });
  
//   //Scrolling Effect
//   $(window).on('scroll', function(){
// 	if($(window).scrollTop()) {
// 	  $('nav').addClass('black');
// 	}
// 	else{
// 	  $('nav').removeClass('black')
// 	}
//   })

$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
      items:1,
      loop:true,
      nav:true,
      dots:true,
      autoplay:true,
      autoplaySpeed:1000,
      smartSpeed:1500,
      autoplayHoverPause:true
  });
});