
// function ZubcwEsdkf(id) {
//     console.log('ajaxstart')
//     $.ajax({
//         url: "{% url 'ajax_fmc_password/' %}",
//         type: 'POST',
//         data: {
//             'value': id,
//             'csrfmiddlewaretoken': '{{ csrf_token }}'
//         },
//         success: function (response) {
//             // $('#existlabel').removeAttr('hidden');
//             console.log('its works')
//         }
//     });
// }




// {/* <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> */}

// $(document).ready(function () {
//     $('#signup-form').submit(function (event) {
//         event.preventDefault();

//         var namesis = $('#yourName').val();
//         var emailis = $('#yourEmail').val();
//         var phoneis = $('#yourPhone').val();
//         var cityis = $('#yourCity').val();

//         console.log($(this).serialize());
//         $('#spin').removeAttr('hidden').show();
//         $('#word').hide();

//         $.ajax({
//             url: "{% url 'signup_ajax' %}",
//             type: 'post',
//             data: $(this).serialize(),
//             success: function (response) {
//                 var save = response.otpnumber;
//                 console.log(save);

//                 sessionStorage.setItem("OTP", save);
//                 sessionStorage.setItem('nameis', namesis);
//                 sessionStorage.setItem('emailis', emailis);
//                 sessionStorage.setItem('phoneis', phoneis);
//                 sessionStorage.setItem('cityis', cityis);

//                 $('#signupform').hide();
//                 $('#otpform').removeAttr('hidden');

//                 $('#hiddenEmail').text(emailis.substr(0, 3) + "******" + emailis.substr(emailis.indexOf("@")));
//             },
//             complete: function () {
//                 $('#spin').hide();
//             }
//         });
//     });
// });




// function UserNameCheck() {
//     var username = $('#inputUsername').val();
//     $.ajax({
//         url: "{% url 'username_checker' %}",
//         type: 'POST',
//         data: {
//             'value': username,
//             'csrfmiddlewaretoken': '{{ csrf_token }}'
//         },
//         success: function (response) {
//             $('#existlabel').removeAttr('hidden');
//         }
//     });
// }
