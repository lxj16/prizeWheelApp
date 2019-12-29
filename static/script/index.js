$("#submit-btn").click(function(event) {
  let phoneNumber = $("#phoneNumber").val();

  let phoneNumberRegex = new RegExp("(^778|^604)[0-9]{7}$");

  if (phoneNumberRegex.test(phoneNumber)) {
  } else {
    alert("invalid phone number");
  }
});
