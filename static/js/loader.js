// static/js/loader.js
document.addEventListener("DOMContentLoaded", function() {
    var loader = document.getElementById('loader');
    var body = document.body;
  
    function showLoader() {
      loader.style.display = 'block';
      body.classList.add('loading');
    }
  
    function hideLoader() {
      // Introduce a delay of 30 seconds (30000 milliseconds)
      setTimeout(function() {
        loader.style.display = 'none';
        body.classList.remove('loading');
      }, 30000); // 30 seconds delay
    }
  
    // Show loader on initial page load
    showLoader();
  
    // Hide loader once the page is fully loaded, after a delay
    window.addEventListener('load', function() {
      hideLoader();
    });
  });
  