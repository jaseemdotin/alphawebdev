function check()
{

var mailpattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
var nopattern = /^\d{10}$/;
var pinpattern = /^\d{6}$/;
var numberonlypattern = /^[0-9]*$/;
var usernamelenght=5;
var clenght=10;
var fnamelength=4;
var citypattern=/^\d+/;

var mail=document.getElementById('mail').value;
var fname=document.getElementById('fname').value;
var uname=document.getElementById('uname').value;
var city=document.getElementById('city').value;
var pincode=document.getElementById('pincode').value;
var pass1=document.getElementById('pass1').value;
var pass2=document.getElementById('pass2').value;
var mobno=document.getElementById('mobno').value;
if(fname.length<=2||fname.length>=26)
{
alert('make sure the firstname is between 3-26 characters long  ');
return false;
}
else if(fname.match(numberonlypattern))
{
alert('make sure the firstname contains at least 1 alphabet ');
return false;
}

else if(uname.length<=5||uname.length>=26)
{
alert('make sure the Username is between 6-26 characters long  ');
return false;
}
else if(uname.match(numberonlypattern))
{
alert('make sure the Username contains at least 1 alphabet ');
return false;
}


else if(city.length<=2||city.length>=100)
{
alert('make sure the city is between 2-100 characters long  ');
return false;
}
else if(city.match(citypattern))
{
alert('city cannot start with number ');
return false;
}


else if(pincode.length!=6)
{
alert('pincode contains 6 letters');
return false;
}
else if(pass1.length<=7)
{
alert('password contain at least 8 digit');
return false;
}

else if(pass1.match(numberonlypattern))
{
alert('password contain at least 1 letter');
return false;
}

else if(pass1!=pass2)
{
alert('password mismatch');
return false;
}


else if(mobno.match(nopattern)&&mail.match(mailpattern))
{
return true;
}
else
{
alert('check mobile number and email');
return false;
}

}
function productcheck()
{
document.getElementById("btnLoad").addEventListener("click", function showFileSize() {
    // (Can't use `typeof FileReader === "function"` because apparently it
    // comes back as "object" on some browsers. So just see if it's there
    // at all.)
    if (!window.FileReader) { // This is VERY unlikely, browser support is near-universal
        console.log("The file API isn't supported on this browser yet.");
        return;
    }

    var input = document.getElementById('fileinput');
    if (!input.files) { // This is VERY unlikely, browser support is near-universal
        console.error("This browser doesn't seem to support the `files` property of file inputs.");
    } else if (!input.files[0]) {
        addPara("Please select a file before clicking 'Load'");
    } else {
        var file = input.files[0];
        addPara("File " + file.name + " is " + file.size + " bytes in size");
    }
});

function addPara(text) {
    var p = document.createElement("p");
    p.textContent = text;
    document.body.appendChild(p);
}

function alt()
{
alert("g");
}


}