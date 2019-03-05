$('#autorizationBtn').click(function() {
    getLogPass();
 });

function getLogPass(){
    var logName = document.getElementById('loginField').value;
    var passName = document.getElementById('passwordField').value;

    alert(logName + passName);
}
