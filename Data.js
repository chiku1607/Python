var firebaseConfig = {
    apiKey: "AIzaSyDk0D7ScuLDGkxnT7yA16jo3D39oVC7_sY",
    authDomain: "contact-form-2058c.firebaseapp.com",
    databaseURL: "https://contact-form-2058c.firebaseio.com",
    projectId: "contact-form-2058c",
    storageBucket: "contact-form-2058c.appspot.com",
    messagingSenderId: "616100050054",
    appId: "1:616100050054:web:6325e24a87d1013f05cd07",
    measurementId: "G-9ENETHY2JP"
};
firebare.initiaizer(config);

// reference messages collection
var messagesRef = firebare.database().ref('messages');

// Listen for form submit
document.getElementById('Contact Form').addEventListener('submit',SubmitForm);

// submit form
function SubmitForm(e){
    e.preventDefault();
    // get values
    var FirstName = getInputVal('FirstName');
    var LastName = getInputVal('LastName');
    var EmailAddress = getInputVal('EmailAddress');
    var Password = getInputVal('Password');
    var ConfirmPassword = getInputVal('ConfirmPassword');
    var MobileNumber = getInputVal('MobileNumber');
    var Message = getInputVal('Message');

    //save message
    SaveMessage(FirstName,LastName,EmailAddress,Password,ConfirmPassword,MobileNumber,Message);

    //show alert
    document.querySelector('.alert').style.display="block";

    //hide alert after 5 sec
    //setTimeout(function(){
    //},5000);

}

// save the message to firebase
function SaveMessage(FirstName,LastName,EmailAddress,Password,ConfirmPassword,MobileNumber,Message){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
        FirstName : FirstName,
        LastName : LastName,
        EmailAddress : EmailAddress,
        Password : Password,
        ConfirmPassword : ConfirmPassword,
        MobileNumber : MobileNumber,
        Message : Message
    });
}




//function to get form values
function getInputVal(id){
    return document.getElementById(id).value;
}