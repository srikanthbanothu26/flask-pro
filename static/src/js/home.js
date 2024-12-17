
function getName() {
    var hello = document.getElementById('name').innerText;
  
    console.log(hello);

    return hello;
}

getName();

document.getElementById('home').addEventListener('click', function() {
    const profileDetails = document.getElementById('home-dropdown1');
    const up = document.getElementById("up");
    const down = document.getElementById("down");

    // Toggle dropdown visibility
    if (profileDetails.style.display === 'none' || profileDetails.style.display === '') {
        up.style.display = 'inline'; // Show up arrow
        down.style.display = 'none';
        profileDetails.style.display = 'block'; // Show dropdown
         // Hide down arrow
    } else {
        up.style.display = 'none'; // Hide up arrow
        down.style.display = 'inline'; // Show down arrow
        profileDetails.style.display = 'none'; // Hide dropdown
    }
});