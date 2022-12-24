function validate()
{
	var username=document.getElementById("username").value;
	var password=document.getElementById("password").value;
	if(username=="user" && password=="user")
	{
		return window.location.href="user.html";
	}
	else if(username=="admin" && password=="admin")
	{
		return window.location.href="admin.html";
	}
	else
	{
		alert("Login failed");
	}
}	

