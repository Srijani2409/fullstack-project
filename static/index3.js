function validateForm(){
    let name=document.forms["myForm"]["name"].value;
    let email=document.forms["myForm"]["email"].value;
    let phone=document.forms["myForm"]["phone"].value;
    if (name==="" || email==="" || phone===""){
        alert("Please fill all fields");
        return false;
    }
    if (phone.length!==10){
        alert("Phone number must be 10 digits")
        return false;
    }
    alert("Form submitted successfully!");
    return true;
}