let map;
let userLocationMarker;

const SUPABASE_URL = 'https://tpxukqnimaudjohiexnj.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRweHVrcW5pbWF1ZGpvaGlleG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTcyMTU3NjQsImV4cCI6MjA3Mjc5MTc2NH0.w29MWgMmx1QSDCxe6RuoOTTm3v56M_o7WjqpIGi4YPQ';
// Why you in here bro 

async function fetchLocationsFromSupabase() {
  try {
    const response = await fetch(`${SUPABASE_URL}/rest/v1/PokeLocation?select=*`, {
      headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const locations = await response.json();
    return locations;
  } catch (error) {
    console.error('Error fetching from Supabase:', error);
    return [];
  }
}

async function initializeMap() {
  try {
    map = L.map('map').setView([37.5, -122], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);
    const locations = await fetchLocationsFromSupabase();
    
    if (locations.length === 0) {
      console.warn('No locations found in Supabase');
      return;
    }
    locations.forEach(location => {
      const marker = L.marker([location.lat, location.lng]).addTo(map);
      marker.bindPopup(`<b>${location.state}</b><br>${location.address}`);
    });

    console.log(`Loaded ${locations.length} locations from Supabase`);
  } catch (error) {
    console.error('Error initializing map:', error);
  }
}
initializeMap();

document.getElementById('locate-btn').addEventListener('click', function() {
  const button = this;
  const originalText = button.innerHTML;
  
  button.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" stroke-dasharray="31.416" stroke-dashoffset="31.416"><animate attributeName="stroke-dasharray" dur="2s" values="0 31.416;15.708 15.708;0 31.416" repeatCount="indefinite"/><animate attributeName="stroke-dashoffset" dur="2s" values="0;-15.708;-31.416" repeatCount="indefinite"/></circle></svg>Locating...';
  button.disabled = true;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(position) {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;

        if (userLocationMarker) {
          map.removeLayer(userLocationMarker);
        }

        userLocationMarker = L.marker([lat, lng], {
          icon: L.divIcon({
            className: 'user-location-marker',
            html: '<div class="location-dot"></div>',
            iconSize: [20, 20],
            iconAnchor: [10, 10]
          })
        }).addTo(map);

        map.setView([lat, lng], 13);

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
