    // const target = document.getElementById("alertDiv");
    // window.onload = setInterval(() => target.style.opacity = '0', 2000)
    // function myFunction() {
    //     var x = document.getElementById("myLinks");
    //     if (x.style.display === "block") {
    //       x.style.display = "none";
    //     } else {
    //       x.style.display = "block";
    //     }
    //   };
    
    //   const navbar = document.querySelector('.navbar');
    //   const mobile = document.querySelector('.mobile');
      
    //   window.onscroll = () => {
    //     if (window.scrollY > 100) {
    //       navbar.classList.add('nav-active');
    //       mobile.classList.add('active');
    //     } else {
    //       navbar.classList.remove('nav-active');
    //       mobile.classList.remove('active');
    //     }
    //   };
    //   var app = new Vue({
    //     el: '#app',
    //     data:{
    //       state: "close"
    //     }
    //   });


    const target = document.getElementById("alertDiv");
window.onload = setInterval(() => target.style.opacity = '0', 2000)
function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  };

const navbar = document.querySelector('.navbar');
const mobile = document.querySelector('.mobile');

window.onscroll = () => {
  if (window.scrollY > 100) {
    navbar.classList.add('nav-active');
    mobile.classList.add('active');
  } else {
    navbar.classList.remove('nav-active');
    mobile.classList.remove('active');
  }
};

var app = new Vue({ el: '#app', data:{ state: "close" } });

      
