function goToLoginPage() {
   window.location.href = "/assets/pages/login.html";
}

document.getElementById('loginForm').addEventListener('submit', function (event) {
   event.preventDefault();

   var username = document.getElementById('username').value;
   var password = document.getElementById('password').value;

   if (username && password) {
      login(username, password);
   } else {
      alert('Please fill in all fields');
   }
});

function login(username, password) {
   var xhr = new XMLHttpRequest();

   xhr.open('POST', 'login_url', true);
   xhr.setRequestHeader('Content-Type', 'application/json');

   xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
         var json = JSON.parse(xhr.responseText);

         if (json.success) {
            alert('Login successful');
            window.location.href = "another_page.html";
         } else {
            alert('Incorrect username or password');
         }
      }
   };

   var data = JSON.stringify({
      username: username,
      password: password
   });

   xhr.send(data);
}