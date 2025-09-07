let map;
let userLocationMarker;

fetch('../files/locations_by_state.json')
  .then(res => res.json())
  .then(data => {
    map = L.map('map').setView([37.5, -122], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    Object.entries(data).forEach(([state, locations]) => {
      locations.forEach(loc => {
        const marker = L.marker([loc.lat, loc.lng]).addTo(map);
        marker.bindPopup(`<b>${state}</b><br>${loc.address}`);
      });
    });
  });

// Locate me functionality
document.getElementById('locate-btn').addEventListener('click', function() {
  const button = this;
  const originalText = button.innerHTML;
  
  // Show loading state
  button.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" stroke-dasharray="31.416" stroke-dashoffset="31.416"><animate attributeName="stroke-dasharray" dur="2s" values="0 31.416;15.708 15.708;0 31.416" repeatCount="indefinite"/><animate attributeName="stroke-dashoffset" dur="2s" values="0;-15.708;-31.416" repeatCount="indefinite"/></circle></svg>Locating...';
  button.disabled = true;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(position) {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        
        // Remove existing user location marker
        if (userLocationMarker) {
          map.removeLayer(userLocationMarker);
        }
        
        // Add new user location marker
        userLocationMarker = L.marker([lat, lng], {
          icon: L.divIcon({
            className: 'user-location-marker',
            html: '<div class="location-dot"></div>',
            iconSize: [20, 20],
            iconAnchor: [10, 10]
          })
        }).addTo(map);
        
        // Zoom to user location
        map.setView([lat, lng], 13);
        
        // Reset button
        button.innerHTML = originalText;
        button.disabled = false;
      },
      function(error) {
        console.error('Geolocation error:', error);
        alert('Unable to get your location. Please enable location services.');
        button.innerHTML = originalText;
        button.disabled = false;
      }
    );
  } else {
    alert('Geolocation is not supported by this browser.');
    button.innerHTML = originalText;
    button.disabled = false;
  }
});
